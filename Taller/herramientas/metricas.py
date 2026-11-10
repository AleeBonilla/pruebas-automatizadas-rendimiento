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
    # Desde T10, la simulación registra la tasa y la duración de cada fase.
    tasa = intervalo.get("tasa_prevista", tasa)
    duracion = intervalo.get("duracion_prevista_s", duracion)
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
        "duracion_prevista_s": duracion,
        # Entre la primera y la última llegada hay iniciadas - 1 intervalos.
        "tasa_lograda": (iniciadas - 1) / inyeccion if iniciadas and iniciadas > 1 and inyeccion else None,
        "inyeccion_s": inyeccion,
        "duracion_s": duracion_real,
        "throughput_correctas": ok / duracion_real if ok is not None and duracion_real else None,
        "tiempos_ms": tiempos(estadisticas["columnas"]["total"]) if estadisticas else None,
        "tiempos_correctas_ms": tiempos(estadisticas["columnas"]["ok"]) if estadisticas else None,
        "errores": estadisticas["errores"] if estadisticas else [],
        # Serie por bloques de la simulación: tiempos medidos por ella, no por Gatling.
        "bloques": intervalo.get("bloques"),
    }


def cumple(p95: float | None, errores_pct: float | None, umbral: float | None, errores_max: float | None) -> bool | None:
    """Criterio del perfil, igual que las aserciones: p95 < umbral y errores <= máximo."""
    if None in (p95, errores_pct, umbral, errores_max):
        return None
    return p95 < umbral and errores_pct <= errores_max


def recuperacion(fases: dict, umbral: float | None, errores_max: float | None, bloque_s: float | None) -> dict | None:
    """Recuperación después de un pico (Taller.md §6.4).

    La recuperación se cuenta desde el primer bloque de la ventana a partir del
    cual todos los bloques cumplen el criterio del perfil hasta el final de la
    ventana. Si el último bloque no cumple, no hubo recuperación en la ventana.
    """
    if not {"base", "pico", "recuperacion"} <= fases.keys():
        return None
    base, pico, ventana = fases["base"], fases["pico"], fases["recuperacion"]
    bloques = ventana.get("bloques") or []

    def cumple_bloque(b: dict) -> bool:
        return bool(b["solicitudes"]) and bool(cumple(b["p95_ms"], 100 * b["fallidas"] / b["solicitudes"], umbral, errores_max))

    desde = len(bloques)
    while desde and cumple_bloque(bloques[desde - 1]):
        desde -= 1
    recuperada = desde < len(bloques) if bloques and umbral is not None and errores_max is not None else None
    return {
        "bloque_s": bloque_s,
        "ventana_s": ventana["duracion_prevista_s"],
        "base_cumple": cumple((base["tiempos_ms"] or {}).get("p95"), base["errores_pct"], umbral, errores_max),
        "pico_cumple": cumple((pico["tiempos_ms"] or {}).get("p95"), pico["errores_pct"], umbral, errores_max),
        "recuperada": recuperada,
        "recuperacion_s": bloques[desde]["desde_s"] if recuperada else None,
        "bloques_que_incumplen": sum(not cumple_bloque(b) for b in bloques),
        "bloques": len(bloques),
    }


def extraer(carpeta: Path) -> dict:
    """Resultados de la ejecución guardada en `carpeta`."""
    ejecucion = leer_env(carpeta / "ejecucion.env")
    fases_json = leer_json(carpeta / "fases.json") or {}
    intervalos = fases_json.get("fases") or {}
    parametros = fases_json.get("parametros") or {}
    informe = informe_gatling(carpeta)
    tasa = numero(ejecucion.get("TASA"))
    umbral = numero(ejecucion.get("UMBRAL_MS"))
    errores_max = numero(ejecucion.get("ERRORES_MAX_PCT"))
    # Las ejecuciones anteriores a T10 no registran la tasa ni la duración de cada fase.
    duraciones = {"calentamiento": numero(ejecucion.get("CALENTAMIENTO_S")), "medicion": numero(ejecucion.get("MEDICION_S"))}
    fases = {
        nombre: fase(nombre, intervalos.get(nombre),
                     estadisticas_solicitud(informe, nombre) if informe else None,
                     tasa, duraciones.get(nombre))
        for nombre in (list(intervalos) or ["calentamiento", "medicion"])
    }
    return {
        "ejecucion": carpeta.name,
        "tipo": ejecucion.get("TIPO"),
        "perfil": ejecucion.get("PERFIL"),
        "variante": ejecucion.get("VARIANTE"),
        "variante_api": fases_json.get("variante_api"),
        "ruta": ejecucion.get("RUTA"),
        "tasa": tasa,
        "pico_tasa": numero(ejecucion.get("PICO_TASA")),
        "umbral_ms": umbral,
        "errores_max_pct": errores_max,
        "bloque_s": parametros.get("bloqueS"),
        "revision": ejecucion.get("REVISION"),
        "inicio_utc": ejecucion.get("INICIO_UTC"),
        "fases": fases,
        "recuperacion": recuperacion(fases, umbral, errores_max, parametros.get("bloqueS")),
    }
