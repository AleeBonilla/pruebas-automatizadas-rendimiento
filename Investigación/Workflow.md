# Flujo de trabajo de la investigación

Cada ejecución del flujo procesa **una sección** (o una subsección, en las secciones largas). El principio es **primero el argumento; la evidencia lo respalda**: el redactor escribe con voz propia y cita solo lo que necesita fuente, según la [Guía de redacción](Guía%20de%20redacción.md). La trazabilidad se conserva, pero solo para lo que el texto cita.

Las skills están en `.claude/skills/<skill>/SKILL.md`. En `.agents/skills/` hay envoltorios que apuntan a ellas para Codex.

## Skills

| Skill | Lee | Escribe |
|---|---|---|
| `/planificador` | `Alcance.md`, `Enunciado.md`, la guía, `Referencias.md`, `Adjuntos/Local` y el plan, si existe | `01 Plan.md`; `Referencias.md` al aprobarse |
| `/redactor` | El plan aprobado, la guía, `Alcance.md`, `Enunciado.md`, las fuentes y la auditoría, si existe | `02 Evidencia.md`, `03 Borrador.md`; `Referencias.md` si agrega una fuente |
| `auditor` (Codex) | La guía, el plan, la evidencia, el borrador, `Referencias.md` y las fuentes | `04 Auditoría.md` |

El usuario invoca solo `/planificador` y `/redactor`. El redactor lanza el auditor con `codex exec` y corrige sus hallazgos sin intervención; si Codex no está disponible, pide ejecutar `$auditor <sección>` a mano.

## Modos

| Modo | Secciones | Plan | Densidad de citas |
|---|---|---|---|
| **Ligero** | Introducción, Metodología, Conclusiones | Esquema argumental y pocas fuentes | ≤ 1 cita por párrafo en promedio |
| **Completo** | Planteamiento del problema, Marco teórico | Además, afirmaciones a respaldar (como tope, 1 por cada 100 palabras) | 1–3 citas por párrafo |

Una sección de más de unas 2 000 palabras se planifica y redacta por subsecciones (por ejemplo, el Marco teórico §5.1 a §5.8).

## Criterios de avance

| Paso | Condición |
|---|---|
| Plan → redacción | El plan está **Aprobado**: aprobado por el usuario, con las fuentes cerradas resueltas y ninguna *por verificar*. |
| Redacción → revisión humana | La última ronda de `04 Auditoría.md` es **Aprobada** (sin hallazgos bloqueantes), o se cumplieron las 2 rondas por invocación y el redactor entrega los bloqueantes pendientes. |

**Bloqueantes:** citas no trazables, no literales o infieles; datos sin cita; fuentes nuevas fuera de criterio; metacomentarios. **Sugerencias:** argumento, legibilidad, densidad, selección de detalles, extensión. Las sugerencias no frenan el avance.

## Modelos y niveles de razonamiento

Principio: **Claude produce, Codex audita.** El auditor no usa el mismo modelo que el redactor.

| Agente | Herramienta | Modelo | Razonamiento | Justificación |
|---|---|---|---|---|
| Planificador | Claude Code | Opus 5.5 | `high` al crear el plan · `medium` al ajustarlo | Si el esquema argumental está mal, falla el texto. Consume pocos tokens. |
| Redactor | Claude Code | Opus 5.5 | `high` | Investiga y redacta en la misma ventana; la prosa es lo que se evalúa. |
| Auditor | Codex (`codex exec`) | GPT-6.1 Sol | `high` | Control de calidad: coteja cada cita con su fuente y revisa la prosa. |

El modelo del auditor sale de `~/.codex/config.toml`; para fijarlo en la invocación, agregá `-m <modelo>` al comando de la skill del redactor.

## Ventanas de contexto

- Por cada sección, el planificador y el redactor trabajan cada uno en su propia ventana. El auditor corre en una sesión nueva de Codex en cada ronda.
- Los **archivos son el único canal entre agentes**. Si una ventana se satura o se pierde, el agente se reinicia a partir de sus archivos.

## Diagrama

![Flujo de trabajo](../Adjuntos/Workflow.png)

```mermaid
sequenceDiagram
    autonumber
    actor U as Usuario
    participant P as Planificador
    participant R as Redactor
    participant A as Auditor (Codex)

    U->>P: /planificador «sección»
    P->>P: Lee Alcance.md, Enunciado.md, la guía y Referencias.md
    P->>U: 01 Plan.md en Borrador (modo, esquema argumental, fuentes)
    loop Mientras haya observaciones
        U->>P: Observaciones al plan
        P->>U: 01 Plan.md revisado
    end
    opt Hay fuentes cerradas
        U->>P: Fuentes cerradas en Adjuntos/Local
        P->>P: Reemplaza las no disponibles por fuentes abiertas
    end
    U->>P: Aprobación explícita
    P->>P: 01 Plan.md en Aprobado y actualiza Referencias.md
    U->>R: /redactor «sección»
    R->>R: Lee las fuentes y escribe 03 Borrador.md y 02 Evidencia.md
    opt Falta respaldo
        R->>R: Reformula, agrega una fuente nueva o marca [FALTA FUENTE]
    end
    loop Hasta 2 rondas, mientras haya bloqueantes
        R->>A: codex exec (auditor)
        A->>A: Coteja las citas con las fuentes y revisa la prosa
        A->>R: 04 Auditoría.md (veredicto, bloqueantes y sugerencias)
        R->>R: Corrige 03 Borrador.md y 02 Evidencia.md
    end
    R->>U: 03 Borrador.md y resumen (extensión, citas, pendientes)
    opt Observaciones al borrador
        U->>R: Observaciones
        R->>R: Aplica los cambios y vuelve a auditar si tocan citas
    end
    U->>U: Revisión humana e integración al documento
```

## Artefactos

```
Adjuntos/Local/                      fuentes cerradas disponibles
Investigación/
├── Guía de redacción.md             reglas de estilo y de citas
├── Referencias.md                   referencias de todo el documento
└── Secciones/<sección>/
    ├── 01 Plan.md
    ├── 02 Evidencia.md              solo las afirmaciones citadas
    ├── 03 Borrador.md
    └── 04 Auditoría.md
```

**Nombre de las carpetas de sección:** `<NN> <Nombre>`, donde `NN` es el número de la sección en el documento, según la estructura del `Enunciado.md`: `02 Introducción`, `03 Planteamiento del problema`, `04 Metodología`, `05 Marco teórico`, `06 Propuesta de taller práctico` y `07 Conclusiones`. Así coincide con la numeración de los subtítulos de los borradores (3.1, 4.1…). Las secciones que se planifican por subsección usan el número de la subsección del documento: por ejemplo, `05.1 Aseguramiento de la calidad en la fase de implementación`.
