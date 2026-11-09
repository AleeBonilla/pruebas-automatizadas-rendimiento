"""Reversión ante fallos (Taller.md 4.3).

Un disparador hace fallar la transacción después de escribir la visita del
producto 7. La API debe responder 500, deshacer la escritura y seguir
atendiendo: en regresion, el candado se libera; en ambas, las conexiones
vuelven al pool aunque fallen más solicitudes que conexiones hay.
"""

import pytest

from conftest import VARIANTES_CON_CONTADOR, sql, visitas

PRODUCTO_QUE_FALLA = 7
FALLOS = 20  # más que las 8 conexiones del pool


@pytest.fixture
def fallo_despues_de_escribir():
    sql("""
        CREATE FUNCTION fallo_inyectado() RETURNS trigger LANGUAGE plpgsql AS $$
        BEGIN
            RAISE EXCEPTION 'fallo inyectado por la prueba de reversión';
        END $$;
    """)
    sql(f"""
        CREATE TRIGGER fallo_inyectado AFTER UPDATE ON productos
        FOR EACH ROW WHEN (NEW.id = {PRODUCTO_QUE_FALLA})
        EXECUTE FUNCTION fallo_inyectado();
    """)
    yield
    sql("DROP TRIGGER IF EXISTS fallo_inyectado ON productos")
    sql("DROP FUNCTION IF EXISTS fallo_inyectado()")


@pytest.mark.parametrize("variante", VARIANTES_CON_CONTADOR)
def test_un_fallo_deshace_la_visita_y_la_api_sigue_atendiendo(
        servidores, variante, fallo_despues_de_escribir):
    servidor = servidores(variante)

    estados = [servidor.get(f"/productos/{PRODUCTO_QUE_FALLA}").status_code for _ in range(FALLOS)]
    siguiente = servidor.get("/productos/8")

    assert estados == [500] * FALLOS
    assert visitas(PRODUCTO_QUE_FALLA) == 0
    assert siguiente.status_code == 200
    assert visitas(8) == 1


@pytest.mark.parametrize("variante", VARIANTES_CON_CONTADOR)
def test_fallos_concurrentes_no_bloquean_a_otras_solicitudes(
        servidores, variante, fallo_despues_de_escribir):
    servidor = servidores(variante)
    rutas = [f"/productos/{PRODUCTO_QUE_FALLA if i % 2 else 100 + i}" for i in range(64)]

    respuestas = servidor.concurrentes(rutas)

    for ruta, respuesta in zip(rutas, respuestas):
        esperado = 500 if ruta.endswith(f"/{PRODUCTO_QUE_FALLA}") else 200
        assert respuesta.status_code == esperado, ruta
    assert visitas(PRODUCTO_QUE_FALLA) == 0
    assert sql("SELECT visitas_totales FROM resumen_datos")[0][0] == 32
