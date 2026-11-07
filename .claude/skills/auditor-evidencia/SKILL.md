---
name: auditor-evidencia
description: Audita la tabla de evidencia de una sección contra sus fuentes y su plan, y entrega un informe de hallazgos con veredicto. No corrige la tabla.
disable-model-invocation: true
---

# Auditor de evidencia

Sección: la que indique el usuario.

## Archivos

| Archivo | Uso |
|---|---|
| `Investigación/Secciones/<sección>/01 Plan.md` | Leer: puntos a investigar y fuentes |
| `Investigación/Secciones/<sección>/02 Evidencia.md` | Leer: la tabla a auditar |
| `Adjuntos/Local` | Leer: fuentes cerradas marcadas como «Local» en el plan |
| `Investigación/Secciones/<sección>/04 Auditoría - Evidencia.md` | Leer si existe y escribir: el informe |

No escribás ningún otro archivo. Usá el idioma del documento.

## Qué revisar

Por cada fila:

1. **Fuente:** es una fuente del plan y el enlace lleva a ella.
2. **Cita:** aparece literal en la fuente, en la ubicación indicada, y no proviene solo del resumen.
3. **Afirmación:** dice lo mismo que la cita, sin agregar ni exagerar.
4. **Punto:** la fila responde al punto que tiene asignado.
5. **Tipo:** es correcto y adecuado para lo que se afirma.

Para toda la tabla:

6. **Cobertura:** cada punto del plan tiene al menos una fila o figura en «Puntos sin respaldo» con un motivo válido.

Cada fila queda **Aprobada**, **Rechazada** (con el hallazgo y la corrección sugerida) o **No verificable**, si no pudiste acceder a la fuente; en este último caso, indicá el motivo. El veredicto es **Aprobada** solo si todas las filas están aprobadas y la cobertura está completa; si no, es **No aprobada**.

## Rondas

Cada auditoría es una ronda nueva que se agrega al inicio del informe, sin borrar las anteriores. A partir de la segunda ronda, revisá las filas rechazadas o no verificables en la ronda anterior y toda fila nueva o modificada según los cambios de la tabla.

## Plantilla

```markdown
# Auditoría de evidencia — <sección>

## Ronda <n> — <AAAA-MM-DD> — Evidencia versión <n>

**Veredicto:** Aprobada / No aprobada | **Filas revisadas:** <IDs>

| Fila | Resultado | Hallazgo | Corrección sugerida |
|---|---|---|---|
| E-01 | Rechazada / No verificable | | |

**Cobertura:** Completa / <puntos sin cubrir>
```

En la tabla, listá solo las filas rechazadas o no verificables; si no hay, omitila.
