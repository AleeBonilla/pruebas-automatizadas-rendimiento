"""Pruebas de decision.py sobre campañas sintéticas (T17).

Uso: python -m unittest discover -s herramientas -p "prueba_*.py"

Los casos reproducen las campañas reales de Taller.md §7: el umbral propuesto
debe coincidir con el que se eligió a mano en perfil-ci-v1 y perfil-local-v1.
"""

from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import decision  # noqa: E402


def ejecucion(variante: str, p95: float, resultado: str) -> dict:
    return {"ejecucion": f"x-carga-{variante}", "tipo": "carga", "variante": variante, "ruta": "productos",
            "tasa": 150, "umbral_ms": 3000, "resultado": resultado, "p95_ms": p95}


def campana(corregida: list, regresion: list, margen: float = 3.0, invalidas: int = 0) -> dict:
    """Campaña con el formato de campana.py; cada lista tiene los p95 válidos."""
    ejecuciones = [ejecucion("corregida", p, "aprobado" if p < 3000 else "rechazado") for p in corregida]
    ejecuciones += [ejecucion("regresion", p, "aprobado" if p < 3000 else "rechazado") for p in regresion]
    ejecuciones += [ejecucion("corregida", None, "invalido") for _ in range(invalidas)]
    grupos = [
        {"tipo": "carga", "ruta": "productos", "tasa": 150, "variante": v, "p95_ms": {"n": len(ps)}}
        for v, ps in (("corregida", corregida), ("regresion", regresion))
    ]
    peor, mejor = max(corregida, default=0), min(regresion, default=0)
    margenes = []
    if corregida and regresion:
        desde, hasta = margen * peor, mejor / margen
        margenes.append({"ruta": "productos", "tasa": 150, "peor_p95_corregida_ms": peor,
                         "mejor_p95_regresion_ms": mejor, "satisfactoria": desde <= hasta,
                         "umbral_admisible_ms": [desde, hasta] if desde <= hasta else None})
    return {"campana": "prueba", "margen_exigido": margen, "ejecuciones": ejecuciones,
            "grupos": grupos, "margenes": margenes}


class UmbralRedondo(unittest.TestCase):
    def test_perfil_ci(self):
        # Primera calibración de ci: de 750 ms a 15,6 s; se eligió 3 000 ms.
        self.assertEqual(decision.umbral_redondo(750, 15_600), 3000)

    def test_perfil_local(self):
        # Calibración local: de 30 ms a 20 s; se eligió 1 000 ms.
        self.assertEqual(decision.umbral_redondo(30, 20_000), 1000)

    def test_dentro_del_intervalo(self):
        umbral = decision.umbral_redondo(410, 470)
        self.assertTrue(410 <= umbral <= 470)


class Calibracion(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())

    def test_satisfactoria_propone_perfil(self):
        codigo, _, env = decision.calibracion(campana([10, 9, 60], [59_200, 54_700, 54_400]), self.dir, 3)
        self.assertEqual(codigo, decision.SATISFACTORIA)
        self.assertIn("TASA=150", env)
        self.assertIn("UMBRAL_MS=", env)

    def test_sin_separacion(self):
        codigo, _, env = decision.calibracion(campana([500, 400, 300], [900, 1000, 1100]), self.dir, 3)
        self.assertEqual(codigo, decision.NO_SATISFACTORIA)
        self.assertIsNone(env)

    def test_incompleta(self):
        codigo, _, _ = decision.calibracion(campana([10, 9], [59_000, 58_000, 57_000], invalidas=1), self.dir, 3)
        self.assertEqual(codigo, decision.INCOMPLETA)


class Validacion(unittest.TestCase):
    def test_pasa(self):
        codigo, _ = decision.validacion(campana([114, 9, 9], [58_400, 58_600, 58_900]), 3)
        self.assertEqual(codigo, decision.SATISFACTORIA)

    def test_corregida_rechazada(self):
        codigo, _ = decision.validacion(campana([114, 9, 4_000], [58_400, 58_600, 58_900]), 3)
        self.assertEqual(codigo, decision.NO_SATISFACTORIA)

    def test_regresion_aprobada(self):
        codigo, _ = decision.validacion(campana([9, 9, 9], [58_400, 2_000, 58_900]), 3)
        self.assertEqual(codigo, decision.NO_SATISFACTORIA)

    def test_incompleta(self):
        codigo, _ = decision.validacion(campana([9, 9], [58_400, 58_600, 58_900], invalidas=1), 3)
        self.assertEqual(codigo, decision.INCOMPLETA)


class Principal(unittest.TestCase):
    def test_escribe_decision_y_propuesta(self):
        carpeta = Path(tempfile.mkdtemp())
        (carpeta / "campana-prueba.json").write_text(
            json.dumps(campana([10, 9, 60], [59_200, 54_700, 54_400])), encoding="utf-8")
        argv = sys.argv
        sys.argv = ["decision.py", "--modo", "calibracion", "--campana", "prueba", str(carpeta)]
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(decision.main(), decision.SATISFACTORIA)
        finally:
            sys.argv = argv
        self.assertTrue((carpeta / "decision-prueba.md").exists())
        self.assertTrue((carpeta / "perfil-propuesto-prueba.env").exists())


if __name__ == "__main__":
    unittest.main()
