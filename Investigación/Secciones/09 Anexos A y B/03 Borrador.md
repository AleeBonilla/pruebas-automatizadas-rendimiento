# Anexo A. Registro resumido de consultas

<!-- Borrador v2 | 2026-11-11 | Resume los registros del repositorio (Investigación/Secciones/*/01 Plan.md y 02 Evidencia.md, y el historial de Git). Sin auditoría independiente. -->

Este anexo resume cómo se usaron las herramientas de inteligencia artificial y cómo se buscaron y descartaron las fuentes (4.2 y 4.3). El registro completo está en `Investigación/Secciones/`, en el repositorio.

### A.1 Herramientas y funciones

**Tabla A1.** Herramientas de inteligencia artificial y su función

| Herramienta | Función | Registro |
|---|---|---|
| Claude Code (Opus 5.5) | Planificar y redactar cada sección; escribir y documentar el código del taller | Plan, evidencia y borrador de cada sección. Al 11 de noviembre de 2026, 57 de los 81 *commits* llevan su coautoría |
| Codex (GPT-6.1 Sol) | Auditar los borradores y su evidencia, en una sesión independiente | Auditoría de cada sección |

*Fuente:* elaboración propia, a partir del repositorio.

### A.2 Consultas de búsqueda

Las consultas de la Introducción, del Planteamiento y de la Metodología no se registraron: de esas secciones solo consta qué fuentes se verificaron. Desde el Marco teórico se registró cada consulta, todas del 7 de noviembre de 2026, en un buscador web.

**Tabla A2.** Consultas, fuentes y evidencia por parte del documento

| Parte | Consultas | Resultados revisados | Con fuente elegida | Sin fuente elegida | Fuentes verificadas | Filas de evidencia |
|---|---:|---:|---:|---:|---:|---:|
| Introducción | — | — | — | — | 8 | 29 |
| Planteamiento del problema | — | — | — | — | 7 | 30 |
| Metodología | — | — | — | — | 2 | 5 |
| Marco teórico, 5.1 y 5.2 | 6 | 85 | 3 | 3 | 7 | 26 |
| Marco teórico, 5.3 y 5.4 | 6 | 60 | 4 | 2 | 5 | 31 |
| Marco teórico, 5.5 a 5.7 | 1 | 19 | 1 | 0 | 5 | 31 |
| Marco teórico, 5.8 | 9 | 74 | 5 | 4 | 9 | 44 |
| Sección 6 | — | — | — | — | 4 | 4 |
| **Total** | **22** | **238** | **13** | **9** | **47** | **200** |

*Fuente:* elaboración propia. Una fuente puede figurar en más de un plan: el documento cita 34 referencias distintas. Una fila de evidencia es una cita literal con su ubicación. En la sección 6 se consultó directamente la documentación oficial.

### A.3 Fuentes descartadas

Las fuentes se descartaron por cinco motivos: ser una copia, un resumen o un espejo de terceros (5.1 y 5.3); ser contenido comercial, un blog o carecer de autoría (5.1 y 5.8); tener accesible solo el resumen, como *The Tail at Scale* (5.3); ser documentación de otro producto o de una versión anterior, como la de LoadRunner Enterprise frente a la de Professional (5.8), o quedar fuera del alcance o sin datos de publicación completos, como un estudio sobre *microbenchmarks* (Introducción y Planteamiento).

# Anexo B. Validación crítica de los productos de IA

<!-- Borrador v2 | 2026-11-11 | Resume los informes de auditoría (Investigación/Secciones/*/04 Auditoría.md) y los controles del taller (Taller/Taller.md §7 y docs/PLAN-DE-PRUEBAS.md). -->

Este anexo resume los hallazgos de las auditorías y cómo se resolvieron (4.3), y los controles con que se validó el código del taller. Los informes completos están en `Investigación/Secciones/`.

### B.1 Resultado de las auditorías

**Tabla B1.** Rondas de auditoría por parte del documento

| Parte | Rondas | No aprobadas | Bloqueantes | Sugerencias |
|---|---:|---:|---:|---:|
| Introducción | 6 | 2 | 4 | 3 |
| Planteamiento del problema | 4 | 1 | 1 | 5 |
| Metodología | 2 | 0 | 0 | 5 |
| Marco teórico (cuatro grupos de subsecciones) | 14 | 7 | 14 | 25 |
| Sección 6 | 2 | 1 | 3 | 7 |
| **Total** | **28** | **11** | **22** | **45** |

*Fuente:* elaboración propia, a partir de los informes de auditoría. Cada parte terminó con una ronda aprobada. En la Introducción, la primera ronda auditó solo la evidencia y rechazó 3 de 22 filas: dos por enlaces locales que no resolvían y una por citar solo un resumen.

### B.2 Hallazgos bloqueantes

**Tabla B2.** Tipos de hallazgo bloqueante y su resolución

| Tipo | Casos | Ejemplo | Resolución |
|---|---:|---|---|
| Fidelidad: la afirmación dice más que la fuente | 15 | Un límite aproximado se presentaba como pérdida categórica | Se reformuló como límite aproximado |
| Respaldo: dato o atribución sin fila que lo sostenga | 9 | Una interpretación propia se atribuía al syllabus del ISTQB | Se presentó como razonamiento propio o se acotó |
| Ubicación: pasaje literal, pero en otra sección o página | 5 | Un pasaje estaba antes del apartado registrado | Se corrigió el registro |
| Literalidad: la cita no está en el cuerpo de la fuente | 3 | Títulos de metadatos registrados como citas textuales | Se usaron pasajes del cuerpo |
| Trazabilidad: faltan citas o identificadores | 1 | Identificadores sin cita de autor y año | Se agregaron |

*Fuente:* elaboración propia. Un hallazgo puede ser de más de un tipo, así que los casos suman más de 22. Ninguno señaló una fuente inexistente.

### B.3 Evolución del procedimiento

La Introducción se produjo primero con una versión de cinco instrucciones permanentes (*skills*) que partía de la evidencia ya auditada. El resultado fue un texto saturado de citas (17 en 880 palabras) y lento de producir. Se sustituyó por la versión de 4.3, que parte del argumento y cita solo lo que lo necesita, y la Introducción se reescribió con ella.

### B.4 Validación del código del taller

**Tabla B3.** Controles aplicados al código que produjo la IA

| Control | Qué comprueba | Resultado |
|---|---|---|
| 38 pruebas funcionales y 36 de las herramientas | Contrato, reversión y contador correcto (una versión sin protección comprueba que la prueba sabe fallar); reglas de validez y de veredicto | Las dos variantes aprueban; corren en cada cambio |
| Compuerta en CI | Las pruebas anteriores y la carga con el perfil `ci` en cada *push* y *pull request* | Rechaza `regresion` y aprueba `corregida` |
| Detección de ejecuciones inválidas | Tasa lograda, solicitudes, configuración y datos de cada medición | Una ejecución interrumpida por falta de memoria quedó inválida y se repitió |

*Fuente:* elaboración propia, a partir de `Taller/Taller.md` y `Taller/docs/PLAN-DE-PRUEBAS.md`.
