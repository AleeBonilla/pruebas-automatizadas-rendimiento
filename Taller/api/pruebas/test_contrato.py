"""Contrato de la API (Taller.md 4.1) en las tres variantes."""

import pytest
from prometheus_client.parser import text_string_to_metric_families

from conftest import TODAS_LAS_VARIANTES, VARIANTES_CON_CONTADOR, sql, visitas

CAMPOS = ["id", "nombre", "categoria", "precio", "visitas"]


@pytest.mark.parametrize("variante", TODAS_LAS_VARIANTES)
def test_producto_existente_cumple_el_contrato(servidores, variante):
    respuesta = servidores(variante).get("/productos/4182")

    assert respuesta.status_code == 200
    assert respuesta.headers["Content-Type"] == "application/json"
    cuerpo = respuesta.json()
    assert list(cuerpo) == CAMPOS
    nombre, categoria, precio = sql(
        "SELECT nombre, categoria, precio FROM productos_semilla WHERE id = 4182")[0]
    assert cuerpo["id"] == 4182
    assert cuerpo["nombre"] == nombre == "Producto 4182"
    assert cuerpo["categoria"] == categoria
    assert cuerpo["precio"] == float(precio)
    assert isinstance(cuerpo["visitas"], int)


@pytest.mark.parametrize("variante", VARIANTES_CON_CONTADOR)
def test_cada_consulta_registra_una_visita(servidores, variante):
    servidor = servidores(variante)

    devueltas = [servidor.get("/productos/17").json()["visitas"] for _ in range(3)]

    assert devueltas == [1, 2, 3]
    assert visitas(17) == 3
    assert visitas(18) == 0


def test_sana_no_registra_visitas(servidores):
    servidor = servidores("sana")

    devueltas = [servidor.get("/productos/17").json()["visitas"] for _ in range(3)]

    assert devueltas == [0, 0, 0]
    assert visitas(17) == 0


@pytest.mark.parametrize("variante", TODAS_LAS_VARIANTES)
@pytest.mark.parametrize("id_", [0, 10_001, 2**31 - 1, 2**31, 10**20])
def test_producto_inexistente_devuelve_404_sin_modificar_contadores(servidores, variante, id_):
    respuesta = servidores(variante).get(f"/productos/{id_}")

    assert respuesta.status_code == 404
    assert respuesta.json() == {"error": "producto no encontrado"}
    assert sql("SELECT visitas_totales FROM resumen_datos")[0][0] == 0


@pytest.mark.parametrize("ruta", ["/productos/abc", "/productos/-1", "/no-existe"])
def test_ruta_inexistente_devuelve_404_en_json(servidores, ruta):
    respuesta = servidores("corregida").get(ruta)

    assert respuesta.status_code == 404
    assert "error" in respuesta.json()


@pytest.mark.parametrize("variante", TODAS_LAS_VARIANTES)
def test_salud_informa_la_variante_sin_tocar_la_base_de_datos(servidores, variante):
    respuesta = servidores(variante).get("/salud")

    assert respuesta.status_code == 200
    assert respuesta.json() == {"estado": "ok", "variante": variante}


def test_metrics_expone_las_metricas_del_taller(servidores):
    servidor = servidores("regresion")
    servidor.get("/productos/1")

    muestras = [
        muestra
        for familia in text_string_to_metric_families(servidor.get("/metrics").text)
        for muestra in familia.samples
    ]
    nombres = {muestra.name for muestra in muestras}

    assert {
        "http_solicitudes_total",
        "http_duracion_solicitud_segundos_bucket",
        "http_solicitudes_en_curso",
        "taller_candado_espera_segundos_bucket",
        "taller_candado_en_espera",
        "taller_variante_info",
        "process_cpu_seconds_total",
        "process_resident_memory_bytes",
    } <= nombres
    assert any(
        m.name == "http_solicitudes_total"
        and m.labels == {"ruta": "/productos/{id}", "metodo": "GET", "estado": "200"}
        and m.value >= 1
        for m in muestras
    )
    # La ruta se etiqueta con su plantilla: no hay una serie por producto.
    assert not any(m.labels.get("ruta", "").startswith("/productos/1") for m in muestras)


def test_datos_semilla(servidores):
    productos, categorias, id_min, id_max, total, _huella = sql("SELECT * FROM resumen_datos")[0]
    precio_min, precio_max = sql("SELECT min(precio), max(precio) FROM productos")[0]

    assert (productos, categorias, id_min, id_max, total) == (10_000, 8, 1, 10_000, 0)
    assert 1 <= precio_min and precio_max <= 500
