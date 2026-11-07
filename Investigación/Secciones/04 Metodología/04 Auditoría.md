# Auditoría — 04 Metodología

## Ronda 2 — 2026-11-07 — Borrador v3 · Evidencia v2

**Veredicto:** Aprobada | **Citas revisadas:** E1, E2, E3 y E4

Plan auditado: versión 3, modo ligero. Se comparó la condensación con el borrador v2 registrado en Git y con la evidencia v1, se revisaron las sugerencias de la ronda 1 y se contrastaron las afirmaciones del procedimiento con los archivos y el historial del repositorio. Resultado: **ningún hallazgo bloqueante y tres sugerencias de precisión del procedimiento**. Los párrafos se numeran dentro de cada subsección. La ronda anterior se conserva íntegra debajo.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Sugerencia | B2, §4.2, párrafo 3, «Toda fuente se verificó en la página del editor…» | 7 — Correspondencia con los insumos internos | La formulación universal excede lo documentado. En el plan del grupo A del Marco teórico, «Verificación», F6, Humble y Farley se verifican mediante los créditos de la copia local: editorial, ISBN y primera impresión. No consta allí una consulta a la página del editor. Los planes de la Introducción también registran comprobaciones en portadas, copias de autor y actas. La revisión bibliográfica sí consta; el repositorio no permite atribuir a todas las fuentes exactamente el mismo canal de verificación. | Sustituir el inicio por «Los datos bibliográficos se comprobaron en páginas oficiales de publicación o en las propias copias consultadas, y los DOI se contrastaron en Crossref cuando correspondía. Las fuentes se leyeron en texto completo». No afirmar que una comprobación no registrada ocurrió. |
| 2 | Sugerencia | B3, §4.3, párrafo 2, «sus hallazgos bloqueantes […] deben resolverse antes de la revisión humana final» | 7 — Precisión del flujo descrito | Resume la condición de aprobación, pero omite una salida que el procedimiento operativo admite: `Workflow.md`, «Criterios de avance», y la skill del redactor, pasos 7–8, permiten entregar bloqueantes pendientes después de dos rondas por invocación. Conviene distinguir la aprobación de la sección de su entrega al usuario con pendientes, para que la frase no describa un avance más estricto que el implementado. | Reformular el cierre como «La aprobación exige resolver los hallazgos bloqueantes; si quedan pendientes tras dos rondas por invocación, se entregan al usuario para revisión». Conservar la exigencia de revisión humana antes de integrar el texto, establecida en `Alcance.md` §5.3. |
| 3 | Sugerencia | B2, §4.2, último enunciado, y B3, §4.3, último enunciado: remisiones a los anexos A y B | 7 y 8 — Estado del trabajo y precisión | El alcance §9 los identifica como anexos previstos y el plan v3 traslada allí el detalle recortado, pero en los archivos disponibles todavía no están redactados. «Resume» y «detalla» funcionan como remisiones para el documento final; no permiten comprobar ahora que el material ya se haya trasladado. | Mientras se trabaja con el borrador, usar «El anexo A previsto resumirá las consultas y las fuentes descartadas» y «El anexo B previsto detallará los hallazgos y sus resoluciones». Al integrar los anexos, restituir el presente y comprobar las remisiones. |

**Seguimiento de la ronda 1:**

- **Sugerencia 1 — Reconsiderada según el plan v3.** El borrador v2 había separado la distribución entre modelos de los pasos. La condensación vuelve a reunirlos, pero ahora el plan pide expresamente el procedimiento en un párrafo. Las oraciones distinguen las tres funciones y permiten seguir la secuencia; no se reitera la sugerencia de dividirlo. La precisión pendiente sobre la entrega con bloqueantes figura en el hallazgo 2 de esta ronda.
- **Sugerencia 2 — Resuelta.** Desaparecen las valoraciones sobre el argumento y la lentitud. El cierre conserva resultados y cambios observables del procedimiento, con fecha de corte, sin anticipar la reflexión de las Conclusiones.

**Cotejo de las citas que cambiaron:**

Las afirmaciones, pasajes, fuentes y ubicaciones de E1–E4 no cambian entre evidencia v1 y v2; E5 pasa a «Filas no usadas» y deja de citarse. Aunque podía conservarse la literalidad aprobada en la ronda 1, se volvieron a consultar los pasajes de E1–E4 para comprobar las dos oraciones citadas que la condensación modifica.

| Filas | Fuente y ubicación comprobadas | Resultado de la condensación |
|---|---|---|
| E1–E3 | [Snyder (2019), versión publicada en la copia de la autora](https://www.researchgate.net/profile/Hannah-Snyder-7/publication/334848557_Literature_review_as_a_research_methodology_An_overview_and_guidelines/links/5d482ec9a6fdcc370a7ccb34/Literature-review-as-a-research-methodology-An-overview-and-guidelines.pdf): §2.1.2, p. 335, y tabla 1, p. 334. | **Conformes.** Los pasajes son literales, normalizando saltos de línea y particiones tipográficas. La oración conserva la diversidad de aproximaciones, la búsqueda sistemática o no y la exigencia de transparencia y estrategia definida. Omite desarrollar la dificultad de una revisión sistemática completa, pero no afirma exhaustividad ni invierte el sentido. La aplicación a las pruebas de rendimiento sigue presentada como razonamiento del autor. |
| E4 | [Walters y Wilder (2023), texto completo del editor disponible en ResearchGate](https://www.researchgate.net/publication/373738246_Fabrication_and_errors_in_the_bibliographic_citations_generated_by_ChatGPT): Resultados, «Extent of fabrication», p. 4. | **Conforme.** Los dos fragmentos aparecen en el cuerpo, en el orden registrado. La oración conserva los porcentajes de obras inventadas por modelo dentro del estudio; no los confunde con errores en referencias reales. Mantiene la advertencia sobre los modelos anteriores y no extrapola las cifras a los empleados aquí. La retirada de E5 no deja una afirmación huérfana. |

**Acceso y límites:** el enlace de NORA no fue accesible y Nature redirigió a una autenticación técnica. F1 se cotejó en el PDF publicado alojado en el perfil de la autora; F2, en la transcripción íntegra identificada como texto suministrado por Springer Nature, con encabezados de página. No se afirma haber descargado el PDF de Nature. Coinciden autores, años, títulos y DOI con las referencias. No quedaron pasajes citados sin comprobar.

**Contraste del procedimiento con el repositorio:**

| Afirmación del borrador | Registro contrastado y resultado |
|---|---|
| Revisión para PI-1–PI-4 y taller experimental para PI-5 | Compatible con `Alcance.md` §§2–3 y `Enunciado.md`. Describe el diseño metodológico; no se verificó una ejecución del taller, cuya Fase 2 sigue por definir. |
| Criterios de selección y búsqueda dirigida a cada afirmación | Coinciden con el alcance §5.3 y con los planes de la Introducción y del Planteamiento: fuentes verificadas y descartadas con motivos, sin registro de cadenas. Se contrasta lo conservado en archivos, no se reconstruye un historial externo del buscador. |
| Registro de consultas desde el Marco teórico y cadena real de ejemplo | Los planes de los grupos A y B contienen fecha, buscador, cadena, resultados y selección o descarte. La cadena del borrador coincide literalmente con la consulta 2 del grupo B, fechada 2026-11-07, que eligió Friedrich et al. (2017). No se presenta una cadena prevista como búsqueda ejecutada. |
| Lectura completa, copias abiertas y fuentes cerradas locales | Los registros de verificación y las auditorías documentan pasajes del cuerpo y las vías de acceso indicadas. Existen copias locales de ISO/IEC 25010 y de Humble y Farley; se elimina correctamente la antigua exclusividad de ISO como fuente cerrada. La afirmación sobre el canal universal de verificación requiere la precisión del hallazgo 1. No se releen en esta ronda todas las fuentes de las demás secciones. |
| Claude produce, Codex audita; plan aprobado, evidencia literal y sesión independiente | La distribución y los modelos nombrados coinciden con `Workflow.md` y el alcance §5.3. Las skills originales del planificador, redactor y auditor establecen los tres pasos, los controles y la aprobación humana. Esto comprueba el procedimiento documentado; los archivos no certifican por sí solos el modelo efectivo de cada ejecución pasada. La excepción de entrega tras dos rondas se recoge en el hallazgo 2. |
| Errores de fidelidad y cambio de antecedente detectados | La ronda 4 de la auditoría de la Introducción documenta las afirmaciones que excedían la fuente y la ronda 5, su resolución. La ronda 1 del Planteamiento observa la ubicación y el antecedente de E25; la ronda 2 verifica su corrección. La condensación no añade casos ni atribuciones nuevas. |
| Introducción de 882 palabras y 17 citas frente a una reescritura similar con 8 | Conteos reproducidos en `8196213` y `577e43c`: **882/17** y **864/8**, respectivamente. La Introducción disponible al cotejar también conserva **864/8**. Se cuentan apariciones de cita con comentario de IDs, no referencias únicas ni filas de evidencia. La comparación es histórica, acorde con el plan v3. |
| La primera redacción solo podía parafrasear evidencia aprobada | En `8196213`, la skill del redactor exige evidencia auditada antes de redactar y restringe las afirmaciones externas a sus filas. El procedimiento actual reúne investigación y redacción y audita después. El cambio está documentado en Git. |

**Comprobaciones restantes:** las dos citas llevan IDs existentes y autores y años correctos; el formato narrativo de Snyder y el parentético de Walters & Wilder siguen APA 7 y las referencias del documento. No hay fuentes nuevas ni datos externos añadidos sin respaldo. F1 y F2 se conservan citadas, como exige la condensación. Los tres bloques mantienen la función asignada por el plan; objetivos y preguntas están integrados, sin listas ni repeticiones. Hay dos citas en ocho párrafos, promedio de 0,25, compatible con el modo ligero. Los metacomentarios son pertinentes en la Metodología; los comentarios HTML se excluyen del texto visible. No se detectan discrepancias con el glosario. El plan no exige tablas ni figuras para esta sección y el borrador no las introduce.

**Extensión:**

| Bloque | Plan | Borrador |
|---|---|---|
| B1. 4.1 Enfoque metodológico | 150; margen 135–165 | 160; +6,7 % — cumple |
| B2. 4.2 Fuentes y estrategia de búsqueda | 250; margen 225–275 | 265; +6,0 % — cumple |
| B3. 4.3 Uso y validación crítica de la inteligencia artificial | 300; margen 270–330 | 294; −2,0 % — cumple |
| **Total** | **700; margen 630–770** | **719; +2,7 % — cumple** |

Conteo por unidades separadas por espacios del texto visible, incluidas citas autor–año y la cadena de búsqueda; sin título, subtítulos, comentarios HTML ni delimitadores de cursiva o código. Todos los bloques cumplen el margen de ±10 %. No hay espacio de tablas o figuras que cotejar. Solo se escribe este informe; no se aplican las reformulaciones sugeridas.

---

## Ronda 1 — 2026-11-07 — Borrador v1 · Evidencia v1

**Veredicto:** Aprobada | **Citas revisadas:** E1, E2, E3, E4 y E5

Plan auditado: versión 2, modo ligero. Se revisaron las dos citas del borrador, sus cinco filas de evidencia y el texto completo contra la guía, el plan, las referencias y el alcance. Resultado: **ningún hallazgo bloqueante y dos sugerencias**. No existía una auditoría anterior para esta sección. Los párrafos se numeran dentro de cada subsección.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Sugerencia | B3, §4.3, párrafo 2, «El procedimiento separa…» | 8 — Legibilidad | El párrafo reúne la distribución entre modelos, los tres pasos y las condiciones de aprobación e integración. La secuencia se entiende, pero la acumulación dificulta distinguir los pasos de los controles de avance. | Separar después de «de otro proveedor, audita». Abrir otro párrafo con «Cada sección pasa por tres pasos: planificación, redacción y auditoría» y desarrollar allí la secuencia. Dejar las dos condiciones finales juntas: «La aprobación exige que no queden hallazgos bloqueantes. La integración al documento requiere además revisión humana». |
| 2 | Sugerencia | B3, §4.3, párrafo 4, «El procedimiento mismo se corrigió…» | 7 y 9 — Ajuste al plan y selección | La comparación aporta resultados verificables, pero «el argumento quedaba enterrado bajo las fuentes» y «un proceso lento» introducen valoraciones. El plan reserva la reflexión para las Conclusiones y pide describir aquí el procedimiento y sus resultados sin valorarlos. | Conservar la secuencia y las cifras con una formulación descriptiva: «La primera versión reunía y auditaba la evidencia antes de redactar y limitaba la redacción a parafrasear las filas aprobadas. La introducción resultante tenía 882 palabras y 17 citas. La versión actual parte del esquema argumental y registra la evidencia de las afirmaciones que requieren respaldo; con ella, la introducción quedó en 864 palabras y 8 citas». Trasladar la valoración del argumento y de la lentitud a las Conclusiones. |

**Cotejo de las fuentes:**

Se localizaron los cinco pasajes en el cuerpo de los artículos o en una tabla de su desarrollo, no solo en sus resúmenes. Para comparar la literalidad se normalizaron saltos de línea, guiones de partición y caracteres tipográficos de la extracción. La omisión señalada en E4 conserva el orden y el sentido del original.

| Fuente | Filas | Ubicación y resultado |
|---|---|---|
| [F1 — Snyder (2019), versión publicada en la copia de la autora](https://www.researchgate.net/profile/Hannah-Snyder-7/publication/334848557_Literature_review_as_a_research_methodology_An_overview_and_guidelines/links/5d482ec9a6fdcc370a7ccb34/Literature-review-as-a-research-methodology-An-overview-and-guidelines.pdf) | E1–E3 | **Conformes.** E1 y E3 aparecen en §2.1.2, p. 335; E2, en la tabla 1, fila de estrategia de búsqueda y columna semisistemática, p. 334. Las filas y la paráfrasis conservan las condiciones del enfoque y la exigencia de transparencia. |
| [F2 — Walters y Wilder (2023), texto completo del editor disponible en ResearchGate](https://www.researchgate.net/publication/373738246_Fabrication_and_errors_in_the_bibliographic_citations_generated_by_ChatGPT) | E4–E5 | **Conformes.** E4 aparece en Resultados, «Extent of fabrication», p. 4; E5, en Discusión, p. 5. El borrador conserva los denominadores: obras citadas para la fabricación y citas a obras reales para los errores sustantivos. Limita los porcentajes al estudio y no los extrapola a los modelos usados en el proyecto. |

**Acceso y límites del cotejo:** ScienceDirect y el enlace del repositorio NORA no fueron accesibles mediante la herramienta de consulta; Nature redirigió a una página de autenticación técnica. Se cotejó F1 en el PDF publicado alojado en el perfil de la autora y F2 en la transcripción íntegra del texto publicado, que ResearchGate identifica como proporcionado por Springer Nature. Coinciden títulos, autores, DOI y datos de publicación con el plan y las referencias. Para F2 se comprobó la paginación mediante los encabezados de página de esa transcripción; no se afirma haber descargado el PDF de Nature. Las limitaciones de acceso no dejaron pasajes pendientes de verificación.

**Comprobaciones del borrador:**

- **Trazabilidad, fidelidad y formato (1, 3 y 6):** Snyder (2019) remite a E1–E3 y Walters & Wilder (2023), a E4–E5. Los IDs existen, sus fuentes corresponden al plan y los autores y años coinciden con `Referencias.md`. Las citas siguen el formato autor–año y llevan sus comentarios HTML. No se detectaron ampliaciones indebidas de lo que respaldan las filas.
- **Respaldo y fuentes (4 y 5):** las afirmaciones metodológicas externas y los porcentajes tienen cita. Las decisiones del trabajo, el procedimiento con IA y sus resultados son contenido interno, que la guía no obliga a citar como bibliografía externa. La aplicación del enfoque semisistemático al tema se presenta como razonamiento del autor. No hay fuentes marcadas «Nueva»; F1 y F2 ya están en el plan aprobado y en las referencias. Ambas son artículos de revistas académicas, de 2019 y 2023 y en inglés, compatibles con los criterios de §5.3 del alcance.
- **Argumento, selección y contenido interno (7–10):** B1 relaciona los componentes con las preguntas; B2 distingue la búsqueda realizada en las secciones 01 y 02 del registro previsto desde el Marco teórico; B3 describe el control y su evolución. Las cadenas se presentan como previstas, sin atribuirlas a búsquedas ya ejecutadas. Los objetivos y las preguntas se integran en prosa. Hay dos citas en diez párrafos, promedio de 0,2, compatible con el modo ligero; ninguna fuente se repite innecesariamente en un mismo párrafo. Quedan las dos sugerencias de la tabla.
- **Metacomentarios (11):** las referencias a modelos, redacción, evidencia y auditorías corresponden al objeto de la Metodología, donde la guía las permite. Los comentarios HTML de versión y fecha de corte no forman parte de la prosa visible.

**Comprobación de los resultados internos de §4.3:**

| Afirmación del borrador | Comprobación |
|---|---|
| Cuatro afirmaciones observadas en la Introducción, incluida una consecuencia posible presentada como segura | La ronda 4 de `01 Introducción/04 Auditoría.md` registra cuatro bloqueantes. El tercero observa precisamente la sustitución de «puede conducir» por «conduce». La ronda 5 registra su resolución. |
| Interpretación asociada al hallazgo equivocado en el Planteamiento | La ronda 1 de `02 Planteamiento del problema/04 Auditoría.md`, hallazgo 1, registra el cambio de antecedente y la ubicación incorrecta de E25. La ronda 2 comprueba la corrección. |
| Rechazo anterior de una cita tomada únicamente del resumen | En el commit `8196213`, `01 Introducción/04 Auditoría - Evidencia.md`, ronda 1, rechaza E13 por proceder de los Highlights de GAO-14-694. La ronda 2 comprueba su sustitución por pasajes del cuerpo. |
| Quince referencias a la fecha de corte | `Referencias.md` contiene quince entradas. Los planes de 01, 02 y 04 documentan su verificación bibliográfica. Esto comprueba el registro interno de la actividad; esta ronda coteja directamente las dos fuentes de la Metodología, no vuelve a verificar las otras trece. |
| Introducción anterior: 882 palabras y 17 citas; reescritura: 864 palabras y 8 citas | Se reprodujeron los conteos sobre `03 Borrador.md` de la Introducción en los commits `8196213` y `577e43c`, respectivamente. La versión actual conserva el segundo resultado y sus comentarios de trazabilidad. |
| Procedimiento anterior de cinco pasos y actual de tres, con aprobación humana | El historial del procedimiento, el alcance §5.3 y `Investigación/Workflow.md` respaldan la descripción. Los tres ejemplos de descarte de §4.2 constan en los planes de 01 y 02. |

**Extensión:**

| Bloque | Plan | Borrador |
|---|---|---|
| B1. 4.1 Enfoque metodológico | 250; margen 225–275 | 245; −2,0 % — cumple |
| B2. 4.2 Fuentes y estrategia de búsqueda | 400; margen 360–440 | 391; −2,3 % — cumple |
| B3. 4.3 Uso y validación crítica de la inteligencia artificial | 550; margen 495–605 | 499; −9,3 % — cumple |
| **Total** | **1 200; margen 1 080–1 320** | **1 135; −5,4 % — cumple** |

Conteo por unidades separadas por espacios del texto visible, incluidas las citas autor–año y las cadenas de búsqueda; sin título, subtítulos, comentarios HTML ni delimitadores de cursiva o código. Los tres bloques cumplen el margen de ±10 % (criterio 12). B3 está próximo al mínimo: al aplicar las sugerencias conviene conservar al menos 495 palabras mediante la explicación del procedimiento, sin añadir valoraciones.

Solo se escribe este informe. No se corrigen el borrador, la evidencia, el plan ni las referencias.
