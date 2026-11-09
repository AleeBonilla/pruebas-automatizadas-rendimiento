"""Infraestructura de las pruebas funcionales y de concurrencia (T4).

Se ejecutan con `docker compose run --rm api pytest`, en un contenedor aparte
conectado al PostgreSQL del entorno. Cada variante se levanta en este mismo
proceso con un servidor HTTP de varios hilos, así que se prueban las tres sin
reiniciar el servicio `api` y con solicitudes HTTP reales y concurrentes.

Las pruebas modifican la tabla productos y la restablecen antes de cada una
y al terminar: no deben correr mientras se ejecuta una prueba de carga.
"""

import threading
from concurrent.futures import ThreadPoolExecutor

import psycopg
import pytest
import requests
from werkzeug.serving import make_server

from tienda import config, crear_app, crear_pool

VARIANTES_CON_CONTADOR = ("regresion", "corregida")
TODAS_LAS_VARIANTES = ("regresion", "corregida", "sana")


def sql(consulta, parametros=None):
    """Ejecuta una consulta directa a PostgreSQL, fuera de la API, y devuelve las filas."""
    with psycopg.connect(config.conninfo(), autocommit=True) as con:
        cursor = con.execute(consulta, parametros)
        return cursor.fetchall() if cursor.description else None


def visitas(id_):
    return sql("SELECT visitas FROM productos WHERE id = %s", (id_,))[0][0]


@pytest.fixture(autouse=True)
def estado_inicial():
    sql("CALL restablecer()")
    yield
    sql("CALL restablecer()")


class Servidor:
    """Una variante de la API servida por HTTP en un puerto libre de este contenedor."""

    def __init__(self, variante):
        self.pool = crear_pool()
        self.app = crear_app(variante, pool=self.pool)
        self._http = make_server("127.0.0.1", 0, self.app, threaded=True)
        self.url = f"http://127.0.0.1:{self._http.server_port}"
        self._hilo = threading.Thread(target=self._http.serve_forever, daemon=True)
        self._hilo.start()

    def get(self, ruta):
        return requests.get(self.url + ruta, timeout=30)

    def concurrentes(self, rutas, hilos=16):
        """Lanza las solicitudes desde varios hilos que arrancan a la vez."""
        barrera = threading.Barrier(hilos)
        local = threading.local()

        def esperar_y_pedir(ruta):
            if not getattr(local, "listo", False):
                barrera.wait()
                local.listo = True
                local.sesion = requests.Session()
            return local.sesion.get(self.url + ruta, timeout=30)

        # Cada hilo pide al menos una ruta, así que todos llegan a la barrera.
        assert len(rutas) >= hilos
        with ThreadPoolExecutor(max_workers=hilos) as ejecutor:
            return list(ejecutor.map(esperar_y_pedir, rutas))

    def cerrar(self):
        self._http.shutdown()
        self._hilo.join(timeout=10)
        self.pool.close()


@pytest.fixture(scope="module")
def servidores():
    """Arranca cada variante una sola vez por módulo y la cierra al final."""
    activos = {}

    def obtener(variante):
        if variante not in activos:
            activos[variante] = Servidor(variante)
        return activos[variante]

    yield obtener
    for servidor in activos.values():
        servidor.cerrar()
