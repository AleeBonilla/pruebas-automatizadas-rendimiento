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
| Prueba de rendimiento | performance testing | prueba de rendimiento | prueba de desempeño, test de performance | Prueba que evalúa el comportamiento temporal y el uso de recursos de un sistema bajo una carga dada. Provisional. | 5.3–5.4 | 02, 03, 04 |
| Fase de implementación | implementation phase | fase de implementación | — | En este trabajo, la validación previa al despliegue del sistema integrado (`Alcance.md` §1). | 5.1 | 02 |
| Integración continua (CI) | continuous integration | integración continua (CI); después, CI | CI/CD cuando solo se habla de integración | Provisional. | 5.1, 5.7 | 02, 03 |
| Entrega continua (CD) | continuous delivery | entrega continua (CD) | — | Provisional. | 5.1 | — |
| Pipeline | pipeline | pipeline (sin cursiva, asimilado) | tubería, *pipeline* en cursiva | Secuencia automatizada de pasos de construcción, prueba y despliegue. | 5.1 | 02, 03 |
| *Quality gate* | quality gate | *quality gate* | puerta de calidad | Control automatizado que aprueba o rechaza un cambio según criterios. Provisional. | 5.1, 5.7 | — |
| *Shift-left* / *shift-right* | shift-left / shift-right | *shift-left*, *shift-right* | — | Provisional. | 5.1 | — |

## Métricas y modelos de carga

| Término | Inglés | Forma en el texto | Evitar | Definición de trabajo | Define | Usado en |
|---|---|---|---|---|---|---|
| Tiempo de respuesta | response time | tiempo de respuesta | — | Se distingue de latencia en 5.3. Provisional. | 5.3 | 02 |
| Latencia | latency | latencia | — | Provisional; ver tiempo de respuesta. | 5.3 | — |
| *Throughput* | throughput | *throughput* | rendimiento (choca con *performance*), caudal | Cantidad de trabajo completado por unidad de tiempo. Provisional. | 5.3 | 02 |
| Tasa de error | error rate | tasa de error | — | Provisional. | 5.3 | — |
| Percentil | percentile | percentil 95 (p95); después, p95 | — | Provisional. | 5.3 | — |
| Concurrencia | concurrency | concurrencia | — | Provisional. | 5.3 | — |
| Usuario virtual | virtual user | usuario virtual | VU sin definir | Provisional. | 5.3 | — |
| *Think time* | think time | tiempo de espera entre acciones (*think time*); después, *think time* | tiempo de pensamiento | Provisional. | 5.3 | — |
| Modelo de carga abierto / cerrado | open / closed workload model | modelo de carga abierto, modelo de carga cerrado | sistema abierto/cerrado sin «modelo de carga» | Provisional. | 5.3 | — |
| *Coordinated omission* | coordinated omission | *coordinated omission* | omisión coordinada sin el término original | Provisional. | 5.3 | — |
| Ley de Little | Little's law | ley de Little | — | Provisional. | 5.3 | — |

## Tipos de prueba

| Término | Inglés | Forma en el texto | Evitar | Definición de trabajo | Define | Usado en |
|---|---|---|---|---|---|---|
| Prueba de carga | load testing | prueba de carga | — | Provisional. | 5.4 | 03 |
| Prueba de estrés | stress testing | prueba de estrés | prueba de esfuerzo | Provisional. | 5.4 | — |
| Prueba de picos | spike testing | prueba de picos (*spike*) | — | Provisional. | 5.4 | — |
| Prueba de resistencia | soak / endurance testing | prueba de resistencia (*soak*) | prueba de remojo | Provisional. | 5.4 | — |
| Prueba de escalabilidad, de volumen, de capacidad | scalability, volume, capacity testing | prueba de escalabilidad, de volumen, de capacidad | — | Solo se mencionan (`Alcance.md` §4). Provisional. | 5.4 | — |
| Prueba comparativa | benchmark | prueba comparativa (*benchmark*); después, prueba comparativa | — | Ejecución repetible que mide el rendimiento para comparar versiones o configuraciones. Provisional. | 5.4 | 02, 03 |
| *Microbenchmark* | microbenchmark | *microbenchmark* | — | Excluido como tema (`Alcance.md` §4); solo se menciona. | — | 03, 04 |

## Ejecución y automatización

| Término | Inglés | Forma en el texto | Evitar | Definición de trabajo | Define | Usado en |
|---|---|---|---|---|---|---|
| Sistema bajo prueba | system under test (SUT) | sistema bajo prueba | SUT sin definir | Provisional. | 5.5 | — |
| Entorno de prueba | test environment | entorno de prueba | ambiente de pruebas | Provisional. | 5.5 | 03 |
| Generador de carga | load generator / load driver | generador de carga | inyector, driver | Provisional. | 5.5, 5.8 | 03 |
| Línea base | baseline | línea base | *baseline* | Provisional. | 5.6 | — |
| Regresión de rendimiento | performance regression | regresión de rendimiento | degradación (se acepta en prosa como sinónimo) | Cambio que empeora el rendimiento respecto de una versión anterior. Provisional. | 5.7 | 02, 03 |
| Aserción de rendimiento | performance assertion | aserción de rendimiento | — | Provisional. | 5.7 | 03 |
| Criterio de aceptación | acceptance criterion | criterio de aceptación | — | Provisional. | 5.6, 5.7 | 03 |
| Objetivo de nivel de servicio (SLO) | service level objective | objetivo de nivel de servicio (SLO); después, SLO | — | Provisional. | 5.7 | — |
| Observabilidad / APM | observability / application performance monitoring | observabilidad; monitoreo del rendimiento de aplicaciones (APM) | — | Solo se mencionan (`Alcance.md` §4). | 5.7 | — |
