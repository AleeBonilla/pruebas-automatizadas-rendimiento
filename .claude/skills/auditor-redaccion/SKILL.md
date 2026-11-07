---
name: auditor-redaccion
description: Audita el borrador de una sección contra su plan y su tabla de evidencia, y entrega un informe de hallazgos con veredicto. No corrige el borrador.
disable-model-invocation: true
---

# Auditor de redacción

Sección: la que indique el usuario.

## Archivos

| Archivo | Uso |
|---|---|
| `Investigación/Secciones/<sección>/01 Plan.md` | Leer: subsecciones, presupuesto e insumos |
| `Investigación/Secciones/<sección>/02 Evidencia.md` | Leer: afirmaciones permitidas |
| `Investigación/Secciones/<sección>/03 Borrador.md` | Leer: el texto a auditar |
| `Investigación/Referencias.md` | Leer: formato y datos de las citas |
| Archivos indicados en la columna «Insumos» del plan | Leer si hace falta: contenido interno |
| `Investigación/Secciones/<sección>/05 Auditoría - Redacción.md` | Leer si existe y escribir: el informe |

No escribás ningún otro archivo. Usá el idioma del documento.

## Qué revisar

1. **Trazabilidad:** cada cita lleva el ID de una fila existente, y el autor y el año corresponden a la fuente de esa fila.
2. **Fidelidad:** el texto no dice más que la afirmación de la fila citada.
3. **Respaldo:** no hay afirmaciones que necesiten respaldo externo sin una cita, ni contenido interno que no salga de los insumos del plan.
4. **Citas textuales:** coinciden con la cita textual de la fila, van entre comillas e incluyen la ubicación.
5. **Formato:** las citas siguen el formato de `Referencias.md`.
6. **Estructura:** el borrador tiene las subsecciones del plan.

El veredicto es **Aprobada** si no hay hallazgos; si no, es **No aprobada**. La extensión se informa pero no afecta el veredicto.

## Rondas

Cada auditoría es una ronda nueva que se agrega al inicio del informe, sin borrar las anteriores. A partir de la segunda ronda, revisá los hallazgos de la ronda anterior y todo lo que haya cambiado según los cambios del borrador.

## Plantilla

```markdown
# Auditoría de redacción — <sección>

## Ronda <n> — <AAAA-MM-DD> — Borrador versión <n>

**Veredicto:** Aprobada / No aprobada

| # | Ubicación | Revisión | Hallazgo | Corrección sugerida |
|---|---|---|---|---|
| 1 | <subsección, párrafo> | <1–6> | | |

**Extensión:**
| Subsección | Plan | Borrador |
|---|---|---|
```

Si no hay hallazgos, omití la tabla de hallazgos.
