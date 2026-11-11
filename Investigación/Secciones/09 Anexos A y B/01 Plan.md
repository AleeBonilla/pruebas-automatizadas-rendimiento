# Plan — 09 Anexos A y B

**Estado:** Aprobado | **Modo:** Ligero | **Versión:** 1 | **Fecha:** 2026-11-11 | **Presupuesto:** 2 páginas en total, con unas 250 palabras de prosa y el resto en cinco tablas

> Este plan se reconstruyó el 2026-11-11, después de redactar el borrador, para poder auditarlo. Los anexos resumen los registros del repositorio y no tienen fuentes externas.

## Objetivo y alcance

`Alcance.md` §9 prevé dos anexos de la fase 1: A, «Registro resumido de consultas de IA», y B, «Resumen de la validación crítica de los productos de IA y su resolución». La Metodología los anuncia: 4.2 dice que «el anexo A resume las consultas y las fuentes descartadas», y 4.3, que «el anexo B resume los hallazgos de la auditoría y su resolución». El usuario pidió que fueran resumidos y estructurados, para no sobrecargar el documento. El detalle completo queda en el repositorio.

La guía, §5, permite hablar del proceso con que se produjo el texto en los anexos. Las cifras son contenido interno: salen de los registros del repositorio y no llevan cita.

## Esquema argumental

| Bloque | Contenido | Respaldo |
|---|---|---|
| A.1 Herramientas y funciones | Qué hizo cada herramienta de IA y dónde queda su registro | Sección 4.3; historial de Git |
| A.2 Consultas de búsqueda | Consultas, resultados, fuentes y evidencia por parte del documento | `01 Plan.md` y `02 Evidencia.md` de cada sección |
| A.3 Fuentes descartadas | Motivos por los que se descartaron fuentes | Registros de búsqueda y listas de fuentes de cada plan |
| B.1 Resultado de las auditorías | Rondas, veredictos y hallazgos por parte | `04 Auditoría.md` de cada sección |
| B.2 Hallazgos bloqueantes | Tipos, ejemplos y resolución | `04 Auditoría.md` de cada sección |
| B.3 Evolución del procedimiento | Cambio de la versión de cinco instrucciones a la actual | `Alcance.md` §5.3 |
| B.4 Validación del código del taller | Controles aplicados al código que produjo la IA | `Taller/Taller.md`; `Taller/docs/PLAN-DE-PRUEBAS.md` |

## Afirmaciones internas a verificar

| Afirmación | Origen |
|---|---|
| Claude Code (Opus 5.5) planifica y redacta; Codex (GPT-6.1 Sol) audita en una sesión independiente | Sección 4.3 |
| Hasta el *commit* `ceacb17`, 57 de los 81 *commits* llevan la coautoría de Claude | `git log`, línea `Co-Authored-By` de cada *commit* |
| Tabla A2: 22 consultas, 238 resultados revisados, 13 con fuente elegida y 9 sin ella; las cuatro partes del Marco teórico tienen 6, 6, 1 y 9 consultas; todas del 7 de noviembre de 2026 | «Registro de búsqueda» de `01 Plan.md` de cada grupo del Marco teórico |
| Tabla A2: 47 fuentes verificadas (8, 7, 2, 7, 5, 5, 9 y 4 por parte) | Tabla «Fuentes» de cada `01 Plan.md` |
| Tabla A2: 200 filas de evidencia (29, 30, 5, 26, 31, 31, 44 y 4 por parte) | `02 Evidencia.md` de cada sección |
| Las consultas de la Introducción, el Planteamiento y la Metodología no se registraron | Sección 4.2 |
| El documento cita 34 referencias distintas | Sección «Referencias» del documento; `Investigación/Referencias.md` |
| A.3: motivos de descarte y ejemplos (resúmenes y copias de terceros, contenido comercial, solo el resumen, otro producto o versión, fuera del alcance o sin datos completos) | Registros de búsqueda de 5.1–5.2, 5.3–5.4 y 5.8; lista de fuentes descartadas de la Introducción y del Planteamiento |
| Tabla B1: 28 rondas, 11 no aprobadas, 22 bloqueantes y 45 sugerencias, con el desglose por parte; cada parte terminó con una ronda aprobada | `04 Auditoría.md` de cada sección |
| En la Introducción, la primera ronda auditó solo la evidencia y rechazó 3 de 22 filas: dos por enlaces locales que no resolvían y una por citar solo un resumen | `02 Introducción/04 Auditoría.md`, ronda 1 |
| Tabla B2: 15 hallazgos de fidelidad, 9 de respaldo, 5 de ubicación, 3 de literalidad y 1 de trazabilidad; ejemplos y resoluciones; ninguno señaló una fuente inexistente | Columna «Criterio» y seguimiento de cada hallazgo bloqueante en `04 Auditoría.md` |
| La Introducción se produjo primero con una versión de cinco instrucciones que partía de la evidencia ya auditada; resultó saturada de citas (17 en 880 palabras) y lenta | `Alcance.md` §5.3, «Evolución del procedimiento» |
| 38 pruebas funcionales y de concurrencia; una usa un «leer, sumar y escribir» sin protección; 36 pruebas de las herramientas; la *quality gate* corre ambas y la carga con el perfil de ejecución `ci` en los *pushes* a `main` y los *pull requests*, en ambos casos con cambios en `Taller/**` o `.github/workflows/**` (`workflow_dispatch` permite además una ejecución manual) | `Taller/docs/GUIA.md` §4; `Taller/docs/PLAN-DE-PRUEBAS.md`; `.github/workflows/compuerta.yml` |
| Una ejecución interrumpida por falta de memoria quedó marcada como inválida y se repitió | `Taller/Taller.md` §7.1 |

## Fuentes

Ninguna externa.
