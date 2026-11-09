# PostgreSQL con tc, para dar a la base de datos una latencia de red realista,
# la de un servidor aparte en la misma región (Taller.md §5.2).
FROM postgres:18.6-alpine

# Versión fija, como el resto del entorno (Taller.md §5.1).
RUN apk add --no-cache iproute2-tc=7.0.0-r0

COPY --chmod=755 latencia.sh /usr/local/bin/latencia.sh

ENTRYPOINT ["latencia.sh"]
CMD ["postgres"]
