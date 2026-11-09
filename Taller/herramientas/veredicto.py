"""Cierra una ejecución: consolida los metadatos y decide el veredicto.

Uso: python veredicto.py /resultados/<ejecucion>

Lee lo que dejaron el script del taller (ejecucion.env, docker-info.json,
compose-config.yaml, imagenes.json) y Gatling (gatling.log, fases.json y el
informe HTML). Escribe metadatos.json, veredicto.json y resumen.md.

Códigos de salida (Taller.md §6.4 y §8):
  0  aprobado
  1  rechazado por rendimiento
  2  error de infraestructura: la preparación falló o la ejecución no se
     puede interpretar. En la fase 2 (T12) pasa a llamarse «inválido».

Solo usa la biblioteca estándar.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

APROBADO, RECHAZADO, ERROR_INFRA = "aprobado", "rechazado", "error-infra"
CODIGOS = {APROBADO: 0, RECHAZADO: 1, ERROR_INFRA: 2}

# Gatling 3.16 imprime cada aserción en la consola al terminar:
#   medicion: 95th percentile of response time is less than 300.0 : true (actual : 30.0)
ASERCION = re.compile(r"^(?P<objetivo>[^:\r\n]+): (?P<descripcion>.+) : (?P<cumple>true|false) \(actual : (?P<actual>[^)]*)\)\s*$")

# Mensajes con los que termina el plugin de Maven (Gatling siempre sale con 1).
FALLO_ASERCIONES = "Gatling simulation assertions failed"
FALLO_GATLING = "Gatling failed"


def leer_env(ruta: Path) -> dict[str, str]:
    """Lee un archivo KEY=VALUE ignorando comentarios, líneas vacías y CRLF."""
    valores: dict[str, str] = {}
    if not ruta.exists():
        return valores
    for linea in ruta.read_text(encoding="utf-8-sig").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        clave, valor = linea.split("=", 1)
        valores[clave.strip()] = valor.strip()
    return valores


def leer_json(ruta: Path):
    if not ruta.exists():
        return None
    try:
        return json.loads(ruta.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError:
        return None


def leer_texto(ruta: Path) -> str:
    if not ruta.exists():
        return ""
    datos = ruta.read_bytes()
    # PowerShell 5.1 puede escribir UTF-16; el resto, UTF-8.
    for codificacion in ("utf-8-sig", "utf-16"):
        try:
            return datos.decode(codificacion)
        except UnicodeDecodeError:
            continue
    return datos.decode("utf-8", errors="replace")


def informe_gatling(carpeta: Path) -> Path | None:
    """Carpeta del informe HTML de Gatling dentro de gatling/, si existe."""
    for indice in sorted((carpeta / "gatling").glob("*/index.html")):
        return indice.parent
    return None


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


def decidir(ejecucion: dict[str, str], log: str, lista: list[dict], informe: Path | None) -> tuple[str, str]:
    """Devuelve (resultado, motivo)."""
    if ejecucion.get("SALUD_ANTES") != "healthy":
        return ERROR_INFRA, f"la API no estaba sana antes de medir (estado: {ejecucion.get('SALUD_ANTES', 'desconocido')})"
    # Un contenedor que dejó de correr es un problema del entorno. "unhealthy" no
    # cuenta: con la regresión, /salud puede tardar en la fila del candado y el
    # healthcheck fallar, y eso es justamente lo que la prueba debe rechazar.
    if ejecucion.get("SALUD_DESPUES") in ("exited", "dead", "ausente"):
        return ERROR_INFRA, f"la API dejó de correr durante la medición (estado: {ejecucion['SALUD_DESPUES']})"
    if FALLO_GATLING in log and FALLO_ASERCIONES not in log:
        return ERROR_INFRA, "Gatling terminó con error antes de evaluar las aserciones"
    if not lista:
        return ERROR_INFRA, "no se encontraron aserciones en la salida de Gatling"
    if informe is None:
        return ERROR_INFRA, "no se generó el informe de Gatling"
    fallidas = [a for a in lista if not a["cumple"]]
    if fallidas:
        detalle = "; ".join(f"{a['objetivo']}: {a['descripcion']} (actual: {a['actual']})" for a in fallidas)
        return RECHAZADO, f"incumple {len(fallidas)} aserción(es): {detalle}"
    return APROBADO, "cumple todas las aserciones"


def metadatos(carpeta: Path, ejecucion: dict[str, str], informe: Path | None) -> dict:
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
        "parametros": {clave: ejecucion.get(clave) for clave in
                       ("TASA", "UMBRAL_MS", "CALENTAMIENTO_S", "MEDICION_S", "ERRORES_MAX_PCT")},
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
            "fases": (leer_json(carpeta / "fases.json") or {}).get("fases"),
        },
        "estado": {
            "restablecido": ejecucion.get("RESTABLECIDO") == "si",
            "salud_antes": ejecucion.get("SALUD_ANTES"),
            "salud_despues": ejecucion.get("SALUD_DESPUES"),
            "codigo_gatling": ejecucion.get("CODIGO_GATLING"),
        },
        "informe_gatling": str(informe.relative_to(carpeta)) if informe else None,
    }


def resumen_md(datos: dict, resultado: str, motivo: str, lista: list[dict]) -> str:
    iconos = {APROBADO: "✅ Aprobado", RECHAZADO: "❌ Rechazado por rendimiento", ERROR_INFRA: "⚠️ Error de infraestructura"}
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
    if lista:
        lineas += ["", "| Aserción | Actual | Cumple |", "|---|---:|:---:|"]
        lineas += [f"| {a['objetivo']}: {a['descripcion']} | {a['actual']} | {'sí' if a['cumple'] else 'no'} |" for a in lista]
    if not datos["estado"]["restablecido"]:
        lineas += ["", "> El estado de la base de datos no se restableció antes de medir."]
    return "\n".join(lineas) + "\n"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    carpeta = Path(sys.argv[1])
    ejecucion = leer_env(carpeta / "ejecucion.env")
    log = leer_texto(carpeta / "gatling.log")
    lista = aserciones(log)
    informe = informe_gatling(carpeta)

    resultado, motivo = decidir(ejecucion, log, lista, informe)
    datos = metadatos(carpeta, ejecucion, informe)

    (carpeta / "metadatos.json").write_text(json.dumps(datos, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (carpeta / "veredicto.json").write_text(json.dumps({
        "resultado": resultado,
        "codigo": CODIGOS[resultado],
        "motivo": motivo,
        "aserciones": lista,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    resumen = resumen_md(datos, resultado, motivo, lista)
    (carpeta / "resumen.md").write_text(resumen, encoding="utf-8")

    print(resumen)
    return CODIGOS[resultado]


if __name__ == "__main__":
    sys.exit(main())
