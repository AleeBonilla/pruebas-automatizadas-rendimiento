#!/bin/sh
# Operaciones del taller (Taller.md §5). Equivale a taller.ps1.
#
#   ./taller.sh preparar    [--variante V]
#   ./taller.sh funcionales [argumentos de pytest]
#   ./taller.sh ejecutar    [--tipo carga|estres|picos] [--perfil local|ci|piloto]
#                           [--variante V] [--ruta productos|salud] [--tasa N]
#                           [--umbral MS] [--tasas N,N,...] [--pico N]
#                           [--duracion-pico S]
#   ./taller.sh campana     --nombre NOMBRE [--margen M] ID...
#   ./taller.sh exportar    [--ejecucion ID]
#   ./taller.sh detener     [--borrar-datos]
#
# ejecutar termina con 0 (aprobado), 1 (rechazado por rendimiento) o
# 2 (inválido: no se pudo medir), para que la compuerta de CI falle en
# los dos últimos casos y el resumen distinga la causa (Taller.md §8).
# Estrés y picos son informativos: terminan con 0, o con 2 si alguna
# ejecución es inválida. Con --tasas, estrés corre un nivel por tasa y
# resume la serie con campana (Taller.md §6.3).
# campana resume varias ejecuciones de resultados/ (Taller.md §7).

set -eu

cd "$(dirname "$0")"
# En Git Bash, evita que /resultados/... se convierta en una ruta de Windows.
export MSYS_NO_PATHCONV=1 MSYS2_ARG_CONV_EXCL='*'

dc() { docker compose -f compose.yaml -f compose.carga.yaml "$@"; }

error() { echo "taller: $*" >&2; exit 2; }
aviso() { echo "taller: $*" >&2; }

ayuda() { sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'; }

# Exporta las líneas KEY=VALUE de un archivo .env sin ejecutarlo como código.
cargar_env() {
  [ -f "$1" ] || error "no existe $1"
  while IFS= read -r linea || [ -n "$linea" ]; do
    linea=$(printf '%s' "$linea" | tr -d '\r')
    case "$linea" in ''|'#'*) continue ;; *=*) ;; *) continue ;; esac
    clave=${linea%%=*}
    case "$clave" in ''|[0-9]*|*[!A-Za-z0-9_]*) error "clave inválida en $1: $clave" ;; esac
    export "$clave=${linea#*=}"
  done < "$1"
}

validar_variante() {
  case "$1" in regresion|corregida|sana) ;; *) error "variante desconocida: $1 (regresion, corregida o sana)" ;; esac
}

# Estado del contenedor de la API: healthy si supera su healthcheck.
salud_api() {
  id=$(dc ps -q api 2>/dev/null || true)
  if [ -z "$id" ]; then echo ausente; return; fi
  docker inspect -f '{{if .State.Health}}{{.State.Health.Status}}{{else}}{{.State.Status}}{{end}}' "$id" 2>/dev/null || echo desconocido
}

# Restablece datos y contadores (T2). Imprime si o no.
restablecer() {
  if [ ! -f base-datos/restablecer.sql ]; then
    aviso "base-datos/restablecer.sql no existe todavía (T2): se omite el restablecimiento"
    echo no; return
  fi
  if dc exec -T postgres sh -c 'psql -v ON_ERROR_STOP=1 -q -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f /base-datos/restablecer.sql' >&2; then
    echo si
  else
    aviso "falló el restablecimiento del estado"
    echo no
  fi
}

procesador() {
  if [ -r /proc/cpuinfo ]; then
    grep -m1 'model name' /proc/cpuinfo | cut -d: -f2 | sed 's/^ *//'
  elif command -v sysctl >/dev/null 2>&1; then
    sysctl -n machdep.cpu.brand_string 2>/dev/null || echo desconocido
  else
    echo desconocido
  fi
}

op_preparar() {
  variante=""
  while [ $# -gt 0 ]; do
    case "$1" in
      --variante) variante=${2:?falta el valor de --variante}; shift 2 ;;
      *) error "opción desconocida para preparar: $1" ;;
    esac
  done
  cargar_env config/variante.env
  [ -n "$variante" ] && VARIANTE=$variante
  validar_variante "$VARIANTE"
  export VARIANTE

  echo "Preparando el entorno con la variante $VARIANTE..."
  # Si la carpeta no existe cuando un contenedor la monta, Docker la crea como
  # root en Linux, y después el script no puede escribir en ella.
  mkdir -p resultados
  dc up -d --wait --build
  dc --profile carga build gatling
  dc --profile carga pull --quiet herramientas
  restablecer >/dev/null
  echo "Entorno listo. API: $(salud_api)."
}

op_funcionales() {
  dc run --rm api pytest "$@"
}

validar_numero() {
  case "$2" in ''|*[!0-9.]*|*.*.*) error "$1 debe ser un número positivo: $2" ;; esac
}

op_ejecutar() {
  tipo=carga perfil=local variante="" ruta=productos tasa="" umbral="" tasas="" pico="" duracion_pico=""
  while [ $# -gt 0 ]; do
    case "$1" in
      --tipo) tipo=${2:?falta el valor de --tipo}; shift 2 ;;
      --perfil) perfil=${2:?falta el valor de --perfil}; shift 2 ;;
      --variante) variante=${2:?falta el valor de --variante}; shift 2 ;;
      --ruta) ruta=${2:?falta el valor de --ruta}; shift 2 ;;
      --tasa) tasa=${2:?falta el valor de --tasa}; shift 2 ;;
      --umbral) umbral=${2:?falta el valor de --umbral}; shift 2 ;;
      --tasas) tasas=${2:?falta el valor de --tasas}; shift 2 ;;
      --pico) pico=${2:?falta el valor de --pico}; shift 2 ;;
      --duracion-pico) duracion_pico=${2:?falta el valor de --duracion-pico}; shift 2 ;;
      *) error "opción desconocida para ejecutar: $1" ;;
    esac
  done
  case "$tipo" in
    carga) simulacion=taller.rendimiento.CargaSimulation ;;
    estres) simulacion=taller.rendimiento.EstresSimulation ;;
    picos) simulacion=taller.rendimiento.PicosSimulation ;;
    *) error "tipo desconocido: $tipo (carga, estres o picos)" ;;
  esac
  case "$ruta" in productos|salud) ;; *) error "ruta desconocida: $ruta (productos o salud)" ;; esac
  if [ -n "$tasas" ]; then
    [ "$tipo" = estres ] || error "--tasas solo sirve con --tipo estres"
    [ -z "$tasa" ] || error "usa --tasa o --tasas, no las dos"
  fi
  if [ -n "$pico$duracion_pico" ] && [ "$tipo" != picos ]; then
    error "--pico y --duracion-pico solo sirven con --tipo picos"
  fi

  # 1. Perfil y variante. Los argumentos tienen prioridad sobre los archivos.
  cargar_env "config/perfiles/$perfil.env"
  cargar_env config/variante.env
  [ -n "$variante" ] && VARIANTE=$variante
  [ -n "$tasa" ] && TASA=$tasa
  [ -n "$umbral" ] && UMBRAL_MS=$umbral
  validar_variante "$VARIANTE"
  export VARIANTE
  validar_numero "la tasa" "$TASA"
  if [ "$tipo" = picos ]; then
    [ -n "$pico" ] && PICO_TASA=$pico
    [ -n "$duracion_pico" ] && PICO_S=$duracion_pico
    [ -n "${PICO_TASA:-}" ] || error "falta la tasa del pico: --pico N o PICO_TASA en el perfil"
    PICO_S=${PICO_S:-30}
    validar_numero "la tasa del pico" "$PICO_TASA"
    validar_numero "la duración del pico" "$PICO_S"
  fi

  if [ -z "$tasas" ]; then
    codigo=0
    ejecutar_una || codigo=$?
    exit "$codigo"
  fi

  # Estrés: una ejecución por nivel (Taller.md §6.3) y un resumen de la serie.
  rutas="" peor=0
  for nivel in $(printf '%s' "$tasas" | tr ',' ' '); do
    validar_numero "cada tasa de --tasas" "$nivel"
  done
  for nivel in $(printf '%s' "$tasas" | tr ',' ' '); do
    TASA=$nivel
    codigo=0
    ejecutar_una || codigo=$?
    rutas="$rutas /resultados/$ultimo_id"
    [ "$codigo" -eq 2 ] && peor=2
  done
  nombre="estres-$VARIANTE-$(date -u +%Y%m%dT%H%M%SZ)"
  # Los identificadores los generó este script: sin espacios ni comodines.
  # shellcheck disable=SC2086
  dc --profile carga run --rm --no-deps -T herramientas campana.py --nombre "$nombre" $rutas || peor=2
  echo "Resumen de la serie en resultados/campana-$nombre.md"
  exit "$peor"
}

# Una ejecución con la configuración ya cargada. Deja su identificador en
# ultimo_id y devuelve el código del veredicto.
ejecutar_una() {
  # 2. API con la variante pedida y estado inicial.
  echo "Levantando la API con la variante $VARIANTE..."
  dc up -d --wait api || aviso "la API no quedó sana"
  restablecido=$(restablecer)

  # 3. Carpeta de la ejecución.
  id="$(date -u +%Y%m%dT%H%M%SZ)-$tipo-$VARIANTE"
  [ "$ruta" = salud ] && id="$id-salud"
  ultimo_id=$id
  dir="resultados/$id"
  mkdir -p "$dir"

  # 4. Entorno y configuración efectiva.
  cp "config/perfiles/$perfil.env" "$dir/perfil.env"
  dc config > "$dir/compose-config.yaml" 2>/dev/null || true
  docker info --format '{{json .}}' > "$dir/docker-info.json" 2>/dev/null || true
  dc --profile carga images --format json > "$dir/imagenes.json" 2>/dev/null || true
  if command -v lscpu >/dev/null 2>&1; then lscpu > "$dir/lscpu.txt"; fi
  salud_antes=$(salud_api)
  inicio=$(date -u +%Y-%m-%dT%H:%M:%SZ)

  # 5. Gatling. Su salida queda en gatling.log; el código, en .codigo.
  set -- "-Dgatling.simulationClass=$simulacion" "-Druta=$ruta" "-Dtasa=$TASA" \
    "-DumbralMs=$UMBRAL_MS" "-DerroresMaxPct=$ERRORES_MAX_PCT" \
    "-DcalentamientoS=$CALENTAMIENTO_S" "-DmedicionS=$MEDICION_S" \
    "-Dresultados=/resultados/$id/gatling" "-Dsalida=/resultados/$id"
  if [ "$tipo" = picos ]; then
    set -- "$@" "-DpicoTasa=$PICO_TASA" "-DpicoS=$PICO_S"
    echo "Ejecutando $simulacion: base de $TASA/s y pico de $PICO_TASA/s durante $PICO_S s ($ruta)..."
  else
    echo "Ejecutando $simulacion a $TASA/s ($ruta)..."
  fi
  set +e
  {
    dc --profile carga run --rm --no-deps -T gatling "$@"
    echo $? > "$dir/.codigo"
  } 2>&1 | tee "$dir/gatling.log"
  set -e
  codigo_gatling=$(cat "$dir/.codigo" 2>/dev/null || echo desconocido)
  rm -f "$dir/.codigo"
  fin=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  salud_despues=$(salud_api)

  # 6. Registros de los servicios.
  dc logs --no-color api postgres > "$dir/servicios.log" 2>&1 || true

  cambios=no
  [ -n "$(git status --porcelain 2>/dev/null)" ] && cambios=si
  cat > "$dir/ejecucion.env" <<EOF
TIPO=$tipo
PERFIL=$perfil
VARIANTE=$VARIANTE
RUTA=$ruta
SIMULACION=$simulacion
TASA=$TASA
UMBRAL_MS=$UMBRAL_MS
CALENTAMIENTO_S=$CALENTAMIENTO_S
MEDICION_S=$MEDICION_S
ERRORES_MAX_PCT=$ERRORES_MAX_PCT
REVISION=$(git rev-parse HEAD 2>/dev/null || echo desconocida)
CAMBIOS_SIN_CONFIRMAR=$cambios
SO=$(uname -sr)
ARQUITECTURA=$(uname -m)
PROCESADOR=$(procesador)
INICIO_UTC=$inicio
FIN_UTC=$fin
RESTABLECIDO=$restablecido
SALUD_ANTES=$salud_antes
SALUD_DESPUES=$salud_despues
CODIGO_GATLING=$codigo_gatling
EOF
  if [ "$tipo" = picos ]; then
    printf 'PICO_TASA=%s\nPICO_S=%s\n' "$PICO_TASA" "$PICO_S" >> "$dir/ejecucion.env"
  fi

  # 7. Veredicto.
  set +e
  dc --profile carga run --rm --no-deps -T herramientas veredicto.py "/resultados/$id"
  resultado=$?
  set -e
  [ -f "$dir/veredicto.json" ] || { aviso "no se pudo calcular el veredicto"; resultado=2; }

  # 8. Resumen en GitHub Actions.
  if [ -n "${GITHUB_STEP_SUMMARY:-}" ] && [ -f "$dir/resumen.md" ]; then
    cat "$dir/resumen.md" >> "$GITHUB_STEP_SUMMARY"
  fi
  echo "Resultados en $dir"
  return "$resultado"
}

op_campana() {
  nombre="" margen=3 rutas=""
  while [ $# -gt 0 ]; do
    case "$1" in
      --nombre) nombre=${2:?falta el valor de --nombre}; shift 2 ;;
      --margen) margen=${2:?falta el valor de --margen}; shift 2 ;;
      -*) error "opción desconocida para campana: $1" ;;
      *)
        id=${1#resultados/}; id=${id%/}
        case "$id" in ''|*[!A-Za-z0-9._/-]*|*..*) error "ejecución inválida: $1" ;; esac
        [ -d "resultados/$id" ] || error "no existe resultados/$id"
        rutas="$rutas /resultados/$id"; shift ;;
    esac
  done
  [ -n "$nombre" ] || error "falta --nombre"
  [ -n "$rutas" ] || error "faltan las ejecuciones de la campaña"
  # Los identificadores ya se validaron: sin espacios ni comodines.
  # shellcheck disable=SC2086
  dc --profile carga run --rm --no-deps -T herramientas campana.py --nombre "$nombre" --margen "$margen" $rutas
}

op_exportar() {
  id=""
  while [ $# -gt 0 ]; do
    case "$1" in
      --ejecucion) id=${2:?falta el valor de --ejecucion}; shift 2 ;;
      *) error "opción desconocida para exportar: $1" ;;
    esac
  done
  if [ -z "$id" ]; then
    id=$(find resultados -mindepth 1 -maxdepth 1 -type d 2>/dev/null | sed 's|.*/||' | sort | tail -n 1)
  fi
  [ -n "$id" ] && [ -d "resultados/$id" ] || error "no hay ejecuciones en resultados/"
  tar -czf "resultados/$id.tar.gz" -C resultados "$id"
  echo "resultados/$id.tar.gz"
}

op_detener() {
  volumenes=""
  while [ $# -gt 0 ]; do
    case "$1" in
      --borrar-datos) volumenes=-v; shift ;;
      *) error "opción desconocida para detener: $1" ;;
    esac
  done
  # shellcheck disable=SC2086
  dc --profile carga down --remove-orphans $volumenes
}

operacion=${1:-ayuda}
[ $# -gt 0 ] && shift
case "$operacion" in
  preparar) op_preparar "$@" ;;
  funcionales) op_funcionales "$@" ;;
  ejecutar) op_ejecutar "$@" ;;
  campana) op_campana "$@" ;;
  exportar) op_exportar "$@" ;;
  detener) op_detener "$@" ;;
  ayuda|-h|--help) ayuda ;;
  *) ayuda; error "operación desconocida: $operacion" ;;
esac
