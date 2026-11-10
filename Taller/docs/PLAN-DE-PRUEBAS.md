# Plan de pruebas

Este plan fija qué se prueba en el taller, con qué carga, con qué criterio y con qué perfil. Las razones de cada decisión están en [`Taller.md`](../Taller.md), y el procedimiento paso a paso, en [`GUIA.md`](GUIA.md). Todo lo que aquí se fija se decide antes de medir: un cambio en el escenario, en los criterios o en un perfil congelado exige una calibración nueva (sección 8).

## 1. Objetivos

El taller tiene que mostrar que una prueba de carga en CI detecta una regresión de rendimiento que las pruebas funcionales dejan pasar, y que confirma su corrección. Cada objetivo tiene su prueba y su evidencia.

| Objetivo | Prueba | Evidencia |
|---|---|---|
| Comprobar que `regresion` y `corregida` son funcionalmente equivalentes | Funcionales y de concurrencia (PF) | Las dos variantes del contador aprueban; una versión sin candado ni SQL atómico pierde visitas y falla |
| Rechazar `regresion` y aprobar `corregida` en cada cambio | Carga (PC), en la compuerta | El *job* de GitHub Actions falla con `regresion` y aprueba con `corregida` |
| Comprobar que ese veredicto se repite | Carga (PC), en una campaña de validación | Todas las repeticiones válidas dan el resultado esperado |
| Ubicar la tasa en la que cada variante deja de cumplir | Estrés (PE) | Serie de niveles con el p95 y las respuestas correctas por segundo de cada uno |
| Describir la respuesta a una ráfaga y la recuperación | Picos (PP) | p95 por bloques de 5 s y tiempo de recuperación |

Quedan fuera del plan la capacidad de producción, que un entorno reducido no estima; un SLO, porque el umbral es experimental; la estabilidad prolongada, porque no hay prueba de resistencia, y la detección de regresiones desconocidas, que un umbral elegido con una regresión conocida no demuestra (sección 10).

## 2. Alcance

| Elemento | Alcance |
|---|---|
| Operación medida | `GET /productos/{id}`, con el contrato de `Taller.md` §4.1 |
| Variantes | `regresion` y `corregida`, que se comparan; `sana`, solo como referencia del costo de la consulta |
| Comprobación del generador | `GET /salud`, que no usa la base de datos |
| Datos | 10 000 productos generados con la semilla 42, restablecidos antes de cada ejecución |
| Configuración | La de `Taller.md` §5.2: 1 proceso de Gunicorn con 8 hilos, *pool* de 8 conexiones, núcleos 2 y 3 fijos para la API y PostgreSQL, 2 ms de latencia hacia PostgreSQL |
| Versiones | Las de `Taller.md` §5.1, fijas durante toda la campaña |

No se prueban otras rutas ni escrituras, varios procesos de Gunicorn, otros tamaños de datos ni sistemas de terceros. Las pruebas se dirigen solo al entorno propio.

## 3. Entorno

Hay dos entornos, y cada uno tiene su perfil calibrado (sección 7):

| Entorno | Equipo | Uso |
|---|---|---|
| `ci` | *Runner* `ubuntu-24.04` de GitHub Actions, con el hardware que GitHub asigne | Compuerta en cada *push* y *pull request*; calibración y validación del perfil `ci` |
| `local` | Computadora de desarrollo: Intel Core i7-13620H, Docker Desktop 29.8 con 12 núcleos y 11,7 GB | Práctica, exploración, calibración y validación del perfil `local` |

En los dos, la pila se levanta con Docker Compose desde el mismo repositorio, y cada ejecución registra el equipo, los recursos de Docker, la revisión del código y la configuración efectiva. Las ejecuciones van de a una: dos mediciones simultáneas compiten por la misma máquina y ninguna sirve. En una computadora distinta de estas dos, el perfil se calibra de nuevo.

## 4. Escenario

| Elemento | Definición |
|---|---|
| Modelo de carga | Abierto: los usuarios virtuales llegan a tasa constante (`constantUsersPerSec`), sin esperar las respuestas anteriores |
| Usuario virtual | Hace una sola consulta y termina, así que la tasa de llegada es la tasa de solicitudes |
| Identificadores | `base-datos/productos.csv`, generado con semilla fija y recorrido siempre en el mismo orden (`circular`) |
| Comprobaciones | Estado `200`, `id` igual al pedido y presencia de `nombre`, `categoria`, `precio` y `visitas`. La exactitud del contador la comprueba pytest |
| Esperas | Las de Gatling por omisión: 10 s para conectar y 60 s para responder. Una espera agotada cuenta como error |
| Reintentos | Ninguno, para no registrar visitas que el escenario no hizo |
| Fases | Cada fase da nombre a sus solicitudes (`calentamiento`, `medicion`, `base`, `pico`, `recuperacion`), y las aserciones se aplican solo a la medición |

## 5. Pruebas

| ID | Prueba | Inyección | Resultado | Cuándo se ejecuta |
|---|---|---|---|---|
| PF | Funcionales y de concurrencia | 38 pruebas de pytest: contrato, `404`, reversión ante fallos y concurrencia sobre el mismo producto y sobre productos distintos | Aprobado o fallido | En la compuerta, antes de la carga; en local, con `funcionales` |
| PG | Comprobación del generador | Carga contra `/salud` a la tasa prevista | Aprobado sin errores, o el generador no sirve a esa tasa | Antes de calibrar |
| PC | Carga | Calentamiento y medición a `TASA`, durante `CALENTAMIENTO_S` y `MEDICION_S`. La medición empieza cuando termina el calentamiento (`andThen`) | Aprobado o rechazado | En la compuerta, en cada *push* a `main` y en cada *pull request* que toca `Taller/`; en la calibración y la validación |
| PE | Estrés | Un nivel por ejecución, con las fases de la carga y llegadas continuas entre ellas | Informativo: cumple o no el criterio | Manual, al explorar antes de calibrar |
| PP | Picos | Base a `TASA` durante `CALENTAMIENTO_S`, pico a `PICO_TASA` durante `PICO_S` y recuperación a `TASA` durante `MEDICION_S`, sin pausas | Informativo: recuperada o no, y en cuánto tiempo | Manual |

En la carga, `andThen` espera a que terminen todas las solicitudes del calentamiento antes de empezar la medición. Con una variante saturada, eso deja hasta 60 s sin llegadas. El estrés no tiene esa pausa, de modo que su medición hereda la fila que ya se formó. La carga la mantiene porque los perfiles vigentes se calibraron así. Cambiarla es un cambio de la simulación, que exige una calibración nueva.

En el estrés, cada nivel es una ejecución aparte, porque en una ejecución escalonada las solicitudes lentas de un nivel se mezclan con las del siguiente. Los percentiles de distintos niveles se informan por separado y nunca se promedian.

## 6. Criterios

### 6.1 Condiciones previas

Una medición empieza solo si se cumplen todas estas condiciones:

- La preparación terminó y todos los servicios superaron su *healthcheck*.
- Las pruebas funcionales aprobaron con la misma revisión del código. En la compuerta también aprueban las 25 pruebas de las herramientas que calculan la validez y el veredicto.
- Los datos y los contadores se restablecieron.
- El perfil está congelado en su etiqueta, salvo en la exploración, que usa el perfil `piloto`.
- No corre otra medición ni otra carga pesada en la misma máquina.

### 6.2 Validez

La validez se comprueba antes que las aserciones, en cada fase medida: la medición en carga y estrés, y las tres fases en picos, porque el generador también debe sostener el pico.

| Comprobación | La ejecución es inválida si |
|---|---|
| Preparación | La API no estaba sana antes de medir, el estado no se restableció, la API se detuvo durante la medición o Gatling falló antes de evaluar las aserciones |
| Configuración | Los parámetros que usó la simulación no son los que pidió el script, o la API atendía otra variante, según `/salud` |
| Generador | Hay errores del propio generador, como quedarse sin puertos; las solicitudes iniciadas se apartan más de un 0,5 % de las previstas, o la tasa lograda queda por debajo del 98 % de la prevista |
| Datos | Faltan `fases.json`, sus conteos o el informe de Gatling; alguna solicitud iniciada no terminó, o el informe no registra todas las iniciadas |

Los errores de la API bajo carga, incluidas las esperas agotadas, no invalidan una ejecución: son lo que la prueba debe rechazar.

### 6.3 Resultado

| Resultado | Condición | Código de salida |
|---|---|---:|
| Aprobado | Carga válida con p95 de la medición menor que `UMBRAL_MS` y errores que no superan `ERRORES_MAX_PCT` | 0 |
| Rechazado por rendimiento | Carga válida que incumple alguna de las dos aserciones | 1 |
| Informativo | Estrés o picos válidos: describen el comportamiento sin aprobar ni rechazar | 0 |
| Inválido | Cualquiera de las condiciones de 6.2. No dice nada de la variante | 2 |

El criterio se aplica al p95, nunca al promedio, y se calcula sobre la medición, nunca sobre el calentamiento.

### 6.4 Recuperación tras un pico

La ventana de observación es la fase de recuperación, de `MEDICION_S` segundos. La simulación agrupa las solicitudes en bloques de `BLOQUE_S` segundos (5 si no se indica) según el momento en que salen, y por cada bloque calcula el p95 y los errores. Un bloque cumple si su p95 es menor que `UMBRAL_MS` y sus errores no superan `ERRORES_MAX_PCT`.

- La API está recuperada desde el primer bloque de la ventana a partir del cual todos los bloques, hasta el final, cumplen. El tiempo de recuperación es el inicio de ese bloque, contado desde el final del pico.
- Si el último bloque no cumple, no hay recuperación dentro de la ventana, y se informa ese límite.
- Si la base ya incumple el criterio, no hay un estado normal al que volver, y el resultado lo advierte.

### 6.5 Terminación

| Actividad | Termina con éxito si | Si no |
|---|---|---|
| Compuerta | La carga aprueba | El *job* falla, tanto si la variante es rechazada como si la ejecución es inválida, y el resumen distingue los dos casos |
| Calibración | El generador sostiene la tasa, hay tres ejecuciones válidas por variante y el umbral cabe con el margen fijado (sección 8) | No es satisfactoria: se revisan la tasa o el entorno, nunca el margen |
| Validación | Todas las ejecuciones válidas de `corregida` aprueban y todas las de `regresion` son rechazadas | Falla. El umbral no se ajusta con esos datos: se abre una calibración nueva |

Las ejecuciones inválidas se informan con su causa y no cuentan para los rangos. Se repiten hasta tener tres válidas por variante.

## 7. Perfiles

Un perfil es un archivo `config/perfiles/<perfil>.env` con la tasa, el umbral y las duraciones. Los scripts lo pasan a Gatling, así que esos valores no se escriben en el código.

| Perfil | Uso | `TASA` | `UMBRAL_MS` | `CALENTAMIENTO_S` | `MEDICION_S` | `ERRORES_MAX_PCT` | Estado |
|---|---|---:|---:|---:|---:|---:|---|
| `piloto` | Exploración: estrés y comprobación del generador | 20 | 300 | 20 | 60 | 1,0 | Sin calibrar; la tasa se indica en cada ejecución |
| `ci` | Compuerta en GitHub Actions | 150 | 3 000 | 60 | 180 | 1,0 | Congelado en `perfil-ci-v1` |
| `local` | Computadora de desarrollo | 150 | 1 000 | 60 | 180 | 1,0 | Congelado en `perfil-local-v1` |

Los picos usan además `PICO_TASA`, sin valor por omisión, y `PICO_S`, de 30 s si no se indica. Los dos se pueden dar en la línea de comandos (`--pico`, `--duracion-pico`).

Los márgenes de cada perfil son la distancia entre el umbral y la variante más cercana en cada campaña:

| Perfil | Campaña | Peor p95 de `corregida` | Mejor p95 de `regresion` | Umbral sobre `corregida` | `regresion` sobre el umbral |
|---|---|---:|---:|---:|---:|
| `ci` | Calibración | 60 ms | 54,4 s | 50 veces | 18 veces |
| `ci` | Validación | 114 ms | 58,4 s | 26 veces | 19,5 veces |
| `local` | Calibración | 10 ms | 60 s | 100 veces | 60 veces |
| `local` | Validación | 10 ms | 60 s | 100 veces | 60 veces |

*Calibración del perfil `ci`: segunda campaña, `calibracion-ci-2`. Las tablas completas de cada campaña están en `Taller.md` §7.*

`regresion` incumple también la aserción de errores en todas las campañas: de 15 a 33 % frente al 1 % permitido. Su rechazo no depende solo del umbral.

Un perfil congelado no se modifica. Un commit que cambia el sistema medido (versiones, configuración de `Taller.md` §5.2, datos, variantes o simulación) lleva la línea `Invalida: perfil-<entorno>-v<n>`, y el perfil se calibra de nuevo con la etiqueta siguiente.

## 8. Calibración y validación

La calibración elige la tasa y el umbral, y la validación los comprueba con datos nuevos. Si el umbral se evaluara con los mismos datos con que se eligió, parecería funcionar siempre.

Antes de medir se fijaron estas reglas, iguales para los dos perfiles:

| Regla | Valor |
|---|---|
| Repeticiones | 3 válidas por variante, en cada campaña |
| Orden | Alternado: `corregida`, `regresion`, `regresion`, `corregida`, `corregida`, `regresion`. La validación usa el orden inverso |
| Duraciones | Las del perfil: 60 s de calentamiento y 180 s de medición |
| Tasa | Bien por encima de la tasa en la que `regresion` deja de cumplir en el estrés, con `corregida` holgada y por debajo del límite del generador |
| Margen | El umbral debe quedar al menos 3 veces por encima del peor p95 de `corregida` y 3 veces por debajo del mejor de `regresion` |
| Umbral | El punto medio en escala logarítmica del intervalo admisible, redondeado |
| Informe | Todas las ejecuciones en orden, incluidas las inválidas y su causa; rango, mediana y coeficiente de variación del p95 por variante |

La secuencia completa es: comprobación del generador (PG), exploración con estrés (PE), elección de la tasa, campaña de calibración con carga (PC), elección del umbral, congelamiento del perfil y campaña de validación. El detalle de cada paso está en `Taller.md` §7.1 y en la sección 9 de la guía.

## 9. Ejecución y registro

| Actividad | Cómo se ejecuta |
|---|---|
| Preparar y funcionales | `taller.ps1` o `taller.sh`, con `preparar` y `funcionales` |
| Una prueba | `ejecutar --tipo carga\|estres\|picos --perfil <perfil> --variante <variante>`, con `--tasa`, `--tasas`, `--pico` o `--ruta salud` según la prueba |
| Una campaña | `campana --nombre <nombre> <ejecuciones...>`, que escribe `resultados/campana-<nombre>.md` |
| Compuerta | `.github/workflows/compuerta.yml`, automática en cada *push* y *pull request*, o manual con la variante, el perfil y la tasa como entradas |

Cada ejecución deja su carpeta en `resultados/`, con el veredicto, `metricas.json`, `fases.json`, el informe de Gatling, los parámetros, la revisión del código y los registros. En CI esa carpeta se guarda como artefacto durante 30 días. Las campañas de calibración y validación del perfil `ci` se corrieron con disparos manuales de la compuerta. Los workflows propios de escenarios, calibración y validación están pendientes (T17).

## 10. Riesgos y límites

| Riesgo | Efecto | Tratamiento |
|---|---|---|
| Ruido del *runner* | El p95 de `corregida` cambió hasta 28 veces entre corridas idénticas en `ci`, con pausas de 200 ms a 1 s de causa no identificada | El umbral queda 12 veces por encima del peor valor observado, 250 ms en la primera calibración. Una corrida con pausas más largas rechazaría una variante correcta; cada validación nueva lo pone a prueba |
| Hardware del *runner* | Fijar `ubuntu-24.04` no fija la máquina asignada | Cada corrida registra CPU, memoria y versión de Docker |
| Límite del generador | Por encima de unas 350 solicitudes por segundo, Gatling se queda sin puertos efímeros | La ejecución queda inválida, no rechazada; la tasa de los perfiles y de los picos queda por debajo |
| *Timeout* de Gatling | Recorta la cola de `regresion` en 60 s, así que su coeficiente de variación subestima la dispersión | Los márgenes se calculan con el mejor p95 de `regresion`, no con su variación |
| Regresión conocida | El umbral se eligió con una regresión que lleva el p95 a decenas de segundos. Una regresión que solo duplique el tiempo de `corregida` aprobaría | El plan no afirma detectar regresiones desconocidas ni pequeñas |
| Validez restringida | Los valores valen para el perfil, la configuración y el entorno en que se midieron | Cada computadora calibra su perfil; los milisegundos de `ci` y de `local` no se comparan |
