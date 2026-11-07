# Plan — Metodología

**Estado:** Aprobado | **Modo:** Ligero | **Versión:** 3 | **Fecha:** 2026-11-07 | **Presupuesto:** 700 palabras

> **Cambios en la versión 3:** condensación al nuevo presupuesto de `Alcance.md` (documento de 30–35 páginas, aprobado por el usuario): de 1 200 a 700 palabras. Se conservan las dos fuentes. El detalle del procedimiento de IA (hallazgos concretos, evolución paso a paso) pasa al anexo B, según `Alcance.md` §5.3 y §9. La sección «Condensación» indica qué se recorta.
>
> **Cambios en la versión 2:** aprobado por el usuario con la opción 1 de la decisión sobre la búsqueda: desde el Marco teórico, cada consulta se registra en el plan, y la Metodología describe con honestidad lo hecho en la Introducción y en el Planteamiento. Se ajustan `Alcance.md` §5.3 y la skill del planificador. F1 y F2 se agregan a `Referencias.md`.

## Objetivo y alcance

Sección 4 del documento (`Alcance.md` §5.3; `Enunciado.md` §4). El enunciado pide tres cosas: el enfoque metodológico; las fuentes de información, los criterios de búsqueda y las estrategias de consulta, y el procedimiento para usar y validar críticamente las herramientas de IA. También responde al objetivo específico 2 («generar estrategias y técnicas para auditar, revisar y mejorar críticamente los productos generados por las herramientas de IA»).

**Incluye:**

- El enfoque teórico-aplicado: revisión de literatura semisistemática y un componente experimental.
- Cómo se buscaron, seleccionaron y verificaron las fuentes, tal como se hizo en la práctica.
- El procedimiento con IA y lo que ese procedimiento detectó y corrigió.

**No incluye (lo cubren otras secciones):**

- El diseño del taller: escenarios, entorno y criterios de aceptación. Eso va en la Propuesta de taller (§6); aquí solo se dice qué papel cumple el taller en el método.
- El registro de consultas y el detalle de cada hallazgo de auditoría, que van en los anexos A y B. Aquí solo se resumen.
- La reflexión sobre lo aprendido con la IA, que va en las Conclusiones (§5.6 del alcance). Aquí se describe el procedimiento y sus resultados, sin valorarlos.

**Forma:** tres subsecciones con subtítulo (4.1 a 4.3), sin párrafo de apertura. A diferencia del resto del documento, esta sección sí habla del proceso de producción, porque es su tema (guía, §5).

## Esquema argumental
| Bloque | Palabras | Idea central | Contenido | Insumos y fuentes |
|---|---|---|---|---|
| B1. 4.1 Enfoque metodológico | 150 | La investigación combina una revisión de literatura semisistemática, que responde PI-1 a PI-4, con un componente experimental que responde PI-5. La revisión es semisistemática porque el tema cruza la investigación académica y la práctica industrial, y ese enfoque exige un proceso transparente. | Las dos fases y su relación con las preguntas y con la pregunta-problema. Qué es una revisión semisistemática y por qué encaja (temas estudiados desde tradiciones distintas; búsqueda que puede no ser sistemática, pero sí documentada). El taller como demostración experimental, sin anticipar su diseño. | `Alcance.md` §1–§3; `Enunciado.md` (objetivo general); F1 |
| B2. 4.2 Fuentes y estrategia de búsqueda | 250 | Las fuentes se buscaron a partir de lo que cada sección necesitaba afirmar, con prioridad a las primarias, y cada una se verificó y se leyó en texto completo antes de usarla. | Tipos de fuente y orden de preferencia (normas, artículos arbitrados, documentación oficial). Dónde y cómo se buscó: búsquedas dirigidas a las afirmaciones de cada plan, en buscadores web y bases bibliográficas, con verificación en Crossref. Desde el Marco teórico, cada consulta queda registrada en el plan de su sección; en la Introducción y en el Planteamiento solo se registraron las fuentes verificadas y las descartadas. Cadenas de búsqueda. Criterios de inclusión y de exclusión, con ejemplos reales de fuentes descartadas y su motivo. Verificación bibliográfica (página del editor y DOI en Crossref). Acceso: copias abiertas legales (actas de SPEC, arXiv, copias de autor, repositorios institucionales) y la norma ISO como fuente cerrada local. Límite: la búsqueda no es exhaustiva. | `Alcance.md` §5.3 y §8; planes de la Introducción y del Planteamiento (secciones «Verificación» y «Descartadas»); `Referencias.md` |
| B3. 4.3 Uso y validación crítica de la IA | 300 | La IA se usó como productora de borradores, bajo un control independiente y con aprobación humana, porque los modelos de lenguaje pueden inventar o alterar citas; el propio procedimiento se corrigió cuando sus resultados lo exigieron. | El riesgo: citas inventadas o con errores, con las cifras de Walters y Wilder (2023) y la aclaración de que estudiaron modelos anteriores. El principio: un modelo produce y otro, de un proveedor distinto, audita. Los tres pasos (planificar, redactar y auditar), la tabla de evidencia con cita literal y ubicación, los hallazgos bloqueantes y las sugerencias, y la aprobación humana. Resultados hasta ahora, como ejemplos: los errores de fidelidad que la auditoría detectó en la Introducción y en el Planteamiento. La evolución: la primera versión, de cinco skills, produjo un texto saturado de citas (17 en 882 palabras) y se reemplazó; con la versión actual, la misma Introducción quedó con 8. | `Alcance.md` §5.3; `Investigación/Workflow.md`; `Investigación/Guía de redacción.md`; `04 Auditoría.md` de la Introducción y del Planteamiento; historial de git; F2 |
| **Total** | **700** | | | |

## Condensación (versión 3)

El borrador v2 aprobado tiene 1 151 palabras. Las ideas centrales no cambian:

- **B1:** las dos fases en un párrafo y la revisión semisistemática en otro, con E1–E3. Sale la frase final sobre qué se documenta, que B2 y B3 ya muestran.
- **B2:** quedan el orden de preferencia de las fuentes, los criterios de inclusión y exclusión, la búsqueda dirigida a las afirmaciones, el registro desde el Marco teórico (con una cadena real de un plan como ejemplo) y la verificación. Sale el párrafo de ejemplos de fuentes descartadas, que va al anexo A. Se corrige que la norma ISO ya no es la única fuente cerrada: también se consultó en copia local el libro de Humble y Farley.
- **B3:** el riesgo con E4; sale el dato de E5 (errores en citas reales). El procedimiento en un párrafo. Los resultados y la evolución del procedimiento en un párrafo, sin los ejemplos uno por uno, que van al anexo B. La comparación de la Introducción se formula sin la cifra de 864 palabras, porque la Introducción también se condensa.

E5 pasa a «Filas no usadas» de la evidencia.

> **Notas para el redactor:**
>
> - **Cifras de B3:** salen del repositorio (auditorías e historial de git), son contenido interno y no llevan cita. Hay que poner la fecha de corte, porque cambiarán al redactar el Marco teórico. Conviene volver a pasar el redactor por esta sección al terminar la Fase 1, para actualizarlas.
> - **F2:** sus porcentajes (55 % de citas inventadas con GPT-3.5 y 18 % con GPT-4) vienen de modelos anteriores a los usados aquí. El texto debe decirlo y usarlos como justificación del riesgo, no como medida de los modelos actuales.
> - **B2:** debe describir lo que se hizo, no lo que el alcance preveía al principio. En la Introducción y en el Planteamiento, las fuentes se encontraron con búsquedas web dirigidas a cada afirmación, se verificaron en Crossref y en la página del editor, y se leyeron en copias abiertas. No se usó Scopus ni se registraron las consultas; solo quedaron anotadas las fuentes verificadas y las descartadas, con su motivo. El texto debe decirlo así, y describir el registro de consultas como la práctica a partir del Marco teórico. Si al redactar ya hay planes del Marco teórico con registro, puede usar sus consultas como ejemplos.

## Fuentes
| ID | Referencia y enlace | Acceso | Disponibilidad |
|---|---|---|---|
| F1 | Snyder, H. (2019). Literature review as a research methodology: An overview and guidelines. *Journal of Business Research, 104*, 333–339. https://doi.org/10.1016/j.jbusres.2019.07.039 | Abierta (CC BY-NC-ND 4.0) | https://hdl.handle.net/11250/2733371 (versión publicada en NORA) · https://www.sciencedirect.com/science/article/pii/S0148296319304564 |
| F2 | Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports, 13*, 14045. https://doi.org/10.1038/s41598-023-41032-5 | Abierta (CC BY 4.0) | https://www.nature.com/articles/s41598-023-41032-5.pdf |

**Verificación (2026-11-07):**

- **F1:** título, autora, revista, volumen, páginas, fecha (noviembre de 2019) y licencias comprobados en Crossref. El texto completo se leyó en la versión publicada del repositorio NORA, porque ScienceDirect bloquea la descarga automática. Pasajes localizados en el cuerpo:
  - La definición de la revisión semisistemática y su propósito: §2.1.2 «Semi-systematic review», p. 335.
  - La exigencia de un proceso transparente y de una estrategia de investigación desarrollada: §2.1.2, p. 335.
  - La tabla 1, donde la estrategia de búsqueda semisistemática «may or may not be systematic»: p. 334.
- **F2:** título, autores, revista, número de artículo, fecha (7 de septiembre de 2023) y licencia comprobados en Crossref; texto completo leído en Nature. Las cifras del 55 % y el 18 % están en el cuerpo (Resultados, p. 4) además del resumen.
