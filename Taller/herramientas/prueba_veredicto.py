"""Pruebas de veredicto.py y metricas.py sobre ejecuciones sintéticas (T10, T11, T12).

Uso: python -m unittest discover -s herramientas -p "prueba_*.py"
En el taller: docker compose -f compose.yaml -f compose.carga.yaml --profile carga \
  run --rm --no-deps herramientas -m unittest discover -s /herramientas -p "prueba_*.py"

Cada prueba parte de una ejecución válida de 150 llegadas por segundo durante
180 s y cambia una sola cosa, para comprobar que cada regla de validez de
Taller.md §6.4 la detecta por sí sola.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import veredicto  # noqa: E402

ESPERADAS = 150 * 180

ENV = {
    "TIPO": "carga", "PERFIL": "ci", "VARIANTE": "corregida", "RUTA": "productos",
    "SIMULACION": "taller.rendimiento.CargaSimulation", "TASA": "150", "UMBRAL_MS": "3000",
    "CALENTAMIENTO_S": "60", "MEDICION_S": "180", "ERRORES_MAX_PCT": "1.0",
    "REVISION": "0" * 40, "CAMBIOS_SIN_CONFIRMAR": "no", "RESTABLECIDO": "si",
    "SALUD_ANTES": "healthy", "SALUD_DESPUES": "healthy", "CODIGO_GATLING": "0",
}

ERROR_HTML = """
<tr>
  <td class="error-col-1 total ko">{mensaje}<span class="value" style="display:none">0</span></td>
  <td class="value error-col-2 total ko">{cantidad}</td>
  <td class="value error-col-3 total ko">100%</td>
</tr>"""


def fila(titulo: str, total, ok, ko) -> str:
    return (f'<tr><td class="title">{titulo}</td><td class="total">{total}</td>'
            f'<td class="ok">{ok}</td><td class="ko">{ko}</td></tr>')


class Ejecucion:
    """Carpeta de una ejecución sintética, con valores modificables antes de escribirla."""

    def __init__(self) -> None:
        self.env = dict(ENV)
        self.fases = {
            "simulacion": "CargaSimulation",
            "variante_api": "corregida",
            "parametros": {"ruta": "productos", "tasa": 150.0, "umbralMs": 3000, "erroresMaxPct": 1.0,
                           "calentamientoS": 60, "medicionS": 180},
            "fases": {
                "calentamiento": {"inicio_ms": 0, "fin_ms": 60_010, "duracion_s": 60.01, "ultimo_inicio_ms": 59_993,
                                  "inyeccion_s": 59.993, "iniciadas": 9000, "terminadas": 9000},
                "medicion": {"inicio_ms": 60_020, "fin_ms": 240_030, "duracion_s": 180.01, "ultimo_inicio_ms": 240_013,
                             "inyeccion_s": 179.993, "iniciadas": ESPERADAS, "terminadas": ESPERADAS},
            },
        }
        self.total, self.ko, self.p95 = ESPERADAS, 0, 9
        self.errores: list[tuple[str, int]] = []
        self.p95_cumple = True
        self.escribir_fases = True

    def escribir(self, carpeta: Path) -> Path:
        carpeta.mkdir(parents=True)
        (carpeta / "ejecucion.env").write_text("\n".join(f"{k}={v}" for k, v in self.env.items()), encoding="utf-8")
        if self.escribir_fases:
            (carpeta / "fases.json").write_text(json.dumps(self.fases), encoding="utf-8")
        errores_pct = 100 * self.ko / self.total if self.total else 0
        (carpeta / "gatling.log").write_text(
            f"medicion: 95th percentile of response time is less than 3000.0 : {str(self.p95_cumple).lower()} "
            f"(actual : {self.p95}.0)\n"
            f"medicion: percentage of failed events is less than or equal to 1.0 : {str(errores_pct <= 1).lower()} "
            f"(actual : {errores_pct})\n", encoding="utf-8")
        informe = carpeta / "gatling" / "cargasimulation-1"
        informe.mkdir(parents=True)
        (informe / "index.html").write_text("<html></html>", encoding="utf-8")
        (informe / "req_medicion--1.html").write_text(pagina(self.total, self.ko, self.p95, self.errores), encoding="utf-8")
        return carpeta


def pagina(total: int, ko: int, p95: int, errores: list[tuple[str, int]]) -> str:
    """Página de una solicitud del informe de Gatling, con la tabla de estadísticas y los errores."""
    filas = [fila("Total count", total, total - ko, ko),
             fila("50th percentile", 8, 8, "-"), fila("95th percentile", p95, p95, "-"),
             fila("99th percentile", 12, 12, "-"), fila("Max", 40, 40, "-")]
    lista = "".join(ERROR_HTML.format(mensaje=m, cantidad=c) for m, c in errores)
    return "<table>" + "".join(filas) + "</table><table id=\"container_errors\"><tbody>" + lista + "</tbody></table>"


def bloque(desde_s: int, p95: int, solicitudes: int = 250, fallidas: int = 0) -> dict:
    return {"desde_s": desde_s, "solicitudes": solicitudes, "fallidas": fallidas, "p50_ms": p95, "p95_ms": p95, "max_ms": p95}


class Pico:
    """Ejecución sintética de picos: base de 50/s durante 20 s, pico de 150/s
    durante 30 s y ventana de recuperación de 60 s a 50/s (T10)."""

    def __init__(self) -> None:
        self.env = dict(ENV, TIPO="picos", PERFIL="piloto", SIMULACION="taller.rendimiento.PicosSimulation",
                        TASA="50", UMBRAL_MS="300", CALENTAMIENTO_S="20", MEDICION_S="60",
                        PICO_TASA="150", PICO_S="30")
        self.fases = {
            "simulacion": "PicosSimulation",
            "variante_api": "corregida",
            "parametros": {"ruta": "productos", "tasa": 50.0, "umbralMs": 300, "erroresMaxPct": 1.0,
                           "calentamientoS": 20, "medicionS": 60, "picoTasa": 150.0, "picoS": 30, "bloqueS": 5},
            "fases": {
                "base": self.fase(0, 50, 20),
                "pico": self.fase(20_000, 150, 30),
                "recuperacion": self.fase(50_000, 50, 60),
            },
        }
        self.p95 = {"base": 15, "pico": 12_000, "recuperacion": 9_000}
        # Por defecto, la ventana se recupera a los 10 s.
        self.fases["fases"]["recuperacion"]["bloques"] = (
            [bloque(0, 9_000), bloque(5, 2_000)] + [bloque(s, 15) for s in range(10, 60, 5)])

    @staticmethod
    def fase(inicio_ms: int, tasa: int, duracion_s: int) -> dict:
        n = tasa * duracion_s
        inyeccion = (n - 1) / tasa
        return {"inicio_ms": inicio_ms, "fin_ms": inicio_ms + duracion_s * 1000 + 20, "duracion_s": duracion_s + 0.02,
                "ultimo_inicio_ms": inicio_ms + round(inyeccion * 1000), "inyeccion_s": inyeccion,
                "iniciadas": n, "terminadas": n, "tasa_prevista": float(tasa), "duracion_prevista_s": duracion_s,
                "bloques": [bloque(s, 15, tasa * 5) for s in range(0, duracion_s, 5)]}

    def escribir(self, carpeta: Path) -> Path:
        carpeta.mkdir(parents=True)
        (carpeta / "ejecucion.env").write_text("\n".join(f"{k}={v}" for k, v in self.env.items()), encoding="utf-8")
        (carpeta / "fases.json").write_text(json.dumps(self.fases), encoding="utf-8")
        # Sin aserciones: Gatling termina sin evaluarlas.
        (carpeta / "gatling.log").write_text("[INFO] BUILD SUCCESS\n", encoding="utf-8")
        informe = carpeta / "gatling" / "picossimulation-1"
        informe.mkdir(parents=True)
        (informe / "index.html").write_text("<html></html>", encoding="utf-8")
        for nombre, f in self.fases["fases"].items():
            (informe / f"req_{nombre}--1.html").write_text(pagina(f["iniciadas"], 0, self.p95[nombre], []), encoding="utf-8")
        return carpeta


class PruebaVeredicto(unittest.TestCase):

    def setUp(self) -> None:
        self.temporal = tempfile.TemporaryDirectory()
        self.base = Path(self.temporal.name)
        self.n = 0

    def tearDown(self) -> None:
        self.temporal.cleanup()

    def cerrar(self, ejecucion: Ejecucion) -> dict:
        self.n += 1
        carpeta = ejecucion.escribir(self.base / f"e{self.n}")
        veredicto.cerrar(carpeta)
        return json.loads((carpeta / "veredicto.json").read_text(encoding="utf-8"))

    def assertInvalida(self, ejecucion: Ejecucion, fragmento: str) -> None:
        resultado = self.cerrar(ejecucion)
        self.assertEqual(resultado["resultado"], "invalido", resultado["motivo"])
        self.assertEqual(resultado["codigo"], 2)
        self.assertIn(fragmento, resultado["motivo"])

    # Ejecuciones válidas.

    def test_ejecucion_valida_que_cumple_aprueba(self):
        resultado = self.cerrar(Ejecucion())
        self.assertEqual((resultado["resultado"], resultado["codigo"]), ("aprobado", 0), resultado["motivo"])

    def test_ejecucion_valida_que_incumple_es_rechazada(self):
        e = Ejecucion()
        e.p95, e.p95_cumple = 46_927, False
        self.assertEqual(self.cerrar(e)["resultado"], "rechazado")

    def test_los_timeouts_de_la_api_rechazan_y_no_invalidan(self):
        e = Ejecucion()
        e.ko, e.p95, e.p95_cumple = 6000, 60_000, False
        e.errores = [("i.n.c.ConnectTimeoutException: connection timed out after 10000 ms: api/172.20.0.3:8000", 5000),
                     ("Request timeout to api/172.20.0.3:8000 after 60000 ms", 1000)]
        self.assertEqual(self.cerrar(e)["resultado"], "rechazado")

    def test_metricas_json_tiene_la_tasa_lograda_y_los_percentiles(self):
        carpeta = Ejecucion().escribir(self.base / "metricas")
        veredicto.cerrar(carpeta)
        medicion = json.loads((carpeta / "metricas.json").read_text(encoding="utf-8"))["fases"]["medicion"]
        self.assertAlmostEqual(medicion["tasa_lograda"], 150.0, places=1)
        self.assertEqual(medicion["tiempos_ms"]["p95"], 9)
        self.assertEqual((medicion["completadas"], medicion["fallidas"]), (ESPERADAS, 0))

    # Preparación.

    def test_api_no_sana_antes_de_medir(self):
        e = Ejecucion()
        e.env["SALUD_ANTES"] = "starting"
        self.assertInvalida(e, "no estaba sana")

    def test_estado_no_restablecido(self):
        e = Ejecucion()
        e.env["RESTABLECIDO"] = "no"
        self.assertInvalida(e, "no se restableció")

    def test_api_detenida_durante_la_medicion(self):
        e = Ejecucion()
        e.env["SALUD_DESPUES"] = "exited"
        self.assertInvalida(e, "dejó de correr")

    # Configuración distinta de la prevista.

    def test_parametro_distinto_del_pedido(self):
        e = Ejecucion()
        e.fases["parametros"]["tasa"] = 20.0
        self.assertInvalida(e, "tasa=20.0")

    def test_variante_de_la_api_distinta_de_la_pedida(self):
        e = Ejecucion()
        e.fases["variante_api"] = "regresion"
        self.assertInvalida(e, "atendía la variante regresion")

    # Generador.

    def test_generador_sin_puertos(self):
        e = Ejecucion()
        e.ko = 300
        e.errores = [("j.n.BindException: Cannot assign requested address", 300)]
        self.assertInvalida(e, "el generador no pudo enviar 300")

    def test_menos_solicitudes_que_las_previstas(self):
        e = Ejecucion()
        e.fases["fases"]["medicion"].update(iniciadas=26_000, terminadas=26_000)
        e.total = 26_000
        self.assertInvalida(e, "se iniciaron 26000")

    def test_tasa_no_alcanzada(self):
        e = Ejecucion()
        e.fases["fases"]["medicion"]["inyeccion_s"] = 200.0
        self.assertInvalida(e, "no sostuvo la tasa")

    # Datos y métricas incompletos.

    def test_solicitudes_sin_terminar(self):
        e = Ejecucion()
        e.fases["fases"]["medicion"]["terminadas"] = ESPERADAS - 5
        self.assertInvalida(e, f"terminaron {ESPERADAS - 5}")

    def test_informe_con_otra_cantidad(self):
        e = Ejecucion()
        e.total = ESPERADAS - 10
        self.assertInvalida(e, "el informe de Gatling registra")

    def test_sin_fases_json(self):
        e = Ejecucion()
        e.escribir_fases = False
        self.assertInvalida(e, "falta fases.json")

    def test_fases_sin_conteos(self):
        e = Ejecucion()
        for clave in ("iniciadas", "terminadas", "inyeccion_s", "ultimo_inicio_ms"):
            del e.fases["fases"]["medicion"][clave]
        self.assertInvalida(e, "no registra las solicitudes")

    # Estrés (T10): informativo, con las mismas reglas de validez.

    def test_estres_que_incumple_es_informativo(self):
        e = Ejecucion()
        e.env["TIPO"] = "estres"
        e.p95, e.p95_cumple = 46_927, False
        resultado = self.cerrar(e)
        self.assertEqual((resultado["resultado"], resultado["codigo"]), ("informativo", 0), resultado["motivo"])
        self.assertFalse(resultado["cumple_criterio"])
        self.assertIn("a 150/s no cumple", resultado["motivo"])

    def test_estres_que_cumple(self):
        e = Ejecucion()
        e.env["TIPO"] = "estres"
        resultado = self.cerrar(e)
        self.assertEqual(resultado["resultado"], "informativo")
        self.assertTrue(resultado["cumple_criterio"])

    def test_estres_con_tasa_no_alcanzada_es_invalido(self):
        e = Ejecucion()
        e.env["TIPO"] = "estres"
        e.fases["fases"]["medicion"]["inyeccion_s"] = 200.0
        self.assertInvalida(e, "no sostuvo la tasa")

    # Picos (T10): recuperación por bloques y validez de las tres fases.

    def test_pico_con_recuperacion(self):
        resultado = self.cerrar(Pico())
        self.assertEqual((resultado["resultado"], resultado["codigo"]), ("informativo", 0), resultado["motivo"])
        r = resultado["recuperacion"]
        self.assertEqual((r["recuperada"], r["recuperacion_s"], r["bloques_que_incumplen"]), (True, 10, 2))
        self.assertEqual((r["base_cumple"], r["pico_cumple"]), (True, False))
        self.assertIn("se recupera 10 s después del pico", resultado["motivo"])

    def test_pico_sin_recuperacion_en_la_ventana(self):
        p = Pico()
        p.fases["fases"]["recuperacion"]["bloques"][-1] = bloque(55, 842)
        resultado = self.cerrar(p)
        self.assertFalse(resultado["recuperacion"]["recuperada"])
        self.assertIn("no se recupera dentro de la ventana de 60 s", resultado["motivo"])

    def test_pico_un_bloque_con_errores_no_cumple(self):
        p = Pico()
        p.fases["fases"]["recuperacion"]["bloques"][-1] = bloque(55, 15, fallidas=10)
        self.assertFalse(self.cerrar(p)["recuperacion"]["recuperada"])

    def test_pico_sin_degradacion(self):
        p = Pico()
        p.p95["pico"] = 20
        p.fases["fases"]["recuperacion"]["bloques"] = [bloque(s, 15) for s in range(0, 60, 5)]
        resultado = self.cerrar(p)
        self.assertEqual(resultado["recuperacion"]["recuperacion_s"], 0)
        self.assertIn("todos los bloques cumplen", resultado["motivo"])

    def test_pico_no_sostenido_por_el_generador(self):
        p = Pico()
        p.fases["fases"]["pico"]["inyeccion_s"] = 40.0
        self.assertInvalida(p, "no sostuvo la tasa en el pico")

    def test_pico_con_parametro_distinto(self):
        p = Pico()
        p.fases["parametros"]["picoTasa"] = 300.0
        self.assertInvalida(p, "picoTasa=300.0")


if __name__ == "__main__":
    unittest.main()
