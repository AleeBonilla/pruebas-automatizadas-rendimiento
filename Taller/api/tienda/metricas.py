"""Métricas que la API expone en /metrics para Prometheus (Taller.md 6.5).

Se usa el registro por defecto de prometheus_client, que con un solo proceso
ya incluye la CPU (process_cpu_seconds_total) y la memoria residente
(process_resident_memory_bytes) del proceso. Ninguna métrica se etiqueta por
producto: la ruta se registra con su plantilla, no con el identificador.
"""

from prometheus_client import Counter, Gauge, Histogram

# Intervalos pensados para tiempos de 1 ms a 10 s; cubren desde una consulta
# rápida hasta la fila que forma el candado bajo sobrecarga.
INTERVALOS = (
    0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.15, 0.2, 0.3,
    0.5, 0.75, 1.0, 1.5, 2.5, 5.0, 10.0,
)

SOLICITUDES = Counter(
    "http_solicitudes",
    "Solicitudes HTTP atendidas, por ruta, método y estado.",
    ("ruta", "metodo", "estado"),
)

DURACION = Histogram(
    "http_duracion_solicitud_segundos",
    "Tiempo que la API tarda en atender una solicitud, medido dentro de Flask.",
    ("ruta", "metodo"),
    buckets=INTERVALOS,
)

EN_CURSO = Gauge(
    "http_solicitudes_en_curso",
    "Solicitudes que la API está atendiendo en este momento (sin contar /metrics).",
)

CANDADO_ESPERA = Histogram(
    "taller_candado_espera_segundos",
    "Tiempo que una solicitud espera para obtener el candado (solo variante regresion).",
    buckets=INTERVALOS,
)

CANDADO_EN_ESPERA = Gauge(
    "taller_candado_en_espera",
    "Hilos esperando el candado en este momento (solo variante regresion).",
)

VARIANTE = Gauge(
    "taller_variante_info",
    "Variante activa de la API; vale 1 para la variante en ejecución.",
    ("variante",),
)
