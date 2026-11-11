# Glosario

Términos del documento y la forma en que se escriben. Sirve para que todas las secciones usen el mismo vocabulario. Lo leen el planificador, el redactor y el auditor.

**Reglas:**

- **Forma en el texto:** es la forma obligatoria. Los sinónimos de la columna «Evitar» no se usan para el mismo concepto.
- **Primera aparición:** un término en inglés va en cursiva. Si tiene equivalente en español, se escribe la primera vez como «equivalente (*término*)» y después con la forma indicada.
- **Definición de trabajo:** solo sirve para mantener la coherencia. No es una cita ni reemplaza a la fuente: en el documento, toda definición sale de una fuente con su fila de evidencia. Mientras la subsección que define el término no esté aprobada, la definición es **provisional**.
- **Altas:** el planificador agrega los términos que su sección define o introduce cuando el plan se aprueba. El redactor puede agregar uno que no estaba previsto y marcarlo como «Agregado por el redactor». Nadie cambia la forma de un término sin revisar dónde se usa ya.

## Calidad y ciclo de vida

| Término | Inglés | Forma en el texto | Evitar | Definición de trabajo | Define | Usado en |
|---|---|---|---|---|---|---|
| Rendimiento | performance | rendimiento | — | Atributo general del sistema relacionado con el tiempo y los recursos. «Desempeño» se acepta como sinónimo en la prosa, pero los términos fijos usan «rendimiento» (pruebas de rendimiento, regresión de rendimiento). | 5.2 | 02, 03, 04 |
| Eficiencia de desempeño | performance efficiency | eficiencia de desempeño | eficiencia de rendimiento | Característica de calidad del producto en ISO/IEC 25010:2023. Es el término normativo, y solo se usa para referirse a la norma. | 5.2 | 02 |
| Comportamiento temporal | time behaviour | comportamiento temporal | comportamiento en el tiempo | Subcaracterística de la eficiencia de desempeño (ISO/IEC 25010:2023). Provisional hasta aprobar 5.2. | 5.2 | — |
| Utilización de recursos | resource utilization | utilización de recursos | uso de recursos (se acepta en prosa) | Subcaracterística de la eficiencia de desempeño (ISO/IEC 25010:2023). Provisional hasta aprobar 5.2. | 5.2 | — |
| Capacidad | capacity | capacidad | — | Subcaracterística de la eficiencia de desempeño (ISO/IEC 25010:2023). No confundir con la prueba de capacidad (5.4). Provisional hasta aprobar 5.2. | 5.2 | — |
| Prueba de rendimiento | performance testing | prueba de rendimiento | prueba de desempeño, test de performance | Prueba que evalúa el comportamiento temporal y el uso de recursos de un sistema bajo una carga dada. Provisional. | 5.3–5.4 | 02, 03, 04 |
| Aseguramiento de la calidad | quality assurance (QA) | aseguramiento de la calidad, sin sigla | QA | Enfoque de proceso, preventivo; las pruebas son una forma de control de la calidad del producto. Provisional hasta aprobar 5.1. | 5.1 | — |
| Modelo en V | V-model | modelo en V | modelo V | Modelo de ciclo de vida secuencial. Provisional hasta aprobar 5.1. | 5.1 | — |
| Nivel de prueba | test level | nivel de prueba: prueba de componentes, de integración de componentes, de sistema, de integración de sistemas y de aceptación | etapa de prueba | Provisional hasta aprobar 5.1. | 5.1 | 02 |
| DevOps | DevOps | DevOps (sin cursiva, asimilado) | — | Provisional hasta aprobar 5.1. | 5.1 | — |
| Fase de implementación | implementation phase | fase de implementación | — | En este trabajo, la validación previa al despliegue del sistema integrado (`Alcance.md` §1). | 5.1 | 02 |
| Integración continua (CI) | continuous integration | integración continua (CI); después, CI | CI/CD cuando solo se habla de integración | Provisional. | 5.1, 5.7 | 02, 03 |
| Entrega continua | continuous delivery | entrega continua, sin sigla propia | CD sola (ambigua: el CTFL la usa para la entrega y Shahin et al. para el despliegue) | Provisional hasta aprobar 5.1. | 5.1 | — |
| Despliegue continuo | continuous deployment | despliegue continuo, sin sigla | CD sola | Provisional hasta aprobar 5.1. | 5.1 | — |
| CI/CD | CI/CD | CI/CD | — | Integración continua junto con entrega o despliegue continuos. Término preferido para hablar de estas prácticas en conjunto (preferencia del usuario). | 5.1 | 03 |
| Pipeline | pipeline | pipeline (sin cursiva, asimilado) | tubería, *pipeline* en cursiva | Secuencia automatizada de pasos de construcción, prueba y despliegue. | 5.1 | 02, 03 |
| Pipeline de despliegue | deployment pipeline | pipeline de despliegue (*deployment pipeline*) la primera vez; después, pipeline | — | Modelo automatizado del camino de cada cambio, desde el control de versiones hasta los usuarios (Humble y Farley). Provisional hasta aprobar 5.1. | 5.1 | — |
| *Quality gate* | quality gate | *quality gate* | puerta de calidad | Compuerta del pipeline: un cambio no avanza a la etapa siguiente si no supera sus criterios (Humble y Farley la llaman *gate*). Provisional hasta aprobar 5.1. | 5.1, 5.7 | — |
| *Shift-left* / *shift-right* | shift-left / shift-right | *shift-left*, *shift-right* | — | Provisional. | 5.1 | — |

## Métricas y modelos de carga

| Término | Inglés | Forma en el texto | Evitar | Definición de trabajo | Define | Usado en |
|---|---|---|---|---|---|---|
| Tiempo de respuesta | response time | tiempo de respuesta | latencia, para lo que mide el cliente | Tiempo que el cliente espera la respuesta a una solicitud. Cuando una fuente dice «latency» en ese sentido, se traduce como tiempo de respuesta. Provisional hasta aprobar 5.3. | 5.3 | 02 |
| Latencia | latency | latencia, solo para la latencia de red | latencia como sinónimo de tiempo de respuesta | Decisión de terminología del trabajo, siguiendo el uso del CT-PT («network latency»). Provisional hasta aprobar 5.3. | 5.3 | — |
| *Throughput* | throughput | *throughput* | rendimiento (choca con *performance*), caudal | Cantidad de trabajo completado por unidad de tiempo. Provisional hasta aprobar 5.3. | 5.3 | 02 |
| Tasa de error | error rate | tasa de error | — | Fracción de las solicitudes que fallan sobre el total recibido (Jones et al., 2016). Provisional hasta aprobar 5.3. | 5.3 | — |
| Percentil | percentile | percentil 95 (p95); después, p95 | — | Provisional hasta aprobar 5.3. | 5.3 | — |
| Promedio | average, mean | promedio | media | Se usa una sola forma para no mezclar términos. | — | — |
| Concurrencia | concurrency | concurrencia | — | Provisional hasta aprobar 5.3. | 5.3 | — |
| Usuario virtual | virtual user | usuario virtual | VU sin definir | Provisional hasta aprobar 5.3. | 5.3 | — |
| *Think time* | think time | tiempo de espera entre acciones (*think time*); después, *think time* | tiempo de pensamiento | Provisional hasta aprobar 5.3. | 5.3 | — |
| Modelo de carga abierto / cerrado | open / closed workload model | modelo de carga abierto, modelo de carga cerrado | sistema abierto/cerrado sin «modelo de carga» | Provisional hasta aprobar 5.3. | 5.3 | — |
| *Coordinated omission* | coordinated omission | *coordinated omission* | omisión coordinada sin el término original | Provisional hasta aprobar 5.3. | 5.3 | — |
| Ley de Little | Little's law | ley de Little | — | Provisional hasta aprobar 5.3. | 5.3 | — |

## Tipos de prueba

| Término | Inglés | Forma en el texto | Evitar | Definición de trabajo | Define | Usado en |
|---|---|---|---|---|---|---|
| Prueba de carga | load testing | prueba de carga | — | Provisional hasta aprobar 5.4. | 5.4 | 03 |
| Prueba de estrés | stress testing | prueba de estrés | prueba de esfuerzo | Provisional hasta aprobar 5.4. | 5.4 | — |
| Prueba de picos | spike testing | prueba de picos (*spike*) | — | Provisional hasta aprobar 5.4. | 5.4 | — |
| Prueba de resistencia | soak / endurance testing | prueba de resistencia (*soak* o *endurance*) | prueba de remojo | El CT-PT usa *endurance*. Provisional hasta aprobar 5.4. | 5.4 | — |
| Prueba de escalabilidad, de volumen, de capacidad | scalability, volume, capacity testing | prueba de escalabilidad, de volumen, de capacidad | — | Solo se mencionan (`Alcance.md` §4). El volumen se trata como la dimensión de datos de la capacidad: el CT-PT no define una prueba de volumen aparte. Provisional hasta aprobar 5.4. | 5.4 | — |
| Perfil de carga | load profile | perfil de carga | — | Forma de la carga en el tiempo (rampas, escalones, mesetas, ráfagas). Provisional hasta aprobar 5.4. | 5.4 | — |
| Rampa de subida / de bajada | ramp-up / ramp-down | rampa de subida (*ramp-up*), rampa de bajada (*ramp-down*) | — | Provisional hasta aprobar 5.4. | 5.4 | — |
| Estado estable | steady state | estado estable (*steady state*) la primera vez; después, estado estable | régimen estacionario | Fase de la prueba en que el comportamiento del sistema es estable, después de la rampa de subida. Agregado por el redactor. Provisional hasta aprobar 5.4. | 5.4 | — |
| Prueba comparativa | benchmark | prueba comparativa (*benchmark*); después, prueba comparativa | — | Ejecución repetible que mide el rendimiento para comparar versiones o configuraciones. Provisional. | 5.4 | 02, 03 |
| *Microbenchmark* | microbenchmark | *microbenchmark* | — | Excluido como tema (`Alcance.md` §4); solo se menciona. | — | 03, 04 |

## Ejecución y automatización

| Término | Inglés | Forma en el texto | Evitar | Definición de trabajo | Define | Usado en |
|---|---|---|---|---|---|---|
| Sistema bajo prueba | system under test (SUT) | sistema bajo prueba | SUT sin definir | Provisional hasta aprobar 5.5. | 5.5 | — |
| Entorno de prueba | test environment | entorno de prueba | ambiente de pruebas | Provisional hasta aprobar 5.5. | 5.5 | 03 |
| Generador de carga | load generator / load driver | generador de carga | inyector, driver | Provisional hasta aprobar 5.5. | 5.5, 5.8 | 03 |
| Perfil operacional | operational profile | perfil operacional | — | Patrón de interacción de un tipo de usuario o componente con el sistema; varios se combinan en un perfil de carga. Provisional hasta aprobar 5.5. | 5.5 | — |
| Línea base | baseline | línea base | *baseline* | Provisional hasta aprobar 5.6. | 5.6 | — |
| Calentamiento | warm-up | período de calentamiento (*warm-up*) la primera vez; después, calentamiento | — | Período inicial que no se mide, mientras el sistema estabiliza su comportamiento. Provisional hasta aprobar 5.6. | 5.6 | — |
| Ruido | noise | ruido | — | Variación entre ejecuciones que no se debe al cambio evaluado. Provisional hasta aprobar 5.6. | 5.6 | 03 |
| Antipatrón | antipattern | antipatrón | — | Provisional hasta aprobar 5.6. | 5.6 | — |
| Regresión de rendimiento | performance regression | regresión de rendimiento | degradación (se acepta en prosa como sinónimo) | Cambio que empeora el rendimiento respecto de una versión anterior. Provisional hasta aprobar 5.7. | 5.7 | 02, 03 |
| Aserción de rendimiento | performance assertion | aserción de rendimiento | — | Provisional hasta aprobar 5.7. | 5.7 | 03 |
| Criterio de aceptación | acceptance criterion | criterio de aceptación | — | Provisional hasta aprobar 5.6. | 5.6, 5.7 | 03 |
| Indicador de nivel de servicio (SLI) | service level indicator | indicador de nivel de servicio (SLI); después, SLI | — | Medida cuantitativa de un aspecto del nivel de servicio (Jones et al., 2016). Provisional hasta aprobar 5.7. | 5.7 | — |
| Objetivo de nivel de servicio (SLO) | service level objective | objetivo de nivel de servicio (SLO); después, SLO | — | Provisional hasta aprobar 5.7. | 5.7 | — |
| Acuerdo de nivel de servicio (SLA) | service level agreement | acuerdo de nivel de servicio (SLA); después, SLA | — | Agregado por el redactor. | — | 05 |
| Umbral | threshold | umbral | — | Valor contra el que se compara una métrica para aprobar o rechazar. Provisional hasta aprobar 5.7. | 5.7 | — |
| Prueba de humo de rendimiento | performance smoke test, guard test | prueba de humo de rendimiento | prueba de guarda | Prueba breve en la etapa de *commit* que vigila puntos críticos conocidos. Provisional hasta aprobar 5.7. | 5.7 | — |
| Detección de puntos de cambio | change point detection | detección de puntos de cambio | — | Provisional hasta aprobar 5.7. | 5.7 | — |
| Observabilidad / APM | observability / application performance monitoring | observabilidad; monitoreo del rendimiento de aplicaciones (APM) | — | Solo se mencionan (`Alcance.md` §4). | 5.7 | — |

## Taller

| Término | Inglés | Forma en el texto | Evitar | Definición de trabajo | Define | Usado en |
|---|---|---|---|---|---|---|
| Candado | lock | candado (*lock*) la primera vez; después, candado | cerrojo, bloqueo (para el objeto) | Mecanismo de exclusión mutua entre hilos; en el taller, un `threading.Lock` compartido por todas las solicitudes. | 6.1 | — |
| Variante | — | variante, con su nombre en código: `regresion`, `corregida`, `sana` | versión (para las variantes) | Implementación de la API que se selecciona por configuración. | 6.1 | — |
| Perfil de ejecución | — | perfil de ejecución, con su nombre en código (`ci`, `local`) | perfil solo (choca con perfil de carga) | Archivo con la tasa, el umbral y las duraciones calibrados para un entorno. | 6.4 | — |
| Campaña | — | campaña de calibración, campaña de validación | — | Conjunto de ejecuciones con reglas fijadas antes de medir, para elegir o comprobar un perfil de ejecución. | 6.4 | — |
| Ejecución inválida | — | ejecución inválida | ejecución fallida (se confunde con un rechazo) | Medición que no se puede interpretar: el generador no sostuvo la tasa, faltan datos o la configuración no es la pedida. | 6.4 | — |
| Workflow | workflow | workflow (sin cursiva, como en 5.7) | flujo de trabajo (choca con el procedimiento de la Metodología) | Archivo YAML de GitHub Actions que define cuándo y qué se ejecuta. Agregado por el redactor. | — | 05, 06 |
