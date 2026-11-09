-- Restablece datos y contadores antes de cada repetición (Taller.md §11).
-- Los scripts taller.ps1 y taller.sh lo ejecutan dentro de postgres:
--   psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f /base-datos/restablecer.sql
-- El procedimiento está definido en esquema.sql.
CALL restablecer();
