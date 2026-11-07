# Auditoría — 05 Marco teórico / B Conceptos y tipos (5.3–5.4)

## Ronda 3 — 2026-11-07 — Borrador v3 · Evidencia v2

**Veredicto:** Aprobada | **Citas revisadas:** E3, E19 y E20, por los cambios en B1 y B5. Trazabilidad y formato comprobados en E1–E30; las demás citas conservan el cotejo favorable de las rondas anteriores.

Se revisaron el plan v3 aprobado, el borrador v3, la evidencia v2, las rondas anteriores, la guía de redacción, el glosario y las referencias. La evidencia conserva su versión 2. La revisión se concentró en los tres hallazgos de la ronda 2 y en los pasajes modificados, con una lectura general del borrador para comprobar respaldo, coherencia y extensión. Resultado: **ningún hallazgo bloqueante ni sugerencia nueva**.

**Seguimiento de la ronda 2:**

| Hallazgo anterior | Estado en v3 | Resultado de la revisión |
|---|---|---|
| 1. Bloqueante: definición de tasa de error sin respaldo en E3 | Resuelto | B1 elimina la definición como proporción. La oración sobre transacción fallida y su efecto sobre el *throughput* se mantiene dentro de lo que acredita E3. La corrección se logra retirando la atribución excedente; no requiere ampliar la evidencia. |
| 2. Sugerencia: duplicación de objetivos entre B5 y la Tabla 2 | Atendida | El contraste definitorio se sustituye por la relación entre pregunta, comportamiento observado y diseño. Se conserva el ejemplo de las fugas de memoria con E20, como proponía la ronda 2; las definiciones comparadas quedan en la tabla. |
| 3. Sugerencia: afirmaciones universales sobre duración y estrés | Atendida | «Una duración insuficiente puede ocultarlos» expresa una posibilidad, sin deducir que ninguna fuga sea visible en una prueba breve. El razonamiento sobre estrés contempla tanto más carga como menos recursos y ya no exige superar siempre la carga prevista. |

La recomendación pedagógica sobre la tasa de error, de la ronda 1, sigue siendo opcional: v3 la menciona, pero no explica su cálculo. Esto no reabre el bloqueante resuelto; si se desarrolla después, la definición deberá contar con evidencia específica.

**Cotejo de los pasajes afectados:**

| Fuente y filas | Ubicación cotejada | Resultado |
|---|---|---|
| [F1 — ISTQB (2018)](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf): E3 | §4.4, p. 52 impresa | La transcripción y su elisión coinciden con el cuerpo. La paráfrasis revisada de B1 es fiel; no atribuye al pasaje una tasa ni un denominador. |
| F1: E19 y E20 | §1.2, p. 12 impresa | Las transcripciones conservan literalidad y ubicación. El ejemplo citado de B5 está respaldado. El razonamiento posterior es propio y compatible con las definiciones; no introduce una duración normativa ni un resultado empírico. E19 sigue citada en la Tabla 2, aunque ya no aparece en la cita del primer párrafo de B5. |

No se volvieron a cotejar las transcripciones sin cambios ya aprobadas, conforme al criterio de rondas de la skill. No hay fuentes nuevas; se mantienen la admisibilidad y las referencias verificadas anteriormente, así como el cierre bibliográfico de F4 registrado en la ronda 2.

**Controles generales:** los treinta IDs existen y se usan, incluidas las notas de tabla y figura; las correspondencias autor–año y el formato APA 7 se mantienen. No se detectaron datos externos nuevos sin respaldo ni excesos de atribución en los cambios. Los seis bloques conservan el argumento del plan y la terminología del glosario. Los ejemplos condicionales y las conexiones del autor siguen identificables como razonamiento propio. No hay metacomentarios visibles; los comentarios HTML son controles ocultos admitidos por la guía.

La Figura 2 y la Tabla 2 mantienen número, título, mención previa y origen trazable. La descripción oculta de la figura cumple el formato previsto para el borrador. La nota de la tabla distingue las definiciones y los modos de falla citados de la síntesis propia de perfiles, duraciones y asignación de fallas.

**Extensión:**

| Bloque | Plan v3 | Borrador v3 |
|---|---|---|
| B1. Métricas básicas | 160; margen 144–176 | 175; +9,4 % — cumple |
| B2. Percentiles frente al promedio | 110; margen 99–121 | 104; −5,5 % — cumple |
| B3. Ley de Little y modelos de carga | 170; margen 153–187 | 186; +9,4 % — cumple |
| B4. *Coordinated omission* | 110; margen 99–121 | 118; +7,3 % — cumple |
| B5. Tipos principales | 200; margen 180–220 | 205; +2,5 % — cumple |
| B6. Variantes | 100; margen 90–110 | 108; +8,0 % — cumple |
| **5.3, B1–B4** | **550; margen 495–605** | **583; +6,0 % — cumple** |
| **5.4, B5–B6** | **300; margen 270–330** | **313; +4,3 % — cumple** |
| **Total** | **850; margen 765–935** | **896; +5,4 % — cumple** |

Conteo por unidades separadas por espacios de la prosa visible, incluidas las citas autor–año. Se excluyen títulos, subtítulos, comentarios HTML, la tabla y los títulos y notas de tabla y figura, con el criterio declarado en las rondas anteriores.

**Espacio de tabla y figura:** el plan reserva 0,4 páginas para la Figura 2 y 0,6 para la Tabla 2. Ninguno de los dos elementos cambió respecto de la ronda 2. Sin maquetación no puede confirmarse que quepan ni declararse un exceso; la comprobación de espacio y legibilidad queda para la integración y no afecta este veredicto.

## Ronda 2 — 2026-11-07 — Borrador v2 · Evidencia v2

**Veredicto:** No aprobada | **Citas revisadas:** E3 y E5, ampliadas en la evidencia; E8, E12–E15 y E19–E20, por las reformulaciones del borrador y de la Figura 2. Trazabilidad y formato comprobados en E1–E30.

Se revisaron la ronda 1, el plan v3 aprobado, el borrador v2 y la evidencia v2 completos, la guía de redacción, el glosario y las referencias. Se cotejaron con las fuentes los pasajes afectados; las citas sin cambios conservan el cotejo favorable de la ronda 1, como permite la skill. No hay fuentes nuevas respecto de esa ronda. Resultado: **un hallazgo bloqueante y dos sugerencias de prosa**. El bloqueante corresponde a una definición incorporada en v2; no revoca el cotejo favorable de las transcripciones anteriores.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante | B1, primer párrafo: «la tasa de error, la proporción de transacciones que no se completaron»; E3 | 3–4 — Fidelidad y respaldo | E3 ampliada define la transacción fallida y su efecto sobre el *throughput*, pero no define una tasa ni una proporción. La oración añade esa definición bajo la cita de ISTQB sin una fila que la respalde. No se cuestiona que pueda adoptarse esa métrica, sino la atribución al pasaje registrado. | Incorporar evidencia que defina explícitamente la proporción y su denominador. Con ese respaldo, precisar: «La tasa de error es la proporción de transacciones fallidas respecto del total de transacciones ejecutadas durante la prueba», ajustando la formulación a lo que efectivamente establezca la fuente. Mantener E3 para el significado de transacción fallida y su efecto sobre el *throughput*; no extenderle por sí sola la definición de la tasa. |
| 2 | Sugerencia | B5, primer párrafo, segunda y tercera oraciones; Tabla 2 | 9, 14 — Selección y duplicación | La sugerencia 4 de la ronda 1 se atendió parcialmente: se amplió la relación entre pregunta y diseño, pero aún se explican los objetivos de carga y resistencia que recoge la tabla. El plan reserva las definiciones a ese elemento. | Sustituir el contraste por «Un mismo escenario puede responder preguntas distintas. La pregunta determina qué comportamiento se necesita observar y, por tanto, cómo se diseña la prueba». Conservar el ejemplo de las fugas de memoria y su cita, y dejar las definiciones comparadas en la Tabla 2. |
| 3 | Sugerencia | B5, primer párrafo, oración nueva: «una prueba de resistencia tan breve como una de carga no deja ver una fuga, y una de estrés que no supera la carga prevista no revela el límite» | 7–8 — Argumento y precisión | El razonamiento propio se formula como una imposibilidad universal: la duración relativa no basta para concluir que ninguna fuga será visible. Además, la condición sobre estrés no contempla la reducción de recursos que sí recoge la propia Tabla 2 con E19. Es una conclusión del autor que conviene acotar, no un resultado atribuido a la fuente. | Reformular como «Una duración insuficiente puede ocultar problemas acumulativos; para explorar los límites, el escenario de estrés debe acercarse a ellos mediante la carga o la reducción de recursos». Mantenerlo como razonamiento propio, sin presentarlo como una transcripción o un hallazgo empírico. |

**Seguimiento de las sugerencias de la ronda 1:**

| Sugerencia anterior | Estado en v2 | Resultado de la revisión |
|---|---|---|
| 1. Definir tasa de error y concurrencia | Parcialmente atendida | La concurrencia queda explícita y E5 ampliada la respalda. Para la tasa se añadió una definición, pero E3 no acredita el cociente: hallazgo 1 de esta ronda. La omisión de desarrollo de v1 era una sugerencia; la atribución sin respaldo introducida en v2 es bloqueante. |
| 2. Explicar p95 y p99 sobre mediciones | Atendida | El argumento se refiere ahora a tiempos de respuesta y solicitudes. «Un sistema puede…» presenta una posibilidad ilustrativa, no un dato observado. Los percentiles altos siguen siendo una extensión razonada del autor, sin atribuirlos a E8. |
| 3. Precisar el ciclo por usuario virtual | Atendida en lo sustantivo | B3 y la descripción de la Figura 2 explicitan que el ciclo corresponde a cada usuario. La oración de cierre introduce «modelo de carga cerrado» y remite de forma inequívoca al abierto. |
| 4. Evitar duplicación con la Tabla 2 | Parcialmente atendida | Se agregó la conexión con el diseño, pero permanece parte del contraste definitorio. Continúa como sugerencia: hallazgo 2. La oración añadida motiva también el hallazgo 3. |

**Cotejo de las citas afectadas:**

| Fuente y filas | Ubicación cotejada | Resultado |
|---|---|---|
| [F1 — ISTQB (2018)](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf): E3 | §4.4, p. 52 impresa | La ampliación es literal y está en el cuerpo. La elisión no altera el sentido. La afirmación de la fila es fiel; el exceso está en la definición añadida al borrador, señalada en el hallazgo 1. |
| F1: E5 | §4.2.5, apartado «Concurrency», p. 44 impresa | Transcripción y ubicación conformes; respalda la reformulación de B1. La repetición inicial de «Concurrency» corresponde al encabezado seguido de la primera palabra del párrafo. |
| F1: E8 y E15 | §4.4, p. 52; §4.2.5, p. 45 impresas | Se conserva la fidelidad de las paráfrasis y se distingue el razonamiento propio posterior. |
| [F3 — Schroeder et al. (2006)](https://www.usenix.org/legacy/events/nsdi06/tech/full_papers/schroeder/schroeder.pdf): E12–E14 | §1, p. 239; figura 1, p. 240 impresas | La precisión por usuario de B3 y de la figura conserva el mecanismo descrito. Se mantiene el alcance histórico de «generadores […] revisados»; no se afirma su predominio actual. |
| F1: E19–E20 | §1.2, p. 12 impresa | El contraste citado y el ejemplo conservan su respaldo. Las reservas sobre su desarrollo posterior se registran como sugerencias 2 y 3. |

**F4 — cierre de la nota bibliográfica de la ronda 1:** se mantienen **215–226**, conforme a la aclaración del usuario. Se corroboraron directamente en la [API de la Biblioteca Digital de la GI](https://dl.gi.de/server/api/core/items/780bef9a-d6df-4776-80e3-e85ae0158e63) los campos `gi.citation.startPage = 215` y `gi.citation.endPage = 226`, junto con el título y el año. El lector web devolvió 403 para la ficha; la consulta directa de los metadatos sí respondió. **Queda sin efecto la recomendación anterior de cambiar el intervalo a 215–225.** La extensión física de una copia y las páginas bibliográficas del registro son datos distintos; la aclaración no modifica los localizadores de E16–E18, ya aprobados. No se requiere cambiar el plan, las referencias ni la evidencia por esta nota.

**Controles generales:** los treinta IDs existen en la evidencia y siguen usados en el borrador, incluidas las notas de tabla y figura. Se mantienen las correspondencias autor–año y el formato APA 7 establecido en las referencias. No se detectaron otros excesos de atribución en los cambios revisados. Las fuentes y su admisibilidad permanecen como se aprobaron en la ronda 1. Los seis bloques conservan su función argumental y el vocabulario es consistente en lo sustantivo con el glosario. No hay metacomentarios visibles; los comentarios HTML de versión, evidencia y figura son controles ocultos admitidos por la guía.

La Figura 2 y la Tabla 2 conservan número, título, mención previa y origen trazable. La figura sigue descrita en el comentario previsto para el borrador; no corresponde exigir aquí su dibujo final. Las notas de la tabla distinguen el contenido externo de la síntesis propia.

**Extensión:**

| Bloque | Plan v3 | Borrador v2 |
|---|---|---|
| B1. Métricas básicas | 160; margen 144–176 | 174; +8,8 % — cumple |
| B2. Percentiles frente al promedio | 110; margen 99–121 | 104; −5,5 % — cumple |
| B3. Ley de Little y modelos de carga | 170; margen 153–187 | 186; +9,4 % — cumple |
| B4. *Coordinated omission* | 110; margen 99–121 | 118; +7,3 % — cumple |
| B5. Tipos principales | 200; margen 180–220 | 217; +8,5 % — cumple |
| B6. Variantes | 100; margen 90–110 | 108; +8,0 % — cumple |
| **5.3, B1–B4** | **550; margen 495–605** | **582; +5,8 % — cumple** |
| **5.4, B5–B6** | **300; margen 270–330** | **325; +8,3 % — cumple** |
| **Total** | **850; margen 765–935** | **907; +6,7 % — cumple** |

Conteo por unidades separadas por espacios de la prosa visible, incluidas las citas autor–año. Se excluyen títulos, subtítulos, comentarios HTML, la tabla y los títulos y notas de tabla y figura, con el mismo criterio de la ronda 1.

**Espacio de tabla y figura:** se mantienen las reservas de 0,4 páginas y 0,6 páginas, respectivamente. La Tabla 2 tiene cinco columnas en total: tipo y cuatro dimensiones de comparación. Sin maquetación no se puede confirmar si cabe en su reserva ni declarar un exceso. La comprobación de páginas y legibilidad queda para la integración; se informa aparte y no constituye el motivo del veredicto.

## Ronda 1 — 2026-11-07 — Borrador v1 · Evidencia v1

**Veredicto:** Aprobada | **Citas revisadas:** E1–E30, incluidas las de la Figura 2, la Tabla 2 y sus notas.

Plan auditado: versión 3, aprobado, modo completo. Se leyeron el borrador y la evidencia completos, la guía de redacción, el glosario, las referencias y los criterios de fuentes de `Alcance.md` §5.3. Se cotejaron las transcripciones con el cuerpo de las cinco fuentes abiertas del plan. Resultado: **ningún hallazgo bloqueante y cuatro sugerencias de prosa**. Se deja además una nota de control bibliográfico sobre F4, sin confundirla con las ubicaciones de los pasajes citados, que son correctas.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Sugerencia | B1, ambos párrafos: tasa de error y concurrencia | 7–8 — Argumento y legibilidad | Se explica por qué importan las transacciones fallidas y cómo se modela la concurrencia, pero no se explicita qué mide cada una de estas dos métricas. Para una subsección que fija el vocabulario de las siguientes, el lector recibe su función antes de su significado. Es una omisión de desarrollo, no una afirmación externa sin respaldo. | Precisar la concurrencia con una formulación como «La concurrencia mide cuántos hilos o usuarios actúan simultáneamente y suele modelarse fijando el número de usuarios virtuales». Ampliar E5 con el pasaje inmediatamente anterior de F1, §4.2.5, p. 44, que sí la define. Para la tasa de error, explicitar qué se contará como error y sobre qué total o intervalo se calculará; respaldar esa definición con una fila apropiada antes de incorporarla, porque E3 solo acredita el efecto de las transacciones fallidas sobre el *throughput*. Compensar las adiciones recortando las explicaciones del mismo bloque para conservar su presupuesto. |
| 2 | Sugerencia | B2, últimas dos oraciones | 8 — Legibilidad y precisión conceptual | «El p95 y el p99 describen a los usuarios que más esperan» puede hacer pensar que los percentiles identifican un grupo de personas, cuando el argumento se refiere a la distribución de mediciones de tiempo de respuesta. El ejemplo de uno de cada veinte usuarios es una posibilidad ilustrativa, no un hallazgo empírico, pero el cambio de mediciones a usuarios vuelve menos precisa la explicación. | Reformular como «El percentil 95 (p95) y el percentil 99 (p99) permiten observar umbrales hacia la cola de los tiempos de respuesta, que el promedio puede ocultar». Si se conserva el ejemplo numérico, presentarlo expresamente como hipotético y formularlo sobre solicitudes o mediciones. Mantener esta extensión como razonamiento del trabajo, sin atribuir a E8 una recomendación de p95 o p99. |
| 3 | Sugerencia | B3, segundo párrafo, y descripción de la Figura 2 | 8, 13 — Legibilidad y terminología | «Una solicitud nueva solo sale cuando termina la anterior» deja implícito que el ciclo corresponde a cada usuario virtual; aislada, la frase puede sugerir una única solicitud pendiente para todo el generador. La descripción de la figura sí fija una población N, pero conviene hacer explícita esa relación. Además, «los montajes […] son cerrados» y «los sistemas […] son abiertos» abrevia las denominaciones que el glosario pide conservar. | Escribir «En el modelo de carga cerrado, cada usuario virtual envía su siguiente solicitud después de recibir la respuesta anterior y completar su *think time*» y usar la misma precisión en el comentario de la figura. Cerrar el párrafo con «Los montajes de prueba típicos usan un modelo de carga cerrado, mientras que muchos sistemas públicos se representan con un modelo de carga abierto (ISTQB, 2018)», conservando E15. |
| 4 | Sugerencia | B5, primer párrafo, y Tabla 2 | 9, 14 — Selección y duplicación entre prosa y tabla | El contraste entre carga y resistencia ayuda al argumento, pero reproduce en prosa sus objetivos y la duración de la resistencia, información que la Tabla 2 vuelve a presentar. El plan v3 reserva esas definiciones y duraciones a la tabla para aprovechar el espacio. | Acortar el contraste a «Un mismo escenario puede servir para preguntas distintas: soportar la carga prevista o conservar la estabilidad a lo largo del tiempo. La segunda pregunta permite buscar problemas acumulativos, como las fugas de memoria (ISTQB, 2018)», con E19 y E20. Conservar la remisión a la Tabla 2 y aprovechar el resto del bloque para explicar por qué la pregunta determina el diseño de la prueba, sin repetir las celdas ni introducir instrucciones del proceso reservado al grupo C. |

**Cotejo de citas y evidencia:**

Las 30 filas citadas existen y todas se usan. Los autores y años corresponden a las fuentes asignadas; no hay IDs inexistentes ni citas sin comentario de evidencia. Se normalizaron saltos de línea, ligaduras, comillas tipográficas y palabras partidas entre líneas. Las elisiones de E3, E10, E14 y E27 conservan el sentido de los pasajes. La corrección de OCR declarada para F2 se comprobó también contra la imagen de la página 46: la variable es Z y la fórmula cierra con paréntesis.

| Fuente y filas | Ubicaciones cotejadas | Resultado |
|---|---|---|
| [F1 — ISTQB (2018)](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf): E1–E8, E11, E15, E19–E20, E22–E30 | Paginación impresa: §1.2, pp. 12–13; §1.5, pp. 15–16; §4.1.2, p. 34; §4.2.2, p. 39; §4.2.4, p. 42; §4.2.5, pp. 44–45; §4.3, p. 50; §4.4, p. 52 | Conforme en literalidad, ubicación y fidelidad. E30 se verifica por la enumeración completa de encabezados de §1.2: no hay un apartado independiente de volumen. La Tabla 2 distingue mediante su nota las definiciones y los modos de falla de la síntesis propia de perfiles, duración y asignación de fallas. |
| [F2 — Lazowska et al. (1984)](https://homes.cs.washington.edu/~lazowska/qsp/Images/Chap_03.pdf): E9–E10 | §3.3, pp. 43 y 46 impresas; páginas 4 y 7 del PDF | Conforme. Ambas expresiones y las magnitudes descritas están en el cuerpo. El borrador conserva las dos oraciones previstas para la ley y su aplicación a la población de usuarios, sin derivaciones. E11 respalda por separado la expresión equivalente del CT-PT. |
| [F3 — Schroeder et al. (2006)](https://www.usenix.org/legacy/events/nsdi06/tech/full_papers/schroeder/schroeder.pdf): E12–E14 | §1, p. 239; figura 1, p. 240 | Conforme. Las tres transcripciones aparecen en la introducción, fuera del resumen. El borrador acota el predominio del modelo cerrado a los generadores revisados, sin convertirlo en una estadística vigente. La Figura 2 adapta los paneles cerrado y abierto y declara que omite el parcialmente abierto. |
| [F4 — Friedrich et al. (2017), copia de los autores](https://vsis-www.informatik.uni-hamburg.de/getDoc.php/publications/569/Coordinated_Omission_in_NoSQL_Database_Benchmarking-Friedrich.pdf): E16–E18 | §2, pp. 2–3; §3, p. 5 de la copia | Conforme. Los pasajes están en el cuerpo y respaldan el mecanismo de omisión, su efecto sobre las mediciones y la solución mediante un modelo abierto con solicitudes asíncronas. No se usa la afirmación de prevalencia que solo aparece en el resumen. |
| [F5 — Jiang y Hassan (2015), copia del autor](https://www.eecs.yorku.ca/~zmjiang/publications/tse2015_jiang.pdf): E21 | §2, p. 1092 impresa; página 2 del PDF | Conforme. El párrafo sobre diversidad de interpretaciones y uso intercambiable de los tres términos coincide literalmente con la fila. El enlace no respondió en el lector web; se recuperó y leyó el PDF del mismo enlace directamente en memoria, sin guardar archivos. |

**Respaldo y forma:** la decisión terminológica sobre latencia se presenta como propia, conforme al plan. La extensión del razonamiento a p95 y p99, los contrastes entre tipos de prueba y el ejemplo condicional de la API son razonamiento o ilustración del autor; no se presentan como datos observados ni como resultados de las fuentes. Las duraciones relativas y los perfiles de la tabla están identificados como síntesis propia, no como duraciones normativas del CT-PT. Las citas autor–año usan las formas APA 7 correspondientes; la abreviatura ISTQB ya se introdujo con el nombre institucional en la Introducción. No se exige expandirla de nuevo aquí.

**Fuentes nuevas:** F2, F3 y F4 figuran en `Referencias.md` y cumplen los tipos y criterios temporales del alcance: F2 es un libro clásico cuya [página de los autores](https://homes.cs.washington.edu/~lazowska/qsp/) acredita la devolución de derechos y su publicación abierta; F3 es el clásico expresamente previsto en el alcance, con [registro de USENIX](https://www.usenix.org/conference/nsdi-06/open-versus-closed-cautionary-tale); F4 es un artículo de taller de 2017, disponible también en el [sitio oficial de BTW 2017](https://www.btw2017.informatik.uni-stuttgart.de/slidesandpapers/E4-11-107/paper_web.pdf). No se incorporaron fuentes ajenas al plan para respaldar afirmaciones del borrador.

**Nota de control bibliográfico:** el PDF de F4 alojado por el congreso tiene 11 páginas y termina en la página impresa 225; el plan y `Referencias.md` consignan 215–226. Conviene normalizar el intervalo bibliográfico a **215–225** y la descripción de extensión de la copia a **1–11**, o documentar una edición distinta que justifique el intervalo actual. Esta discrepancia editorial no altera los autores, el año, la identificación de la obra ni las ubicaciones verificadas de E16–E18 (pp. 2, 3 y 5 de la copia; 216, 217 y 219 impresas), por lo que no constituye un fallo de trazabilidad o de fidelidad de las citas del borrador. No se modificaron el plan, las referencias ni la evidencia.

**Prosa y elementos gráficos:** los seis bloques desarrollan las ideas del plan y mantienen una progresión reconocible: métricas, distribución de tiempos, relaciones entre magnitudes, generación de carga y clasificación. La densidad corresponde al modo completo; no se repite una fuente innecesariamente dentro de un párrafo ni hay más de una cita narrativa por párrafo. Las remisiones a 5.8 y las decisiones terminológicas son contenido interno pertinente. No aparecen metacomentarios visibles sobre producción o auditoría; los comentarios HTML de control y de figura son los admitidos por la guía.

La Figura 2 y la Tabla 2 tienen número, título, mención previa y origen con IDs. La figura está presente en el formato de descripción oculta exigido para el borrador; su dibujo se realiza al integrar el documento final. La sugerencia 4 atiende la duplicación parcial entre la prosa y la tabla.

**Extensión:**

| Bloque | Plan v3 | Borrador v1 |
|---|---|---|
| B1. Métricas básicas | 160; margen 144–176 | 173; +8,1 % — cumple |
| B2. Percentiles frente al promedio | 110; margen 99–121 | 103; −6,4 % — cumple |
| B3. Ley de Little y modelos de carga | 170; margen 153–187 | 183; +7,6 % — cumple |
| B4. *Coordinated omission* | 110; margen 99–121 | 118; +7,3 % — cumple |
| B5. Tipos principales | 200; margen 180–220 | 205; +2,5 % — cumple |
| B6. Variantes | 100; margen 90–110 | 108; +8,0 % — cumple |
| **5.3, B1–B4** | **550; margen 495–605** | **577; +4,9 % — cumple** |
| **5.4, B5–B6** | **300; margen 270–330** | **313; +4,3 % — cumple** |
| **Total** | **850; margen 765–935** | **890; +4,7 % — cumple** |

Conteo por unidades separadas por espacios de la prosa visible, incluidas las citas autor–año. Se excluyen títulos, subtítulos, comentarios HTML, la tabla y los títulos y notas de tabla y figura. Los delimitadores de cursiva no agregan palabras.

**Espacio de tabla y figura:** el plan reserva 0,4 páginas para la Figura 2 y 0,6 para la Tabla 2, una página en conjunto. La tabla contiene aproximadamente 262 palabras con sus encabezados y 63 en la nota de origen, además del título; sus seis columnas hacen exigente el espacio de 0,6 páginas. Sin maquetación no puede confirmarse un exceso ni darse por cumplida esa reserva. Al integrar, verificar que tabla y figura quepan con tipografía legible; si hace falta, abreviar celdas y nota. Esta comprobación pendiente de páginas se informa por separado del presupuesto de prosa y no impide aprobar el borrador.
