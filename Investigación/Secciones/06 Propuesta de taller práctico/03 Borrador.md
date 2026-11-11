# 06 Propuesta de taller práctico

<!-- Borrador v2 | Plan v1 | Evidencia v2 | 2026-11-10 -->
<!-- v2: corrige los hallazgos bloqueantes 1–3 y aplica las sugerencias 4, 5, 6 (salvo la cursiva de «workflow»), 7, 8, 9 y 10 de la auditoría, ronda 1. -->

## 6.1 Contexto de aplicación

El taller parte de un caso que cualquier equipo de desarrollo puede encontrar: una API REST de productos de una tienda a la que se le agrega un contador de visitas. La primera implementación, la variante `regresion`, protege el contador con un candado (*lock*) que comparten todos los hilos del servidor. Lee el valor, lo incrementa y lo escribe sin perder visitas, pero obliga a atender las solicitudes de a una, aunque consulten productos distintos. La corrección, la variante `corregida`, elimina el candado y hace el incremento con una sola instrucción SQL atómica, de modo que la base de datos solo bloquea la fila modificada. La variante `sana`, sin contador, sirve de referencia.

Las dos implementaciones del contador aprueban las mismas 38 pruebas funcionales y de concurrencia: ninguna prueba funcional las distingue. Es la situación que plantean 5.1 y 5.2, en la que el rendimiento es un atributo de calidad propio y necesita pruebas propias. El defecto, además, no se fabrica con pausas en el código. Para que la espera del candado tenga el peso que tendría en producción, PostgreSQL recibe 2 ms de latencia de red en cada ida y vuelta, como si estuviera en otro servidor, y esa condición se aplica por igual a las tres variantes. La hipótesis es que `regresion` se degrada a tasas en las que `corregida` todavía cumple; la magnitud de la diferencia la fijan las mediciones (6.6).

## 6.2 Recursos y código

El código, la guía y los resultados de referencia están en un repositorio público (https://github.com/AleeBonilla/pruebas-automatizadas-rendimiento), en la carpeta `Taller/`. Ahí están la API con sus pruebas, el esquema y los datos sintéticos, las simulaciones de Gatling, la configuración de Prometheus y Grafana, los perfiles de ejecución, las herramientas que calculan el veredicto y los scripts `taller.ps1` y `taller.sh`. Los workflows de CI están en `.github/workflows/`, en la raíz del repositorio.

Para reproducir el taller basta con Git y Docker con Compose: no hace falta instalar Python, Java ni Maven. La computadora necesita al menos cuatro núcleos, y Docker, unas 5 CPU y 5,5 GB de memoria. El procedimiento se comprobó en Windows, con PowerShell y con Git Bash, y en Linux, en los *runners* de GitHub Actions. Los entregables son el código, la guía paso a paso, el plan de pruebas y una guía de interpretación de los resultados. El anexo C reúne el enlace y extractos del código.

## 6.3 Stack tecnológico

El stack, resumido en la Tabla 4, persigue un objetivo: que las variantes se midan en condiciones idénticas y que la medición se pueda repetir. Docker Compose define y ejecuta los servicios como una aplicación de varios contenedores (Docker Inc., s. f.) <!-- E1 -->. Cada imagen tiene una versión exacta, y la API y PostgreSQL se ejecutan en núcleos distintos, fijados en la configuración del entorno.

Gatling se eligió por los criterios de 5.8: modelo de carga abierto, un generador que no necesita un hilo por usuario virtual, licencia abierta y aserciones que hacen fallar la simulación cuando no se cumplen (Gatling Corp., 2026) <!-- E4 -->. Gatling decide el veredicto; Prometheus y Grafana explican lo que ocurre dentro del servidor. Prometheus recoge las métricas de la API consultándolas por HTTP (Prometheus Authors, s. f.) <!-- E2 -->, y Grafana las muestra en un panel que se carga solo al levantar el entorno. La Figura 4 muestra cómo se conectan los componentes.

**Tabla 4.** Stack tecnológico del taller

| Componente | Versión | Función en el taller |
|---|---|---|
| Flask y Gunicorn, sobre Python 3.14 | 3.1.3 · 26.2.0 | API REST con las tres variantes: un proceso con 8 hilos |
| PostgreSQL y Psycopg | 18.6 · 3.3.8 | Productos y visitas: 10 000 productos sintéticos generados con semilla fija |
| pytest | 9.2.0 | Pruebas funcionales y de concurrencia |
| Gatling Community, sobre Java 25 | 3.16.0 | Generador de carga; decide el veredicto con sus aserciones |
| Docker Compose | v2 | Servicios con versiones y recursos fijos |
| Prometheus | 3.15.1 | Lectura de las métricas de la API cada 5 s |
| Grafana | 13.2.5 | Panel con solicitudes, tiempos, espera del candado, CPU y memoria de la API |
| GitHub Actions | *Runner* `ubuntu-24.04` | *Quality gate* en cada cambio y workflows manuales |

*Fuente:* elaboración propia. Versiones usadas en el taller; las dependencias exactas están en el repositorio.

<!-- FIGURA 4: Arquitectura del entorno del taller. Diagrama de bloques. A la izquierda, Gatling (2 CPU, 2 GB) envía solicitudes HTTP a la API (Flask y Gunicorn, núcleo 2 fijo, 512 MB), que consulta PostgreSQL (núcleo 3 fijo, 512 MB) a través de un enlace marcado «2 ms de latencia». Debajo de la API, Prometheus lee /metrics cada 5 s y Grafana consulta a Prometheus. Arriba, un recuadro «taller.ps1 / taller.sh · GitHub Actions» con flechas punteadas hacia todos los servicios: preparar, ejecutar, exportar y detener. pytest con una flecha hacia la API y PostgreSQL. Fuente: elaboración propia. -->

## 6.4 Plan de pruebas

El plan de pruebas fija antes de medir qué se prueba, con qué carga y con qué criterio. Persigue dos objetivos: que la prueba de carga rechace `regresion` y apruebe `corregida` en cada cambio, y que ese veredicto se repita. El escenario sigue el modelo de carga abierto (5.3): los usuarios virtuales llegan a una tasa constante, cada uno hace una consulta y termina, y los productos consultados salen siempre en el mismo orden. Así, una variante lenta no frena la llegada de solicitudes y su demora no queda oculta.

La Tabla 5 resume las pruebas. Las funcionales son una condición previa; la de carga es la *quality gate*, y las de estrés y de picos son informativas: ubican dónde empieza la degradación y cómo se recupera la API tras una ráfaga (5.4). La carga se aprueba si, en la medición posterior al calentamiento, el p95 queda bajo el umbral y la tasa de error no supera el 1 %. Antes de aplicar ese criterio se comprueba que la medición sea interpretable (5.6). Una ejecución inválida, en la que el generador no sostuvo la tasa, faltan datos o la configuración no era la pedida, no aprueba ni rechaza: se repite.

**Tabla 5.** Pruebas del taller

| Prueba | Pregunta | Inyección | Resultado | Cuándo se ejecuta |
|---|---|---|---|---|
| Funcional y de concurrencia | ¿Cumple el contrato y conserva el contador? | 38 pruebas de pytest | Aprobada o fallida | Antes de cada prueba de carga |
| Comprobación del generador | ¿Sostiene Gatling la tasa prevista? | Carga contra una ruta que no usa la base de datos | Válida o inválida | Antes de calibrar |
| Carga | ¿Cumple a la tasa del perfil de ejecución? | 60 s de calentamiento y 180 s de medición a tasa constante | Aprobada o rechazada | En cada *push* y *pull request*; en las campañas |
| Estrés | ¿Dónde empieza la degradación? | Un nivel de tasa por ejecución | Informativo | A mano, antes de calibrar |
| Picos | ¿Cómo responde a una ráfaga y cuánto tarda en recuperarse? | Base, pico abrupto de 30 s y regreso a la base | Informativo | A mano |

*Fuente:* elaboración propia.

Como cada computadora es distinta, la tasa y el umbral no se fijan de antemano: cada entorno tiene su perfil de ejecución, calibrado con sus propias mediciones (5.5). La campaña de calibración repite la carga tres veces por variante, en orden alternado, y ubica el umbral al menos tres veces por encima del peor p95 de `corregida` y tres veces por debajo del mejor de `regresion`. Después, el perfil de ejecución se congela y se comprueba con una campaña de validación nueva, porque un umbral evaluado con los mismos datos con que se eligió parecería funcionar siempre (5.7). Los dos perfiles de ejecución quedaron en 150 solicitudes por segundo, con umbrales de 3 000 ms en `ci` y de 1 000 ms en `local`.

## 6.5 Guía paso a paso

La práctica usa cuatro operaciones de `taller.ps1`, en Windows, o de `taller.sh`, en Linux. `preparar` levanta los servicios y deja los datos en su estado inicial, y `funcionales` muestra que las dos variantes del contador aprueban pytest. `ejecutar --perfil ci --variante corregida` mide durante unos cuatro minutos y termina con «Aprobado»; con `--variante regresion` tarda unos seis y termina con «Rechazado por rendimiento». Cada ejecución deja un resumen, el informe HTML de Gatling y la hora de cada fase. `detener` apaga el entorno.

En GitHub Actions, un workflow es un archivo YAML del repositorio que se dispara ante eventos, y cada ejecución corre en una máquina virtual nueva (GitHub, s. f.) <!-- E3 -->. El workflow de la *quality gate* corre en cada *push* y en cada *pull request* que modifica el taller: prepara el entorno, ejecuta las pruebas funcionales y la carga con el perfil de ejecución `ci`, y falla si la variante es rechazada o si la ejecución es inválida. La variante medida sale de un archivo de configuración: el *pull request* que la cambia a `regresion` reproduce un defecto y quedó rechazado con un p95 de 46,3 s; el que vuelve a `corregida` quedó aprobado con 9 ms. Tres workflows manuales cubren los escenarios, la calibración y la validación, que se repite cada semana (5.7).

## 6.6 Resultados e interpretación

Las 19 ejecuciones de validación, resumidas en la Tabla 6, fueron válidas y dieron los veredictos esperados. El menor margen de `corregida` apareció en `validacion-ci-1`, 26 veces por debajo del umbral; el de `regresion`, en `validacion-ci-2`, con 18 veces por encima. La Figura 5 muestra la separación. `regresion` incumple además la tasa de error, con 17 a 33 % frente al 1 % permitido, por esperas agotadas del cliente y no por respuestas de error de la API.

**Tabla 6.** Resultados de las campañas de validación

| Campaña | Entorno | Válidas | p95 de `corregida` | p95 de `regresion` | Errores de `regresion` | Umbral | Veredictos esperados |
|---|---|---:|---:|---:|---:|---:|---|
| `validacion-ci-1` | *Runner* de GitHub Actions | 7 de 7 | 8–114 ms | 58,4–58,9 s | 19,0–23,0 % | 3 000 ms | Sí |
| `validacion-ci-2` | *Runner* de GitHub Actions | 6 de 6 | 8–10 ms | 54,1–59,1 s | 16,9–18,8 % | 3 000 ms | Sí |
| `validacion-local` | Computadora de desarrollo | 6 de 6 | 10 ms | 60 s | 31,6–33,0 % | 1 000 ms | Sí |

*Fuente:* elaboración propia, con las campañas del 10 de noviembre de 2026. Un p95 de 60 s es el límite de espera de Gatling: el tiempo real fue mayor.

<!-- FIGURA 5: p95 de cada ejecución de validación frente al umbral. Diagrama de puntos con el eje vertical en escala logarítmica (de 1 ms a 100 s) y, en el horizontal, las tres campañas de la Tabla 6. Cada ejecución es un punto: círculos para corregida (de 8 a 114 ms) y triángulos para regresion (de 54,1 a 60 s). Las repeticiones con el mismo valor se desplazan un poco en horizontal para que se vean todas. Una línea horizontal marca el umbral de cada perfil de ejecución: 3 000 ms en las dos campañas ci y 1 000 ms en la local. Fuente: elaboración propia con los valores individuales de las tres campañas de validación (Taller/Taller.md §7.2). -->

La mayor variación se observó en `corregida`, en GitHub Actions, y su causa no quedó identificada. Entre corridas idénticas de la calibración, su p95 varió hasta 28 veces, mientras su p50 se mantenía entre 7 y 9 ms; en la computadora de desarrollo fue de 10 ms en todas. Esa variación es la que justifica exigir un margen (5.6). En una segunda computadora, con el perfil de ejecución `ci`, los veredictos se repitieron.

En Grafana, con `regresion`, al empezar la sobrecarga, hay siete consultas en curso, que con la lectura de `/metrics` ocupan los ocho hilos; seis o siete esperan el candado, y la CPU queda por debajo de la de `corregida`: el servidor espera, no calcula. Poco después, la lectura de métricas espera en la misma fila y Prometheus se queda sin muestras: esa falta de datos también es un síntoma.

## 6.7 Límites

Lo demostrado tiene límites precisos. El umbral se eligió con una regresión conocida que lleva el p95 a decenas de segundos; una regresión que solo duplicara el tiempo de `corregida` aprobaría, así que el taller no demuestra que se detecten regresiones pequeñas o desconocidas. Los resultados valen para los perfiles de ejecución y los entornos medidos. El entorno es reducido: compara versiones y no estima la capacidad de producción (5.5). Además, fijar el sistema operativo del *runner* no fija su hardware, que cambió entre corridas. Tampoco hay prueba de resistencia, así que nada dice de la estabilidad prolongada. Quedan pendientes la reproducción por una persona ajena al desarrollo y la comprobación en macOS.

---

## Anexo C. Material del taller

### C.1 Repositorio

El taller está en https://github.com/AleeBonilla/pruebas-automatizadas-rendimiento, carpeta `Taller/`, que reúne la API, los datos, las simulaciones de Gatling, la observabilidad, los perfiles de ejecución, las herramientas de resultados y la documentación: la guía paso a paso (`docs/GUIA.md`), el plan de pruebas (`docs/PLAN-DE-PRUEBAS.md`) y la interpretación de resultados (`docs/INTERPRETACION.md`). Los *workflows* están en `.github/workflows/`, y los resultados de cada ejecución en CI se descargan como artefactos desde la pestaña *Actions*.

### C.2 Simulación de carga

La simulación separa el calentamiento de la medición y aplica las aserciones solo a la medición. La tasa, las duraciones y el umbral los recibe del perfil de ejecución.

```java
setUp(
    Escenarios.consulta("calentamiento", ...)
        .injectOpen(constantUsersPerSec(TASA).during(CALENTAMIENTO_S))
        .andThen(
            Escenarios.consulta("medicion", ...)
                .injectOpen(
                    constantUsersPerSec(TASA).during(MEDICION_S))))
    .protocols(Escenarios.protocolo())
    .assertions(
        details("medicion").responseTime().percentile(95.0).lt(UMBRAL_MS),
        details("medicion").failedRequests().percent().lte(ERRORES_MAX_PCT));
```

*Fuente:* `CargaSimulation.java`, en `Taller/rendimiento/`, abreviado.

### C.3 Workflow de la *quality gate*

```yaml
on:
  push:
    branches: [main]
    paths: ["Taller/**", ".github/workflows/**"]
  pull_request:
    paths: ["Taller/**", ".github/workflows/**"]
jobs:
  rendimiento:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@v7
      - run: ./taller.sh preparar
      - run: ./taller.sh funcionales
      - run: ./taller.sh ejecutar --tipo carga --perfil ci
      - uses: actions/upload-artifact@v7
        if: always()   # conserva el informe aunque la prueba falle
        with: { path: Taller/resultados/ }
```

*Fuente:* `.github/workflows/compuerta.yml`, abreviado.

### C.4 Informe de Gatling

La Figura 6 compara la medición de una ejecución de cada variante de `validacion-ci-2`. En `corregida`, las respuestas siguen a las solicitudes, unas 150 por segundo; en `regresion`, las correctas se quedan en unas 100 por segundo y el resto termina en esperas agotadas.

<!-- FIGURA 6: Informe de Gatling de la medición, por variante. Dos capturas lado a lado de la página «medicion» del informe HTML, con el perfil de ejecución ci: a la izquierda, corregida (20261110T231112Z-carga-corregida: p50 7 ms, p95 8 ms, sin errores); a la derecha, regresion (20261110T230416Z-carga-regresion: p50 24,0 s, p95 59,1 s, 18,8 % de errores). Cada captura muestra la tabla de estadísticas y el gráfico de respuestas por segundo. Fuente: ejecuciones de la campaña validacion-ci-2, en un runner de GitHub Actions, 10 de noviembre de 2026. Archivo: figuras/fig6.png. -->
