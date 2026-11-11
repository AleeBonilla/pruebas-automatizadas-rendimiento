# Plan — 07 Conclusiones

**Estado:** Aprobado | **Modo:** Ligero | **Versión:** 1 | **Fecha:** 2026-11-11 | **Presupuesto:** 430 palabras (1 página)

> Este plan se reconstruyó el 2026-11-11, después de redactar el borrador, para poder auditarlo. La sección se redactó a partir de las secciones 3, 5 y 6, de los informes de auditoría y de `Taller/Taller.md`, y no tiene fuentes externas.

## Objetivo y alcance

Sección 7 del documento (`Enunciado.md` §7; `Alcance.md` §5.6). Reúne los hallazgos principales, el balance técnico y las reflexiones metodológicas. Responde PI-1 a PI-5 y la pregunta-problema, sin repetir las definiciones ni las citas de las secciones anteriores: remite a ellas por número.

**Excepción a la guía, §5 (metacomentarios):** `Enunciado.md` pide «reflexiones metodológicas» y `Alcance.md` §5.6 incluye una «reflexión metodológica sobre el uso y la validación de la IA» en las Conclusiones. Por eso el último bloque trata el uso de la IA. Lo hace en los términos que ya presenta la Metodología (4.3) y remite al anexo B para el detalle.

## Esquema argumental

| Bloque | Palabras | Idea central | Contenido y respaldo |
|---|---|---|---|
| B1. Hallazgos por pregunta de investigación | 135 | Automatizar estas pruebas es, antes que un problema técnico, un problema de criterio | PI-1 (5.3, 5.4), PI-2 (3.1 a 3.3), PI-3 (5.6, 5.7) y PI-4 (5.8). Síntesis de lo ya citado: no lleva citas |
| B2. Respuesta a PI-5 | 66 | Solo la prueba de carga distingue las dos implementaciones, y el veredicto se repite | Sección 6; `Taller/Taller.md` §5.2, §7.1 y §7.2 |
| B3. Respuesta a la pregunta-problema | 74 | La respuesta es afirmativa pero condicionada | Secciones 6.2, 6.4 y 6.5; `Taller/Taller.md` §6.4 |
| B4. Balance técnico | 77 | Tres lecciones: el entorno, el ruido y el alcance | `Taller/Taller.md` §5.2, §7.1 y sección 6.7 |
| B5. Reflexión sobre el uso de la IA | 76 | La IA aceleró la producción, pero no sustituyó la verificación | `04 Auditoría.md` de cada sección; anexo B; sección 4.3 |

## Afirmaciones internas a verificar

Todas son contenido interno del trabajo: no llevan cita, pero cada una debe coincidir con su origen.

| Afirmación | Origen |
|---|---|
| Las dos implementaciones aprueban las mismas 38 pruebas funcionales | Sección 6.1; `Taller/docs/GUIA.md` §4 |
| `regresion` colapsa entre 75 y 100 solicitudes por segundo; `corregida` mantiene un p95 de unos 10 ms hasta 300 | `Taller/Taller.md` §5.2 |
| 19 ejecuciones de validación, todas válidas, en dos entornos; siempre `regresion` rechazada y `corregida` aprobada | Sección 6.6, Tabla 6; `Taller/Taller.md` §7.2 (7 + 6 + 6) |
| Bastan Git y Docker y entre cuatro y seis minutos por ejecución | Secciones 6.2 y 6.5; `Taller/docs/GUIA.md` §1 y §9 |
| El veredicto confiable exige calibrar el umbral por entorno, validarlo con una campaña nueva y comprobar la validez de cada medición | Sección 6.4; `Taller/Taller.md` §6.4 y §7 |
| Con 1 CPU por contenedor y la base de datos en la misma máquina, las variantes no se separaban | `Taller/Taller.md` §5.2 |
| El p95 de `corregida` varió hasta 28 veces entre corridas idénticas en GitHub Actions | `Taller/Taller.md` §7.1 |
| Una regresión pequeña aprobaría, porque el umbral se calibró con una regresión que lleva el p95 a decenas de segundos | Sección 6.7 |
| 28 rondas de auditoría, 11 no aprobadas y 22 hallazgos bloqueantes; los más frecuentes, de fidelidad y de respaldo; ninguno señaló una fuente inexistente | `04 Auditoría.md` de cada sección; anexo B |
| Partir de la evidencia ya auditada saturó el texto de citas | `Alcance.md` §5.3; anexo B, B.3 |
| Claude Code produce y Codex audita, con la última decisión humana | Sección 4.3 |

## Fuentes

Ninguna externa.
