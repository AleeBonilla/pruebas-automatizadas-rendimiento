---
name: planificador
description: Planifica una sección de un documento de investigación. Propone qué investigar y con qué fuentes. No redacta la sección.
argument-hint: <sección>
disable-model-invocation: true
---

# Planificador

Encargo: $ARGUMENTS

## Archivos

| Archivo | Uso |
|---|---|
| `Alcance.md` | Leer: alcance, presupuesto de la sección, inclusiones y exclusiones |
| `Enunciado.md` | Leer: requisitos para la sección |
| `Investigación/Secciones/<sección>/01 Plan.md` | Leer si existe y escribir: el plan |
| `Investigación/Referencias.md` | Leer y, al cerrar el plan, escribir: referencias del documento |

No escribás ningún otro archivo. Si el plan ya existe, partí de él y no reiniciés lo que ya está definido. Preguntá solo si la sección es ambigua o si los requisitos se contradicen. Usá el idioma del documento.

## Contenido

- **Subsecciones:** proponé las subsecciones de la sección **si es necesario**. Para cada una, indicá qué debe comunicar y de dónde sale su contenido. No repitás lo que cubren otras secciones.
- **Presupuesto:** tomá de `Alcance.md` las palabras asignadas a la sección. Si la dividís en subsecciones, repartí esas palabras entre ellas de modo que sumen el total. Si `Alcance.md` no le asigna palabras, poné «Por definir». Si lo planificado no cabe en ese total, indicá qué recortarías o cómo dividirías la sección en varios planes.
- **Puntos a investigar:** escribí como preguntas acotadas lo que necesite respaldo externo, de modo que se respondan con una cita. «¿Cómo define la norma X el concepto Y?» sirve; «Investigar Y» no. No agregués preguntas de relleno.
- **Fuentes:** usá primero las de `Referencias.md` que sirvan y después buscá las que falten, preferiblemente originales (normas, artículos, documentación oficial). Verificá cada una en su página de publicación: título, autor, fecha o versión y enlace.
  - **Acceso:** *abierta* si el texto completo se lee gratis y de forma legal; *cerrada* si requiere pago o suscripción, o si solo se puede leer el resumen; *por verificar* si no lo pudiste comprobar.

## Estados

1. **Borrador:** presentá el plan y atendé las observaciones. Conservá los IDs que sigan vigentes.
2. **Aprobado:** marcalo así solo cuando el usuario lo apruebe explícitamente.
3. **Final:** revisá las fuentes cerradas que aporte el usuario y reemplazá las no disponibles por fuentes abiertas que cubran el mismo punto. Si un reemplazo cambia el enfoque o elimina contenido, pedí aprobación antes de cerrar. Si no hay fuentes cerradas, el plan pasa directo a Final. No lo marqués Final mientras quede alguna fuente *por verificar*.

**Al pasar a Final**, agregá las fuentes del plan a `Referencias.md`:
- Si la fuente ya está en el archivo (mismo DOI o enlace, o mismo autor, año y título), dejá la entrada que existe.
- Si no está, agregala con el formato que use el archivo, o en APA 7 si el archivo está vacío.

## Plantilla

```markdown
# Plan — <sección>

**Estado:** Borrador / Aprobado / Final | **Versión:** <n> | **Fecha:** <AAAA-MM-DD> | **Presupuesto:** <palabras / Por definir>

## Objetivo y alcance

## Subsecciones
| Subsección | Palabras | Qué comunica | Insumos | Puntos |
|---|---|---|---|---|

## Puntos a investigar
| ID | Pregunta | Subsección | Fuentes |
|---|---|---|---|

## Fuentes
| ID | Referencia y enlace | Acceso | Disponibilidad |
|---|---|---|---|
```

- **Disponibilidad:** en las fuentes abiertas, el enlace al texto completo. En las cerradas, «Pendiente», «No disponible» o «Local» para las que se tienen localmente.
- **Sin investigación externa:** si la sección no la necesita, omití las tablas de puntos y de fuentes.
- **Revisiones:** en cada una, subí la versión.
