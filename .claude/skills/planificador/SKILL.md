---
name: planificador
description: Planifica una sección de un documento de investigación. Define su modo, su esquema argumental y sus fuentes. No redacta la sección.
argument-hint: <sección>
disable-model-invocation: true
---

# Planificador

Encargo: $ARGUMENTS

## Archivos

| Archivo | Uso |
|---|---|
| `Alcance.md` | Leer: alcance, presupuesto de la sección, inclusiones y exclusiones |
| `Enunciado.md` | Leer: requisitos de la sección |
| `Investigación/Guía de redacción.md` | Leer: estilo y densidad de citas que tendrá el texto |
| `Investigación/Secciones/<sección>/01 Plan.md` | Leer si existe y escribir: el plan |
| `Investigación/Referencias.md` | Leer y, al aprobarse el plan, escribir: referencias del documento |
| `Adjuntos/Local` | Leer: fuentes cerradas que aporte el usuario |

No escribás ningún otro archivo. Si el plan ya existe, partí de él y no reiniciés lo que ya está definido. Preguntá solo si la sección es ambigua o si los requisitos se contradicen. Usá el idioma del documento.

## Contenido

- **Modo:**
  - *Ligero*: secciones que se sostienen sobre todo en contenido interno o en pocas ideas externas (introducción, metodología, conclusiones). Pocas fuentes; no lleva tabla de afirmaciones.
  - *Completo*: secciones cuyo valor depende de la evidencia (planteamiento del problema, marco teórico).
  - Una sección de más de unas 2 000 palabras se divide en varios planes, uno por subsección (por ejemplo, el Marco teórico §5.1 a §5.8).
- **Esquema argumental:** dividí la sección en bloques o subsecciones. Para cada uno, escribí en una oración la **idea central**: lo que el lector debe concluir, no el tema. Indicá de dónde sale el contenido: fuentes o insumos internos. No repitás lo que cubren otras secciones. Indicá si los bloques llevan subtítulos en el documento.
- **Presupuesto:** tomá de `Alcance.md` las palabras de la sección y repartilas entre los bloques. Si no le asigna palabras, poné «Por definir». Si lo planificado no cabe, indicá qué recortarías.
- **Afirmaciones a respaldar** (solo en modo completo): las afirmaciones externas clave, formuladas como preguntas acotadas que se respondan con una cita. Como tope, una por cada 100 palabras del presupuesto. Lo que es conocimiento común o razonamiento propio no se incluye (ver la guía, §2).
- **Fuentes:** usá primero las de `Referencias.md` que sirvan y después buscá las que falten. Preferí originales: normas, artículos arbitrados y documentación oficial, según los criterios de `Alcance.md` §5.3. Verificá cada una en su página de publicación: título, autor, fecha o versión y enlace.
  - **Acceso:** *abierta* si el texto completo se lee gratis y de forma legal; *cerrada* si requiere pago o suscripción, o si solo se lee el resumen; *por verificar* si no lo pudiste comprobar.

## Estados

1. **Borrador:** presentá el plan y atendé las observaciones. Conservá los IDs que sigan vigentes.
2. **Aprobado:** solo cuando el usuario lo apruebe explícitamente y no quede ninguna fuente *por verificar*. Antes de marcarlo, resolvé las fuentes cerradas: las disponibles en `Adjuntos/Local` quedan como «Local»; las demás se reemplazan por fuentes abiertas que cubran lo mismo. Si un reemplazo cambia el enfoque, pedí aprobación de nuevo.

**Al aprobarse**, agregá las fuentes del plan a `Referencias.md`. Si la fuente ya está (mismo DOI o enlace, o mismo autor, año y título), dejá la entrada existente. Si no, agregala con el formato del archivo, o en APA 7 si está vacío.

## Plantilla

```markdown
# Plan — <sección>

**Estado:** Borrador / Aprobado | **Modo:** Ligero / Completo | **Versión:** <n> | **Fecha:** <AAAA-MM-DD> | **Presupuesto:** <palabras / Por definir>

## Objetivo y alcance
<Qué cubre la sección y qué no (lo que va en otras secciones).>

## Esquema argumental
| Bloque | Palabras | Idea central | Contenido | Insumos y fuentes |
|---|---|---|---|---|

## Afirmaciones a respaldar
| ID | Pregunta | Bloque | Fuentes |
|---|---|---|---|

## Fuentes
| ID | Referencia y enlace | Acceso | Disponibilidad |
|---|---|---|---|
```

- **Afirmaciones a respaldar:** omití la tabla en modo ligero.
- **Disponibilidad:** en las fuentes abiertas, el enlace al texto completo; en las cerradas, «Local» o el motivo por el que no está.
- **Sin fuentes externas:** si la sección no las necesita, omití la tabla de fuentes.
- **Revisiones:** en cada una, subí la versión y anotá los cambios al inicio.
