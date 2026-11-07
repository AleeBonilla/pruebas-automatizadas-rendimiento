---
name: redactor
description: Lee las fuentes del plan, redacta una sección del documento con su registro de evidencia, la manda a auditar con Codex y corrige los hallazgos.
argument-hint: <sección>
disable-model-invocation: true
---

# Redactor

Encargo: $ARGUMENTS

## Archivos

| Archivo | Uso |
|---|---|
| `Investigación/Guía de redacción.md` | Leer: reglas de estilo y de citas. Son obligatorias |
| `Investigación/Secciones/<sección>/01 Plan.md` | Leer: modo, esquema argumental, presupuesto y fuentes. Debe estar en estado Aprobado |
| `Alcance.md` y `Enunciado.md` | Leer: contenido interno (alcance, objetivos, preguntas, estructura) y criterios de fuentes (§5.3) |
| Fuentes del plan (enlaces y `Adjuntos/Local`) | Leer en texto completo |
| `Investigación/Referencias.md` | Leer: datos para citar. Escribir solo si agregás una fuente nueva |
| `Investigación/Glosario.md` | Leer: forma obligatoria de los términos. Escribir solo para agregar un término no previsto, marcado «Agregado por el redactor» |
| `Investigación/Secciones/<sección>/02 Evidencia.md` | Leer si existe y escribir: registro de las afirmaciones citadas |
| `Investigación/Secciones/<sección>/03 Borrador.md` | Leer si existe y escribir: el texto de la sección |
| `Investigación/Secciones/<sección>/04 Auditoría.md` | Leer si existe: hallazgos a corregir. Lo escribe solo el auditor |

No escribás ningún otro archivo. Si el plan no está Aprobado, detenete y avisá.

## Pasos

1. **Leer.** Leé el plan, la guía y las fuentes en texto completo; nunca respaldés una afirmación solo con el resumen de una fuente. Si ya hay borrador y auditoría, partí de ellos y corregí lo señalado en vez de reescribir.
2. **Redactar.** Escribí `03 Borrador.md` siguiendo el esquema argumental del plan: cada bloque desarrolla su idea central con voz propia y usa las fuentes donde la guía pide cita. Respetá la densidad del modo y el presupuesto (±10 %). Incluí las tablas y figuras del plan según la guía (§7); no cuentan en el presupuesto de palabras. Usá los términos con la forma de `Glosario.md` (guía, §8).
3. **Registrar la evidencia.** Por cada cita del borrador, agregá a `02 Evidencia.md` una fila con la cita textual mínima, literal y en su idioma original, que respalda lo que el texto afirma. Poné su ID en el comentario oculto que sigue a la cita en el borrador. Lo mismo vale para cada dato de una tabla que venga de una fuente. Las filas de versiones anteriores que ya no se citan pueden quedarse; los IDs no se renumeran.
4. **Resolver los vacíos sin volver a planificar.** Si una idea necesita respaldo que las fuentes del plan no dan:
   - reformulala como razonamiento propio sin datos externos, si se sostiene así, o
   - buscá una fuente nueva que cumpla los criterios de `Alcance.md` §5.3, verificala, agregala a `Referencias.md` y registrala en la evidencia como «Nueva», o
   - si nada de lo anterior sirve, dejá `[FALTA FUENTE: <qué falta>]` en el texto y registralo en «Pendientes».
5. **Revisar antes de auditar.** Releé el borrador contra la guía: idea propia en cada párrafo, sin cadenas de «Según X», sin metacomentarios, sin listas copiadas del enunciado, términos según el glosario, tablas con su origen y citas, y extensión dentro del margen.
6. **Auditar.** Ejecutá el auditor de Codex desde la raíz del repositorio, en segundo plano (puede tardar varios minutos), y esperá a que termine:

   ```bash
   codex exec -C "<raíz del repositorio>" -s workspace-write \
     -c sandbox_workspace_write.network_access=true \
     -c model_reasoning_effort=high \
     "Ejecutá la skill auditor (.agents/skills/auditor/SKILL.md) para la sección «<sección>». Escribí solo en 04 Auditoría.md."
   ```

   Si el comando falla (Codex no instalado, sin sesión iniciada, error de sandbox), no lo repitás: avisale al usuario que ejecute `$auditor <sección>` en Codex y detenete.
7. **Corregir.** Leé la última ronda de `04 Auditoría.md`. Corregí todos los hallazgos **bloqueantes**. Aplicá las **sugerencias** con las que estés de acuerdo; las que no, dejalas y explicá por qué en el resumen final. Si quedan bloqueantes, volvé al paso 6. **Como máximo, 2 rondas de auditoría por invocación.**
8. **Entregar.** Respondé al usuario con: extensión por bloque contra el presupuesto (sin tablas ni figuras), las tablas y figuras incluidas, número de citas, términos agregados al glosario, veredicto de la última auditoría, sugerencias no aplicadas y pendientes.

**Observaciones del usuario:** aplicalas. Si cambian afirmaciones citadas o agregan citas, volvé al paso 6; si solo cambian la prosa sin tocar citas, no hace falta auditar de nuevo.

## Plantillas

`03 Borrador.md`:

```markdown
# <sección>

<!-- Borrador v<n> | Plan v<n> | Evidencia v<n> | <AAAA-MM-DD> -->

## <bloque o subsección, si el plan indica subtítulos; si no, un comentario <!-- B1. ... -->>

<Texto. Citas: (Autor, año) <!-- E1 -->>

---

## Pendientes
| Bloque | Qué falta |
|---|---|
```

`02 Evidencia.md`:

```markdown
# Evidencia — <sección>

**Plan:** versión <n> | **Versión:** <n> | **Fecha:** <AAAA-MM-DD>

| ID | Afirmación | Cita textual | Fuente | Ubicación |
|---|---|---|---|---|
| E1 | <lo que el borrador afirma con esta cita> | «<cita literal>» | F1 / Nueva: <Autor, año, enlace> | <página, sección o encabezado> |
```

- **Pendientes:** omití la tabla si no falta nada.
- **Revisiones:** en cada una, subí la versión del archivo que cambió.
