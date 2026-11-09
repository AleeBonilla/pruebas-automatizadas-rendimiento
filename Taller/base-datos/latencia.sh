#!/bin/sh
# Aplica la latencia de red de PostgreSQL y arranca el servidor (Taller.md §5.2).
#
# netem retrasa los paquetes que salen por eth0, así que cada ida y vuelta entre
# la API y PostgreSQL tarda LATENCIA_BD_MS milisegundos más. No afecta a la
# interfaz local, la que usa el healthcheck. Si tc falla, el contenedor no
# arranca: medir sin la latencia prevista sería medir otro sistema.
set -eu

ms="${LATENCIA_BD_MS:-0}"
if [ "$ms" != "0" ]; then
  tc qdisc replace dev eth0 root netem delay "${ms}ms"
  echo "latencia: ${ms} ms en cada ida y vuelta hacia PostgreSQL"
fi

exec docker-entrypoint.sh "$@"
