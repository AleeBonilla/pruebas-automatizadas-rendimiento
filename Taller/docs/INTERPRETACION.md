# Interpretación de los resultados

Esta guía explica cómo leer lo que deja cada ejecución: el resumen y el veredicto, el informe de Gatling, los archivos de métricas y los paneles de Grafana. El procedimiento para obtenerlos está en [`GUIA.md`](GUIA.md), y las razones del diseño, en [`Taller.md`](../Taller.md) §6.4 y §6.5.

Los ejemplos salen de dos ejecuciones de carga con el perfil `ci` (150 solicitudes por segundo, 60 s de calentamiento y 180 s de medición) en una segunda computadora, distinta de la que calibró el perfil `local`: Intel Core i5-12450H, Docker Desktop 29.9 con 12 núcleos y 7,6 GB, Windows 11 con `taller.sh` en Git Bash, el 10 de noviembre de 2026.

| Variante | p50 | p95 | p99 | Errores | Correctas/s | Veredicto |
|---|---:|---:|---:|---:|---:|---|
| `corregida` | 9 ms | 12 ms | 14 ms | 0 % | 150,0 | Aprobado |
| `regresion` | 31,0 s | 60 s | 60 s | 42,9 % | 66,3 | Rechazado por rendimiento |

*Medición de `20261110T224259Z-carga-corregida` y `20261110T224735Z-carga-regresion`. El techo de `regresion` es más bajo que en la computadora de desarrollo (unas 81 respuestas correctas por segundo), pero el veredicto es el mismo: es lo que debe repetirse entre computadoras, no los milisegundos.*

## 1. Orden de lectura

1. **`resumen.md`**: el veredicto y, si es inválido, el motivo. Una ejecución inválida no dice nada de la variante, así que no se sigue leyendo: se corrige la causa y se repite.
2. **Informe de Gatling**, en la página de la solicitud `medicion`: qué vio el cliente y por qué se aprobó o se rechazó.
3. **`metricas.json` y `fases.json`**: los conteos de cada fase, la tasa lograda y, en los picos, la serie por bloques de 5 s.
4. **Grafana**, con el intervalo de `fases.json`: qué pasaba dentro de la API mientras tanto.

Gatling decide el veredicto; Grafana lo explica. Si los dos parecen contradecirse, manda Gatling, y la diferencia suele decir dónde se pierde el tiempo (sección 6).

## 2. Resumen y veredicto

`resumen.md` empieza con el resultado: ✅ aprobado, ❌ rechazado por rendimiento, ℹ️ informativo (estrés y picos) o ⚠️ inválido. Debajo aparecen tres tablas:

| Tabla | Columna | Interpretación |
|---|---|---|
| Ejecución | Revisión | El commit medido. «(con cambios)» indica que había archivos sin confirmar: sirve para practicar, pero no para una campaña de calibración o validación |
| Fases | p50 · p95 · p99 | Percentiles de Gatling sobre **todas** las solicitudes de la fase, también las fallidas, con el tiempo que tardaron en fallar. Son los que evalúan las aserciones |
| Fases | Errores | Solicitudes fallidas sobre completadas. Incluye esperas agotadas, conexiones no aceptadas y respuestas distintas de `200` |
| Fases | Iniciadas | «27000 de 27000»: solicitudes que salieron frente a las previstas (tasa × duración). Si se apartan más de un 0,5 %, la ejecución es inválida |
| Fases | Tasa lograda | Llegadas por segundo que sostuvo el generador. Por debajo del 98 % de la prevista, la ejecución es inválida |
| Aserciones | Actual | El valor con que Gatling comparó cada aserción. En `regresion`: 60000,0 ms frente a 3000 y 42,85 % frente a 1,0 |

Un rechazo con las dos aserciones incumplidas, como el de `regresion`, no depende de un umbral fino: la variante está lejos de cumplir. Un rechazo por poco, con el p95 apenas sobre el umbral y sin errores, se repite antes de sacar conclusiones, porque puede ser ruido (`Taller.md` §7.1).

## 3. Informe de Gatling

El informe está en `gatling/cargasimulation-*/index.html`. La página principal mezcla el calentamiento y la medición. Lo que cuenta está en el menú *Details*, en la solicitud `medicion` (en los picos: `base`, `pico` y `recuperacion`).

| Sección | Qué muestra | `corregida` | `regresion` | Cuidado |
|---|---|---|---|---|
| *Global Information* / *Stats* | Cantidad, percentiles, media y desviación, en tres columnas: *Total*, *OK* y *KO* | p50 9 ms y p95 12 ms; p50 y p95 casi iguales | p50 de 31 s: no son unas pocas solicitudes lentas, es toda la fila. p95 *Total* de 60 s y p95 *OK* de 44,4 s | Las aserciones usan la columna *Total*. El p95 *OK* deja afuera justamente las peores |
| *Ranges* | Solicitudes de menos de 800 ms, entre 800 y 1 200 ms, de más de 1 200 ms y fallidas | Todas en el primer rango | Casi ninguna en el primero; el resto, lentas o fallidas | Los cortes de 800 y 1 200 ms son los de Gatling por omisión, no el umbral del perfil |
| *Errors* | Cada tipo de error con su cantidad | Vacía | 9 265 `ConnectTimeoutException ... after 10000 ms`, 2 075 `Request timeout ... after 60000 ms` y 230 `PrematureCloseException` | Ninguno es un error de la API: son esperas del cliente (sección 6) |
| *Assertions* | Cada aserción con su resultado | Las dos cumplen | Las dos fallan | Es la misma tabla de `resumen.md` |
| *Users start rate* | Usuarios que empiezan por segundo | Recta en 150 | Recta en 150 | Debe ser plana: es el modelo abierto. Si baja, el generador no sostuvo la tasa |
| *Concurrent users* | Usuarios con una solicitud en curso | 1 o 2: 150 por segundo por unos 10 ms (ley de Little) | Crece hasta miles: cada usuario que espera en la fila sigue activo | Del lado del cliente sí se ve la fila completa; en Grafana, no (sección 5) |
| *Response time distribution* | Histograma de tiempos | Un pico angosto cerca de 10 ms | Repartido hasta 60 s, con un pico en el límite de espera | El pico en 60 s es el *timeout*, no un tiempo real |
| *Response time percentiles* | Percentiles a lo largo de la ejecución | Planos | Crecen mientras la fila crece | Solo incluye las respuestas correctas (*OK*): subestima la cola de `regresion` |
| *Requests / sec* · *Responses / sec* | Solicitudes enviadas y respuestas recibidas por segundo | Las dos en 150 | Se envían 150; se responden unas 66 correctas y el resto falla. Las respuestas siguen después de la inyección, mientras se vacía la fila | La distancia entre las dos curvas es la fila que se acumula |

En la carga, la medición empieza cuando terminan todas las solicitudes del calentamiento (`andThen`, `Taller.md` §6.3). En `regresion`, el calentamiento duró 105,6 s en lugar de 60: el servidor pasó unos 45 s vaciando la fila sin llegadas nuevas, y la medición empezó con el servidor descansado. En los gráficos se ve como un hueco entre las dos fases.

## 4. `metricas.json` y `fases.json`

`fases.json` lo escribe la simulación: el inicio y el fin UTC de cada fase, las solicitudes iniciadas y terminadas, la tasa y la duración previstas, y la serie por bloques de 5 s con los tiempos que mide ella misma. `metricas.json` lo escribe `veredicto.py` combinando `fases.json` con el informe.

| Campo de cada fase | Interpretación |
|---|---|
| `esperadas` · `iniciadas` · `terminadas` | Previstas, enviadas y cerradas por la simulación. Deben coincidir; si no, la ejecución es inválida |
| `completadas` · `correctas` · `fallidas` | Las que registró el informe y cómo terminaron. `fallidas` sobre `completadas` es la tasa de error |
| `tasa_lograda` | Ritmo real de la inyección: `(iniciadas − 1) / inyeccion_s` |
| `duracion_s` | Desde la primera llegada hasta la última respuesta. En `regresion` supera la duración prevista porque la fila tarda en vaciarse |
| `throughput_correctas` | Respuestas correctas por segundo: 150,0 en `corregida` y 66,3 en `regresion`, el techo del candado en esta computadora |
| `tiempos_ms` · `tiempos_correctas_ms` | Percentiles de la columna *Total* y de la *OK*. El veredicto usa los primeros |
| `bloques` | Por cada bloque de 5 s según la hora de salida: cantidad, fallidas, p50, p95 y máximo. Los picos los usan para calcular la recuperación |

## 5. Paneles de Grafana

El panel «API del taller» está en <http://localhost:3000>. Las horas de `fases.json` están en UTC y Grafana muestra la hora local, así que el intervalo se ajusta con esa diferencia. Prometheus consulta `/metrics` cada 5 s y espera hasta 4 s cada respuesta.

| Panel | Mide | `corregida` | `regresion` | Cuidado |
|---|---|---|---|---|
| Variante activa | `taller_variante_info` | `corregida` | `regresion` | Confirma qué variante atendía antes de leer el resto |
| Respuestas por segundo | Respuestas de `GET /productos/{id}` contadas por la API | 150 | De 40 a 70 mientras hay datos | Cuenta lo que la API terminó, no lo que llegó |
| Errores | Fracción de respuestas 5xx | 0 | 0 | Solo cuenta errores que la API respondió. Los 42,9 % de errores de Gatling son esperas del cliente y no aparecen aquí |
| Recolección | `up`: 1 si la última consulta a `/metrics` respondió | 1 | 0 durante casi toda la sobrecarga | Un 0 con la API en pie significa que `/metrics` no respondió en 4 s |
| Solicitudes y errores | Respuestas por segundo según el código de estado | Solo `200`, en 150 | Solo `200`, más bajo y con huecos | Igual que el panel de errores: los *timeouts* no tienen código |
| Tiempo en la API | p50, p95 y p99 estimados con el histograma, desde que un hilo toma la solicitud | p50 de unos 8 ms; p95 de 10 a 18 ms | Bajo mientras hay datos: cada visita tarda unos 10 ms con el candado | No es el tiempo del cliente. Además, el percentil se interpola dentro de intervalos fijos (5, 10, 25 ms...), así que es aproximado |
| Solicitudes en curso | Indicador de solicitudes atendidas y la ley de Little (X·R) | 1 o 2; X·R ≈ 1,3 | 7 al empezar la sobrecarga | No supera los hilos de Gunicorn: la fila que sigue creciendo está afuera, en las conexiones que esperan un hilo |
| Espera del candado | Histograma de la espera e hilos que esperan | Sin datos: no hay candado | 6 o 7 hilos esperando al empezar | Es la evidencia directa de la contención |
| CPU de la API | Fracción del núcleo de la API | Unos 0,27 | De 0,1 a 0,16 | Más baja con más fila: la API espera, no calcula |
| Memoria de la API | Memoria residente del proceso | Unos 57 MB | Sin cambios mientras hay datos | El límite es 512 MB |
| Salud de la recolección | `up` y la duración de cada consulta | `up` 1 y consultas de 2 a 3 ms | `up` 0 y consultas de 4 s, el límite | Muestra cuándo los demás paneles dejan de ser confiables |

### Paneles vacíos durante la sobrecarga

Con `regresion` a 150 por segundo, los paneles se ven como en la tabla solo durante los primeros segundos. En esta computadora, Prometheus obtuvo una sola respuesta de `/metrics` en los seis minutos de la ejecución, y fue en la pausa entre el calentamiento y la medición, cuando la fila ya se había vaciado. El resto del tiempo, los paneles de valores instantáneos quedan sin datos y los de ritmos muestran tramos sueltos.

La causa es la misma que la del rechazo. `/metrics` lo atienden los mismos 8 hilos de Gunicorn que las consultas, y su solicitud espera en la misma fila de conexiones. Cuando la fila supera unos segundos, no llega a tiempo. A 100 por segundo con el perfil `piloto`, la fila crece más despacio y quedan tramos de unos 20 s con datos: 7 solicitudes en curso, 6 o 7 hilos esperando el candado, entre 40 y 70 respuestas por segundo y la CPU por debajo de 0,16.

Un panel vacío no significa que no haya problemas: aquí es un síntoma de la saturación. Para observar la contención con datos, se mira el comienzo de la ejecución o un nivel de estrés apenas sobre el quiebre, como 100 por segundo. Separar `/metrics` en otro puerto, con su propio hilo, evitaría el hueco, pero cambiaría el sistema medido y obligaría a calibrar de nuevo los perfiles (`CONTRIBUIR.md`, Perfiles).

## 6. Cruzar Gatling y Grafana

| Lo que se ve | Lectura probable |
|---|---|
| p95 alto en Gatling y bajo en «Tiempo en la API» | El tiempo se pierde antes de que un hilo tome la solicitud: fila de conexiones, como en `regresion`, o pausas del contenedor. En el piloto, una cuota de CPU (`cpus: 1`) producía ese patrón (`Taller.md` §5.2) |
| p95 alto en los dos | La API tarda en atender: base de datos, CPU o un recurso compartido dentro del código |
| CPU cerca de 1 núcleo y la fila creciendo | Saturación por cálculo |
| CPU baja y la fila creciendo | Espera: un candado, la base de datos o la red. Es el caso de `regresion` |
| Errores en Gatling y 0 en el panel de errores | Esperas agotadas o conexiones no aceptadas: la API nunca respondió con error |
| `ConnectTimeoutException` | Todos los hilos ocupados durante más de 10 s: la API no aceptó la conexión a tiempo |
| `Request timeout ... 60000 ms` | La solicitud entró, pero pasó 60 s en la fila sin respuesta |
| `PrematureCloseException` | La conexión se cerró antes de la respuesta. Solo aparece con la API muy sobrecargada, y en pocas solicitudes |
| Recolección en 0 | La API está saturada o caída. `SALUD_DESPUES` en `ejecucion.env` dice si seguía en pie al terminar |
| Tasa lograda por debajo del 98 % o `Cannot assign requested address` | El problema es el generador, no la API: la ejecución es inválida |

## 7. Estrés y picos

**Estrés.** `campana-estres-<variante>-<fecha>.md` tiene una fila por nivel. La columna de resultado dice si ese nivel cumple el criterio del perfil, y «Correctas/s» muestra el techo: mientras la variante da abasto, las respuestas correctas por segundo siguen a la tasa; cuando se satura, dejan de crecer aunque la tasa suba. Ese es el punto de quiebre. Los p95 de los niveles se comparan entre sí, nunca se promedian.

**Picos.** El resumen da el p95 de la base, del pico y de la recuperación, y dice si la API se recuperó dentro de la ventana y cuándo. La recuperación se cuenta desde el final del pico hasta el primer bloque a partir del cual todos cumplen el criterio del perfil. Un p95 alto en la fase de recuperación no contradice una recuperación rápida: la fase incluye los primeros bloques, todavía con fila.

En el *runner* de GitHub Actions, con el perfil `ci`, un pico de 50 a 150 por segundo durante 30 s sobre `regresion` llevó el p95 del pico a 12,0 s, sin errores, y la API se recuperó 20 s después del pico. En la ventana de 180 s, 4 de 36 bloques incumplieron el criterio, y el p95 de toda la fase de recuperación fue de 7,8 s. Con el perfil `local`, la API tarda más en considerarse recuperada (55 s en la computadora de desarrollo) porque su umbral es de 1 000 ms en lugar de 3 000: el tiempo de recuperación depende del criterio con que se mide.

## 8. Errores frecuentes de interpretación

- **Leer la página global del informe.** Mezcla el calentamiento con la medición; las aserciones solo miran `medicion`.
- **Usar el p95 de las respuestas correctas.** Deja afuera las solicitudes que fallaron por esperar demasiado, que son las peores.
- **Tomar 60 s como un tiempo de respuesta.** Es el límite de espera de Gatling: el tiempo real habría sido mayor.
- **Promediar percentiles** de distintas ejecuciones o niveles. Se informan por separado, con su rango y su mediana.
- **Comparar milisegundos entre computadoras.** Cada entorno tiene su perfil; lo que se compara es el veredicto.
- **Confundir los tiempos de Grafana con los de Gatling.** Miden en puntos distintos: Grafana, desde que un hilo toma la solicitud; Gatling, desde que el cliente la envía.
- **Concluir que no hay problema porque un panel está vacío.** Bajo sobrecarga, `/metrics` también deja de responder.
- **Culpar a la API de una ejecución inválida.** Si el generador no sostuvo la tasa, la medición no dice nada de la variante.
