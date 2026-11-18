"""Compara UTC y reloj monotónico dentro de Docker, sin generar carga.

Uso: docker compose exec -T api python - < herramientas/diagnostico_reloj.py
En PowerShell: Get-Content herramientas/diagnostico_reloj.py | docker compose exec -T api python -
"""

import json
import time


def medir(segundos=90):
    inicio = previo = time.monotonic()
    utc = time.time()
    desajuste_previo = 0
    saltos, pausas = [], []
    while time.monotonic() - inicio < segundos:
        time.sleep(0.01)
        ahora = time.monotonic()
        desajuste = (time.time() - utc) - (ahora - inicio)
        if abs(desajuste - desajuste_previo) > 0.1:
            saltos.append({"desde_s": round(ahora - inicio, 3),
                           "salto_ms": round((desajuste - desajuste_previo) * 1000, 3)})
        if ahora - previo > 0.1:
            pausas.append(round(ahora - previo, 3))
        desajuste_previo, previo = desajuste, ahora
    return {"monotonico_s": time.monotonic() - inicio, "utc_s": time.time() - utc,
            "saltos_utc": saltos, "pausas_mayores_100ms_s": pausas}


if __name__ == "__main__":
    print(json.dumps(medir(), indent=2))
