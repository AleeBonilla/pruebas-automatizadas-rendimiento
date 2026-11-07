# Auditoría de evidencia — Introducción

## Ronda 2 — 2026-11-06 — Evidencia versión 2

**Veredicto:** Aprobada | **Filas revisadas:** E1, E2 y E13

Plan auditado: versión 4. Se revisaron las tres filas rechazadas en la ronda anterior, que son también las únicas modificadas en la tabla. No hay filas nuevas. Las otras 19 filas conservan su aprobación de la ronda 1. Resultado acumulado: 22 filas aprobadas, ninguna rechazada y ninguna no verificable.

- **E1 y E2 — Aprobadas:** los enlaces Markdown relativos resuelven desde la carpeta de la sección hasta la copia local F7 y el archivo existe. Se volvieron a cotejar las citas en §3.2, p. impresa 2, y §4.1, p. impresa 9, respectivamente (páginas 12 y 19 del PDF). Las afirmaciones son fieles, responden a P1 y el tipo «Norma» es correcto.
- **E13 — Aprobada:** la cita se sustituyó por dos pasajes del cuerpo de [GAO-14-694](https://www.gao.gov/assets/gao-14-694.pdf), p. impresa 23 (página 28 del PDF), en el apartado indicado. Ambos pasajes son literales; la omisión intermedia está señalada con `[...]` y conserva su sentido y orden. La afirmación refleja el calendario inicial y el revisado y el escaso margen para atender imprevistos. La fuente F5 pertenece al plan, el enlace lleva al informe, la fila responde a P4 y «Literatura gris» es adecuado. Queda subsanado el respaldo exclusivo en Highlights observado en la ronda 1.

**Cobertura:** Completa. P1: E1–E5; P2: E6–E9; P3: E10–E11; P4: E12–E15; P5: E16–E18; P6: E19–E22. Todos los puntos tienen filas aprobadas.

Se agregó esta ronda sin borrar la anterior. La tabla de evidencia y el plan no se modificaron durante la auditoría.

## Ronda 1 — 2026-11-06 — Evidencia versión 1

**Veredicto:** No aprobada | **Filas revisadas:** E1–E22

Plan auditado: versión 4. Resultado: 19 filas aprobadas, 3 rechazadas y ninguna no verificable. Se revisaron fuente, enlace, literalidad y ubicación, fidelidad de la afirmación, correspondencia con el punto y tipo de fuente. Las diferencias de saltos de línea y comillas tipográficas no se consideran alteraciones del contenido.

| Fila | Resultado | Hallazgo | Corrección sugerida |
|---|---|---|---|
| E1 | Rechazada | La definición es literal y la afirmación, el punto y el tipo son correctos. Se comprobó §3.2, p. impresa 2 (página 12 del PDF local). Sin embargo, la columna «Enlace» contiene solamente `ISO-IEC 25010-2023.pdf`, sin un enlace ni una ruta que resuelva desde la sección hasta la fuente local prevista en F7. | Convertir el nombre en un enlace Markdown a `../../../Adjuntos/Local/ISO-IEC%2025010-2023.pdf`. Mantener la cita y la página impresa. |
| E2 | Rechazada | La enumeración es literal y respalda la afirmación. Se comprobó §4.1, p. impresa 9 (página 19 del PDF local). Presenta el mismo problema de enlace de E1: el nombre aislado del archivo no enlaza con la copia local del plan. El punto y el tipo son correctos. | Incorporar el mismo enlace relativo sugerido para E1. Mantener la cita y la ubicación. |
| E13 | Rechazada | La cita es literal en «Highlights — What GAO Found» de GAO-14-694 y la afirmación es fiel, pero la evidencia textual de esta fila procede únicamente del resumen. Incumple el criterio de la skill que exige que la cita no provenga solo del resumen. La conclusión sí se corrobora en el cuerpo del informe, p. impresa 25, que ya utiliza E14. | Sustituir la cita y la ubicación por un pasaje del cuerpo y ajustar la afirmación a ese pasaje; o retirar esta fila por redundancia con E14. Si se conserva el detalle del cambio de marzo a septiembre, respaldarlo también con el pasaje correspondiente del cuerpo. |

**Filas aprobadas:** E3–E12 y E14–E22. Sus citas y afirmaciones corresponden a las fuentes y puntos asignados; los tipos son adecuados.

**Cobertura:** Completa. P1: E1–E5 (E3–E5 aprobadas; la definición y la ubicación normativa de E1–E2 se verificaron, con el defecto de enlace indicado). P2: E6–E9. P3: E10–E11. P4: E12–E15 (E12, E14 y E15 aprobadas). P5: E16–E18. P6: E19–E22. Ningún punto carece de filas; B3 y B4 no tienen puntos de investigación asignados en el plan. La cobertura completa no subsana los hallazgos individuales.

**Trazabilidad de la comprobación:**

- **F7:** lectura directa de `Adjuntos/Local/ISO-IEC 25010-2023.pdf`, adopción británica BS ISO/IEC 25010:2023 contemplada por el plan. Las páginas consignadas en E1 y E2 corresponden a la numeración impresa.
- **F2:** [PDF oficial de ISTQB](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf), §1.1, p. 10, y §1.3.2, pp. 13–14. E3–E5 tienen correcta la p. 10; la nota de verificación del plan que sitúa §1.1 en p. 11 no coincide con el PDF. E19 señala sus omisiones con `[...]` y conserva el orden de los niveles.
- **F3:** el DOI y las direcciones de York devolvieron errores de acceso o tiempo de espera en la herramienta; esto no demuestra que los enlaces estén rotos. Se cotejó el texto íntegro del mismo artículo en la [copia subida por Ahmed E. Hassan](https://www.researchgate.net/publication/282551435_A_Survey_on_Load_Testing_of_Large-Scale_Software_Systems), §1, p. 1091. Coinciden título, autores, revista, paginación y DOI con F3. Las dos citas están en la introducción, fuera del abstract. La atribución de E10 a estudios previos es apropiada; no presenta la revisión como una medición propia.
- **F4:** [artículo de Nielsen](https://www.nngroup.com/articles/response-times-3-important-limits/), cuerpo del extracto de 1993 y apartado añadido en 2014. E6–E9 no se apoyan solo en el resumen de la página. Los umbrales se refieren a la interacción percibida por el usuario, conforme al alcance del plan.
- **F5:** [informe completo GAO-14-694](https://www.gao.gov/assets/gao-14-694.pdf), p. impresa 1 para E12, Highlights para E13, p. 25 para E14 y p. 27 para E15. E14 proporciona respaldo del cuerpo para la falta de verificación. Las cifras de E15 coinciden con el pasaje citado.
- **F6:** páginas oficiales de AWS sobre [eficiencia de desempeño](https://docs.aws.amazon.com/wellarchitected/latest/framework/performance-efficiency.html) y [definición de optimización de costos](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-def.html). Las tres citas aparecen en el cuerpo. E17 conserva el carácter posible de la consecuencia descrita por AWS.

Se escribió únicamente este informe. La tabla de evidencia y el plan no se modificaron.
