# Guía de redacción

Reglas de estilo del documento. Las aplica el redactor al escribir y las verifica el auditor. Si una regla choca con el plan de una sección, manda esta guía, salvo que el plan diga explícitamente lo contrario.

**Principio:** primero el argumento; la evidencia lo respalda. El texto lo conduce el autor, no las fuentes.

## 1. Voz propia

- Cada párrafo tiene una idea central formulada por el autor, por lo general en su primera oración. Las fuentes respaldan esa idea; no la sustituyen.
- El razonamiento propio está permitido y es lo esperado: conectar ideas, explicar por qué algo importa, relacionarlo con el tema del trabajo, sacar conclusiones. No lleva cita, pero tampoco se presenta como si lo dijera una fuente ni trae datos o cifras sin respaldo.
- No se encadenan oraciones que empiezan con «Según X…», «X señala…» o «X afirma…». Como máximo, una cita narrativa por párrafo.

## 2. Qué se cita y qué no

| Lleva cita | No lleva cita |
|---|---|
| Definiciones de normas y estándares | Conocimiento común de la disciplina (qué es una API, qué hace un pipeline de CI) |
| Datos, cifras, estadísticas y resultados empíricos | Razonamiento, conexiones y conclusiones del autor |
| Casos concretos y hechos históricos | Contenido interno del documento: alcance, objetivos, preguntas, estructura |
| Afirmaciones discutibles o atribuibles a un autor | Transiciones y síntesis de lo ya citado |

## 3. Densidad y selección

- **Modo ligero** (introducción, metodología, conclusiones): en promedio, a lo sumo una cita por párrafo.
- **Modo completo** (planteamiento del problema, marco teórico): entre una y tres citas por párrafo.
- Cada fuente se cita una vez por párrafo, salvo que haya ambigüedad. Si dos oraciones seguidas vienen de la misma fuente, la cita va al final de la segunda.
- No hace falta usar toda la evidencia disponible. Se eligen los datos que sostienen el argumento de la sección. Los detalles finos (montos, fechas secundarias, nombres de sistemas internos) se usan solo si la idea los necesita.
- Las citas textuales entre comillas se reservan para definiciones o frases cuya formulación importa.

## 4. Contenido interno

- Los objetivos, las preguntas de investigación y los elementos del alcance se integran donde cumplen una función. No se copian como lista del `Enunciado.md` ni del `Alcance.md`.
- Cada elemento se menciona una sola vez en la sección. Por ejemplo, en la introducción cada pregunta de investigación aparece junto a la sección que la responde.

## 5. Sin metacomentarios

- El texto no habla del proceso con el que se produjo: uso de IA, skills, auditorías ni validación. Eso solo se trata en la Metodología y en los anexos, donde es el tema.
- No se anuncia lo que hará el texto («en este párrafo se expone…»). La única excepción es la descripción de la estructura del documento en la introducción.

## 6. Forma

- Español, registro académico y oraciones claras. Se prefiere una oración simple a una con varias subordinadas.
- Los términos técnicos en inglés van en cursiva (*throughput*, *commit*), salvo los ya asimilados (API, pipeline, CI).
- Las citas siguen APA 7 con el formato de `Referencias.md`. Después de cada cita va un comentario oculto con los IDs de las filas de evidencia que la respaldan: `(Autor, año) <!-- E7, E8 -->`.
- La extensión se ajusta al presupuesto del plan, con un margen de ±10 %. Las tablas y las figuras no cuentan en ese presupuesto: el plan les asigna un espacio aparte, en páginas.

## 7. Tablas y figuras

- Se usan cuando ordenan mejor que la prosa: comparaciones con varios criterios, clasificaciones o procesos. No repiten lo que ya dice el texto.
- Cada una lleva número y título («Tabla 1. …», «Figura 1. …»), numerados en orden en todo el documento, y el texto la menciona antes de que aparezca y dice qué muestra.
- **Respaldo:** todo dato de una tabla que venga de una fuente (una cifra, una característica de una herramienta, una definición) lleva cita, en la celda o en una nota bajo la tabla, con el comentario oculto de su fila de evidencia. Debajo de cada tabla o figura va su origen: «Fuente: Autor (año)», «Adaptado de Autor (año)» o «Elaboración propia» si es una síntesis del autor a partir de fuentes ya citadas.
- **Formato en el borrador:** las tablas van en Markdown. Las figuras se describen con un comentario `<!-- FIGURA: … -->` que indica qué representa y de qué fuente sale; se dibujan al pasar el texto al documento final.

## 8. Terminología

- Los términos técnicos siguen `Glosario.md`: se usa la forma indicada y no sus sinónimos. Un mismo concepto se nombra siempre igual en todo el documento.
- La primera vez que aparece un término en inglés, va en cursiva y con su equivalente en español, si lo tiene, según el glosario.
