"""Decide el resultado de una campaña de calibración o de validación (T17).

Uso: python decision.py --modo calibracion|validacion --campana NOMBRE
                        [--repeticiones N] RESULTADOS

Lee resultados/campana-NOMBRE.json, que escribe campana.py, y aplica las
reglas de Taller.md §7 y de docs/PLAN-DE-PRUEBAS.md §6.5:

- Calibración: hacen falta N ejecuciones de carga válidas por variante y un
  umbral que quede a la distancia exigida de las dos. Si la hay, propone el
  umbral: el número redondo (1, 2, 3 o 5 por una potencia de 10) más cercano,
  en escala logarítmica, al punto medio del intervalo admisible, y escribe
  perfil-propuesto-NOMBRE.env con la tasa, el umbral y las duraciones de la
  campaña. La propuesta se revisa antes de congelarla: nunca se aplica sola.
- Validación: hacen falta N ejecuciones válidas por variante, y todas las de
  corregida deben aprobar y todas las de regresion deben ser rechazadas.

Escribe la decisión en decision-NOMBRE.md y termina con 0 si la campaña es
satisfactoria, 1 si no lo es y 2 si está incompleta (faltan ejecuciones
válidas: se repiten las inválidas antes de concluir).

Solo usa la biblioteca estándar.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from metricas import leer_env  # noqa: E402

SATISFACTORIA, NO_SATISFACTORIA, INCOMPLETA = 0, 1, 2
VARIANTES = ("corregida", "regresion")
REDONDOS = (1, 2, 3, 5)


def umbral_redondo(desde: float, hasta: float) -> float:
    """Número redondo dentro de [desde, hasta] más cercano al punto medio logarítmico."""
    medio = math.sqrt(desde * hasta)
    candidatos = [
        r * 10 ** e
        for e in range(math.floor(math.log10(desde)) - 1, math.ceil(math.log10(hasta)) + 1)
        for r in REDONDOS
        if desde <= r * 10 ** e <= hasta
    ]
    if not candidatos:
        return round(medio)
    return min(candidatos, key=lambda c: (abs(math.log(c / medio)), c))


def ms(valor: float) -> str:
    return f"{valor / 1000:,.1f} s".replace(",", " ").replace(".", ",") if valor >= 10_000 else f"{valor:,.0f} ms".replace(",", " ")


def grupos_carga(datos: dict) -> dict[str, dict]:
    """Grupo de cada variante en las ejecuciones de carga contra /productos."""
    return {g["variante"]: g for g in datos["grupos"]
            if g["tipo"] == "carga" and g["ruta"] == "productos" and g["variante"] in VARIANTES}


def faltantes(grupos: dict[str, dict], repeticiones: int) -> list[str]:
    lineas = []
    for v in VARIANTES:
        validas = grupos[v]["p95_ms"]["n"] if v in grupos else 0
        if validas < repeticiones:
            lineas.append(f"`{v}` tiene {validas} ejecuciones válidas de {repeticiones}.")
    return lineas


def configuracion(resultados: Path, variante: str) -> dict[str, str]:
    """Parámetros efectivos de una ejecución de la campaña (ejecucion.env)."""
    for env in sorted(resultados.rglob("ejecucion.env")):
        valores = leer_env(env)
        if valores.get("TIPO") == "carga" and valores.get("VARIANTE") == variante:
            return valores
    return {}


def calibracion(datos: dict, resultados: Path, repeticiones: int) -> tuple[int, list[str], str | None]:
    grupos = grupos_carga(datos)
    faltan = faltantes(grupos, repeticiones)
    if faltan:
        return INCOMPLETA, ["La campaña está incompleta: se repiten las ejecuciones inválidas antes de elegir el umbral.", *faltan], None
    tasas = {grupos[v]["tasa"] for v in VARIANTES}
    if len(tasas) != 1:
        return NO_SATISFACTORIA, ["Las variantes se midieron a tasas distintas: no se pueden comparar."], None
    tasa = tasas.pop()
    margen = next((m for m in datos["margenes"] if m["tasa"] == tasa and m["ruta"] == "productos"), None)
    if not margen or not margen["satisfactoria"]:
        exigido = datos["margen_exigido"]
        return NO_SATISFACTORIA, [f"No cabe un umbral a {exigido:g} veces de cada variante: la calibración no es "
                                  "satisfactoria. Se revisan la tasa o el entorno, nunca el margen."], None
    desde, hasta = margen["umbral_admisible_ms"]
    umbral = umbral_redondo(desde, hasta)
    base = configuracion(resultados, "corregida")
    perfil = base.get("PERFIL", "ci")
    lineas = [
        f"La calibración es satisfactoria. El umbral puede ir de {ms(desde)} a {ms(hasta)}; el punto medio en escala "
        f"logarítmica es {ms(math.sqrt(desde * hasta))} y la propuesta es {ms(umbral)}: "
        f"{umbral / margen['peor_p95_corregida_ms']:.0f} veces el peor p95 de `corregida` y "
        f"{margen['mejor_p95_regresion_ms'] / umbral:.0f} veces por debajo del mejor de `regresion`.",
        f"La propuesta está en `perfil-propuesto-{datos['campana']}.env`. Se revisa antes de copiarla a "
        f"`config/perfiles/{perfil}.env` y congelarla con una etiqueta nueva, y después se valida con una campaña nueva.",
    ]
    env = "\n".join([
        f"# Propuesta de perfil {perfil} de la campaña {datos['campana']} (Taller.md §7.1).",
        f"# Umbral admisible con un margen de {datos['margen_exigido']:g} veces: de {desde:.0f} a {hasta:.0f} ms.",
        "# Se revisa antes de congelarla; la validación es una campaña nueva (§7.2).",
        f"TASA={tasa:g}",
        f"UMBRAL_MS={umbral:g}",
        f"CALENTAMIENTO_S={base.get('CALENTAMIENTO_S', '')}",
        f"MEDICION_S={base.get('MEDICION_S', '')}",
        f"ERRORES_MAX_PCT={base.get('ERRORES_MAX_PCT', '')}",
    ]) + "\n"
    return SATISFACTORIA, lineas, env


def validacion(datos: dict, repeticiones: int) -> tuple[int, list[str]]:
    grupos = grupos_carga(datos)
    inesperadas = [e for e in datos["ejecuciones"]
                   if e["tipo"] == "carga" and e["ruta"] == "productos" and e["variante"] in VARIANTES
                   and e["resultado"] in ("aprobado", "rechazado")
                   and e["resultado"] != {"corregida": "aprobado", "regresion": "rechazado"}[e["variante"]]]
    if inesperadas:
        lineas = ["La validación falla: hay veredictos distintos de los esperados. El umbral no se ajusta con "
                  "estos datos; se abre una calibración nueva."]
        lineas += [f"`{e['ejecucion']}`: `{e['variante']}` quedó {e['resultado']} (p95 de {ms(e['p95_ms'])})."
                   for e in inesperadas if e["p95_ms"] is not None]
        return NO_SATISFACTORIA, lineas
    faltan = faltantes(grupos, repeticiones)
    if faltan:
        return INCOMPLETA, ["La validación está incompleta: las ejecuciones válidas dieron el veredicto esperado, "
                            "pero faltan repeticiones. Se repiten las inválidas.", *faltan]
    return SATISFACTORIA, ["La validación pasa: todas las ejecuciones válidas de `corregida` aprobaron y todas las de "
                           "`regresion` fueron rechazadas."]


def main() -> int:
    analizador = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizador.add_argument("--modo", required=True, choices=("calibracion", "validacion"))
    analizador.add_argument("--campana", required=True, help="nombre de la campaña, como en campana.py")
    analizador.add_argument("--repeticiones", type=int, default=3, help="ejecuciones válidas exigidas por variante")
    analizador.add_argument("resultados", type=Path, help="carpeta con campana-NOMBRE.json y las ejecuciones")
    args = analizador.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9._-]+", args.campana):
        analizador.error("el nombre solo admite letras, números, punto, guion y guion bajo")

    archivo = args.resultados / f"campana-{args.campana}.json"
    if not archivo.exists():
        print(f"decision: no existe {archivo}", file=sys.stderr)
        return INCOMPLETA
    datos = json.loads(archivo.read_text(encoding="utf-8"))

    env = None
    if args.modo == "calibracion":
        codigo, lineas, env = calibracion(datos, args.resultados, args.repeticiones)
    else:
        codigo, lineas = validacion(datos, args.repeticiones)
    titulo = {SATISFACTORIA: "✅", NO_SATISFACTORIA: "❌", INCOMPLETA: "⚠️"}[codigo]
    modo = "Calibración" if args.modo == "calibracion" else "Validación"
    texto = "\n\n".join([f"### {titulo} {modo} `{args.campana}`", *lineas]) + "\n"
    (args.resultados / f"decision-{args.campana}.md").write_text(texto, encoding="utf-8")
    if env:
        (args.resultados / f"perfil-propuesto-{args.campana}.env").write_text(env, encoding="utf-8")
    print(texto)
    return codigo


if __name__ == "__main__":
    sys.exit(main())
