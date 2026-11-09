"""Las tres implementaciones de GET /productos/{id} (Taller.md 4.2).

Todas reciben el pool y el identificador, y devuelven el producto como dict
o None si no existe. Ninguna modifica contadores cuando el producto no existe.
Cada bloque `with pool.connection()` es una transacción: se confirma al salir
sin error y se deshace si ocurre una excepción.
"""

import threading
import time

from . import metricas

COLUMNAS = "id, nombre, categoria, precio, visitas"

# Compartido por todos los hilos del proceso: Gunicorn usa un solo proceso.
candado = threading.Lock()


def visitar_regresion(pool, id_):
    """Lee, suma y escribe dentro de un candado global: correcta, pero serializa."""
    espera = time.perf_counter()
    metricas.CANDADO_EN_ESPERA.inc()
    with candado:  # una solicitud a la vez, sea cual sea el producto
        metricas.CANDADO_EN_ESPERA.dec()
        metricas.CANDADO_ESPERA.observe(time.perf_counter() - espera)
        with pool.connection() as con:
            producto = con.execute(
                f"SELECT {COLUMNAS} FROM productos WHERE id = %s", (id_,)
            ).fetchone()
            if producto is None:
                return None
            producto["visitas"] += 1
            con.execute(
                "UPDATE productos SET visitas = %s WHERE id = %s",
                (producto["visitas"], id_),
            )
            return producto


def visitar_corregida(pool, id_):
    """Incremento atómico en SQL, sin candado: PostgreSQL bloquea solo esa fila."""
    with pool.connection() as con:
        return con.execute(
            f"UPDATE productos SET visitas = visitas + 1 WHERE id = %s RETURNING {COLUMNAS}",
            (id_,),
        ).fetchone()


def visitar_sana(pool, id_):
    """Referencia: la consulta sola, sin registrar la visita."""
    with pool.connection() as con:
        return con.execute(
            f"SELECT {COLUMNAS} FROM productos WHERE id = %s", (id_,)
        ).fetchone()


VARIANTES = {
    "regresion": visitar_regresion,
    "corregida": visitar_corregida,
    "sana": visitar_sana,
}
