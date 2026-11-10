<#
Operaciones del taller (Taller.md §5). Equivale a taller.sh.

  .\taller.ps1 preparar    [-Variante V]
  .\taller.ps1 funcionales [argumentos de pytest]
  .\taller.ps1 ejecutar    [-Tipo carga|estres|picos] [-Perfil local|ci|piloto]
                           [-Variante V] [-Ruta productos|salud] [-Tasa N]
                           [-Umbral MS] [-Tasas N,N,...] [-Pico N]
                           [-DuracionPico S]
  .\taller.ps1 campana     -Nombre NOMBRE [-Margen M] ID...
  .\taller.ps1 exportar    [-Ejecucion ID]
  .\taller.ps1 detener     [-BorrarDatos]

ejecutar termina con 0 (aprobado), 1 (rechazado por rendimiento) o
2 (inválido: no se pudo medir), para que la compuerta de CI falle en los dos
últimos casos y el resumen distinga la causa (Taller.md §8).
Estrés y picos son informativos: terminan con 0, o con 2 si alguna
ejecución es inválida. Con -Tasas, estrés corre un nivel por tasa y
resume la serie con campana (Taller.md §6.3).
campana resume varias ejecuciones de resultados/ (Taller.md §7).

Funciona con Windows PowerShell 5.1 y con PowerShell 7.
#>
[CmdletBinding(PositionalBinding = $false)]
param(
    [Parameter(Position = 0)]
    [ValidateSet('preparar', 'funcionales', 'ejecutar', 'campana', 'exportar', 'detener', 'ayuda')]
    [string]$Operacion = 'ayuda',
    [ValidateSet('carga', 'estres', 'picos')]
    [string]$Tipo = 'carga',
    [string]$Perfil = 'local',
    [string]$Variante = '',
    [ValidateSet('productos', 'salud')]
    [string]$Ruta = 'productos',
    [string]$Tasa = '',
    [string]$Umbral = '',
    [string[]]$Tasas = @(),
    [string]$Pico = '',
    [string]$DuracionPico = '',
    [string]$Ejecucion = '',
    [string]$Nombre = '',
    [string]$Margen = '3',
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
    # Si la carpeta no existe cuando un contenedor la monta, Docker la crea por
    # su cuenta (como root en Linux), y después el script no puede escribir en ella.
    $null = New-Item -ItemType Directory -Force -Path 'resultados'
    if ((Invoke-Docker ($Compose + @('up', '-d', '--wait', '--build'))) -ne 0) { Stop-Taller 'no se pudo levantar el entorno' }
    if ((Invoke-Docker ($Compose + @('--profile', 'carga', 'build', 'gatling'))) -ne 0) { Stop-Taller 'no se pudo construir la imagen de Gatling' }
    if ((Invoke-Docker ($Compose + @('--profile', 'carga', 'pull', '--quiet', 'herramientas'))) -ne 0) { Stop-Taller 'no se pudo descargar la imagen de herramientas' }
    $null = Reset-Estado
    Write-Host "Entorno listo. API: $(Get-SaludApi)."
}

function Invoke-Funcionales {
    exit (Invoke-Docker ($Compose + @('run', '--rm', 'api', 'pytest') + $Resto))
}

function Assert-Numero([string]$Nombre, [string]$Valor) {
    if ($Valor -notmatch '^[0-9]+(\.[0-9]+)?$') { Stop-Taller "$Nombre debe ser un número positivo: $Valor" }
}

function Invoke-Ejecutar {
    switch ($Tipo) {
        'carga' { $simulacion = 'taller.rendimiento.CargaSimulation' }
        'estres' { $simulacion = 'taller.rendimiento.EstresSimulation' }
        'picos' { $simulacion = 'taller.rendimiento.PicosSimulation' }
    }
    if ($Tasas) {
        if ($Tipo -ne 'estres') { Stop-Taller '-Tasas solo sirve con -Tipo estres' }
        if ($Tasa) { Stop-Taller 'usa -Tasa o -Tasas, no las dos' }
    }
    if (($Pico -or $DuracionPico) -and $Tipo -ne 'picos') { Stop-Taller '-Pico y -DuracionPico solo sirven con -Tipo picos' }

    # 1. Perfil y variante. Los argumentos tienen prioridad sobre los archivos.
    $script:ArchivoPerfil = "config/perfiles/$Perfil.env"
    Import-Env $script:ArchivoPerfil
    Import-Env 'config/variante.env'
    if ($Variante) { $env:VARIANTE = $Variante }
    if ($Tasa) { $env:TASA = $Tasa }
    if ($Umbral) { $env:UMBRAL_MS = $Umbral }
    Assert-Variante $env:VARIANTE
    Assert-Numero 'la tasa' $env:TASA
    if ($Tipo -eq 'picos') {
        if ($Pico) { $env:PICO_TASA = $Pico }
        if ($DuracionPico) { $env:PICO_S = $DuracionPico }
        if (-not $env:PICO_TASA) { Stop-Taller 'falta la tasa del pico: -Pico N o PICO_TASA en el perfil' }
        if (-not $env:PICO_S) { $env:PICO_S = '30' }
        Assert-Numero 'la tasa del pico' $env:PICO_TASA
        Assert-Numero 'la duración del pico' $env:PICO_S
    }

    if (-not $Tasas) {
        exit (Invoke-EjecucionUna $simulacion)
    }

    # Estrés: una ejecución por nivel (Taller.md §6.3) y un resumen de la serie.
    $niveles = @($Tasas | ForEach-Object { $_ -split ',' } | ForEach-Object { $_.Trim() } | Where-Object { $_ })
    foreach ($nivel in $niveles) { Assert-Numero 'cada tasa de -Tasas' $nivel }
    $rutas = New-Object System.Collections.Generic.List[string]
    $peor = 0
    foreach ($nivel in $niveles) {
        $env:TASA = $nivel
        $codigo = Invoke-EjecucionUna $simulacion
        $rutas.Add("/resultados/$($script:UltimoId)")
        if ($codigo -eq 2) { $peor = 2 }
    }
    $nombreSerie = 'estres-{0}-{1}' -f $env:VARIANTE, (Get-Date).ToUniversalTime().ToString("yyyyMMdd'T'HHmmss'Z'")
    $codigo = Invoke-Docker ($Compose + @('--profile', 'carga', 'run', '--rm', '--no-deps', '-T', 'herramientas',
            'campana.py', '--nombre', $nombreSerie) + $rutas.ToArray())
    if ($codigo -ne 0) { $peor = 2 }
    Write-Host "Resumen de la serie en resultados/campana-$nombreSerie.md"
    exit $peor
}

# Una ejecución con la configuración ya cargada. Deja su identificador en
# $script:UltimoId y devuelve el código del veredicto.
function Invoke-EjecucionUna([string]$Simulacion) {
    $v = $env:VARIANTE

    # 2. API con la variante pedida y estado inicial.
    Write-Host "Levantando la API con la variante $v..."
    if ((Invoke-Docker ($Compose + @('up', '-d', '--wait', 'api'))) -ne 0) { Write-Aviso 'la API no quedó sana' }
    $restablecido = Reset-Estado

    # 3. Carpeta de la ejecución.
    $id = '{0}-{1}-{2}' -f (Get-Date).ToUniversalTime().ToString("yyyyMMdd'T'HHmmss'Z'"), $Tipo, $v
    if ($Ruta -eq 'salud') { $id = "$id-salud" }
    $script:UltimoId = $id
    $dir = "resultados/$id"
    $null = New-Item -ItemType Directory -Force -Path $dir

    # 4. Entorno y configuración efectiva.
    Copy-Item -LiteralPath $script:ArchivoPerfil -Destination "$dir/perfil.env"
    Write-Utf8 "$dir/compose-config.yaml" (Get-Docker ($Compose + @('config')))
    Write-Utf8 "$dir/docker-info.json" (Get-Docker @('info', '--format', '{{json .}}'))
    Write-Utf8 "$dir/imagenes.json" (Get-Docker ($Compose + @('--profile', 'carga', 'images', '--format', 'json')))
    $saludAntes = Get-SaludApi
    $inicio = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd'T'HH:mm:ss'Z'")

    # 5. Gatling.
    $argumentos = $Compose + @(
        '--profile', 'carga', 'run', '--rm', '--no-deps', '-T', 'gatling',
        "-Dgatling.simulationClass=$Simulacion",
        "-Druta=$Ruta",
        "-Dtasa=$($env:TASA)",
        "-DumbralMs=$($env:UMBRAL_MS)",
        "-DerroresMaxPct=$($env:ERRORES_MAX_PCT)",
        "-DcalentamientoS=$($env:CALENTAMIENTO_S)",
        "-DmedicionS=$($env:MEDICION_S)",
        "-Dresultados=/resultados/$id/gatling",
        "-Dsalida=/resultados/$id")
    if ($Tipo -eq 'picos') {
        $argumentos += @("-DpicoTasa=$($env:PICO_TASA)", "-DpicoS=$($env:PICO_S)")
        Write-Host "Ejecutando $Simulacion`: base de $($env:TASA)/s y pico de $($env:PICO_TASA)/s durante $($env:PICO_S) s ($Ruta)..."
    }
    else {
        Write-Host "Ejecutando $Simulacion a $($env:TASA)/s ($Ruta)..."
    }
    $codigoGatling = Invoke-Docker -Log "$dir/gatling.log" -Argumentos $argumentos
    $fin = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd'T'HH:mm:ss'Z'")
    $saludDespues = Get-SaludApi

    # 6. Registros de los servicios.
    Write-Utf8 "$dir/servicios.log" (Get-Docker ($Compose + @('logs', '--no-color', 'api', 'postgres')))

    $revision = (git rev-parse HEAD 2>$null)
    if (-not $revision) { $revision = 'desconocida' }
    $cambios = if (git status --porcelain 2>$null) { 'si' } else { 'no' }
    $so = [System.Runtime.InteropServices.RuntimeInformation]::OSDescription
    $arquitectura = [System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture
    $lineas = @(
        "TIPO=$Tipo"
        "PERFIL=$Perfil"
        "VARIANTE=$v"
        "RUTA=$Ruta"
        "SIMULACION=$Simulacion"
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
    )
    if ($Tipo -eq 'picos') { $lineas += @("PICO_TASA=$($env:PICO_TASA)", "PICO_S=$($env:PICO_S)") }
    Write-Utf8 "$dir/ejecucion.env" ($lineas -join "`n")

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
    return $resultado
}

function Invoke-Campana {
    if (-not $Nombre) { Stop-Taller 'falta -Nombre' }
    if (-not $Resto) { Stop-Taller 'faltan las ejecuciones de la campaña' }
    $rutas = foreach ($ejecucionCampana in $Resto) {
        $id = ($ejecucionCampana -replace '\\', '/' -replace '^resultados/', '').TrimEnd('/')
        if ($id -notmatch '^[A-Za-z0-9._/-]+$' -or $id.Contains('..')) { Stop-Taller "ejecución inválida: $ejecucionCampana" }
        if (-not (Test-Path -LiteralPath "resultados/$id" -PathType Container)) { Stop-Taller "no existe resultados/$id" }
        "/resultados/$id"
    }
    exit (Invoke-Docker ($Compose + @('--profile', 'carga', 'run', '--rm', '--no-deps', '-T', 'herramientas',
                'campana.py', '--nombre', $Nombre, '--margen', $Margen) + @($rutas)))
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
    'campana' { Invoke-Campana }
    'exportar' { Invoke-Exportar }
    'detener' { Invoke-Detener }
    'ayuda' { (Get-Content -LiteralPath $PSCommandPath -Encoding UTF8 | Select-Object -Skip 1 -First 21) -join "`n" | Write-Host }
}
