"""Genera los datos sintéticos del taller con una semilla fija.

Produce dos archivos en esta carpeta:

- productos_semilla.csv: los 10 000 productos (id, nombre, categoria, precio),
  que PostgreSQL carga al inicializarse y que restablecer() vuelve a copiar.
- productos.csv: los identificadores 1..10 000, cada uno una vez, en un orden
  barajado con la misma semilla. Es el alimentador de Gatling.

Solo usa la biblioteca estándar. Con la misma semilla, la salida es idéntica
byte a byte; los archivos generados se versionan junto con este script.

Uso: python generar_datos.py [--semilla 42] [--cantidad 10000]
"""

import argparse
import random
from pathlib import Path

CATEGORIAS = (
    "alimentos",
    "belleza",
    "deportes",
    "hogar",
    "juguetes",
    "libros",
    "mascotas",
    "ropa",
)
PRECIO_MIN_CENTAVOS = 100      # 1.00
PRECIO_MAX_CENTAVOS = 50_000   # 500.00


def generar(semilla: int, cantidad: int, carpeta: Path) -> None:
    rng = random.Random(semilla)

    with open(carpeta / "productos_semilla.csv", "w", encoding="utf-8", newline="\n") as f:
        f.write("id,nombre,categoria,precio\n")
        for id_ in range(1, cantidad + 1):
            categoria = rng.choice(CATEGORIAS)
            centavos = rng.randint(PRECIO_MIN_CENTAVOS, PRECIO_MAX_CENTAVOS)
            precio = f"{centavos // 100}.{centavos % 100:02d}"
            f.write(f"{id_},Producto {id_},{categoria},{precio}\n")

    ids = list(range(1, cantidad + 1))
    rng.shuffle(ids)
    with open(carpeta / "productos.csv", "w", encoding="utf-8", newline="\n") as f:
        f.write("id\n")
        f.writelines(f"{id_}\n" for id_ in ids)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--semilla", type=int, default=42)
    parser.add_argument("--cantidad", type=int, default=10_000)
    args = parser.parse_args()
    generar(args.semilla, args.cantidad, Path(__file__).resolve().parent)


if __name__ == "__main__":
    main()
