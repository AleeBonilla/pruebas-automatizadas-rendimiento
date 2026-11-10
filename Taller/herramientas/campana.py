"""Resume una campaña: varias ejecuciones de calibración, de validación o de estrés (T11).

Uso: python campana.py --nombre NOMBRE [--margen M] RUTA...

Cada RUTA es la carpeta de una ejecución o una carpeta que contiene
ejecuciones, como un artefacto de GitHub Actions descomprimido. Escribe
campana-NOMBRE.json y campana-NOMBRE.md junto a la primera ruta (en el taller,
en resultados/).

El resumen sigue Taller.md §7: todas las ejecuciones en orden, incluidas las
inválidas y su motivo; por variante, el rango, la mediana y el coeficiente de
variación del p95 de las ejecuciones válidas, y, si hay `corregida` y
`regresion` a la misma tasa, los márgenes respecto del umbral y el intervalo
de umbrales que respeta el margen M. Los márgenes y los veredictos esperados
solo se calculan con ejecuciones de carga; las de estrés y picos son informativas.

Solo usa la biblioteca estándar.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from metricas import extraer, leer_json  # noqa: E402

VALIDOS = ("aprobado", "rechazado", "informativo")
ESPERADO = {"corregida": "aprobado", "regresion": "rechazado"}


def ejecuciones(rutas: list[Path]) -> list[Path]:
    encontradas: set[Path] = set()
    for ruta in rutas:
        if (ruta / "ejecucion.env").exists():
            encontradas.add(ruta)
        else:
            encontradas.update(p.parent for p in ruta.rglob("ejecucion.env"))
    # El nombre empieza con la hora UTC, así que ordena por fecha.
    return sorted(encontradas, key=lambda p: p.name)


def ejecucion(carpeta: Path) -> dict:
    resultados = leer_json(carpeta / "metricas.json") or extraer(carpeta)
    veredicto = leer_json(carpeta / "veredicto.json") or {}
    fases = resultados["fases"]
    # En picos, la fase que resume la ejecución es el pico.
    medicion = fases.get("medicion") or fases.get("pico") or {}
    recuperacion = resultados.get("recuperacion") or {}
    return {
        "ejecucion": resultados["ejecucion"],
        "tipo": resultados.get("tipo") or "carga",
        "variante": resultados["variante"],
        "ruta": resultados["ruta"],
        "perfil": resultados["perfil"],
        "tasa": resultados["tasa"],
        "umbral_ms": resultados["umbral_ms"],
        "resultado": veredicto.get("resultado", "sin veredicto"),
        "motivo": veredicto.get("motivo"),
        "cumple_criterio": veredicto.get("cumple_criterio"),
        "recuperada": recuperacion.get("recuperada"),
        "recuperacion_s": recuperacion.get("recuperacion_s"),
        "p50_ms": (medicion.get("tiempos_ms") or {}).get("p50"),
        "p95_ms": (medicion.get("tiempos_ms") or {}).get("p95"),
        "p99_ms": (medicion.get("tiempos_ms") or {}).get("p99"),
        "errores_pct": medicion.get("errores_pct"),
        "tasa_lograda": medicion.get("tasa_lograda"),
        "throughput_correctas": medicion.get("throughput_correctas"),
    }


def resumen(valores: list[float]) -> dict:
    if not valores:
        return {"n": 0}
    media = statistics.fmean(valores)
    return {
        "n": len(valores),
        "min": min(valores),
        "mediana": statistics.median(valores),
        "max": max(valores),
        "media": media,
        # Con una sola ejecución no hay variación que medir.
        "cv_pct": 100 * statistics.stdev(valores) / media if len(valores) > 1 and media else None,
    }


def grupos(lista: list[dict]) -> dict[tuple, list[dict]]:
    agrupadas: dict[tuple, list[dict]] = {}
    for e in lista:
        agrupadas.setdefault((e["tipo"], e["ruta"], e["tasa"], e["variante"]), []).append(e)
    return agrupadas


def margenes(por_variante: dict[str, list[dict]], margen: float) -> dict | None:
    corregida = [e["p95_ms"] for e in por_variante.get("corregida", []) if e["resultado"] in VALIDOS and e["p95_ms"] is not None]
    regresion = [e["p95_ms"] for e in por_variante.get("regresion", []) if e["resultado"] in VALIDOS and e["p95_ms"] is not None]
    if not corregida or not regresion:
        return None
    peor_corregida, mejor_regresion = max(corregida), min(regresion)
    umbrales = {e["umbral_ms"] for v in ("corregida", "regresion") for e in por_variante.get(v, [])}
    umbral = umbrales.pop() if len(umbrales) == 1 else None
    desde, hasta = margen * peor_corregida, mejor_regresion / margen
    return {
        "peor_p95_corregida_ms": peor_corregida,
        "mejor_p95_regresion_ms": mejor_regresion,
        "separacion": mejor_regresion / peor_corregida if peor_corregida else None,
        "umbral_ms": umbral,
        "margen_sobre_corregida": umbral / peor_corregida if umbral and peor_corregida else None,
        "margen_bajo_regresion": mejor_regresion / umbral if umbral else None,
        "margen_exigido": margen,
        "umbral_admisible_ms": [desde, hasta] if desde <= hasta else None,
        "satisfactoria": desde <= hasta,
    }


def campana(nombre: str, carpetas: list[Path], margen: float) -> dict:
    lista = [ejecucion(c) for c in carpetas]
    salida = {"campana": nombre, "margen_exigido": margen, "ejecuciones": lista, "grupos": []}
    por_tasa: dict[tuple, dict[str, list[dict]]] = {}
    for (tipo, ruta, tasa, variante), miembros in grupos(lista).items():
        validas = [e for e in miembros if e["resultado"] in VALIDOS]
        esperado = ESPERADO.get(variante) if tipo == "carga" else None
        salida["grupos"].append({
            "tipo": tipo, "ruta": ruta, "tasa": tasa, "variante": variante,
            "ejecuciones": len(miembros),
            "invalidas": len(miembros) - len(validas),
            "veredicto_esperado": esperado,
            "veredictos_esperados": all(e["resultado"] == esperado for e in validas) if esperado and validas else None,
            "p95_ms": resumen([e["p95_ms"] for e in validas if e["p95_ms"] is not None]),
            "errores_pct": resumen([e["errores_pct"] for e in validas if e["errores_pct"] is not None]),
        })
        if tipo == "carga":
            por_tasa.setdefault((ruta, tasa), {})[variante] = miembros
    salida["margenes"] = [
        {"ruta": ruta, "tasa": tasa, **m}
        for (ruta, tasa), por_variante in por_tasa.items()
        if (m := margenes(por_variante, margen))
    ]
    return salida


def ms(valor) -> str:
    if valor is None:
        return "—"
    return f"{valor / 1000:,.1f} s".replace(",", " ").replace(".", ",") if valor >= 10_000 else f"{valor:,.0f} ms".replace(",", " ")


def pct(valor) -> str:
    return "—" if valor is None else f"{valor:.1f} %".replace(".", ",")


def veces(valor) -> str:
    return "—" if valor is None else f"{valor:.1f}×".replace(".", ",")


ETIQUETAS = {"aprobado": "aprobado", "rechazado": "rechazado", "invalido": "inválido"}


def etiqueta(e: dict) -> str:
    """Resultado de una ejecución; las informativas dicen qué observaron."""
    if e["resultado"] != "informativo":
        return ETIQUETAS.get(e["resultado"], e["resultado"])
    if e["tipo"] == "estres":
        return "cumple" if e["cumple_criterio"] else "no cumple"
    if e["recuperada"] is None:
        return "informativo"
    return f"recuperada a los {e['recuperacion_s']:g} s" if e["recuperada"] else "sin recuperación"


def variante(nombre: str, ruta: str | None) -> str:
    """Las ejecuciones contra /salud comprueban el generador, no la variante."""
    return f"`{nombre}`" + (" (`/salud`)" if ruta == "salud" else "")


def markdown(datos: dict) -> str:
    lineas = [f"# Campaña {datos['campana']}", "", "## Ejecuciones", "",
              "| # | Ejecución | Tipo | Variante | Tasa | Resultado | p50 | p95 | p99 | Errores | Tasa lograda "
              "| Correctas/s |",
              "|---:|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|"]
    for i, e in enumerate(datos["ejecuciones"], 1):
        tasa = "—" if e["tasa_lograda"] is None else f"{e['tasa_lograda']:.1f}/s".replace(".", ",")
        correctas = "—" if e["throughput_correctas"] is None else f"{e['throughput_correctas']:.1f}".replace(".", ",")
        lineas.append(f"| {i} | `{e['ejecucion']}` | {e['tipo']} | {variante(e['variante'], e['ruta'])} | {e['tasa']:g}/s "
                      f"| {etiqueta(e)} "
                      f"| {ms(e['p50_ms'])} | {ms(e['p95_ms'])} | {ms(e['p99_ms'])} | {pct(e['errores_pct'])} | {tasa} "
                      f"| {correctas} |")
    invalidas = [e for e in datos["ejecuciones"] if e["resultado"] not in VALIDOS]
    if invalidas:
        lineas += ["", "Ejecuciones sin veredicto válido:", ""]
        lineas += [f"- `{e['ejecucion']}`: {e['motivo'] or e['resultado']}." for e in invalidas]

    lineas += ["", "## p95 de las ejecuciones válidas", "",
               "| Tipo | Variante | Tasa | Válidas | Rango | Mediana | Coef. de variación | Veredictos esperados |",
               "|---|---|---:|---:|---|---:|---:|---|"]
    for g in datos["grupos"]:
        p = g["p95_ms"]
        rango = f"{ms(p['min'])} – {ms(p['max'])}" if p["n"] else "—"
        esperados = {True: "sí", False: "no", None: "—"}[g["veredictos_esperados"]]
        lineas.append(f"| {g['tipo']} | {variante(g['variante'], g['ruta'])} | {g['tasa']:g}/s | {p['n']} de {g['ejecuciones']} | {rango} "
                      f"| {ms(p.get('mediana'))} | {pct(p.get('cv_pct'))} | {esperados} |")

    for m in datos["margenes"]:
        lineas += ["", f"## Márgenes a {m['tasa']:g}/s", "",
                   f"- Peor p95 de `corregida`: {ms(m['peor_p95_corregida_ms'])}; mejor p95 de `regresion`: "
                   f"{ms(m['mejor_p95_regresion_ms'])}; separación: {veces(m['separacion'])}."]
        if m["umbral_ms"]:
            lineas.append(f"- Umbral de {ms(m['umbral_ms'])}: {veces(m['margen_sobre_corregida'])} sobre el peor "
                          f"`corregida` y {veces(m['margen_bajo_regresion'])} bajo el mejor `regresion`.")
        if m["satisfactoria"]:
            desde, hasta = m["umbral_admisible_ms"]
            lineas.append(f"- Con un margen de {veces(m['margen_exigido'])} a cada lado, el umbral puede ir de "
                          f"{ms(desde)} a {ms(hasta)}.")
        else:
            lineas.append(f"- No cabe un umbral con un margen de {veces(m['margen_exigido'])} a cada lado: "
                          "la calibración no es satisfactoria.")
    lineas += ["", "*El p95 de una ejecución con más de un 5 % de* timeouts *queda acotado por el límite de espera "
               "de Gatling (60 s), así que la dispersión de esas ejecuciones se subestima. En picos, los tiempos "
               "son los del pico.*"]
    return "\n".join(lineas) + "\n"


def main() -> int:
    analizador = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizador.add_argument("--nombre", required=True, help="nombre de la campaña, sin espacios")
    analizador.add_argument("--margen", type=float, default=3.0, help="margen mínimo a cada lado del umbral")
    analizador.add_argument("rutas", nargs="+", type=Path)
    args = analizador.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9._-]+", args.nombre):
        analizador.error("el nombre solo admite letras, números, punto, guion y guion bajo")

    carpetas = ejecuciones(args.rutas)
    if not carpetas:
        print("campana: no se encontraron ejecuciones en las rutas indicadas", file=sys.stderr)
        return 2
    datos = campana(args.nombre, carpetas, args.margen)
    destino = args.rutas[0] if not (args.rutas[0] / "ejecucion.env").exists() else args.rutas[0].parent
    (destino / f"campana-{args.nombre}.json").write_text(
        json.dumps(datos, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    texto = markdown(datos)
    (destino / f"campana-{args.nombre}.md").write_text(texto, encoding="utf-8")
    print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
