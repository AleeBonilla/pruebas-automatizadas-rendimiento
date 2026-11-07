# Auditoría — 01 Introducción

## Ronda 5 — 2026-11-07 — Borrador v4 · Evidencia v5

**Veredicto:** Aprobada | **Citas revisadas:** E1, E2, E7, E8, E9, E10, E11, E12, E14, E17, E19, E22, E23, E24, E26, E28 y E29

Plan auditado: versión 7, modo ligero. Se revisaron los seis hallazgos de la ronda 4 y el borrador completo contra la evidencia v5, la guía de redacción, el plan, las referencias, el alcance y el enunciado. Resultado: **ningún hallazgo bloqueante y ninguna sugerencia pendiente**.

**Continuidad y alcance del cotejo.** Se compararon las 29 filas de la evidencia v5 con la evidencia v4 registrada en Git: no cambian las afirmaciones, las citas textuales, las fuentes ni las ubicaciones. La migración reorganiza las filas utilizadas y no utilizadas y remite los enlaces a la tabla de fuentes del plan. Los 17 IDs citados están en la tabla principal; las otras 12 filas permanecen en «Filas no usadas». Se conserva la aprobación de literalidad y ubicación de las rondas 1–3 y el cotejo adicional documentado en la ronda 4. Conforme a la skill, no se repitió la consulta externa de pasajes sin cambios; esta ronda verifica su uso en el borrador actual y no se presenta como una nueva lectura directa de las fuentes.

**Seguimiento de la ronda 4:**

- **Hallazgo 1 — Resuelto.** B1, párrafo 2, presenta uno y diez segundos como límites aproximados. Conserva la percepción de demora alrededor del primer límite y sitúa el deseo de hacer otra tarea en esperas mayores que el segundo. La oración concuerda con E7–E9.
- **Hallazgo 2 — Resuelto.** B1, párrafo 3, elimina la afirmación de que HealthCare.gov no tenía problemas funcionales. El cierre se limita al riesgo de lanzar sin verificar el desempeño, a partir de E12 y E14.
- **Hallazgo 3 — Resuelto.** B1, párrafo 4, dice «puede conducir a despliegues sobreaprovisionados» y conserva el carácter posible de la consecuencia recogida en E17.
- **Hallazgo 4 — Resuelto.** B2 presenta las dos recomendaciones del ISTQB como tales y expone después la elección de los niveles de prueba como decisión del trabajo. Ya no atribuye al syllabus una supuesta tensión entre las recomendaciones de E19 y E22.
- **Sugerencia 5 — Atendida.** B1, párrafo 1, separa la justificación, la ubicación en el modelo y la definición en oraciones distintas, con una sola cita final para E1 y E2.
- **Sugerencia 6 — Resuelta por el plan vigente.** B4 conserva 128 palabras. El plan v7 asigna 125, frente a las 150 de la ronda anterior; ahora cumple el margen de ±10 %. No hace falta ampliar el párrafo para satisfacer un presupuesto que ya fue sustituido.

**Comprobaciones:**

- **Trazabilidad, fidelidad y respaldo (1, 3 y 4):** las ocho citas remiten a 17 filas existentes y sus autores y años corresponden a las fuentes del plan y de `Referencias.md`. Las definiciones normativas, los umbrales de percepción, el caso histórico y la experiencia de automatización tienen respaldo. La relación entre la espera del usuario y el backend, la elección del foco del estudio y la motivación de automatizar se leen como conexiones del autor. El cierre de B3 sobre relacionar degradaciones con cambios conserva el carácter de síntesis ya admitido en la ronda 4; no agrega un resultado empírico atribuido a Daly et al.
- **Literalidad y ubicación (2):** se mantiene el cotejo aprobado para E1–E2, E7–E12, E14, E17, E19, E22–E24, E26 y E28–E29, sin cambios en sus pasajes ni ubicaciones. Las rondas anteriores documentan su presencia en el cuerpo de las fuentes, no únicamente en resúmenes.
- **Fuentes nuevas y formato (5 y 6):** no se incorporan fuentes nuevas ni filas marcadas «Nueva». Todas las fuentes citadas figuran en las referencias. Las citas siguen el formato APA 7 utilizado por el documento, introducen las siglas institucionales y llevan comentarios con los IDs correspondientes. El sufijo s. f.-a de AWS corresponde a *Cost optimization: Definition*.
- **Argumento, legibilidad y densidad (7–9):** B1 desarrolla los tres frentes de relevancia; B2 justifica el foco en implementación; B3 enlaza la automatización con el enfoque y el objetivo; B4 relaciona las preguntas con las secciones. Hay ocho citas en ocho párrafos, compatible con el modo ligero. Los dos párrafos con dos citas se compensan con los dos sin citas; la guía fija el límite como promedio. Cada fuente aparece una sola vez dentro de cada párrafo. No se detectan detalles ajenos al argumento ni nuevas dificultades de lectura.
- **Contenido interno y metacomentarios (10 y 11):** el enfoque y el objetivo están integrados en B3; las cinco preguntas aparecen una vez en B4, junto a las secciones que las responden. No hay listas copiadas ni metacomentarios de producción en el texto visible. Los comentarios HTML de versión, bloques y evidencia se consideran información de control y se excluyen de la prosa auditada.

**Extensión:**

| Bloque | Plan | Borrador |
|---|---|---|
| B1. El rendimiento como atributo de calidad | 375; margen entero 338–412 | 374; −0,3 % — cumple |
| B2. Ubicación en el ciclo de vida | 150; margen 135–165 | 147; −2,0 % — cumple |
| B3. Motivación, enfoque y objetivo | 225; margen entero 203–247 | 215; −4,4 % — cumple |
| B4. Estructura del documento y preguntas | 125; margen entero 113–137 | 128; +2,4 % — cumple |
| **Total** | **875; margen entero 788–962** | **864; −1,3 % — cumple** |

Conteo reproducible: palabras separadas por espacios en el texto visible de cada bloque; incluye las citas autor–año, excluye el título y todos los comentarios HTML, y elimina los delimitadores de cursiva. Los márgenes enteros incluyen solo cantidades comprendidas dentro de ±10 %.

Se agrega esta ronda al inicio y se conservan íntegramente las rondas 1–4. Se escribe únicamente `04 Auditoría.md`.

## Ronda 4 — 2026-11-07 — Borrador v3 · Evidencia v4

**Veredicto:** No aprobada | **Citas revisadas:** E1, E2, E7, E8, E9, E10, E11, E12, E14, E17, E19, E22, E23, E24, E26, E28 y E29

Plan auditado: versión 6, modo ligero. Se revisó todo el borrador v3 contra la evidencia v4, la guía de redacción, el plan, las referencias y el alcance. Resultado: **4 hallazgos bloqueantes y 2 sugerencias**. Los bloqueantes corresponden al uso de la evidencia en el borrador; no revocan la aprobación de las filas.

**Continuidad con la ronda anterior.** La ronda 3 aprobó las 29 filas de la evidencia v4 y no dejó pendientes. La evidencia mantiene esa versión y no presenta diferencias respecto de la versión registrada en Git. Se conserva el cotejo de literalidad y ubicación ya aprobado en las rondas 1–3, conforme a la regla de no repetir comprobaciones de citas sin cambios. Esta ronda agrega la revisión de trazabilidad, fidelidad y respaldo de las ocho citas del borrador, que remiten a 17 filas. Se volvieron a consultar directamente Nielsen, AWS y el cuerpo del informe de la GAO para resolver las diferencias de sentido señaladas abajo. No se presenta como nuevo cotejo directo de fuentes lo que se conserva de las rondas anteriores.

Los párrafos se numeran dentro de cada bloque; las líneas remiten a la versión auditada de `03 Borrador.md`.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante | B1, párrafo 2, línea 10; E7–E9 | 3 — Fidelidad | «Cerca de los diez, pierde la atención y busca otra cosa que hacer» convierte un límite aproximado para mantener la atención en una pérdida categórica cerca de ese valor. E8 sitúa el deseo de hacer otras tareas en demoras mayores. Además, «hasta un segundo, el usuario nota la demora» abarca incluso respuestas que Nielsen describe como percibidas de forma instantánea. | Reformular: «Alrededor de un segundo se sitúa el límite para conservar el hilo de pensamiento, aunque se perciba la demora; unos diez segundos son el límite aproximado para mantener la atención, y con esperas mayores el usuario querrá hacer otras tareas». Mantener la cita y E7–E9. |
| 2 | Bloqueante | B1, párrafo 3, cierre, línea 12; E12 y E14 | 3 y 4 — Fidelidad y respaldo | «No fallaba lo que el sistema hacía, sino cómo respondía a la demanda» afirma que el caso HealthCare.gov carecía de problemas funcionales. E12 enumera fallas, errores y lentitud; E14 acredita la falta de verificación de requisitos de desempeño. Ninguna permite excluir fallas funcionales. La GAO también documenta capacidades pospuestas en el cuerpo del informe, p. 26. La conclusión sobre este caso concreto excede la evidencia y no queda justificada como razonamiento propio. | Suprimir ese cierre o sustituirlo por una conclusión limitada a lo documentado: «El caso muestra la importancia de verificar los requisitos de desempeño antes del lanzamiento». No atribuir al caso una corrección funcional que las filas no establecen. |
| 3 | Bloqueante | B1, párrafo 4, línea 14; E17 | 3 — Fidelidad | «Conduce a despliegues sobreaprovisionados» atribuye a AWS una consecuencia necesaria. La fila y la fuente conservan expresamente el carácter posible del resultado. | Sustituir «conduce» por «puede conducir». Mantener Amazon Web Services (AWS, s. f.-a) y E17. |
| 4 | Bloqueante | B2, párrafo 1, segunda oración, línea 18; E19 y E22 | 3 y 4 — Fidelidad y atribución del razonamiento | «Una tensión que el propio syllabus del ISTQB reconoce» atribuye al syllabus una interpretación del autor. E19 recomienda probar temprano y E22 exige realismo en niveles superiores; ninguna fila afirma que estas recomendaciones constituyan una tensión. La justificación de la elección del estudio es válida como razonamiento propio, pero debe distinguirse de lo que declara la fuente. | Sustituir la entrada por «La elección se apoya en dos recomendaciones del syllabus del ISTQB: …». Conservar las recomendaciones y su cita; formular después la decisión de concentrarse en la validación del sistema integrado como decisión del trabajo. |
| 5 | Sugerencia | B1, párrafo 1, segunda oración, línea 8 | 8 — Legibilidad; guía §6 | Una misma oración reúne la justificación de la relevancia, la ubicación en el modelo, las nueve características, la definición y dos nombres institucionales extensos. La acumulación dificulta distinguir la idea central de su respaldo normativo. | Dividirla, manteniendo una sola cita al final: «Por eso el rendimiento es un atributo de calidad. ISO/IEC 25010:2023 lo incluye, con el nombre de eficiencia de desempeño, entre las nueve características de su modelo de calidad del producto. Lo define como la capacidad de ejecutar las funciones dentro de parámetros especificados de tiempo y de *throughput*, con un uso eficiente de los recursos en condiciones especificadas [cita actual e IDs]». |
| 6 | Sugerencia | B4, párrafo 1, línea 28 | 12 — Extensión | Tiene 128 palabras frente a las 150 previstas: −14,7 %, por debajo del mínimo de 135. El total de la sección sí cumple; el criterio exige también revisar cada bloque. | Añadir una oración que explique la lógica del recorrido sin volver a enumerar las preguntas; por ejemplo, después de la primera: «Este recorrido conecta los fundamentos del tema con su demostración experimental». La adición sitúa B4 dentro del margen. |

**Comprobaciones y fuentes:**

- **Trazabilidad y formato (1 y 6):** las ocho citas incluyen IDs existentes, con autores y años correspondientes a las referencias. El sufijo s. f.-a de AWS remite correctamente a *Cost optimization: Definition*. No se detectaron defectos adicionales de formato APA 7.
- **Literalidad y ubicación (2):** se conserva la aprobación previa de las filas utilizadas. El nuevo cotejo de E7–E9 se hizo en el cuerpo de [Nielsen, *Response times: The 3 important limits*](https://www.nngroup.com/articles/response-times-3-important-limits/), en los límites de uno y diez segundos y en la actualización web de 2014. E17 se comprobó en el párrafo sobre decisiones apresuradas y pruebas comparativas de [AWS, *Definition*](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-def.html). E12 y E14 se comprobaron en el cuerpo de [GAO-14-694](https://www.gao.gov/assets/gao-14-694.pdf), pp. impresas 1 y 25; el contraste adicional sobre capacidades pospuestas está en la p. 26. Estos pasajes no proceden solo de resúmenes.
- **Fidelidad y respaldo (3 y 4):** salvo los hallazgos 1–4, las afirmaciones citadas se mantienen dentro de las filas utilizadas. La motivación de automatizar y relacionar degradaciones con cambios se lee como síntesis del autor apoyada en E23, E24, E26, E28 y E29; no se interpreta como garantía de que automatizar por sí solo resuelva la atribución. No se exige citar el alcance, los objetivos ni las preguntas internas, ni las conexiones propias que no introducen hechos externos.
- **Fuentes nuevas (5):** el borrador no incorpora fuentes nuevas respecto del plan y de la evidencia aprobada. Todas las utilizadas figuran en `Referencias.md`; no hay fuentes marcadas «Nueva» que requieran una evaluación adicional de inclusión según `Alcance.md` §5.3.
- **Argumento y selección (7–9):** los cuatro bloques cumplen su función argumental. Hay ocho citas en ocho párrafos: promedio de una por párrafo, compatible con el modo ligero. Ninguna fuente se repite dentro del mismo párrafo. No es obligatorio utilizar las 29 filas disponibles; la selección omite detalles que no necesita la introducción.
- **Contenido interno y metacomentarios (10 y 11):** el enfoque y el objetivo general están integrados en B3 y las cinco preguntas aparecen una vez en B4, junto a sus secciones. No hay listas copiadas ni referencias al uso de IA, skills o auditorías en la prosa del documento. Para esta revisión de prosa se excluyeron los comentarios HTML de control de versión, bloques y trazabilidad.

**Extensión:**

| Bloque | Plan | Borrador |
|---|---|---|
| B1. El rendimiento como atributo de calidad | 350; margen 315–385 | 359; +2,6 % — cumple |
| B2. Ubicación en el ciclo de vida | 150; margen 135–165 | 148; −1,3 % — cumple |
| B3. Motivación, enfoque y objetivo | 225; margen entero 203–247 | 215; −4,4 % — cumple |
| B4. Estructura del documento y preguntas | 150; margen 135–165 | 128; −14,7 % — fuera de margen |
| **Total** | **875; margen entero 788–962** | **850; −2,9 % — cumple** |

Conteo reproducible: palabras separadas por espacios en el texto visible de cada bloque; incluye las citas autor–año, excluye el título y todos los comentarios HTML, y elimina los delimitadores de cursiva. La extensión fuera de margen de B4 es una sugerencia, no la causa del veredicto.

Se agrega esta ronda al inicio y se conservan las rondas 1–3. Solo se escribe `04 Auditoría.md`; no se corrigen el borrador, la evidencia, el plan ni las referencias.

## Ronda 3 — 2026-11-07 — Evidencia versión 4

**Veredicto:** Aprobada | **Filas revisadas:** E14 y E23–E29

Plan auditado: versión 5. La ronda 2 no dejó filas rechazadas ni no verificables. Se revisaron las siete filas nuevas E23–E29 y E14, cuyo apartado se corrigió en la versión 3, posterior a la versión auditada en la ronda 2. La comparación del historial y de la tabla actual no muestra otros cambios en E1–E22 fuera de las correcciones ya comprobadas en la ronda 2. Las otras 21 filas conservan su aprobación. Resultado de esta ronda: 8 filas aprobadas, ninguna rechazada y ninguna no verificable. Resultado acumulado: 29 filas aprobadas.

Se comprobaron fuente prevista en el plan, enlace, literalidad y ubicación de la cita en el cuerpo, fidelidad de la afirmación, correspondencia con el punto y adecuación del tipo. Los saltos de línea y de párrafo no se consideran alteraciones del contenido.

- **E14 — Aprobada:** la cita aparece en el cuerpo de [GAO-14-694](https://www.gao.gov/assets/gao-14-694.pdf), p. impresa 25 (página 30 del PDF), bajo «Some Governance Reviews Were Not Fully Conducted or Approved». La ubicación corregida es válida; la afirmación, P4, F5 y el tipo «Literatura gris» son adecuados.
- **E23 y E24 — Aprobadas:** las citas son literales en §4.4 de [SPEC-RG-2015-01, copia de arXiv prevista en F8](https://arxiv.org/pdf/1508.04752), p. impresa 20 (página 24 del PDF). El contexto inmediato respalda la referencia de E23 al entorno de negocio. E24 conserva el carácter posible de los cambios de desempeño. Ambas aportan a P7; «Literatura gris» corresponde al informe técnico.
- **E25 — Aprobada:** cita literal en §4.4 del mismo informe, p. impresa 21 (página 25 del PDF). La afirmación conserva la propuesta de integración en CI y explicita que el antecedente son pruebas unitarias de rendimiento. Esa precisión respeta el contexto y permite usarla para P7 sin generalizar el pasaje a pruebas de carga de API REST. Fuente, enlace y tipo correctos.
- **E26 y E27 — Aprobadas:** citas literales del cuerpo de [Daly et al. (2020), versión publicada de F9](https://research.spec.org/icpe_proceedings/2020/proceedings/p67.pdf), §1.1 y §1 respectivamente, p. impresa 67 (página 1 del PDF). Las afirmaciones distinguen el seguimiento de cada *commit* de la ejecución periódica de los *benchmarks*; no afirman que cada prueba de rendimiento se ejecute con cada cambio. Ambas responden a P8 y el tipo «Artículo arbitrado» es adecuado.
- **E28 — Aprobada:** cita literal del cuerpo del mismo artículo, §1.1, p. impresa 68 (página 2 del PDF). Respalda la dificultad de sostener la revisión manual y la incorporación de detección automatizada, sin atribuirle resultados adicionales. Corresponde a P8; fuente, enlace y tipo correctos.
- **E29 — Aprobada:** cita literal de «Problem 1», §2, p. impresa 69 (página 3 del PDF). Aunque el plan orienta la búsqueda de P8 a §1 y §1.1, este pasaje de la misma fuente responde directamente a la finalidad investigada. La afirmación se limita al problema de atribuir cambios de desempeño a *commits*; no desarrolla el algoritmo ni sus umbrales. Fuente, enlace y tipo correctos.

**Cobertura:** Completa. P1: E1–E5; P2: E6–E9; P3: E10–E11; P4: E12–E15; P5: E16–E18; P6: E19–E22; P7: E23–E25; P8: E26–E29. Todos los puntos del plan vigente tienen filas aprobadas; no hay puntos sin respaldo. B4 no tiene puntos de investigación asignados.

Se agregó esta ronda sin borrar las anteriores. Se escribió únicamente este informe; la tabla de evidencia y el plan no se modificaron.

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
