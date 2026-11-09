<#
Operaciones del taller (Taller.md §5). Equivale a taller.sh.

  .\taller.ps1 preparar    [-Variante V]
  .\taller.ps1 funcionales [argumentos de pytest]
  .\taller.ps1 ejecutar    [-Tipo carga] [-Perfil local|ci] [-Variante V]
                           [-Ruta productos|salud] [-Tasa N] [-Umbral MS]
  .\taller.ps1 exportar    [-Ejecucion ID]
  .\taller.ps1 detener     [-BorrarDatos]

ejecutar termina con 0 (aprobado), 1 (rechazado por rendimiento) o
2 (error de infraestructura), para que la compuerta de CI falle en los dos
últimos casos y el resumen distinga la causa (Taller.md §8).

Funciona con Windows PowerShell 5.1 y con PowerShell 7.
#>
[CmdletBinding(PositionalBinding = $false)]
param(
    [Parameter(Position = 0)]
    [ValidateSet('preparar', 'funcionales', 'ejecutar', 'exportar', 'detener', 'ayuda')]
    [string]$Operacion = 'ayuda',
    [ValidateSet('carga', 'estres', 'picos')]
    [string]$Tipo = 'carga',
    [string]$Perfil = 'local',
    [string]$Variante = '',
    [ValidateSet('productos', 'salud')]
    [string]$Ruta = 'productos',
    [string]$Tasa = '',
    [string]$Umbral = '',
    [string]$Ejecucion = '',
    [switch]$BorrarDatos,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Resto = @()
)

$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$Compose = @('compose', '-f', 'compose.yaml', '-f', 'compose.carga.yaml')
$Utf8 = New-Object System.Text.UTF8Encoding($false)

function Stop-Taller([string]$Mensaje) {
    [Console]::Error.WriteLine("taller: $Mensaje")
    exit 2
}

function Write-Aviso([string]$Mensaje) {
    [Console]::Error.WriteLine("taller: $Mensaje")
}

function Write-Utf8([string]$Ruta, [string]$Contenido) {
    [System.IO.File]::WriteAllText((Join-Path $PSScriptRoot $Ruta), $Contenido, $Utf8)
}

# Ejecuta docker y muestra su salida en la consola. Devuelve el código de salida.
# Con -Log también guarda la salida, en UTF-8, en ese archivo.
function Invoke-Docker([string[]]$Argumentos, [string]$Log = '') {
    $previo = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $lineas = New-Object System.Collections.Generic.List[string]
        & docker @Argumentos 2>&1 | ForEach-Object {
            $texto = "$_"
            Write-Host $texto
            $lineas.Add($texto)
        }
        $codigo = $LASTEXITCODE
        if ($Log) {
            [System.IO.File]::WriteAllLines((Join-Path $PSScriptRoot $Log), $lineas, $Utf8)
        }
        return $codigo
    }
    finally {
        $ErrorActionPreference = $previo
    }
}

# Ejecuta docker y devuelve su salida estándar como texto, sin mostrarla.
function Get-Docker([string[]]$Argumentos) {
    $previo = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $salida = & docker @Argumentos 2>$null
        return ($salida -join "`n")
    }
    finally {
        $ErrorActionPreference = $previo
    }
}

# Carga las líneas KEY=VALUE de un archivo .env como variables de entorno.
function Import-Env([string]$Ruta) {
    if (-not (Test-Path -LiteralPath $Ruta)) { Stop-Taller "no existe $Ruta" }
    foreach ($linea in Get-Content -LiteralPath $Ruta -Encoding UTF8) {
        $linea = $linea.Trim()
        if (-not $linea -or $linea.StartsWith('#') -or -not $linea.Contains('=')) { continue }
        $clave, $valor = $linea.Split('=', 2)
        if ($clave -notmatch '^[A-Za-z_][A-Za-z0-9_]*$') { Stop-Taller "clave inválida en ${Ruta}: $clave" }
        Set-Item -Path "Env:$clave" -Value $valor
    }
}

function Assert-Variante([string]$Valor) {
    if ($Valor -notin @('regresion', 'corregida', 'sana')) {
        Stop-Taller "variante desconocida: $Valor (regresion, corregida o sana)"
    }
}

# Estado del contenedor de la API: healthy si supera su healthcheck.
function Get-SaludApi {
    $id = (Get-Docker ($Compose + @('ps', '-q', 'api'))).Trim()
    if (-not $id) { return 'ausente' }
    $estado = (Get-Docker @('inspect', '-f', '{{if .State.Health}}{{.State.Health.Status}}{{else}}{{.State.Status}}{{end}}', $id)).Trim()
    if ($estado) { return $estado } else { return 'desconocido' }
}

# Restablece datos y contadores (T2). Devuelve si o no.
function Reset-Estado {
    if (-not (Test-Path -LiteralPath 'base-datos/restablecer.sql')) {
        Write-Aviso 'base-datos/restablecer.sql no existe todavía (T2): se omite el restablecimiento'
        return 'no'
    }
    $comando = 'psql -v ON_ERROR_STOP=1 -q -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f /base-datos/restablecer.sql'
    $codigo = Invoke-Docker ($Compose + @('exec', '-T', 'postgres', 'sh', '-c', $comando))
    if ($codigo -eq 0) { return 'si' }
    Write-Aviso 'falló el restablecimiento del estado'
    return 'no'
}

function Get-Procesador {
    try { return (Get-CimInstance Win32_Processor | Select-Object -First 1).Name.Trim() }
    catch { return 'desconocido' }
}

function Invoke-Preparar {
    Import-Env 'config/variante.env'
    if ($Variante) { $env:VARIANTE = $Variante }
    Assert-Variante $env:VARIANTE

    Write-Host "Preparando el entorno con la variante $($env:VARIANTE)..."
    if ((Invoke-Docker ($Compose + @('up', '-d', '--wait', '--build'))) -ne 0) { Stop-Taller 'no se pudo levantar el entorno' }
    if ((Invoke-Docker ($Compose + @('--profile', 'carga', 'build', 'gatling'))) -ne 0) { Stop-Taller 'no se pudo construir la imagen de Gatling' }
    if ((Invoke-Docker ($Compose + @('--profile', 'carga', 'pull', '--quiet', 'herramientas'))) -ne 0) { Stop-Taller 'no se pudo descargar la imagen de herramientas' }
    $null = Reset-Estado
    Write-Host "Entorno listo. API: $(Get-SaludApi)."
}

function Invoke-Funcionales {
    exit (Invoke-Docker ($Compose + @('run', '--rm', 'api', 'pytest') + $Resto))
}

function Invoke-Ejecutar {
    switch ($Tipo) {
        'carga' { $simulacion = 'taller.rendimiento.CargaSimulation' }
        default { Stop-Taller "el tipo $Tipo todavía no está disponible (T10)" }
    }

    # 1. Perfil y variante. Los argumentos tienen prioridad sobre los archivos.
    $archivoPerfil = "config/perfiles/$Perfil.env"
    Import-Env $archivoPerfil
    Import-Env 'config/variante.env'
    if ($Variante) { $env:VARIANTE = $Variante }
    if ($Tasa) { $env:TASA = $Tasa }
    if ($Umbral) { $env:UMBRAL_MS = $Umbral }
    Assert-Variante $env:VARIANTE
    $v = $env:VARIANTE

    # 2. API con la variante pedida y estado inicial.
    Write-Host "Levantando la API con la variante $v..."
    if ((Invoke-Docker ($Compose + @('up', '-d', '--wait', 'api'))) -ne 0) { Write-Aviso 'la API no quedó sana' }
    $restablecido = Reset-Estado

    # 3. Carpeta de la ejecución.
    $id = '{0}-{1}-{2}' -f (Get-Date).ToUniversalTime().ToString("yyyyMMdd'T'HHmmss'Z'"), $Tipo, $v
    if ($Ruta -eq 'salud') { $id = "$id-salud" }
    $dir = "resultados/$id"
    $null = New-Item -ItemType Directory -Force -Path $dir

    # 4. Entorno y configuración efectiva.
    Copy-Item -LiteralPath $archivoPerfil -Destination "$dir/perfil.env"
    Write-Utf8 "$dir/compose-config.yaml" (Get-Docker ($Compose + @('config')))
    Write-Utf8 "$dir/docker-info.json" (Get-Docker @('info', '--format', '{{json .}}'))
    Write-Utf8 "$dir/imagenes.json" (Get-Docker ($Compose + @('--profile', 'carga', 'images', '--format', 'json')))
    $saludAntes = Get-SaludApi
    $inicio = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd'T'HH:mm:ss'Z'")

    # 5. Gatling.
    Write-Host "Ejecutando $simulacion a $($env:TASA)/s ($Ruta)..."
    $codigoGatling = Invoke-Docker -Log "$dir/gatling.log" -Argumentos ($Compose + @(
            '--profile', 'carga', 'run', '--rm', '--no-deps', '-T', 'gatling',
            "-Dgatling.simulationClass=$simulacion",
            "-Druta=$Ruta",
            "-Dtasa=$($env:TASA)",
            "-DumbralMs=$($env:UMBRAL_MS)",
            "-DerroresMaxPct=$($env:ERRORES_MAX_PCT)",
            "-DcalentamientoS=$($env:CALENTAMIENTO_S)",
            "-DmedicionS=$($env:MEDICION_S)",
            "-Dresultados=/resultados/$id/gatling",
            "-Dsalida=/resultados/$id"))
    $fin = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd'T'HH:mm:ss'Z'")
    $saludDespues = Get-SaludApi

    # 6. Registros de los servicios.
    Write-Utf8 "$dir/servicios.log" (Get-Docker ($Compose + @('logs', '--no-color', 'api', 'postgres')))

    $revision = (git rev-parse HEAD 2>$null)
    if (-not $revision) { $revision = 'desconocida' }
    $cambios = if (git status --porcelain 2>$null) { 'si' } else { 'no' }
    $so = [System.Runtime.InteropServices.RuntimeInformation]::OSDescription
    $arquitectura = [System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture
    Write-Utf8 "$dir/ejecucion.env" (@(
            "TIPO=$Tipo"
            "PERFIL=$Perfil"
            "VARIANTE=$v"
            "RUTA=$Ruta"
            "SIMULACION=$simulacion"
            "TASA=$($env:TASA)"
            "UMBRAL_MS=$($env:UMBRAL_MS)"
            "CALENTAMIENTO_S=$($env:CALENTAMIENTO_S)"
            "MEDICION_S=$($env:MEDICION_S)"
            "ERRORES_MAX_PCT=$($env:ERRORES_MAX_PCT)"
            "REVISION=$revision"
            "CAMBIOS_SIN_CONFIRMAR=$cambios"
            "SO=$so"
            "ARQUITECTURA=$arquitectura"
            "PROCESADOR=$(Get-Procesador)"
            "INICIO_UTC=$inicio"
            "FIN_UTC=$fin"
            "RESTABLECIDO=$restablecido"
            "SALUD_ANTES=$saludAntes"
            "SALUD_DESPUES=$saludDespues"
            "CODIGO_GATLING=$codigoGatling"
        ) -join "`n")

    # 7. Veredicto.
    $resultado = Invoke-Docker ($Compose + @('--profile', 'carga', 'run', '--rm', '--no-deps', '-T', 'herramientas', 'veredicto.py', "/resultados/$id"))
    if (-not (Test-Path -LiteralPath "$dir/veredicto.json")) {
        Write-Aviso 'no se pudo calcular el veredicto'
        $resultado = 2
    }

    # 8. Resumen en GitHub Actions.
    if ($env:GITHUB_STEP_SUMMARY -and (Test-Path -LiteralPath "$dir/resumen.md")) {
        [System.IO.File]::AppendAllText($env:GITHUB_STEP_SUMMARY, [System.IO.File]::ReadAllText((Join-Path $PSScriptRoot "$dir/resumen.md")), $Utf8)
    }
    Write-Host "Resultados en $dir"
    exit $resultado
}

function Invoke-Exportar {
    $id = $Ejecucion
    if (-not $id) {
        $ultima = Get-ChildItem -LiteralPath 'resultados' -Directory -ErrorAction SilentlyContinue | Sort-Object Name | Select-Object -Last 1
        if ($ultima) { $id = $ultima.Name }
    }
    if (-not $id -or -not (Test-Path -LiteralPath "resultados/$id" -PathType Container)) { Stop-Taller 'no hay ejecuciones en resultados/' }
    & tar -czf "resultados/$id.tar.gz" -C resultados $id
    if ($LASTEXITCODE -ne 0) { Stop-Taller 'no se pudo crear el archivo' }
    Write-Host "resultados/$id.tar.gz"
}

function Invoke-Detener {
    $argumentos = $Compose + @('--profile', 'carga', 'down', '--remove-orphans')
    if ($BorrarDatos) { $argumentos += '-v' }
    exit (Invoke-Docker $argumentos)
}

switch ($Operacion) {
    'preparar' { Invoke-Preparar }
    'funcionales' { Invoke-Funcionales }
    'ejecutar' { Invoke-Ejecutar }
    'exportar' { Invoke-Exportar }
    'detener' { Invoke-Detener }
    'ayuda' { (Get-Content -LiteralPath $PSCommandPath -Encoding UTF8 | Select-Object -Skip 1 -First 15) -join "`n" | Write-Host }
}
