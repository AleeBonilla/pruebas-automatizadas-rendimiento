"""Configuración de Gunicorn (Taller.md 2 y 5.2).

Un solo proceso gthread con varios hilos: el candado de la variante regresion
es un threading.Lock, que solo coordina los hilos de su propio proceso.
"""

import os

wsgi_app = "tienda:crear_app()"
bind = "0.0.0.0:8000"
workers = 1
worker_class = "gthread"
threads = int(os.environ.get("HILOS", "8"))
timeout = 60
graceful_timeout = 10
keepalive = 5
accesslog = None  # escribir cada solicitud en el registro costaría tiempo durante la medición
errorlog = "-"
loglevel = "info"
