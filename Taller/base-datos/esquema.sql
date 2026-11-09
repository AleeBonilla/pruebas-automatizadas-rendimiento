-- Esquema y datos iniciales del taller.
--
-- PostgreSQL ejecuta este archivo una sola vez, al inicializar un volumen de
-- datos vacío (docker-entrypoint-initdb.d). Después, el estado se restablece
-- con restablecer.sql, que llama a CALL restablecer().

-- Copia inmutable de los datos generados con la semilla 42 (generar_datos.py).
CREATE TABLE productos_semilla (
    id        integer       PRIMARY KEY,
    nombre    text          NOT NULL,
    categoria text          NOT NULL,
    precio    numeric(6, 2) NOT NULL
);

COPY productos_semilla (id, nombre, categoria, precio)
    FROM '/base-datos/productos_semilla.csv'
    WITH (FORMAT csv, HEADER true);

-- Tabla que consulta y modifica la API.
CREATE TABLE productos (
    id        integer       PRIMARY KEY,
    nombre    text          NOT NULL,
    categoria text          NOT NULL,
    precio    numeric(6, 2) NOT NULL CHECK (precio BETWEEN 1 AND 500),
    visitas   integer       NOT NULL DEFAULT 0 CHECK (visitas >= 0)
);

-- Restablece datos y contadores. TRUNCATE y la nueva carga también eliminan
-- las versiones muertas que dejan los UPDATE de una repetición anterior, así
-- que cada repetición empieza con la tabla en el mismo estado físico.
CREATE PROCEDURE restablecer()
LANGUAGE plpgsql
AS $$
BEGIN
    TRUNCATE productos;
    INSERT INTO productos (id, nombre, categoria, precio)
        SELECT id, nombre, categoria, precio
        FROM productos_semilla
        ORDER BY id;
    ANALYZE productos;
END;
$$;

-- Resumen para comprobar el estado antes y después de una ejecución:
-- la huella solo depende de los datos de catálogo, no de las visitas.
CREATE VIEW resumen_datos AS
SELECT
    count(*)                         AS productos,
    count(DISTINCT categoria)        AS categorias,
    min(id)                          AS id_min,
    max(id)                          AS id_max,
    coalesce(sum(visitas), 0)        AS visitas_totales,
    md5(string_agg(id || ',' || nombre || ',' || categoria || ',' || precio,
                   E'\n' ORDER BY id)) AS huella
FROM productos;

CALL restablecer();
