"""API REST de productos del taller (Taller.md 4.1).

Operaciones:
- GET /productos/<id>: el producto; en las variantes con contador, registra una visita.
- GET /salud: respuesta mínima sin base de datos (healthcheck y prueba del generador).
- GET /metrics: métricas para Prometheus.

Gunicorn la carga con `tienda:crear_app()` (gunicorn.conf.py).
"""

import re
import time

from flask import Flask, g, jsonify, request
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool
from werkzeug.exceptions import HTTPException

from . import config, metricas
from .variantes import VARIANTES

ID_MAXIMO = 2**31 - 1  # rango de integer en PostgreSQL
SIN_MEDIR = {"/metrics"}


def plantilla(regla):
    """'/productos/<int:id>' -> '/productos/{id}': una serie por ruta, no por producto."""
    return re.sub(r"<(?:[^:>]+:)?([^>]+)>", r"{\1}", regla)


def crear_pool(conexiones=None):
    conexiones = conexiones or config.conexiones()
    pool = ConnectionPool(
        config.conninfo(),
        min_size=conexiones,
        max_size=conexiones,  # pool fijo: una conexión por hilo (5.2)
        kwargs={"row_factory": dict_row},
        open=True,
        name="api-taller",
    )
    pool.wait(timeout=30)  # falla al arrancar si PostgreSQL no responde
    return pool


def crear_app(variante=None, pool=None):
    variante = variante or config.variante()
    visitar = VARIANTES[variante]
    pool = pool or crear_pool()

    app = Flask(__name__)
    app.json.sort_keys = False  # conserva el orden de campos del contrato
    app.extensions["pool"] = pool
    app.extensions["variante"] = variante

    for nombre in VARIANTES:
        metricas.VARIANTE.labels(nombre).set(1 if nombre == variante else 0)

    @app.get("/productos/<int:id>")
    def producto(id):  # noqa: A002 - el nombre coincide con el contrato
        fila = visitar(pool, id) if id <= ID_MAXIMO else None
        if fila is None:
            return jsonify(error="producto no encontrado"), 404
        return jsonify(
            id=fila["id"],
            nombre=fila["nombre"],
            categoria=fila["categoria"],
            precio=float(fila["precio"]),
            visitas=fila["visitas"],
        )

    @app.get("/salud")
    def salud():
        return jsonify(estado="ok", variante=variante)

    @app.get("/metrics")
    def metrics():
        return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

    @app.errorhandler(HTTPException)
    def error_http(error):
        return jsonify(error=error.description), error.code

    @app.errorhandler(Exception)
    def error_interno(error):
        app.logger.exception("Error al atender %s %s", request.method, request.path)
        return jsonify(error="error interno"), 500

    # Instrumentación: cuenta y mide cada solicitud, excepto /metrics.
    @app.before_request
    def iniciar_medicion():
        if request.path not in SIN_MEDIR:
            g.inicio = time.perf_counter()
            metricas.EN_CURSO.inc()

    @app.after_request
    def registrar_medicion(respuesta):
        if "inicio" in g:
            ruta = plantilla(request.url_rule.rule) if request.url_rule else "sin_ruta"
            metricas.DURACION.labels(ruta, request.method).observe(time.perf_counter() - g.inicio)
            metricas.SOLICITUDES.labels(ruta, request.method, str(respuesta.status_code)).inc()
        return respuesta

    @app.teardown_request
    def terminar_medicion(_error):
        if "inicio" in g:
            metricas.EN_CURSO.dec()

    return app
