"""Extracción de resultados de una ejecución (Taller.md §6.4, T11).

Lo usan veredicto.py, que escribe metricas.json al cerrar cada ejecución, y
campana.py, que resume varias. Toma los conteos y los intervalos de fases.json,
que escribe la simulación, y los percentiles del informe HTML de Gatling: son
los mismos valores con los que Gatling evalúa las aserciones.

Solo usa la biblioteca estándar.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

# Filas de la tabla de estadísticas de cada solicitud en el informe de Gatling 3.16.
FILAS = {
    "Total count": "cantidad",
    "Min": "min",
    "50th percentile": "p50",
    "75th percentile": "p75",
    "95th percentile": "p95",
    "99th percentile": "p99",
    "Max": "max",
    "Mean": "media",
    "Standard Deviation": "desviacion",
}
FILA = re.compile(
    r'<td class="title">(?P<titulo>[^<]+)(?:</abbr>)?</td>\s*'
    r'<td class="total">(?P<total>[^<]*)</td>\s*<td class="ok">(?P<ok>[^<]*)</td>\s*<td class="ko">(?P<ko>[^<]*)</td>')
ERROR = re.compile(
    r'<td class="error-col-1 total ko">(?P<mensaje>.*?)<span[^>]*>[^<]*</span></td>\s*'
    r'<td class="value error-col-2 total ko">(?P<cantidad>[^<]*)</td>', re.S)


def leer_env(ruta: Path) -> dict[str, str]:
    """Lee un archivo KEY=VALUE ignorando comentarios, líneas vacías y CRLF."""
    valores: dict[str, str] = {}
    if not ruta.exists():
        return valores
    for linea in leer_texto(ruta).splitlines():
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
        return json.loads(leer_texto(ruta))
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


def numero(texto: str | None) -> float | None:
    """Convierte un valor del informe; «-» y vacío significan que no hay datos."""
    if texto is None:
        return None
    texto = texto.strip().replace(",", "")
    try:
        return float(texto)
    except ValueError:
        return None


def informe_gatling(carpeta: Path) -> Path | None:
    """Carpeta del informe HTML de Gatling dentro de gatling/, si existe."""
    for indice in sorted((carpeta / "gatling").glob("*/index.html")):
        return indice.parent
    return None


def estadisticas_solicitud(informe: Path, nombre: str) -> dict | None:
    """Tabla de estadísticas y errores de la solicitud `nombre` (una por fase)."""
    paginas = sorted(informe.glob(f"req_{nombre}-*.html"))
    if not paginas:
        return None
    pagina = leer_texto(paginas[0])
    columnas: dict[str, dict] = {"total": {}, "ok": {}, "ko": {}}
    for fila in FILA.finditer(pagina):
        clave = FILAS.get(fila["titulo"].strip())
        if clave:
            for columna in columnas:
                columnas[columna][clave] = numero(fila[columna])
    errores = [{"mensaje": html.unescape(e["mensaje"]).strip(), "cantidad": int(numero(e["cantidad"]) or 0)}
               for e in ERROR.finditer(pagina)]
    if columnas["total"].get("cantidad") is None:
        return None
    return {"columnas": columnas, "errores": errores}


def tiempos(columna: dict) -> dict:
    return {clave: columna.get(clave) for clave in ("p50", "p75", "p95", "p99", "max", "media", "desviacion", "min")}


def fase(nombre: str, intervalo: dict | None, estadisticas: dict | None, tasa: float | None, duracion: float | None) -> dict:
    """Resultados de una fase. Los campos que no se pueden calcular quedan en None."""
    intervalo = intervalo or {}
    iniciadas = intervalo.get("iniciadas")
    inyeccion = intervalo.get("inyeccion_s")
    duracion_real = intervalo.get("duracion_s")
    total = ok = ko = None
    if estadisticas:
        total = estadisticas["columnas"]["total"].get("cantidad")
        ok = estadisticas["columnas"]["ok"].get("cantidad")
        ko = estadisticas["columnas"]["ko"].get("cantidad")
        total, ok, ko = (int(v) if v is not None else None for v in (total, ok, ko))
    return {
        "fase": nombre,
        # Prevista: llegadas por segundo por duración de la inyección.
        "esperadas": round(tasa * duracion) if tasa is not None and duracion is not None else None,
        "iniciadas": iniciadas,
        "terminadas": intervalo.get("terminadas"),
        "completadas": total,
        "correctas": ok,
        "fallidas": ko,
        "errores_pct": 100.0 * ko / total if total else None,
        "tasa_prevista": tasa,
        # Entre la primera y la última llegada hay iniciadas - 1 intervalos.
        "tasa_lograda": (iniciadas - 1) / inyeccion if iniciadas and iniciadas > 1 and inyeccion else None,
        "inyeccion_s": inyeccion,
        "duracion_s": duracion_real,
        "throughput_correctas": ok / duracion_real if ok is not None and duracion_real else None,
        "tiempos_ms": tiempos(estadisticas["columnas"]["total"]) if estadisticas else None,
        "tiempos_correctas_ms": tiempos(estadisticas["columnas"]["ok"]) if estadisticas else None,
        "errores": estadisticas["errores"] if estadisticas else [],
    }


def extraer(carpeta: Path) -> dict:
    """Resultados de la ejecución guardada en `carpeta`."""
    ejecucion = leer_env(carpeta / "ejecucion.env")
    fases_json = leer_json(carpeta / "fases.json") or {}
    intervalos = fases_json.get("fases") or {}
    informe = informe_gatling(carpeta)
    tasa = numero(ejecucion.get("TASA"))
    duraciones = {"calentamiento": numero(ejecucion.get("CALENTAMIENTO_S")), "medicion": numero(ejecucion.get("MEDICION_S"))}
    return {
        "ejecucion": carpeta.name,
        "tipo": ejecucion.get("TIPO"),
        "perfil": ejecucion.get("PERFIL"),
        "variante": ejecucion.get("VARIANTE"),
        "variante_api": fases_json.get("variante_api"),
        "ruta": ejecucion.get("RUTA"),
        "tasa": tasa,
        "umbral_ms": numero(ejecucion.get("UMBRAL_MS")),
        "errores_max_pct": numero(ejecucion.get("ERRORES_MAX_PCT")),
        "revision": ejecucion.get("REVISION"),
        "inicio_utc": ejecucion.get("INICIO_UTC"),
        "fases": {
            nombre: fase(nombre, intervalos.get(nombre),
                         estadisticas_solicitud(informe, nombre) if informe else None,
                         tasa, duraciones[nombre])
            for nombre in ("calentamiento", "medicion")
        },
    }
