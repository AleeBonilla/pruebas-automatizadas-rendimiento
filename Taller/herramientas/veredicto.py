"""Cierra una ejecución: extrae sus resultados, la valida y decide el veredicto.

Uso: python veredicto.py /resultados/<ejecucion>

Lee lo que dejaron el script del taller (ejecucion.env, docker-info.json,
compose-config.yaml, imagenes.json) y Gatling (gatling.log, fases.json y el
informe HTML). Escribe metricas.json, metadatos.json, veredicto.json y resumen.md.

Códigos de salida (Taller.md §6.4 y §8):
  0  aprobado
  1  rechazado por rendimiento
  2  inválido: la preparación falló o la medición no se puede interpretar, así
     que no dice nada de la variante (T12)

Solo usa la biblioteca estándar.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

# python -I no agrega la carpeta del script a sys.path.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from metricas import extraer, informe_gatling, leer_env, leer_json, leer_texto, numero  # noqa: E402

APROBADO, RECHAZADO, INVALIDO = "aprobado", "rechazado", "invalido"
CODIGOS = {APROBADO: 0, RECHAZADO: 1, INVALIDO: 2}

# Tolerancias de la validez (Taller.md §6.4). La inyección de Gatling es exacta
# mientras el generador da abasto: un desvío mayor indica que no sostuvo la tasa.
TOLERANCIA_TASA = 0.02        # tasa lograda al menos el 98 % de la prevista
TOLERANCIA_CANTIDAD = 0.005   # solicitudes iniciadas a ±0,5 % de las esperadas

# Errores que nacen en el generador, no en la API: sin puertos o sin
# descriptores, Gatling no llega a enviar la solicitud (Taller.md §7.1).
ERRORES_GENERADOR = re.compile(
    r"Cannot assign requested address|BindException|Too many open files|No buffer space available", re.I)

# Gatling 3.16 imprime cada aserción en la consola al terminar:
#   medicion: 95th percentile of response time is less than 300.0 : true (actual : 30.0)
ASERCION = re.compile(r"^(?P<objetivo>[^:\r\n]+): (?P<descripcion>.+) : (?P<cumple>true|false) \(actual : (?P<actual>[^)]*)\)\s*$")

# Mensajes con los que termina el plugin de Maven (Gatling siempre sale con 1).
FALLO_ASERCIONES = "Gatling simulation assertions failed"
FALLO_GATLING = "Gatling failed"

# Parámetros que el script pidió (ejecucion.env) y los que usó la simulación (fases.json).
PARAMETROS = (("TASA", "tasa"), ("UMBRAL_MS", "umbralMs"), ("ERRORES_MAX_PCT", "erroresMaxPct"),
              ("CALENTAMIENTO_S", "calentamientoS"), ("MEDICION_S", "medicionS"))


def aserciones(log: str) -> list[dict]:
    encontradas = []
    for linea in log.splitlines():
        coincidencia = ASERCION.match(linea.strip())
        if coincidencia:
            encontradas.append({
                "objetivo": coincidencia["objetivo"],
                "descripcion": coincidencia["descripcion"],
                "cumple": coincidencia["cumple"] == "true",
                "actual": coincidencia["actual"],
            })
    return encontradas


def invalidez(ejecucion: dict[str, str], fases_json: dict, resultados: dict, log: str,
              lista: list[dict], informe: Path | None) -> str | None:
    """Motivo por el que la ejecución no se puede interpretar, o None si es válida.

    Las reglas siguen Taller.md §6.4: preparación fallida, configuración distinta
    de la prevista, generador saturado, datos incompletos o métricas perdidas.
    """
    # Preparación.
    if ejecucion.get("SALUD_ANTES") != "healthy":
        return f"la API no estaba sana antes de medir (estado: {ejecucion.get('SALUD_ANTES', 'desconocido')})"
    if ejecucion.get("RESTABLECIDO") != "si":
        return "no se restableció el estado de la base de datos antes de medir"
    # Un contenedor que dejó de correr es un problema del entorno. "unhealthy" no
    # cuenta: con la regresión, /salud puede tardar en la fila del candado y el
    # healthcheck fallar, y eso es justamente lo que la prueba debe rechazar.
    if ejecucion.get("SALUD_DESPUES") in ("exited", "dead", "ausente"):
        return f"la API dejó de correr durante la medición (estado: {ejecucion['SALUD_DESPUES']})"
    if FALLO_GATLING in log and FALLO_ASERCIONES not in log:
        return "Gatling terminó con error antes de evaluar las aserciones"

    # Configuración: lo que midió la simulación debe ser lo que pidió el script.
    if not fases_json:
        return "falta fases.json: no se sabe qué midió la simulación"
    usados = fases_json.get("parametros") or {}
    for clave_env, clave_sim in PARAMETROS:
        pedido, usado = numero(ejecucion.get(clave_env)), numero(str(usados.get(clave_sim)))
        if pedido is None or usado is None or abs(pedido - usado) > 1e-9:
            return f"la simulación usó {clave_sim}={usados.get(clave_sim)}, pero se pidió {ejecucion.get(clave_env)}"
    if usados.get("ruta") != ejecucion.get("RUTA"):
        return f"la simulación consultó la ruta {usados.get('ruta')}, pero se pidió {ejecucion.get('RUTA')}"
    variante_api = fases_json.get("variante_api")
    if variante_api != ejecucion.get("VARIANTE"):
        return f"la API atendía la variante {variante_api or 'desconocida'}, pero se pidió {ejecucion.get('VARIANTE')}"

    # Métricas exigidas.
    medicion = resultados["fases"]["medicion"]
    if not lista:
        return "no se encontraron aserciones en la salida de Gatling"
    if informe is None or medicion["completadas"] is None:
        return "no se generó el informe de Gatling de la medición"
    if medicion["iniciadas"] is None or medicion["tasa_lograda"] is None:
        return "fases.json no registra las solicitudes de la medición"

    # Generador: sin estos errores ni desvíos, la carga fue la prevista.
    for error in medicion["errores"]:
        if ERRORES_GENERADOR.search(error["mensaje"]):
            return f"el generador no pudo enviar {error['cantidad']} solicitudes ({error['mensaje']})"
    esperadas = medicion["esperadas"]
    if abs(medicion["iniciadas"] - esperadas) > max(1, TOLERANCIA_CANTIDAD * esperadas):
        return f"se iniciaron {medicion['iniciadas']} solicitudes de las {esperadas} previstas"
    if medicion["tasa_lograda"] < (1 - TOLERANCIA_TASA) * medicion["tasa_prevista"]:
        return (f"el generador no sostuvo la tasa: {medicion['tasa_lograda']:.1f}/s "
                f"de {medicion['tasa_prevista']:g}/s previstas")

    # Datos completos: cada solicitud iniciada debe haber terminado y figurar en el informe.
    if medicion["terminadas"] != medicion["iniciadas"]:
        return f"terminaron {medicion['terminadas']} de las {medicion['iniciadas']} solicitudes iniciadas"
    if medicion["completadas"] != medicion["iniciadas"]:
        return (f"el informe de Gatling registra {medicion['completadas']} solicitudes, "
                f"pero se iniciaron {medicion['iniciadas']}")
    return None


def decidir(ejecucion, fases_json, resultados, log, lista, informe) -> tuple[str, str]:
    """Devuelve (resultado, motivo)."""
    motivo = invalidez(ejecucion, fases_json, resultados, log, lista, informe)
    if motivo:
        return INVALIDO, motivo
    fallidas = [a for a in lista if not a["cumple"]]
    if fallidas:
        detalle = "; ".join(f"{a['objetivo']}: {a['descripcion']} (actual: {a['actual']})" for a in fallidas)
        return RECHAZADO, f"incumple {len(fallidas)} aserción(es): {detalle}"
    return APROBADO, "cumple todas las aserciones"


def metadatos(carpeta: Path, ejecucion: dict[str, str], fases_json: dict, informe: Path | None) -> dict:
    docker = leer_json(carpeta / "docker-info.json") or {}
    compose = carpeta / "compose-config.yaml"
    hash_compose = None
    if compose.exists():
        normalizado = leer_texto(compose).replace("\r\n", "\n").encode("utf-8")
        hash_compose = hashlib.sha256(normalizado).hexdigest()
    return {
        "ejecucion": carpeta.name,
        "tipo": ejecucion.get("TIPO"),
        "perfil": ejecucion.get("PERFIL"),
        "variante": ejecucion.get("VARIANTE"),
        "ruta": ejecucion.get("RUTA"),
        "simulacion": ejecucion.get("SIMULACION"),
        "parametros": {clave: ejecucion.get(clave) for clave, _ in PARAMETROS},
        "codigo": {
            "revision": ejecucion.get("REVISION"),
            "cambios_sin_confirmar": ejecucion.get("CAMBIOS_SIN_CONFIRMAR") == "si",
        },
        "entorno": {
            "so_anfitrion": ejecucion.get("SO"),
            "arquitectura": ejecucion.get("ARQUITECTURA"),
            "procesador": ejecucion.get("PROCESADOR"),
            "docker_version": docker.get("ServerVersion"),
            "docker_cpus": docker.get("NCPU"),
            "docker_memoria_bytes": docker.get("MemTotal"),
            "docker_so": docker.get("OperatingSystem"),
            "hash_compose": hash_compose,
            "imagenes": leer_json(carpeta / "imagenes.json"),
        },
        "intervalos": {
            "inicio_utc": ejecucion.get("INICIO_UTC"),
            "fin_utc": ejecucion.get("FIN_UTC"),
            "fases": fases_json.get("fases"),
        },
        "estado": {
            "restablecido": ejecucion.get("RESTABLECIDO") == "si",
            "salud_antes": ejecucion.get("SALUD_ANTES"),
            "salud_despues": ejecucion.get("SALUD_DESPUES"),
            "variante_api": fases_json.get("variante_api"),
            "codigo_gatling": ejecucion.get("CODIGO_GATLING"),
        },
        "informe_gatling": str(informe.relative_to(carpeta)) if informe else None,
    }


def ms(valor) -> str:
    return "—" if valor is None else f"{valor:,.0f} ms".replace(",", " ")


def resumen_md(datos: dict, resultados: dict, resultado: str, motivo: str, lista: list[dict]) -> str:
    iconos = {APROBADO: "✅ Aprobado", RECHAZADO: "❌ Rechazado por rendimiento", INVALIDO: "⚠️ Inválido"}
    p = datos["parametros"]
    lineas = [
        f"### {iconos[resultado]}",
        "",
        f"{motivo[:1].upper()}{motivo[1:]}.",
        "",
        "| Ejecución | Variante | Perfil | Tasa | Umbral p95 | Revisión |",
        "|---|---|---|---:|---:|---|",
        f"| `{datos['ejecucion']}` | `{datos['variante']}` | `{datos['perfil']}` | {p['TASA']}/s | {p['UMBRAL_MS']} ms "
        f"| `{(datos['codigo']['revision'] or '?')[:7]}`{' (con cambios)' if datos['codigo']['cambios_sin_confirmar'] else ''} |",
    ]
    m = resultados["fases"]["medicion"]
    if m["completadas"] is not None:
        t = m["tiempos_ms"] or {}
        tasa = "—" if m["tasa_lograda"] is None else f"{m['tasa_lograda']:.1f}/s".replace(".", ",")
        iniciadas = "—" if m["iniciadas"] is None else f"{m['iniciadas']}"
        errores = f"{m['errores_pct']:.2f} %".replace(".", ",")
        lineas += [
            "",
            "| Medición | p50 | p95 | p99 | Errores | Iniciadas | Tasa lograda |",
            "|---|---:|---:|---:|---:|---:|---:|",
            f"| {m['completadas']} solicitudes | {ms(t.get('p50'))} | {ms(t.get('p95'))} | {ms(t.get('p99'))} "
            f"| {errores} | {iniciadas} de {m['esperadas']} | {tasa} |",
        ]
    if lista:
        lineas += ["", "| Aserción | Actual | Cumple |", "|---|---:|:---:|"]
        lineas += [f"| {a['objetivo']}: {a['descripcion']} | {a['actual']} | {'sí' if a['cumple'] else 'no'} |" for a in lista]
    return "\n".join(lineas) + "\n"


def escribir_json(ruta: Path, datos) -> None:
    ruta.write_text(json.dumps(datos, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    resumen, codigo = cerrar(Path(sys.argv[1]))
    print(resumen)
    return codigo


def cerrar(carpeta: Path) -> tuple[str, int]:
    """Escribe los archivos de cierre de la ejecución; devuelve el resumen y el código."""
    ejecucion = leer_env(carpeta / "ejecucion.env")
    fases_json = leer_json(carpeta / "fases.json") or {}
    log = leer_texto(carpeta / "gatling.log")
    lista = aserciones(log)
    informe = informe_gatling(carpeta)
    resultados = extraer(carpeta)

    resultado, motivo = decidir(ejecucion, fases_json, resultados, log, lista, informe)
    datos = metadatos(carpeta, ejecucion, fases_json, informe)

    escribir_json(carpeta / "metricas.json", resultados)
    escribir_json(carpeta / "metadatos.json", datos)
    escribir_json(carpeta / "veredicto.json", {
        "resultado": resultado,
        "codigo": CODIGOS[resultado],
        "motivo": motivo,
        "aserciones": lista,
    })
    resumen = resumen_md(datos, resultados, resultado, motivo, lista)
    (carpeta / "resumen.md").write_text(resumen, encoding="utf-8")
    return resumen, CODIGOS[resultado]


if __name__ == "__main__":
    sys.exit(main())
