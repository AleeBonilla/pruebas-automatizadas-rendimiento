"""Concurrencia (Taller.md 4.3): el contador final coincide con las visitas confirmadas.

Una visita confirmada es una respuesta 200. Además de contarlas, se comprueba
que los valores de `visitas` devueltos para un mismo producto sean 1..N sin
repetirse: si dos solicitudes devolvieran el mismo número, una visita se
habría perdido aunque el total coincidiera por casualidad.

La última prueba es el control negativo: un leer-sumar-escribir sin candado,
que solo existe aquí, debe fallar esta misma comprobación.
"""

from collections import Counter, defaultdict

import pytest

from conftest import VARIANTES_CON_CONTADOR, Servidor, sql, visitas
from tienda import variantes

SOLICITUDES = 400
HILOS = 16


def comprobar_contadores(rutas, respuestas):
    """Devuelve la lista de discrepancias entre la base de datos y las respuestas 200."""
    confirmadas = Counter()
    devueltas = defaultdict(list)
    for ruta, respuesta in zip(rutas, respuestas):
        assert respuesta.status_code == 200, f"{ruta}: {respuesta.status_code}"
        cuerpo = respuesta.json()
        confirmadas[cuerpo["id"]] += 1
        devueltas[cuerpo["id"]].append(cuerpo["visitas"])

    problemas = []
    for id_, n in confirmadas.items():
        if visitas(id_) != n:
            problemas.append(f"producto {id_}: {n} confirmadas, {visitas(id_)} registradas")
        if sorted(devueltas[id_]) != list(range(1, n + 1)):
            problemas.append(f"producto {id_}: valores devueltos repetidos o con huecos")
    total = sql("SELECT visitas_totales FROM resumen_datos")[0][0]
    if total != sum(confirmadas.values()):
        problemas.append(f"total: {sum(confirmadas.values())} confirmadas, {total} registradas")
    return problemas


@pytest.mark.parametrize("variante", VARIANTES_CON_CONTADOR)
def test_mismo_producto(servidores, variante):
    rutas = ["/productos/1"] * SOLICITUDES

    respuestas = servidores(variante).concurrentes(rutas, hilos=HILOS)

    assert comprobar_contadores(rutas, respuestas) == []
    assert visitas(1) == SOLICITUDES


@pytest.mark.parametrize("variante", VARIANTES_CON_CONTADOR)
def test_productos_distintos(servidores, variante):
    # 40 productos con 10 visitas cada uno, intercalados para que coincidan en el tiempo.
    rutas = [f"/productos/{1 + (i % 40) * 250}" for i in range(SOLICITUDES)]

    respuestas = servidores(variante).concurrentes(rutas, hilos=HILOS)

    assert comprobar_contadores(rutas, respuestas) == []
    assert sql("SELECT count(*) FROM productos WHERE visitas = 10")[0][0] == 40


def visitar_sin_candado(pool, id_):
    """El error que la corrección debe evitar: leer, sumar y escribir sin protección."""
    with pool.connection() as con:
        producto = con.execute(
            f"SELECT {variantes.COLUMNAS} FROM productos WHERE id = %s", (id_,)
        ).fetchone()
        if producto is None:
            return None
        producto["visitas"] += 1
        con.execute("UPDATE productos SET visitas = %s WHERE id = %s",
                    (producto["visitas"], id_))
        return producto


def test_control_negativo_un_contador_sin_proteccion_pierde_visitas(monkeypatch):
    monkeypatch.setitem(variantes.VARIANTES, "sin_candado", visitar_sin_candado)
    servidor = Servidor("sin_candado")
    rutas = ["/productos/1"] * SOLICITUDES
    try:
        respuestas = servidor.concurrentes(rutas, hilos=HILOS)
    finally:
        servidor.cerrar()

    problemas = comprobar_contadores(rutas, respuestas)

    assert problemas, "la prueba de concurrencia no detectó visitas perdidas"
    assert visitas(1) < SOLICITUDES
