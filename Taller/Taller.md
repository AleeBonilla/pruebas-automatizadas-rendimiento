# Taller práctico: pruebas de rendimiento reproducibles sobre una API REST

Diseño del taller de la Fase 2 de la investigación y plan de la sección 6 del documento. El alcance general está en [`Alcance.md`](../Alcance.md) §7.

**Estado:** fase 1 en construcción. T1–T6 y T16 están terminadas, T8 tiene el workflow pero le faltan los *pull requests* de demostración, el piloto (T7) ya fijó la configuración de 5.2 y el perfil `ci` tiene una calibración preliminar (7.1). Faltan la calibración local y la validación.

## 1. Propósito

El taller demuestra que una prueba de rendimiento automatizada con Gatling, ejecutada en un pipeline de CI, detecta una regresión que las pruebas funcionales no detectan, y que confirma después su corrección. Con eso responde a PI-5 y lleva a la práctica la pregunta-problema del documento (3.4): integrar estas pruebas en CI con un costo de adopción bajo y con un veredicto confiable.

El caso es una API REST de productos de una tienda, a la que se agrega un contador de visitas. La primera implementación protege el contador con un candado (*lock*) compartido por todas las solicitudes. No pierde visitas, pero obliga a que las solicitudes se atiendan de a una, aunque consulten productos distintos. Con poca carga no se nota; con carga, las solicitudes hacen fila y el tiempo de respuesta crece. La corrección elimina el candado y hace el incremento en la base de datos con una sola instrucción SQL atómica.

Las dos versiones del contador cumplen las mismas pruebas funcionales; la diferencia solo aparece bajo carga. Es lo que plantean 5.1 y 5.2 del Marco teórico: el rendimiento es un atributo de calidad propio, la eficiencia de desempeño de ISO/IEC 25010, y requiere pruebas propias. El defecto, además, es realista: no se fabrica con pausas artificiales.

El taller se presenta en y cada participante puede reproducirlo en su computadora con la guía del repositorio. Al completarlo, el participante puede:

1. Levantar un entorno reproducible con Docker Compose.
2. Ejecutar pruebas funcionales y pruebas de carga, estrés y picos con Gatling.
3. Interpretar el p95, la tasa de error y el *throughput*, junto con las métricas del servidor en Grafana.
4. Calibrar un umbral para su entorno y comprobar que el veredicto se repite.
5. Explicar cómo una prueba de rendimiento funciona como compuerta de calidad en CI.

## 2. Tecnologías

| Tecnología | Descripción | Uso en el taller |
|---|---|---|
| Flask | *Framework* ligero de Python para construir APIs web | Implementa `GET /productos/{id}` y sus variantes |
| Gunicorn | Servidor de aplicaciones para Python; reemplaza al servidor de desarrollo de Flask, que no es apto para medir | Atiende las solicitudes con un proceso y varios hilos |
| PostgreSQL y Psycopg | Base de datos relacional y su controlador para Python | Guarda productos y visitas, y maneja las transacciones |
| `tc netem` | Herramienta de Linux que retrasa los paquetes de una interfaz de red | Da a PostgreSQL la latencia de un servidor aparte (5.2) |
| pytest | Herramienta de pruebas de Python | Pruebas funcionales y de concurrencia |
| Gatling Community | Generador de carga: simula usuarios que llaman a la API y mide sus respuestas | Pruebas de carga, estrés y picos; decide el veredicto |
| Maven Wrapper | Script (`mvnw`) que descarga una versión fija de Maven para compilar proyectos Java | Compila y ejecuta las simulaciones de Gatling |
| Docker y Docker Compose | Contenedores que empaquetan un programa con sus dependencias; Compose levanta varios a la vez | Levanta API, base de datos, Gatling, Prometheus y Grafana |
| Prometheus | Base de datos de métricas que consulta periódicamente a los servicios | Recoge las métricas de la API |
| Grafana | Herramienta de paneles para visualizar métricas | Muestra lo que ocurre en el servidor durante cada prueba |
| GitHub Actions | Servicio de CI de GitHub que ejecuta tareas ante cada cambio | Ejecuta las pruebas en cada *push* o *pull request* |

**Gunicorn, hilos y candado.** Gunicorn ejecuta la aplicación en uno o más procesos trabajadores. Con el modo `gthread`, cada proceso atiende varias solicitudes a la vez, una por hilo. En Python, los hilos de un mismo proceso no ejecutan código en paralelo, por el *GIL*, pero sí se superponen mientras esperan: cuando un hilo espera la respuesta de PostgreSQL, otro avanza. Un `threading.Lock` compartido elimina esa superposición, porque mientras un hilo lo tiene, los demás esperan. Como un candado de Python solo coordina los hilos de su proceso, el taller usa un único proceso con varios hilos.

**Transacciones.** Una transacción agrupa operaciones que se confirman juntas (*commit*) o se deshacen juntas (*rollback*). `UPDATE productos SET visitas = visitas + 1 ... RETURNING ...` lee, incrementa y devuelve el valor en un solo paso atómico. PostgreSQL bloquea solo la fila modificada: dos visitas al mismo producto se esperan entre sí, pero visitas a productos distintos no.

**Contenedores.** Una imagen contiene un programa y sus dependencias; un contenedor es esa imagen en ejecución. `compose.yaml` declara los servicios, sus redes, volúmenes y límites de CPU y memoria. Con un *healthcheck*, Compose espera a que la base de datos esté lista antes de arrancar la API. Todo corre en contenedores, así que no hace falta instalar Python, Java ni Maven.

**Gatling.** Cada prueba es una simulación, una clase Java con tres partes: el escenario, que define lo que hace cada usuario virtual; la inyección, que define cuántos usuarios llegan y a qué ritmo, y las aserciones, que son las condiciones para aprobar, por ejemplo «p95 menor que 300 ms». Si una aserción falla, Gatling termina con error y el pipeline falla. Cada ejecución produce un informe HTML con percentiles y gráficos.

**Prometheus y Grafana.** La API expone sus métricas en `/metrics` y Prometheus las lee cada pocos segundos. El taller usa tres tipos de métrica: el contador, que solo aumenta (solicitudes atendidas); el indicador (*gauge*), que sube y baja (solicitudes en curso), y el histograma, que reparte las duraciones en intervalos y permite estimar percentiles. Grafana consulta a Prometheus y muestra paneles que se cargan desde archivos del repositorio al levantar el entorno.

**GitHub Actions.** Un *workflow* es un archivo YAML en `.github/workflows/` que define cuándo se ejecuta (*push*, *pull request*, de forma manual o programada) y qué *jobs* corre. Cada *job* se ejecuta en una máquina virtual nueva, el *runner*, y puede guardar archivos como artefactos, por ejemplo los informes de Gatling. Si un paso falla, el *job* falla y GitHub lo muestra en el *pull request*.

## 3. Fundamento en el Marco teórico

Cada decisión del taller aplica un concepto desarrollado y citado en la sección 5 del documento.

| Concepto | Definición | Marco teórico | Aplicación en el taller |
|---|---|---|---|
| Rendimiento como atributo de calidad | Una versión puede ser funcionalmente correcta y, aun así, lenta | 5.1, 5.2 | Las dos variantes del contador aprueban las pruebas funcionales; solo la prueba de carga las distingue |
| Eficiencia de desempeño | Comportamiento temporal, utilización de recursos y capacidad | 5.2, Tabla 1 | p95 para el comportamiento temporal, CPU y memoria en Grafana para los recursos, estrés para la capacidad del entorno |
| *Quality gate* | Prueba automatizada que puede detener la integración | 5.1, 5.7 | El *job* de GitHub Actions falla si fallan las aserciones de Gatling |
| *Shift-left* | Probar desde etapas tempranas | 5.1 | La prueba corre en CI con cada cambio, antes de cualquier despliegue |
| Métricas | Tiempo de respuesta, *throughput* y tasa de error | 5.3 | Son las métricas del veredicto y del informe |
| Percentiles | El p95 es el tiempo que no supera el 95 % de las solicitudes; el promedio oculta la cola | 5.3, 5.6 | El criterio usa el p95, no el promedio |
| Modelo abierto y *coordinated omission* | Las llegadas no dependen de las respuestas; el modelo cerrado puede ocultar las demoras | 5.3, Figura 3 | Inyección a tasa constante; cada usuario virtual hace una consulta y termina |
| Ley de Little | Con X llegadas por segundo y un tiempo medio R, hay en promedio X·R solicitudes en el sistema | 5.3 | Interpreta el panel de solicitudes en curso; vale para promedios en estado estable, no durante una sobrecarga |
| Tipos de prueba | Carga, estrés, picos y resistencia | 5.4, Tabla 2 | Carga como compuerta; estrés y picos informativos; resistencia excluida |
| Proceso de pruebas | Planificación, análisis, diseño, implementación, ejecución y cierre | 5.5 | Plan de pruebas documentado y operaciones de preparación, ejecución y exportación |
| Entorno de prueba | En un entorno reducido se comparan versiones, no capacidad absoluta | 5.5 | Las variantes se comparan en el mismo entorno; no se estima capacidad de producción |
| Línea base | Medición de referencia para comparar versiones | 5.6 | `corregida` frente a `regresion`, con `sana` como referencia adicional |
| Ruido | Variación entre ejecuciones ajena al cambio evaluado | 5.6, 5.7 | Repeticiones, rangos y margen del umbral medidos en cada entorno |
| Calentamiento | El estado inicial no representa el comportamiento estable | 5.4, 5.6 | El calentamiento se separa de la medición y no entra en las aserciones |
| Validación del generador | Comprobar que la prueba alcanza la tasa antes de culpar al sistema | 5.6 | Primer paso de la calibración, contra una respuesta mínima |
| Antipatrones | Probar sin objetivos, resumir con promedios, compartir el entorno, medir sin criterio | 5.6 | Objetivos escritos, p95, pruebas en secuencia y aserciones automáticas |
| Umbral y SLO | El umbral debe ser explícito y su margen debe justificarse con la variación medida | 5.7 | Umbral experimental calibrado con margen; no se presenta como SLO de producción |
| Pruebas en CI | Pruebas breves en cada cambio; las extensas, en una etapa propia | 5.7 | Carga breve en cada *push* o *pull request*; estrés, picos y campañas, de forma manual |
| Observabilidad | Muestra dentro del sistema lo que la prueba mide desde afuera | 5.7 | Prometheus y Grafana explican la degradación; Gatling decide el veredicto |
| Selección de herramienta | Modelo abierto, generador eficiente, aserciones que fallan la ejecución y licencia abierta | 5.8, Tabla 3 | Gatling Community con DSL de Java |

## 4. Sistema bajo prueba

### 4.1 API

| Elemento | Definición |
|---|---|
| Operaciones | `GET /productos/{id}`: devuelve el producto y, en las variantes con contador, registra una visita · `GET /salud`: respuesta mínima sin base de datos, para el *healthcheck* y la comprobación del generador · `GET /metrics`: métricas para Prometheus |
| Contrato | Producto existente: `200` con `id`, `nombre`, `categoria`, `precio` y `visitas`; inexistente: `404` con `{"error": "producto no encontrado"}`, sin modificar contadores |
| Datos | 10 000 productos sintéticos generados con la semilla 42: ocho categorías, precios entre 1 y 500 y visitas en cero |
| Estado inicial | Datos y contadores restablecidos antes de cada repetición |
| Alcance | Las pruebas se dirigen solo al entorno propio, nunca a sistemas de terceros |

```json
{"id": 4182, "nombre": "Producto 4182", "categoria": "hogar", "precio": 129.90, "visitas": 17}
```

Con 10 000 productos la tabla cabe en la memoria de PostgreSQL, de modo que la medición no depende del disco, y las solicitudes concurrentes rara vez coinciden en la misma fila. Así, la espera que aparezca bajo carga proviene del candado y no de la base de datos.

Que una consulta incremente un contador es una simplificación didáctica documentada en el contrato. Los reintentos automáticos del cliente están desactivados para no registrar visitas que el escenario no hizo.

### 4.2 Variantes

Las variantes comparten código, contrato, dependencias, instrumentación y configuración del servidor, y se seleccionan por configuración.

| Variante | Implementación | Papel |
|---|---|---|
| `regresion` | Lee el contador, lo incrementa y lo escribe dentro de un `threading.Lock` compartido | Correcta, pero serializa todas las solicitudes |
| `corregida` | Incrementa con un `UPDATE ... RETURNING` atómico, sin candado | Misma función, sin serializar productos distintos |
| `sana` | Consulta sin incrementar el contador | Referencia del costo de la consulta sola |

```python
candado = threading.Lock()  # compartido por todos los hilos del proceso

def visitar_regresion(id):
    with candado:   # una solicitud a la vez, sea cual sea el producto
        with pool.connection() as con:   # se confirma al salir del bloque
            visitas = con.execute("SELECT visitas FROM productos WHERE id = %s", (id,)).fetchone()[0]
            con.execute("UPDATE productos SET visitas = %s WHERE id = %s", (visitas + 1, id))

def visitar_corregida(id):
    with pool.connection() as con:   # sin candado: PG bloquea solo esa fila
        return con.execute(
            "UPDATE productos SET visitas = visitas + 1 WHERE id = %s RETURNING id, nombre, precio, visitas",
            (id,)).fetchone()
```

En `regresion`, el candado abarca la conexión, la lectura, la escritura y la confirmación: mientras una solicitud espera a la base de datos, todas las demás esperan al candado. La comparación principal es `regresion` frente a `corregida`, porque cumplen la misma función; de `corregida` no se espera que iguale a `sana`, que hace menos trabajo.

### 4.3 Corrección funcional

Quitar el candado sin cambiar el algoritmo de leer, sumar y escribir no corregiría el problema: dos hilos leerían el mismo valor y se perderían visitas. Por eso, antes de medir rendimiento, pytest comprueba en ambas variantes del contador el contrato, la reversión ante fallos y que, con solicitudes concurrentes al mismo producto y a productos distintos, el contador final coincida con las visitas confirmadas.

El cambio a SQL atómico también modifica el acceso a datos, así que se comparan las implementaciones completas, sin atribuir toda la diferencia de tiempo al candado.

### 4.4 Hipótesis

Se espera que `regresion` se degrade a tasas en las que `corregida` todavía cumple, sin que ninguna pierda visitas. La magnitud de la diferencia se determina experimentalmente.

## 5. Entorno reproducible

```text
Gatling ── HTTP ──> API (Flask + Gunicorn) ── SQL ──> PostgreSQL
                         │
                         └── /metrics <── Prometheus <── Grafana

pytest ──> API y estado en PostgreSQL
taller.ps1 / taller.sh ──> preparar, ejecutar, exportar, detener
```

Todos los servicios se definen en `compose.yaml`. La práctica local requiere Git y Docker con Compose. El entorno controla:

- versiones exactas de dependencias e imágenes (5.1), sin la etiqueta `latest`;
- la misma configuración para todas las variantes: hilos de Gunicorn, conexiones a PostgreSQL, núcleos y memoria de cada contenedor y latencia de red hacia PostgreSQL;
- esquema y datos semilla, restablecidos antes de cada repetición;
- *healthchecks* antes de medir;
- ejecución secuencial de variantes, pruebas y repeticiones, para evitar el antipatrón del entorno compartido (5.6);
- registro de cada campaña: equipo, arquitectura, recursos asignados a Docker, versiones, revisión del código y configuración efectiva.

Reproducir significa repetir el mismo código, datos, procedimiento y condiciones, no obtener los mismos milisegundos en otra computadora. Por eso cada entorno calibra su propio perfil de tasa y umbral, y GitHub Actions tiene el suyo, el perfil `ci` (5.5).

### 5.1 Versiones

| Componente | Versión | Origen |
|---|---|---|
| Python | 3.14.10 | Imagen `python:3.14.10-slim-trixie` |
| Flask · Gunicorn | 3.1.3 · 26.2.0 | PyPI |
| Psycopg · psycopg-pool | 3.3.8 (`psycopg[binary]`) · 3.3.3 | PyPI |
| prometheus-client | 0.26.0 | PyPI |
| pytest · requests | 9.2.0 · 2.34.2 | PyPI |
| PostgreSQL · iproute2-tc | 18.6 · 7.0.0-r0 | Imagen `postgres:18.6-alpine`, con `tc` agregado en `base-datos/Dockerfile` |
| Java | Temurin 25.0.5 (LTS) | Imagen `eclipse-temurin:25.0.5_8-jdk-noble` |
| Maven · Maven Wrapper | 3.9.16 · 3.3.4 | Maven Central |
| Gatling · gatling-maven-plugin | 3.16.0 · 4.21.12 | Maven Central |
| Prometheus | 3.15.1 | Imagen `prom/prometheus:v3.15.1` |
| Grafana | 13.2.5 | Imagen `grafana/grafana:13.2.5` |
| GitHub Actions | `ubuntu-24.04` · `actions/checkout@v7` · `actions/upload-artifact@v7` | GitHub |

Son las versiones estables vigentes al 8 de noviembre de 2026. Las dependencias de Python se fijan en `requirements.txt` y las de Java en `pom.xml`. Solo se actualizan entre campañas, porque cambiar una versión cambia el sistema medido e invalida la calibración (5.6).

### 5.2 Configuración

| Parámetro | Valor |
|---|---|
| Gunicorn | 1 proceso `gthread` con 8 hilos |
| Conexiones a PostgreSQL | *Pool* fijo de 8, una por hilo |
| Recursos de la API | Núcleo 2 fijo (`cpuset`) y 512 MB |
| Recursos de PostgreSQL | Núcleo 3 fijo (`cpuset`) y 512 MB |
| Latencia de red de PostgreSQL | 2 ms en cada ida y vuelta (`tc netem`, `LATENCIA_BD_MS`) |
| Límites de Gatling | 2 CPU y 2 GB |
| Límites de Prometheus y Grafana | 0,5 CPU y 512 MB cada uno |

Por el *GIL*, un proceso de Python ejecuta código en un solo núcleo a la vez, así que un núcleo no limita artificialmente a la API. Con tantas conexiones como hilos, ninguna solicitud espera una conexión libre, y la única espera que distingue a las variantes es la del candado. Gatling recibe más recursos que la API para que el generador no sea el cuello de botella. La pila completa ocupa unas 5 CPU y 5,5 GB, que deben estar disponibles para Docker, y necesita al menos 4 núcleos, porque la API y PostgreSQL usan el 2 y el 3.

Dos valores salieron del piloto (T7). En la primera configuración, con un límite de 1 CPU por contenedor y PostgreSQL en la misma máquina, las variantes no se separaban: a 300 solicitudes por segundo, `regresion` aprobó con un p95 de 88 ms y `corregida` fue rechazada con 482 ms.

- **Núcleo fijo en lugar de cuota.** Con `cpus: 1`, el kernel detiene el contenedor hasta el final del período de 100 ms cada vez que un pico agota la cuota. En una medición de 60 s, la API quedó detenida 9,4 s en total, repartidos en 102 de 886 períodos. Mientras tanto, el histograma del servidor marcaba un p95 de 12 a 22 ms. Esas pausas forman la cola que mide Gatling y son ajenas a las variantes. Con `cpuset`, el contenedor usa un núcleo entero sin cuota, y la cola desaparece: `corregida` mantiene un p95 de unos 10 ms hasta 300 solicitudes por segundo.
- **Latencia de red de PostgreSQL.** Con la base de datos local, cada ida y vuelta tardaba menos de un milisegundo. El candado se retenía tan poco que la API se saturaba por CPU antes que por la fila del candado. En producción, la base de datos suele estar en otro servidor, y cada ida y vuelta cuesta uno o dos milisegundos. Con 2 ms, cada visita de `regresion` retiene el candado durante cuatro idas y vueltas (BEGIN, SELECT, UPDATE y COMMIT), unos 10 ms. Eso limita su capacidad a unas 100 visitas por segundo, mientras `corregida` sigue atendiendo en paralelo con sus 8 hilos.

La latencia es una condición del entorno, aplicada por igual a todas las variantes, y no una pausa en el código: el defecto sigue siendo solo el candado. `LATENCIA_BD_MS` forma parte de la configuración medida y queda registrada en cada ejecución.

| Tasa (sol./s) | `corregida` p95 | `regresion` p95 | `regresion` errores |
|---:|---:|---:|---:|
| 25 | — | 17 ms | 0 % |
| 50 | 12 ms | 15 ms | 0 % |
| 75 | — | 14 ms | 0 % |
| 100 | 11 ms | 8 027 ms | 0 % |
| 150 | 10 ms | 35 777 ms | 4,8 % |
| 200 | 9 ms | 54 915 ms | 25,5 % |
| 300 | 10 ms | 47 352 ms | 50,1 % |

*Piloto con la configuración final: una ejecución por punto, 20 s de calentamiento y 60 s de medición (perfil `piloto`). Por encima de 100 sol./s, los errores de `regresion` son* timeouts *de 60 s de Gatling. Estos valores orientan la calibración, pero no la reemplazan (7.1).*

`regresion` no se degrada de forma gradual: entre 75 y 100 solicitudes por segundo pasa de cumplir holgadamente a colapsar, porque la tasa de llegada supera la capacidad del candado y la fila crece sin límite. Para la compuerta conviene una tasa claramente por encima de ese punto y por debajo del límite del generador (7.1), donde `corregida` todavía tiene holgura. La elección final se hace en la calibración, con repeticiones.

## 6. Plan de pruebas

### 6.1 Escenario

Cada usuario virtual hace una consulta y termina, de modo que la tasa de llegada de usuarios es la tasa de solicitudes. Es el modelo abierto de 5.3: las llegadas no esperan a que terminen las anteriores y no se ocultan las demoras.

Los identificadores consultados salen de un archivo CSV generado con semilla fija y se recorren siempre en el mismo orden (alimentador `circular`), así que todas las variantes reciben la misma secuencia. La carga se reparte entre muchos productos. La distribución es sintética y no reproduce el tráfico de una tienda real.

Gatling comprueba estado `200`, identificador y campos; la exactitud del contador la comprueba pytest.

### 6.2 Calentamiento y medición

Una aserción global de Gatling incluye todas las solicitudes, también las del calentamiento. Por eso el calentamiento usa otro nombre de solicitud y las aserciones se aplican solo a la medición con `details(...)`. Con `andThen`, la medición empieza cuando terminan los usuarios del calentamiento.

```java
public class CargaSimulation extends Simulation {
  int tasa = Integer.getInteger("tasa", 20);                  // llegadas por segundo
  int umbralMs = Integer.getInteger("umbralMs", 300);
  int calentamientoS = Integer.getInteger("calentamientoS", 60);
  int medicionS = Integer.getInteger("medicionS", 180);

  HttpProtocolBuilder protocolo = http.baseUrl("http://api:8000");
  FeederBuilder<String> productos = csv("productos.csv").circular();

  ScenarioBuilder consulta(String nombre) {
    return scenario(nombre).feed(productos)
        .exec(http(nombre).get("/productos/#{id}").check(status().is(200)));
  }

  {
    setUp(
        consulta("calentamiento").injectOpen(constantUsersPerSec(tasa).during(calentamientoS))
            .andThen(consulta("medicion").injectOpen(constantUsersPerSec(tasa).during(medicionS))))
        .protocols(protocolo)
        .assertions(
            details("medicion").responseTime().percentile(95.0).lt(umbralMs),
            details("medicion").failedRequests().percent().lte(1.0));
  }
}
```

La tasa, las duraciones y el umbral no se escriben en el código: se leen del perfil, un archivo `config/perfiles/<perfil>.env` (`local.env`, `ci.env`) que los scripts pasan a Gatling como propiedades del sistema (`-Dtasa=20`). El formato `.env` lo leen Compose, PowerShell y `sh` sin dependencias adicionales.

```ini
TASA=20
UMBRAL_MS=300
CALENTAMIENTO_S=60
MEDICION_S=180
ERRORES_MAX_PCT=1.0
```

### 6.3 Tipos de prueba

| Prueba | Pregunta | Perfil | Uso del resultado |
|---|---|---|---|
| Funcional y concurrente | ¿Cumple el contrato y conserva el contador? | Solicitudes controladas y concurrentes | Condición previa a las pruebas de rendimiento |
| Carga | ¿Cumple a la tasa prevista para el entorno? | Calentamiento y meseta a tasa constante | Compuerta: aserciones de p95 y tasa de error |
| Estrés | ¿Dónde empieza la degradación? | Mesetas crecientes, una por ejecución | Informativo; orienta la calibración |
| Picos | ¿Cómo responde a una ráfaga y cuánto tarda en recuperarse? | Base, subida abrupta, pico y regreso a la base | Informativo: errores, tiempos y recuperación |

La resistencia queda fuera: una ejecución breve no demuestra estabilidad prolongada (5.4).

Cada nivel de estrés se ejecuta por separado. En una única ejecución escalonada, las solicitudes lentas de un nivel se mezclan con las del siguiente y el p95 global no describe ninguno; con una ejecución por nivel, el informe de Gatling da el p95 de cada uno. Los percentiles de distintas ejecuciones se informan por separado y nunca se promedian.

### 6.4 Métricas y resultados

Cada medición registra p50, p95 y p99; solicitudes iniciadas, completadas y fallidas; *throughput* de respuestas correctas y tasa de error. Una ejecución que no alcanza la tasa prevista no puede aprobar.

| Resultado | Condición |
|---|---|
| Aprobado | Medición válida que cumple las aserciones |
| Rechazado por rendimiento | Medición válida que incumple alguna aserción; incluye los errores HTTP y *timeouts* de la API bajo carga |
| Inválido | Preparación fallida o medición no interpretable: generador saturado, datos incompletos, configuración distinta de la prevista o pérdida de métricas exigidas |

En los picos, la ventana de observación y la condición de recuperación se fijan antes de medir. Si no hay recuperación dentro de la ventana, se informa ese límite. Los picos no bloquean la integración.

### 6.5 Observabilidad

Gatling mide desde el cliente y decide el veredicto; Prometheus y Grafana muestran las causas dentro del servidor.

| Panel | Métrica | Interpretación |
|---|---|---|
| Solicitudes y errores | Contador por ruta, método y estado | Ritmo de respuestas y errores en el servidor |
| Tiempo en la API | Histograma de duración | Distribución estimada del tiempo de servicio |
| Solicitudes en curso | Indicador | La fila que se forma (ley de Little) |
| Espera del candado | Histograma e indicador en `regresion` | Evidencia directa de la contención |
| CPU de la API | Tiempo de CPU del proceso, como fracción de un núcleo | Distingue la saturación de la espera |
| Memoria de la API | Memoria residente del proceso | Presión de memoria durante cada fase |
| Salud de la recolección | Estado de cada consulta de Prometheus | Muestras ausentes |

La instrumentación está en la propia API, con `prometheus_client`. Como Gunicorn usa un solo proceso, basta el registro por defecto de la biblioteca, que ya incluye la CPU y la memoria del proceso. PostgreSQL y Gatling no necesitan métricas propias. Si la base de datos fuera el cuello de botella, `corregida` también se degradaría, porque recibe la misma carga sobre los mismos datos. La saturación del generador se detecta porque la ejecución no alcanza la tasa prevista (6.4). Los paneles se alinean con las fases de Gatling mediante los intervalos UTC que guarda cada ejecución.

Los tiempos del servidor y los de Gatling no son intercambiables, porque miden en puntos distintos. Las métricas no se etiquetan por producto, para no crear una serie por cada uno. Una CPU baja no demuestra por sí sola que haya contención, y la falta de muestras no demuestra que no haya problemas: bajo sobrecarga, `/metrics` también puede tardar.

## 7. Calibración y validación

Cada computadora es distinta, así que un umbral fijo de antemano no sirve para todas. Y un umbral ajustado con los mismos datos con que después se evalúa parece funcionar siempre. Por eso se separan dos campañas: una para elegir los parámetros y otra, nueva, para comprobarlos (5.6, 5.7).

### 7.1 Calibración

Antes de recoger datos se fijan las repeticiones, las duraciones y el margen mínimo aceptable.

1. **Comprobar el generador.** Se aplica la carga a `GET /salud` y se verifica que Gatling sostiene la tasa prevista; durante esa prueba, `docker stats` muestra si el contenedor de Gatling se acerca a su límite de CPU. Cada usuario virtual abre su propia conexión TCP, y las conexiones cerradas ocupan un puerto mientras están en TIME_WAIT. En el piloto, Gatling sostuvo 350 solicitudes por segundo sin errores, pero a 500 se quedó sin puertos efímeros (`Cannot assign requested address`). Esa ejecución es inválida, no un rechazo de la API.
2. **Explorar.** Se ejecutan mesetas de estrés sobre las variantes para ubicar dónde se degrada cada una.
3. **Elegir la tasa.** `corregida` debe cumplir con holgura y `regresion` ya debe degradarse.
4. **Elegir el umbral.** Se repite la carga en ambas variantes del contador y el umbral de p95 se ubica entre sus rangos, con el margen fijado.
5. **Informar.** Se reportan rangos, mediana, coeficiente de variación y márgenes. Sin separación, o si el generador no sostiene la carga, la calibración no es satisfactoria.
6. **Congelar el perfil**: tasa, umbral, errores permitidos, duraciones, datos, recursos y repeticiones.

Un umbral elegido con una regresión conocida no demuestra, por sí solo, que se detecten regresiones desconocidas.

#### Perfil `ci`

Antes de medir se fijaron tres repeticiones por variante, con las duraciones del perfil (60 s de calentamiento y 180 s de medición) y en orden alternado, y un margen de 3 veces: el umbral debía quedar al menos 3 veces por encima del peor p95 de `corregida` y 3 veces por debajo del mejor p95 de `regresion`.

La exploración en el *runner*, con el perfil `piloto`, encontró el mismo punto de quiebre que en local. `regresion` cumplió a 75 solicitudes por segundo, con un p95 de 13 ms, y colapsó a 100, con 514 ms. `corregida` se mantuvo en 10 ms a 150 y en 16 ms a 300. La tasa elegida fue 150: está bien por encima del quiebre de `regresion`, deja a `corregida` lejos de su límite y no se acerca al del generador.

| Orden | Variante | p50 | p95 | p99 | Errores |
|---:|---|---:|---:|---:|---:|
| 1 | `corregida` | 9 ms | 250 ms | 677 ms | 0 % |
| 2 | `regresion` | 22,7 s | 46,9 s | 60 s | 14,6 % |
| 3 | `regresion` | 23,8 s | 59,3 s | 60 s | 24,9 % |
| 4 | `corregida` | 8 ms | 52 ms | 178 ms | 0 % |
| 5 | `corregida` | 7 ms | 9 ms | 10 ms | 0 % |
| 6 | `regresion` | 24,4 s | 58,7 s | 60 s | 20,1 % |

*Perfil `ci` a 150 sol./s en el* runner *de GitHub Actions: corridas manuales de `compuerta.yml`, de la 42723845007 a la 42728497708. Los 60 s del p99 de `regresion` son el* timeout *de Gatling.*

| p95 | Rango | Mediana | Coeficiente de variación |
|---|---:|---:|---:|
| `corregida` | 9–250 ms | 52 ms | 124 % |
| `regresion` | 46,9–59,3 s | 58,7 s | 13 % |

Con ese margen, el umbral podía ir de 750 ms a 15,6 s. Se eligió 3 000 ms, que redondea el punto medio en escala logarítmica entre los dos extremos (unos 3,4 s) y queda a unas 12 veces del peor `corregida` y a unas 16 del mejor `regresion`. La calibración es satisfactoria. Además, `regresion` incumple la aserción de errores, con 15 a 25 % frente al 1 % permitido, así que su rechazo no depende solo del umbral. El valor inicial de 300 ms no habría servido: la primera corrida de `corregida` quedó a 50 ms de él. El coeficiente de variación de `regresion` subestima su dispersión, porque el *timeout* recorta la cola.

Lo que más condiciona el umbral es la variación de `corregida`. Su p95 cambió 28 veces entre corridas idénticas, mientras el p50 se mantuvo entre 7 y 9 ms: casi todas las solicitudes respondieron igual, pero en algunas corridas aparecieron pausas de 200 ms a 1 s repartidas por toda la medición. La causa no está identificada. Las candidatas son la latencia irregular del disco del *runner* al escribir el WAL de PostgreSQL y la competencia con otras máquinas virtuales del mismo servidor. Tres repeticiones no descartan una corrida con pausas más largas, que haría rechazar una variante correcta; eso lo pone a prueba la validación.

La calibración es preliminar porque todavía no existe la detección de ejecuciones inválidas (T12), de la que depende T13: nada comprueba aún, por ejemplo, que el generador sostuviera la tasa en las seis corridas. Cuando T12 esté lista, se revisan con ella, se congela el perfil con la etiqueta `perfil-ci-v1` y se ejecuta la validación.

### 7.2 Validación

Con el perfil congelado se ejecuta una campaña nueva. Se espera que todas las repeticiones válidas de `corregida` aprueben y que todas las de `regresion` sean rechazadas. El orden de las variantes se alterna y queda registrado, y en CI las campañas se reparten en momentos distintos. Se informan todas las ejecuciones, incluidas las inválidas y su causa. Si el resultado esperado no se mantiene, la validación falla, y el umbral no se ajusta sobre esos datos: se abre una nueva calibración.

## 8. Integración en CI

GitHub Actions reutiliza el procedimiento local con el perfil `ci`. El código del taller está en la carpeta `Taller/` del repositorio de la investigación. Los workflows están en `.github/workflows/`, en la raíz, porque GitHub solo los busca ahí, y ejecutan sus comandos dentro de `Taller/`.

| Workflow | Disparo | Función |
|---|---|---|
| Compuerta | `push` y `pull_request` que modifican `Taller/` o los workflows | Pruebas funcionales y carga breve sobre la variante activa |
| Escenarios | Manual | Carga, estrés o picos sobre una variante |
| Calibración | Manual | Propuesta de perfil `ci` para revisión |
| Validación | Manual o programada | Campaña nueva con el perfil congelado |

La variante activa se define en la configuración. Un *pull request* que la cambia a `regresion` reproduce un cambio defectuoso y la compuerta lo rechaza; uno que la cambia a `corregida` aprueba.

```yaml
on:
  push: { paths: ["Taller/**", ".github/workflows/**"] }
  pull_request: { paths: ["Taller/**", ".github/workflows/**"] }
jobs:
  rendimiento:
    runs-on: ubuntu-24.04
    defaults:
      run: { working-directory: Taller }
    steps:
      - uses: actions/checkout@v7
      - run: ./taller.sh preparar
      - run: ./taller.sh funcionales
      - run: ./taller.sh ejecutar --tipo carga --perfil ci
      - uses: actions/upload-artifact@v7
        if: always()                     # conserva el informe aunque la prueba falle
        with: { name: resultados, path: Taller/resultados/ }
```

La compuerta falla tanto por rendimiento como por errores de infraestructura, y el resumen distingue ambas causas. Cada medición usa su propio entorno; dos *jobs* que comparten servicios no se ejecutan en paralelo. Las características del runner quedan registradas, porque fijar `ubuntu-24.04` no fija el hardware asignado.

## 9. Construcción

La construcción avanza en tres fases. Cada una deja un resultado demostrable, y el piloto de la primera comprueba pronto que el caso separa las variantes.

| Fase | Etapa | Criterio de terminación |
|---|---|---|
| 1. Núcleo | Entorno base: Compose con API y PostgreSQL, datos semilla, versiones fijas | Una preparación limpia levanta los servicios y supera los *healthchecks* |
| | Variantes de la API y métricas en `/metrics` | pytest aprueba contrato y concurrencia en ambas variantes del contador |
| | Simulación de carga | El informe separa calentamiento y medición, y las aserciones fallan cuando corresponde |
| | Piloto | Hay separación entre `regresion` y `corregida`, y el generador sostiene la tasa |
| | Compuerta en CI | El *pull request* con `regresion` falla, el de `corregida` aprueba y quedan los artefactos |
| | Guía, `taller.ps1` y `taller.sh` | La práctica se completa siguiendo solo la guía |
| 2. Rigor | Estrés y picos | Los informes muestran degradación y recuperación |
| | Calibración y validación, local y `ci` | Se obtienen perfiles con márgenes y se mantienen los veredictos esperados |
| | Detección de ejecuciones inválidas | Una ejecución con el generador saturado o datos incompletos se marca como inválida |
| 3. Observabilidad y alcance | Prometheus y paneles de Grafana | Los paneles aparecen sin configuración manual y muestran la espera del candado |
| | Plataformas soportadas | El procedimiento funciona en Windows y en Linux o macOS |
| | Workflows manuales y programados | Cada uno conserva su informe como artefacto |
| | Reproducción externa | Una persona ajena al desarrollo completa la práctica con la guía |

**Parámetros por definir durante la construcción:** la tasa y el umbral del perfil `local`, que salen de su calibración, y la forma de exportar las métricas del informe de Gatling. La configuración de 5.2 ya quedó fijada en el piloto, y el perfil `ci` tiene tasa, umbral, repeticiones y margen de una calibración preliminar (7.1).

```text
Taller/
├── Taller.md             este documento
├── CONTRIBUIR.md         reglas de Git
├── api/                  Flask, variantes, métricas, pruebas y Dockerfile
├── base-datos/           esquema y datos sintéticos
├── rendimiento/          simulaciones Gatling, Maven Wrapper y Dockerfile
├── observabilidad/       Prometheus y paneles de Grafana
├── config/               perfiles (local.env, ci.env) y reglas de calibración
├── herramientas/         extracción y agregación de resultados
├── compose.yaml          sistema bajo prueba y observabilidad
├── compose.carga.yaml    Gatling y herramientas
├── taller.ps1 · taller.sh
├── docs/                 GUIA.md, PLAN-DE-PRUEBAS.md, INTERPRETACION.md
└── resultados/           generados por cada ejecución, fuera del control de versiones

.github/workflows/        compuerta y workflows manuales, en la raíz del repositorio
```

Cada ejecución guarda en su carpeta la revisión del código, la variante, el perfil, la semilla, el entorno, los intervalos de tiempo, el informe de Gatling, las métricas exportadas, los registros y el veredicto.

## 10. Sección 6 del documento de investigación

La sección 6 es un resumen ejecutivo de 6 páginas, con tablas y figuras incluidas. Se organiza según los cuatro elementos que exige el enunciado —contexto de aplicación, recursos y código, stack tecnológico y guía paso a paso— y agrega el plan de pruebas, los resultados y los límites. El detalle técnico queda en el repositorio y en el anexo C.

| Subsección | Págs. | Contenido | Marco teórico | Tablas y figuras |
|---|---:|---|---|---|
| 6.1 Contexto de aplicación | 0,75 | Caso de la tienda, regresión, corrección y relación con PI-5 | 5.1, 5.2 | — |
| 6.2 Recursos y código | 0,50 | Repositorio, estructura, requisitos y entregables | — | — |
| 6.3 Stack tecnológico | 0,75 | Componentes, versiones y función; elección de Gatling | 5.8 | Tabla 4. Stack del taller · Figura 4. Arquitectura del entorno |
| 6.4 Plan de pruebas | 1,50 | Objetivos, escenario y modelo abierto, tipos de prueba, criterios, calibración y validación | 5.3–5.7 | Tabla 5. Pruebas del taller |
| 6.5 Guía paso a paso | 1,00 | Procedimiento local y compuerta en CI | 5.7 | — |
| 6.6 Resultados e interpretación | 1,00 | Veredictos de la validación, márgenes, variación y observaciones de Grafana | 5.3, 5.6, 5.7 | Tabla 6. Resultados de la validación · Figura 5. p95 por variante o panel de Grafana |
| 6.7 Límites | 0,50 | Regresión conocida, recursos compartidos y validez restringida al perfil y al entorno | 5.5 | — |
| **Total** | **6,00** | | | |

La sección remite al Marco teórico por número de subsección en lugar de repetir sus citas, y solo incorpora fuentes nuevas para el stack: documentación oficial de Docker Compose, Prometheus y GitHub Actions, además de la de Gatling, ya citada. Los resultados de 6.6 se redactan a partir de la campaña de validación.

El anexo C contiene el enlace al repositorio, extractos de la simulación y del workflow, y una captura del informe de Gatling o de Grafana. Las conclusiones (sección 7) responden PI-5 con los resultados de 6.6.

## 11. Tareas

Las tareas siguen las fases de la sección 9 y se reparten en dos líneas de trabajo que avanzan en paralelo:

- **Persona 1, sistema bajo prueba:** entorno, datos, API, pruebas funcionales y observabilidad.
- **Persona 2, carga y automatización:** Gatling, scripts, resultados, calibración en CI y workflows.

Cada persona sube sus cambios directamente a `main` y usa ramas y *pull requests* solo cuando hacen falta. El flujo y las convenciones de nombres están en [`CONTRIBUIR.md`](CONTRIBUIR.md).

### Acuerdos entre las dos líneas

Estos acuerdos se fijan en T1, así ninguna línea espera a que la otra termine para empezar a escribir código:

| Acuerdo | Valor |
|---|---|
| Contrato de la API | El de 4.1 |
| Servicios de Compose | `api` en el puerto 8000, `postgres`, `prometheus` y `grafana` en `compose.yaml` (persona 1); `gatling` y `herramientas`, con el perfil `carga`, en `compose.carga.yaml` (persona 2). Los scripts usan los dos archivos |
| Selección de variante | Variable de entorno `VARIANTE` (`regresion`, `corregida` o `sana`). La variante activa está en `config/variante.env` y `compose.yaml` la recibe como `${VARIANTE:-corregida}` |
| Salud de la API | *Healthcheck* de `api` sobre `/salud`. Los scripts exigen el estado `healthy` antes de medir |
| Restablecimiento | `base-datos/restablecer.sql`, que los scripts ejecutan con `psql` dentro de `postgres`. Requiere `base-datos/` montada en `/base-datos` y `POSTGRES_USER` y `POSTGRES_DB` definidas |
| Identificadores para Gatling | `base-datos/productos.csv`, con encabezado `id` y valores de 1 a 10 000 |
| Pruebas funcionales | `docker compose run --rm api pytest` |
| Perfiles | Claves de 6.2 en `config/perfiles/<perfil>.env` |

Con estos acuerdos, la persona 2 escribe la simulación contra `/salud` y con un CSV provisional mientras la persona 1 implementa la API.

### Fase 1. Núcleo

| ID  | Tarea                                                                                                                                                                               | Depende de | Resultado esperado                                                                                          | Responsable |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| T1  | Estructura de `Taller/`, acuerdos de esta sección y `compose.yaml` con PostgreSQL y un esqueleto de la API que responde `/salud`; *healthchecks*, límites de 5.2 y versiones de 5.1 | —          | Una preparación limpia levanta los servicios sanos                                                          | 1           |
| T2  | Esquema SQL, generador de datos con semilla, CSV de identificadores y restablecimiento del estado                                                                                   | T1         | Datos idénticos en cada preparación                                                                         | 1           |
| T3  | API con Flask, Gunicorn y psycopg-pool: `/productos/{id}`, las tres variantes por configuración y `/metrics`                                                                        | T2         | Las tres variantes responden según el contrato                                                              | 1           |
| T4  | Pruebas con pytest: contrato, `404`, reversión ante fallos y concurrencia sobre el mismo producto y sobre productos distintos                                                       | T3         | Ambas variantes del contador aprueban, y un leer-sumar-escribir sin candado falla la prueba de concurrencia | 1           |
| T5  | Proyecto Gatling: Maven Wrapper, `pom.xml`, Dockerfile y `CargaSimulation`                                                                                                          | T1         | La simulación corre contra la API y falla con un umbral inalcanzable                                        | 2           |
| T6  | Perfiles `.env` y scripts `taller.ps1` y `taller.sh`: preparar, funcionales, ejecutar, exportar y detener; carpeta de resultados con sus metadatos                                  | T5         | Cada operación se ejecuta con un comando y deja su resultado                                                | 2           |
| T7  | Piloto: carga sobre `regresion` y `corregida`, y ajuste de los valores de 5.2                                                                                                       | T3, T6     | Hay separación entre las variantes y el generador sostiene la tasa                                          | 1           |
| T8  | Workflow de la compuerta y los dos *pull requests* de demostración                                                                                                                  | T4, T6     | El de `regresion` falla, el de `corregida` aprueba y quedan los artefactos                                  | 2           |
| T9  | `docs/GUIA.md` con el procedimiento local y la compuerta                                                                                                                            | T7, T8     | La práctica se completa siguiendo solo la guía                                                              | 1           |

### Fase 2. Rigor

| ID | Tarea | Depende de | Resultado esperado | Responsable |
|---|---|---|---|---|
| T10 | Simulaciones de estrés, una meseta por ejecución, y de picos, con su ventana de recuperación | T5 | Informes que muestran la degradación y la recuperación | 2 |
| T11 | Extracción de resultados: p50, p95, p99, conteos, tasa lograda y resumen por campaña | T6 | Un archivo de resultados por ejecución y uno por campaña | 2 |
| T12 | Detección de ejecuciones inválidas | T11 | Una ejecución con tasa no alcanzada, datos incompletos o configuración distinta queda marcada como inválida | 2 |
| T13 | Calibración local y `ci` (7.1) | T10, T12, T16 | Perfiles congelados con sus márgenes | 1: local · 2: `ci` |
| T14 | Validación local y `ci` (7.2) | T13 | Veredictos esperados en todas las repeticiones válidas | 1: local · 2: `ci` |
| T15 | `docs/PLAN-DE-PRUEBAS.md` | T13 | Objetivos, escenario, criterios y perfiles documentados | 2 |

### Fase 3. Observabilidad y alcance

| ID  | Tarea                                                                     | Depende de | Resultado esperado                                                                           | Responsable |
| --- | ------------------------------------------------------------------------- | ---------- | -------------------------------------------------------------------------------------------- | ----------- |
| T16 | Prometheus y paneles de Grafana provisionados (6.5)                       | T3         | Los paneles aparecen al levantar el entorno y muestran la espera del candado                 | 1           |
| T17 | Workflows manuales y programados: escenarios, calibración y validación    | T8, T13    | Cada uno conserva su informe como artefacto                                                  | 2           |
| T18 | Ejecución en Linux o macOS; en Windows sirve WSL2                         | T6         | El procedimiento funciona igual que en Windows                                               | 1           |
| T19 | `docs/INTERPRETACION.md`: lectura del informe de Gatling y de los paneles | T14, T16   | Cada panel y métrica del informe tiene su interpretación                                     | 1           |
| T20 | Reproducción externa                                                      | T9, T19    | Una persona ajena al desarrollo completa la práctica y se corrigen los problemas encontrados | 1 y 2       |

T16 pertenece a la fase 3, pero se hace antes de calibrar. Así Prometheus está activo desde la primera campaña, la recolección forma parte de las condiciones medidas y no hay que repetir la validación.

### Documento

| ID | Tarea | Depende de | Resultado esperado | Responsable |
|---|---|---|---|---|
| T21 | Sección 6 y anexo C, según la sección 10 | T14, T16 | Sección de 6 páginas con los resultados de la validación | 1: 6.1, 6.3, 6.6 y 6.7 · 2: 6.2, 6.4, 6.5 y anexo C |

### Secuencia

| Persona | Orden |
|---|---|
| 1 | T1 → T2 → T3 → T4 → T16 → T7 → T9 → T18 → T13 y T14 local → T19 |
| 2 | T5 → T6 → T8 → T10 → T11 → T12 → T13 y T14 `ci` → T15 → T17 |
| Ambas | T20 → T21 |

La persona 2 empieza T5 el mismo día que la persona 1 empieza T1: el proyecto de Gatling compila sin la API, y cuando T1 está integrado ya se puede ejecutar contra `/salud`. Mientras la persona 1 termina T4 y T16, la persona 2 ya tiene T6 listo para el piloto (T7). Cuando la persona 1 llega a la calibración, la persona 2 ya terminó T10 y T12. La sección 6 se reparte en 3 páginas para cada una.
