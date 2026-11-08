# Auditoría — 05 Marco teórico / C Proceso y práctica (5.5–5.7)

## Ronda 3 — 2026-11-07 — Borrador v3 · Evidencia v3

**Veredicto:** Aprobada | **Citas revisadas:** E7, E9, E20, E21 y E31. Trazabilidad comprobada para E1–E31.

Se revisaron el hallazgo bloqueante 1 y las sugerencias 3 y 4 pendientes de la ronda 2, las modificaciones del borrador v3 y de la evidencia v3, y su ajuste al plan v2, la guía de redacción, el glosario y las referencias. Se cotejó la nueva E31 con el cuerpo de F2 y se consultaron nuevamente el pasaje de E7 y las definiciones de F5. Para las transcripciones sin cambios se conserva el cotejo aprobado en las rondas anteriores, conforme a la skill. Resultado: **ningún hallazgo bloqueante ni sugerencia pendiente**.

**Seguimiento de la ronda 2:**

| Hallazgo anterior | Estado | Comprobación |
|---|---|---|
| 1. Bloqueante: atribución del umbral de prueba a F5 | Resuelto | En B6, la oración con E20–E21 termina después de las definiciones de SLO y SLI. La siguiente, «Si existe un SLO, es un buen punto de partida para el umbral», queda fuera de esa cita y funciona como conexión propia y condicional. No presenta la aplicación a CI como afirmación de Jones et al. ni como origen obligatorio del umbral; es compatible con la alternativa de B3 cuando faltan requisitos. |
| 3. Sugerencia: alcance de «pruebas de capacidad» en F2 | Resuelta | B2 aclara una sola vez que Humble y Farley llaman así a un conjunto más amplio que el tipo de 5.4. E31 respalda la aclaración, y E7 sigue respaldando la limitación del hardware reducido. B7 puede aplicar los pasajes de F2 sin repetirla. |
| 4. Sugerencia: «criterio de aceptación» | Resuelta | B3 y B5 usan la forma obligatoria del glosario. La afirmación de E9 también la adopta y conserva intacta la transcripción original en inglés. |

La sugerencia 2, ya resuelta en la ronda 2, permanece corregida: B4 conserva la conclusión explícita sobre separar el estado inicial del estable y justificar cuándo empieza la medición.

**Cotejo de los cambios:**

| Fuente y filas | Ubicación consultada | Resultado |
|---|---|---|
| F2 — Humble y Farley (2010): E31 | Copia local indicada por el plan, cap. 9, «Measuring Capacity», p. 231 impresa; marcador de la copia: página PDF 265, etiqueta 231 | El enunciado introductorio y los cuatro rótulos transcritos aparecen literalmente en el cuerpo. Se presentan como fragmentos separados, sin ocultar su procedencia. La enumeración de escalabilidad, longevidad, *throughput* y carga respalda el alcance amplio de la afirmación y su aplicación en B2. La comparación con el tipo específico de 5.4 es una conexión del texto, coherente con esa subsección y con la nota terminológica del plan. |
| F2: E7 | Cap. 9, «The Capacity-Testing Environment», p. 236 impresa | Se mantiene la distinción entre revelar problemas graves en hardware de menor capacidad y demostrar el cumplimiento de los objetivos. La cita narrativa ampliada de B2 remite a E31 y E7 y no excede su respaldo conjunto. |
| F4 — Jiang y Hassan (2015): E9 | Fila de evidencia y B3; cotejo de la transcripción de §2.1.1, p. 1092, conservado de la ronda 1 | El cambio es terminológico: «criterio de aceptación» mantiene el sentido de *pass/fail criteria*. No modifica el principio comparativo ni requiere una transcripción nueva. |
| [F5 — Jones et al. (2016)](https://sre.google/sre-book/service-level-objectives/): E20–E21 | «Objectives» e «Indicators» | Ambas transcripciones aparecen literalmente en el cuerpo. La nueva oración de B6 conserva las definiciones y la cita termina antes de la aplicación al umbral. La conexión posterior es razonamiento propio permitido por la guía y previsto expresamente por el plan. |

**Controles generales:** las dieciocho citas remiten a filas existentes y los treinta y un IDs se emplean una vez cada uno. Se mantienen las correspondencias autor–año y el formato APA 7. E31 pertenece a F2, ya incluida en `Referencias.md`; no incorpora una fuente nueva. Se conserva la admisibilidad de F5 comprobada en la ronda 1. No se identificaron datos externos sin respaldo ni excesos de atribución en los cambios revisados.

Los siete bloques mantienen las ideas del plan. La aclaración de B2 está integrada en la argumentación, y B6 distingue las definiciones de la propuesta del autor sin perder continuidad. Se cumple la densidad del modo completo: entre una y tres citas por párrafo, sin reiterar una fuente dentro del mismo párrafo y con un máximo de una cita narrativa. No hay listas internas copiadas ni metacomentarios visibles; los comentarios HTML de control permanecen ocultos. Los términos corregidos siguen el glosario y la observabilidad conserva su tratamiento breve.

**Extensión:**

| Bloque | Plan v2 | Borrador v3 |
|---|---|---|
| B1. Actividades del proceso | 150; margen 135–165 | 165; +10,0 % — cumple, en el límite superior |
| B2. Entorno y datos | 110; margen 99–121 | 120; +9,1 % — cumple |
| B3. Línea base y repetibilidad | 130; margen 117–143 | 142; +9,2 % — cumple |
| B4. Realismo de la ejecución | 120; margen 108–132 | 131; +9,2 % — cumple |
| B5. Antipatrones | 100; margen 90–110 | 105; +5,0 % — cumple |
| B6. Umbrales y regresiones | 140; margen 126–154 | 153; +9,3 % — cumple |
| B7. Frecuencia, etapa y observabilidad | 120; margen 108–132 | 131; +9,2 % — cumple |
| **5.5, B1–B2** | **260; margen 234–286** | **285; +9,6 % — cumple** |
| **5.6, B3–B5** | **350; margen 315–385** | **378; +8,0 % — cumple** |
| **5.7, B6–B7** | **260; margen 234–286** | **284; +9,2 % — cumple** |
| **Total** | **870; margen 783–957** | **947; +8,9 % — cumple** |

Conteo recalculado por unidades separadas por espacios de la prosa visible, incluidas las citas autor–año y excluidos títulos, subtítulos y comentarios HTML. No se trasladaron los conteos de la ronda anterior.

**Tablas y figuras:** el plan no solicita ni reserva espacio para estos elementos y el borrador no los incorpora. No hay omisiones ni exceso por este concepto. La ocupación de las 2,5 páginas queda sujeta a la maquetación.

## Ronda 2 — 2026-11-07 — Borrador v2 · Evidencia v2

**Veredicto:** No aprobada | **Citas revisadas:** E1, E2, E7, E14, E15, E20, E21 y E30. Trazabilidad comprobada para E1–E30.

Se revisaron los cuatro hallazgos de la ronda 1, las modificaciones presentes en el borrador v2 y la evidencia v2, y su ajuste al plan v2, la guía, el glosario y las referencias. Se cotejó E30 con el cuerpo de F1 y se volvieron a consultar los pasajes de F2 y F5 relacionados con las correcciones. Para las citas sin cambios se conserva el cotejo aprobado en la ronda 1, según la skill. Resultado: **un hallazgo bloqueante y dos sugerencias pendientes**. Los números siguientes conservan la correspondencia con la ronda anterior.

La sugerencia **2 queda resuelta**: B4 reemplaza «Lo mismo vale para sistemas con cachés o conexiones…» por «Por eso conviene separar el estado inicial del estable (5.4) y justificar cuándo empieza a medirse». La conclusión propia es clara y no extiende a otros sistemas los varios minutos de calentamiento que la fuente describe para plataformas con optimización en tiempo de ejecución.

El encabezado del borrador declara aplicadas las sugerencias 2–4, pero el texto visible conserva las dos omisiones señaladas en 3 y 4. El veredicto se basa en el contenido de los archivos leídos.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante | 5.7, B6, segunda oración: «El umbral puede fijarse a partir de un objetivo de nivel de servicio…», E20–E21 | 3. Fidelidad; 4. Respaldo | **Parcialmente corregido.** «Puede» elimina el origen necesario que se objetó en la ronda 1 y permite la alternativa de B3. Sin embargo, la cita de Jones et al. sigue cerrando una oración que incluye la derivación del umbral de prueba desde un SLO. E20–E21 respaldan las definiciones, no esa aplicación a las pruebas en CI. Falta distinguir la conexión propia de la afirmación atribuida, como exige la nota sobre SLO del plan. | Separar las definiciones de la propuesta, sin agregar otra fuente: «Un objetivo de nivel de servicio (SLO) fija un valor o rango objetivo medido por un indicador de nivel de servicio (SLI), una medida cuantitativa de algún aspecto del nivel de servicio (Jones et al., 2016)», con el comentario E20–E21. Después: «Cuando exista un SLO, proponemos usarlo para orientar el umbral de la prueba». Recortar el resto de B6 para conservar su presupuesto. |
| 3 | Sugerencia | 5.5, B2, primera cita de Humble y Farley; aplicación posterior en 5.7, B7 | 7. Argumento; 13. Terminología | **Pendiente.** No aparece la aclaración solicitada sobre el uso de «pruebas de capacidad» en F2. El borrador aplica sus pasajes a las pruebas de rendimiento sin explicar una vez la relación con ese vocabulario ni distinguirlo del tipo específico de 5.4. | Integrar al introducir F2: «Humble y Farley usan “pruebas de capacidad” para un conjunto más amplio que el tipo específico de 5.4». Recortar B2 al incorporarlo: actualmente tiene 115 palabras y su límite es 121. No hace falta repetir la aclaración en B7. |
| 4 | Sugerencia | 5.6, B3, primer párrafo; B5, última oración; afirmación de E9 | 13. Terminología | **Pendiente.** Siguen presentes «el criterio de aprobación suele derivarse…» y «la medición sin criterio de aprobación…». Para ese concepto, la forma obligatoria del glosario es «criterio de aceptación». E9 mantiene también la denominación anterior en su paráfrasis. | Sustituir por «el criterio de aceptación suele derivarse…» y «la medición sin criterio de aceptación…». Armonizar la afirmación de E9, manteniendo intacta su transcripción original en inglés. |

**Cotejo de los cambios y seguimiento:**

| Fuente y filas | Ubicación consultada | Resultado |
|---|---|---|
| [F1 — ISTQB (2018)](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf): E30; contexto de E1–E2 | §3.1, «Test Monitoring and Control», p. 24 impresa; contexto de las actividades, pp. 23–25 | Los dos fragmentos de E30 aparecen literalmente en el cuerpo, en el apartado y la página indicados. La paráfrasis sobre acciones ante desvíos y evaluación de criterios de salida es fiel. La cita de B1 incluye el nuevo ID junto con E1 y E2, con autor y año correctos. La incorporación no introduce un bloqueante. |
| F2 — Humble y Farley (2010): E7, E14–E15 | Copia local indicada por el plan, cap. 9: pp. 236, 245 y 244 impresas, respectivamente | Los pasajes conservan el alcance aprobado en la ronda 1. B4 mantiene la restricción del calentamiento a las plataformas pertinentes; su nueva conclusión es razonamiento propio permitido. El libro conserva su vocabulario de pruebas de capacidad; la aclaración pedida por el plan todavía falta en B2. |
| [F5 — Jones et al. (2016)](https://sre.google/sre-book/service-level-objectives/): E20–E21 | «Objectives» e «Indicators» | Las dos transcripciones siguen siendo literales y las definiciones del borrador son fieles. El problema restante es el alcance de la oración citada, que añade la aplicación al umbral de prueba. No se requiere modificar las transcripciones de la evidencia. |

**Controles generales:** las dieciocho citas remiten a filas existentes y los treinta IDs se emplean una vez cada uno. E30 usa F1; no hay fuentes nuevas respecto de la ronda 1. Se mantienen la correspondencia autor–año, las cinco entradas bibliográficas y la admisibilidad ya comprobada de F5. No se detectaron otros datos externos sin respaldo ni otros excesos de atribución en las modificaciones revisadas.

Los siete bloques mantienen sus ideas centrales y la densidad del modo completo: entre una y tres citas por párrafo, sin reiterar una fuente dentro del mismo párrafo y con un máximo de una cita narrativa. Las conexiones con el taller y la justificación del margen según la variación medida siguen siendo razonamiento propio permitido. No hay listas internas copiadas ni metacomentarios visibles; los comentarios HTML de control permanecen ocultos. La observabilidad conserva su tratamiento breve. Las cuestiones terminológicas pendientes se limitan a las sugerencias registradas.

**Extensión:**

| Bloque | Plan v2 | Borrador v2 |
|---|---|---|
| B1. Actividades del proceso | 150; margen 135–165 | 165; +10,0 % — cumple, en el límite superior |
| B2. Entorno y datos | 110; margen 99–121 | 115; +4,5 % — cumple |
| B3. Línea base y repetibilidad | 130; margen 117–143 | 142; +9,2 % — cumple |
| B4. Realismo de la ejecución | 120; margen 108–132 | 131; +9,2 % — cumple |
| B5. Antipatrones | 100; margen 90–110 | 105; +5,0 % — cumple |
| B6. Umbrales y regresiones | 140; margen 126–154 | 150; +7,1 % — cumple |
| B7. Frecuencia, etapa y observabilidad | 120; margen 108–132 | 131; +9,2 % — cumple |
| **5.5, B1–B2** | **260; margen 234–286** | **280; +7,7 % — cumple** |
| **5.6, B3–B5** | **350; margen 315–385** | **378; +8,0 % — cumple** |
| **5.7, B6–B7** | **260; margen 234–286** | **281; +8,1 % — cumple** |
| **Total** | **870; margen 783–957** | **939; +7,9 % — cumple** |

Conteo de la versión actual por unidades separadas por espacios de la prosa visible, incluidas las citas autor–año y excluidos títulos, subtítulos y comentarios HTML. Se recalcularon todos los bloques; no se trasladaron los conteos de la ronda 1. Las correcciones propuestas requieren recortes en los bloques donde agreguen palabras.

**Tablas y figuras:** el plan no solicita ni reserva espacio para estos elementos y el borrador no los incorpora. No hay omisiones ni exceso por este concepto. La ocupación de las 2,5 páginas queda sujeta a la maquetación.

## Ronda 1 — 2026-11-07 — Borrador v1 · Evidencia v1

**Veredicto:** No aprobada | **Citas revisadas:** E1–E29.

Se revisaron el plan v2 aprobado, el borrador v1 y la evidencia v1 completos, la guía de redacción, el glosario, las referencias y los criterios de fuentes de `Alcance.md` §5.3. Se cotejaron todas las transcripciones con el cuerpo de las cinco fuentes y con sus ubicaciones. F2 se consultó en la copia local indicada por el plan, con su paginación impresa. Resultado: **un hallazgo bloqueante y tres sugerencias**. El bloqueante afecta la atribución de una oración del borrador; las definiciones registradas en E20 y E21 son correctas.

**Identificación de los insumos auditados:** SHA-256 del borrador v1: `a44d0066712a8fcae779493eb89d79c46db2235c8929ce177851c604abb9c92e`; SHA-256 de la evidencia v1: `6e0ba23b2ae0bcea84bd092c5f83015f3f1d325b6cd12641b658323222b7cc62`. Durante la comprobación final, ambos archivos fueron reemplazados concurrentemente por versiones 2. Esta ronda conserva la revisión de las versiones 1 solicitada; no emite un veredicto sobre las versiones 2 ni abre una segunda ronda.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante | 5.7, B6, segunda oración: «Su origen es un objetivo de nivel de servicio…», cita E20–E21 | 3. Fidelidad; 4. Respaldo | La cita de Jones et al. queda al final de una oración que presenta al SLO como origen necesario del umbral de una prueba. E20 y E21 solo respaldan las definiciones de SLO y SLI. El capítulo no establece esa regla para pruebas en CI. El plan v2 exige presentar esa derivación como conexión del autor; además, B3 ya contempla criterios derivados de una línea base cuando faltan requisitos. | Separar las definiciones citadas de la aplicación propuesta y evitar el carácter universal. Por ejemplo: «Un SLO fija un valor o rango objetivo para el nivel de servicio medido por un SLI, una medida cuantitativa de ese nivel (Jones et al., 2016)», con E20–E21. Después, como razonamiento propio: «Cuando exista un SLO, proponemos usarlo para orientar el umbral de la prueba en CI». No hace falta cambiar las transcripciones de E20–E21. |
| 2 | Sugerencia | 5.6, B4, última oración: «Lo mismo vale para sistemas con cachés o conexiones…» | 8. Legibilidad | El antecedente de «lo mismo» es ambiguo: entre el calentamiento y esta oración se intercala la comprobación contra un *stub*. Puede entenderse que la conclusión extiende esa comprobación o que extiende el calentamiento de varios minutos. La conexión propia está permitida por el plan; conviene precisar qué se deduce, sin trasladar una duración fija a otros sistemas. | Sustituir por una inferencia condicional explícita: «Por el mismo criterio, si el inicio incluye llenar cachés o abrir conexiones, conviene separar ese estado transitorio de la medición estable (5.4)». Puede moverse junto a la oración sobre calentamiento. |
| 3 | Sugerencia | 5.5, B2, y 5.7, B7: uso de Humble y Farley para las pruebas de rendimiento | 7. Argumento; 13. Terminología | Las paráfrasis de F2 son aplicables, pero falta la aclaración que pide el plan sobre el alcance de sus «pruebas de capacidad». Sin ella, la transición desde la clasificación de 5.4 deja implícita una diferencia terminológica relevante. | Aclararlo una sola vez, al introducir F2: «Humble y Farley agrupan estas pruebas de rendimiento como pruebas de capacidad; ese uso es más amplio que el tipo específico de 5.4». Integrar la precisión mediante recorte de la prosa existente para conservar el presupuesto. |
| 4 | Sugerencia | 5.6, B3 y B5: «criterio de aprobación» | 13. Terminología | Para el criterio que determina si una prueba se acepta, el glosario prescribe «criterio de aceptación». El borrador usa otra denominación para el mismo concepto. | Usar «criterio de aceptación» en «el criterio de aprobación suele derivarse…» y «la medición sin criterio de aprobación…». Se pueden conservar «aprobar» y «fallar» como verbos al explicar el resultado. |

**Cotejo de fuentes y evidencia:**

| Fuente y filas | Ubicación cotejada | Resultado |
|---|---|---|
| [F1 — ISTQB (2018)](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf): E1–E4 | §3.1, pp. 23–25; §4.2.3, p. 40; §4.1.2, «Profiles», p. 35 | Transcripciones y ubicaciones correctas. Las paráfrasis del proceso, la iteración y los perfiles se mantienen dentro de la evidencia. |
| F1: E5, E6, E8, E12, E13 y E16 | §4.2.8, pp. 48–49; §4.1.2, «Acceptance Criteria», p. 34; §2.1.1, p. 17 | Literalidad y fidelidad comprobadas para entorno, datos, línea base, generadores y selección previa de métricas. |
| F1: E26 y E29 | §3.4, pp. 30–31 | El subconjunto de pruebas en CI y el monitoreo tras la entrega están respaldados en el cuerpo. |
| F2 — Humble y Farley (2010): E7, E10, E17, E19, E22 y E23 | Cap. 9: E7, p. 236; E10, E22 y E23, p. 233; E17, pp. 227–228; E19, p. 232 | Coinciden con la copia local `Adjuntos/Local/Continuous-Delivery - Jez Humble & David Farley/Continuous-Delivery - Jez Humble & David Farley.md`. E17 atraviesa el salto entre las páginas impresas 227 y 228; no es una alteración del texto. |
| F2: E14, E15, E18, E27 y E28 | Cap. 9: pp. 245, 244, 245, 245 y 246, respectivamente | Transcripciones y ubicaciones correctas. La evidencia de calentamiento está limitada a tecnologías con optimización en tiempo de ejecución. La etapa separada y la intervención manual conservan el carácter condicionado al proyecto que les da la fuente. |
| [F3 — Daly et al. (2020)](https://research.spec.org/icpe_proceedings/2020/proceedings/p67.pdf): E11, E24 y E25 | §1, p. 67; §1.1, p. 68; §8, p. 75 | Las cifras, el problema de los umbrales estáticos y la reducción de falsos positivos aparecen en el cuerpo. La elisión de E11 es identificable y no cambia el sentido. El borrador presenta los resultados como un caso industrial, sin convertirlos en valores generales. |
| [F4 — Jiang y Hassan (2015)](https://www.eecs.yorku.ca/~zmjiang/publications/tse2015_jiang.pdf): E9 | §2.1.1, p. 1092 | Se comprobó directamente la página de la copia del autor. La transcripción y la paráfrasis del principio comparativo son fieles. |
| [F5 — Jones et al. (2016)](https://sre.google/sre-book/service-level-objectives/): E20 y E21 | «Objectives» e «Indicators» | Ambas definiciones son literales y están en el cuerpo. El exceso está en su aplicación dentro de B6, señalado en el hallazgo 1. |

Los cotejos respetan los saltos de página y línea y las variantes tipográficas de comillas, apóstrofos y ligaduras de las copias. No se detectaron citas inventadas, ubicaciones erróneas ni transcripciones limitadas al resumen.

**Admisibilidad y referencias:** F5 es la única fuente marcada como nueva en el plan. Es un capítulo de autoría identificada publicado en el sitio oficial de Google SRE y está incorporado en `Referencias.md`. El capítulo identifica a Jones, Wilkes, Murphy y Smith; el [prefacio](https://sre.google/sre-book/preface/) confirma los editores, O'Reilly y 2016. Cumple el criterio de documentación oficial y la admisión prevista en el plan. Las otras cuatro fuentes también constan en las referencias; no se introdujeron fuentes adicionales.

**Controles generales:** las dieciocho citas del borrador remiten a filas existentes; E1–E29 se usan una vez cada una en los comentarios de esas citas. Las correspondencias autor–año y el formato APA 7 son correctos. No se identificaron otros excesos de atribución ni datos externos sin respaldo. La remisión al promedio en 5.3 recupera contenido ya desarrollado; las conexiones con el taller y la justificación del margen mediante la variación medida son razonamiento propio permitido por la guía. La conexión sobre cachés se trata como sugerencia de claridad, no como un segundo bloqueante.

Los siete bloques desarrollan las ideas asignadas por el plan, con una a tres citas por párrafo y sin repetir una misma fuente en un párrafo. Hay como máximo una cita narrativa por párrafo. El alcance y la relación con el taller están integrados, sin listas de objetivos copiadas ni detalles de implementación de la Fase 2. No hay metacomentarios visibles: los comentarios HTML de versiones, bloques e IDs son controles ocultos admitidos por la guía. La observabilidad se mantiene como mención breve. Las precisiones terminológicas pendientes se recogen en las sugerencias 3 y 4.

**Extensión:**

| Bloque | Plan v2 | Borrador v1 |
|---|---|---|
| B1. Actividades del proceso | 150; margen 135–165 | 161; +7,3 % — cumple |
| B2. Entorno y datos | 110; margen 99–121 | 115; +4,5 % — cumple |
| B3. Línea base y repetibilidad | 130; margen 117–143 | 142; +9,2 % — cumple |
| B4. Realismo de la ejecución | 120; margen 108–132 | 129; +7,5 % — cumple |
| B5. Antipatrones | 100; margen 90–110 | 105; +5,0 % — cumple |
| B6. Umbrales y regresiones | 140; margen 126–154 | 152; +8,6 % — cumple |
| B7. Frecuencia, etapa y observabilidad | 120; margen 108–132 | 130; +8,3 % — cumple |
| **5.5, B1–B2** | **260; margen 234–286** | **276; +6,2 % — cumple** |
| **5.6, B3–B5** | **350; margen 315–385** | **376; +7,4 % — cumple** |
| **5.7, B6–B7** | **260; margen 234–286** | **282; +8,5 % — cumple** |
| **Total** | **870; margen 783–957** | **934; +7,4 % — cumple** |

Conteo por unidades separadas por espacios de la prosa visible, incluidas las citas autor–año. Se excluyen títulos, subtítulos y comentarios HTML. Todos los bloques y las tres subsecciones caben en su margen de ±10 %. Las reformulaciones propuestas deberán acompañarse de recortes cuando sea necesario para conservarlo.

**Tablas y figuras:** el plan no reserva espacio ni solicita estos elementos; el borrador no contiene ninguno. No hay omisiones ni exceso de espacio por este concepto. La ocupación final de las 2,5 páginas se comprobará al maquetar.
