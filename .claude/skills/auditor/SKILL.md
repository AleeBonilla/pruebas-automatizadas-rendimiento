---
name: auditor
description: Audita el borrador de una sección y su registro de evidencia. Verifica las citas contra las fuentes y revisa la prosa contra la guía de redacción. Entrega un informe con veredicto y no corrige nada.
argument-hint: <sección>
disable-model-invocation: true
---

# Auditor

Sección: $ARGUMENTS (o la que indique el usuario). Puede ejecutarse sin intervención humana (`codex exec`): no hagás preguntas; si algo impide auditar, registralo en el informe.

## Archivos

| Archivo | Uso |
|---|---|
| `Investigación/Guía de redacción.md` | Leer: reglas contra las que se revisa la prosa |
| `Investigación/Secciones/<sección>/01 Plan.md` | Leer: modo, esquema argumental, presupuesto y fuentes |
| `Investigación/Secciones/<sección>/02 Evidencia.md` | Leer: registro de las afirmaciones citadas |
| `Investigación/Secciones/<sección>/03 Borrador.md` | Leer: el texto a auditar |
| `Investigación/Referencias.md` | Leer: formato y datos de las citas |
| `Investigación/Glosario.md` | Leer: forma obligatoria de los términos |
| `Alcance.md` | Leer si hace falta: alcance y criterios de fuentes (§5.3) |
| Fuentes (enlaces y `Adjuntos/Local`) | Leer: para cotejar las citas |
| `Investigación/Secciones/<sección>/04 Auditoría.md` | Leer si existe y escribir: el informe |

No escribás ningún otro archivo. Usá el idioma del documento.

## A. Citas — hallazgos bloqueantes

Por cada cita del borrador:

1. **Trazabilidad:** lleva el ID de una fila existente de la evidencia, y el autor y el año corresponden a la fuente de esa fila.
2. **Literalidad:** la cita textual de la fila aparece literal en la fuente, en la ubicación indicada, y en el cuerpo del texto, no solo en el resumen.
3. **Fidelidad:** la fila dice lo mismo que la cita textual, y la oración del borrador que cita no dice más que la fila.

Para todo el borrador:

4. **Respaldo:** ninguna definición normativa, dato, cifra, caso concreto ni hallazgo empírico aparece sin cita, tampoco en una tabla, una figura o sus notas. El razonamiento propio no se presenta como si lo dijera una fuente, y una tabla marcada «Elaboración propia» no introduce datos externos sin citar.
5. **Fuentes nuevas:** las marcadas «Nueva» cumplen los criterios de `Alcance.md` §5.3 y están en `Referencias.md`.
6. **Formato:** las citas siguen APA 7 con el formato de `Referencias.md`.

El razonamiento propio sin cita **no** es un hallazgo, mientras no introduzca datos externos (guía, §1 y §2).

## B. Prosa — sugerencias

Revisá el borrador contra la guía y el plan:

7. **Argumento:** cada bloque desarrolla la idea central que le asigna el plan, y cada párrafo tiene una idea propia que las fuentes respaldan.
8. **Legibilidad:** el texto se entiende y fluye; no se lee como una sucesión de citas; las transiciones conectan las ideas.
9. **Densidad y selección:** la cantidad de citas corresponde al modo; ninguna fuente se repite sin necesidad en un mismo párrafo; no hay detalles que no aporten al argumento.
10. **Contenido interno:** objetivos, preguntas y alcance aparecen integrados, una sola vez, sin listas copiadas.
11. **Metacomentarios:** el texto no habla del proceso con que se produjo (IA, skills, auditorías), salvo en la Metodología y los anexos.
12. **Extensión:** cada bloque cabe en su presupuesto con un margen de ±10 %, sin contar tablas ni figuras. Informá aparte si las tablas y figuras exceden el espacio que les da el plan.
13. **Terminología:** los términos siguen la forma de `Glosario.md`, y un mismo concepto no se nombra de dos maneras.
14. **Tablas y figuras:** las del plan están presentes, llevan número, título y origen, el texto las menciona y no repiten lo que ya dice la prosa (guía, §7).

Los hallazgos de B son **sugerencias**, salvo los de 11, que son **bloqueantes**. Cada sugerencia debe ser concreta: dónde, qué falla y una reformulación propuesta.

## Veredicto y rondas

- **Aprobada:** ningún hallazgo bloqueante. Las sugerencias no impiden aprobar.
- **No aprobada:** al menos un hallazgo bloqueante.
- Cada auditoría es una ronda nueva que se agrega al inicio del informe, sin borrar las anteriores. A partir de la segunda ronda, revisá los hallazgos de la ronda anterior y todo lo que haya cambiado en el borrador o en la evidencia; no hace falta volver a cotejar las citas que no cambiaron y ya estaban aprobadas.

## Plantilla

```markdown
# Auditoría — <sección>

## Ronda <n> — <AAAA-MM-DD> — Borrador v<n> · Evidencia v<n>

**Veredicto:** Aprobada / No aprobada | **Citas revisadas:** <IDs>

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante / Sugerencia | <bloque, párrafo o tabla> | <1–14> | | |

**Extensión:**
| Bloque | Plan | Borrador |
|---|---|---|
```

Si no hay hallazgos, omití la tabla de hallazgos.
