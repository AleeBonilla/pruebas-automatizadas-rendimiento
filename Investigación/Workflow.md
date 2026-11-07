# Flujo de trabajo de la investigación

Cada ejecución del flujo procesa **una sección** indicada al invocar las skills. Cada flecha entre agentes representa la entrega de un archivo. Cada skill es atómica: lee archivos definidos y escribe solo los suyos.

Las skills están en `.claude/skills/<skill>/SKILL.md`. Las de auditoría también deben estar en la carpeta de skills que lea Codex.

## Skills

| Skill | Lee | Escribe |
|---|---|---|
| `/planificador` | `Alcance.md`, `Enunciado.md`, `Referencias.md` y el plan, si existe | `01 Plan.md`; `Referencias.md` al pasar a Final |
| `/investigador` | `01 Plan.md` en estado Final, `Adjuntos/Local` y `04 Auditoría - Evidencia.md`, si existe | `02 Evidencia.md` |
| `auditor-evidencia` | `01 Plan.md`, `02 Evidencia.md` y `Adjuntos/Local` | `04 Auditoría - Evidencia.md` |
| `/redactor` | `01 Plan.md`, `02 Evidencia.md`, `04 Auditoría - Evidencia.md`, `Referencias.md`, los insumos del plan y `05 Auditoría - Redacción.md`, si existe | `03 Borrador.md` |
| `auditor-redaccion` *(opcional)* | `01 Plan.md`, `02 Evidencia.md`, `03 Borrador.md`, `Referencias.md` y los insumos del plan, si hacen falta | `05 Auditoría - Redacción.md` |

## Criterios de avance

| Paso | Condición para avanzar |
|---|---|
| Plan → investigación | El plan está en estado **Final**: aprobado por el usuario, con las fuentes cerradas resueltas y ninguna fuente *por verificar*. |
| Evidencia → redacción | La última ronda de `04 Auditoría - Evidencia.md` tiene veredicto **Aprobada**: todas las filas aprobadas y la cobertura completa. |
| Borrador → revisión humana | Si se aplica la auditoría de redacción, la última ronda tiene veredicto **Aprobada**. La extensión se informa, pero no afecta el veredicto. |

## Modelos y niveles de razonamiento

Principio: **Claude produce, Codex audita.** Ningún auditor usa el mismo modelo que el agente que revisa.

| Agente | Herramienta | Modelo | Nivel | Razonamiento | Justificación |
|---|---|---|---|---|---|
| Planificador | Claude Code | Opus 5.5 | Potente | `high` al crear el plan · `medium` al revisarlo y ajustarlo a las fuentes | Si el plan está mal, falla todo lo que viene después. Consume pocos tokens. |
| Investigador | Claude Code | Sonnet 5.5 | Ligero | `medium` | Es el que más tokens consume; sus errores los detecta el auditor de evidencia. |
| Auditor de evidencia | Codex | GPT-6.1 Sol | Potente | `high` | Es el control de calidad principal: juzga si cada paráfrasis es fiel a su cita. |
| Redactor | Claude Code | Opus 5.5 | Potente | `high` al redactar · `medium` al corregir | La prosa académica es lo que se evalúa. |
| Auditor de redacción *(opcional)* | Codex | GPT-6.1 Terra | Ligero | `medium` | Gracias a los IDs ocultos, la trazabilidad es casi mecánica. Compara archivos locales sin consultar la web. |

**Ajuste:** si en una sección el auditor de evidencia rechaza filas de forma recurrente, el investigador sube a Opus 5.5 para esa sección (a criterio del usuario).

## Ventanas de contexto

- Por cada sección, **cada agente trabaja en su propia ventana de contexto** y la conserva durante todas sus intervenciones en esa sección. Al pasar a otra sección, se abren ventanas nuevas.
- Los **archivos son el único canal entre agentes**: ningún agente ve la ventana de otro. Si una ventana se satura o se pierde, el agente se reinicia a partir de sus archivos de entrada.
- En las rondas posteriores, cada auditor revisa los hallazgos de la ronda anterior y todo lo nuevo o modificado.

## Artefactos

```
Adjuntos/Local/                      fuentes cerradas disponibles
Investigación/
├── Referencias.md                   referencias de todo el documento
└── Secciones/<sección>/
    ├── 01 Plan.md
    ├── 02 Evidencia.md
    ├── 03 Borrador.md
    ├── 04 Auditoría - Evidencia.md
    └── 05 Auditoría - Redacción.md  (solo si se aplica)
```
