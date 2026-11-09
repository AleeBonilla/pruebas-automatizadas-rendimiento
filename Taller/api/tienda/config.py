"""Configuración de la API, leída de variables de entorno (compose.yaml)."""

import os

VARIANTES_VALIDAS = ("regresion", "corregida", "sana")


def variante() -> str:
    valor = os.environ.get("VARIANTE", "corregida").strip().lower()
    if valor not in VARIANTES_VALIDAS:
        raise ValueError(f"VARIANTE={valor!r} no es válida; use una de {VARIANTES_VALIDAS}")
    return valor


def conninfo() -> str:
    return (
        f"host={os.environ.get('PGHOST', 'postgres')} "
        f"port={os.environ.get('PGPORT', '5432')} "
        f"dbname={os.environ.get('PGDATABASE', 'tienda')} "
        f"user={os.environ.get('PGUSER', 'taller')} "
        f"password={os.environ.get('PGPASSWORD', 'taller')} "
        "application_name=api-taller"
    )


def conexiones() -> int:
    """Tamaño fijo del pool: por defecto, una conexión por hilo de Gunicorn (5.2)."""
    return int(os.environ.get("POOL_CONEXIONES", os.environ.get("HILOS", "8")))
