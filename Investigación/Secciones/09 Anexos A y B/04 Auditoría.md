# Auditoría — 09 Anexos A y B

## Ronda 2 — 2026-11-11 — Borrador v4 · Evidencia sin versión (sin filas)

**Veredicto:** Aprobada | **Citas revisadas:** ninguna; no hay citas externas | **Seguimiento:** 2 bloqueantes resueltos y 5 sugerencias atendidas | **Hallazgos de esta ronda:** 0 bloqueantes y 3 sugerencias | **Plan:** v1, aprobado, modo ligero; presupuesto actual de 2 páginas, unas 250 palabras de prosa y cinco tablas

Se aplicó la skill auditor al seguimiento de los siete hallazgos de la ronda 1 y a los cambios del borrador: menciones de las cinco tablas, párrafos A.3 y B.3, título y rótulo agrupado de B1, nota de B1, fila de respaldo y fila y nota de literalidad de B2, y las dos primeras filas de B3. Se cotejaron nuevamente las afirmaciones internas afectadas con sus registros de origen, incluida la configuración efectiva de `.github/workflows/compuerta.yml`. La evidencia sigue sin filas: estos anexos sintetizan registros internos y no requieren citas bibliográficas externas para esas cifras. No hay fuentes nuevas a las que aplicar los criterios 5 y 6.

La identificación v4 corresponde a la revisión solicitada y al comentario inicial del archivo. El comentario oculto situado bajo el título del Anexo B todavía dice «Borrador v2»; se revisó su contenido actual, que sí incorpora cambios, sin tomar ese comentario como prueba de que B permaneciera intacto. Se mantiene como referencia del repositorio HEAD `061554e`.

No se repitieron los recuentos de A2, B1 y B2 aprobados en la ronda 1. Se conservan sus métodos y resultados, y se comprobó si las modificaciones alteran el conjunto contado o su interpretación. Tampoco se repitieron el cómputo histórico de coautorías ni el cotejo de las afirmaciones sin cambios de A1 y A2. Se revisaron la guía y el glosario actuales, el plan y la evidencia de los anexos, la Metodología y `Alcance.md` §5.3, los planes con los descartes, los informes de auditoría afectados y la documentación y el workflow del taller. No se ejecutaron las pruebas del taller ni se modificaron sus fuentes.

### Seguimiento de la ronda 1

| # anterior | Tipo | Estado | Comprobación en la versión actual |
|---|---|---|---|
| 1 | Bloqueante | Resuelto en el borrador | B3, líneas 87–88, elimina «cada cambio» y «cada push y pull request». Ahora sitúa ambas baterías en la *quality gate* y especifica `main` y los cambios en el taller o los workflows. El cotejo del YAML confirma las restricciones de rama y rutas. La afirmación 13 del plan conserva la redacción anterior; se registra por separado como sugerencia de coherencia, junto con una formulación inequívoca de los filtros comunes. |
| 2 | Bloqueante | Resuelto | B2, línea 72, incluye la ubicación cuando el informe la agrupa con literalidad y admite dos resoluciones: usar pasajes del cuerpo o corregir el localizador. La nota de la línea 75 explicita el conteo por la columna «Criterio» y el solapamiento. Ya no afirma que los tres casos fueran citas ausentes del cuerpo. |
| 3 | Sugerencia | Atendida | El título de B1 delimita las ocho partes anteriores a las Conclusiones. El rótulo «Marco teórico (cuatro grupos)» mantiene explícita la agrupación: tres partes iniciales + cuatro grupos + sección 6 = ocho. No incorpora Conclusiones ni los anexos y conserva los totales del mismo conjunto. |
| 4 | Sugerencia | Atendida | La apertura de A menciona A1 y A2 antes de ambas tablas y dice que muestran herramientas y consultas; la de B hace lo mismo con B1–B3, en el orden rondas, bloqueantes y controles. La guía §7 no exige una oración separada antes de cada tabla si la mención previa conjunta identifica qué muestran. Se conservan los cinco números, títulos y notas de origen. |
| 5 | Sugerencia | Atendida | B3 usa *quality gate* y «perfil de ejecución `ci`». La nueva cursiva de *workflows* contradice otra entrada del glosario actual y se informa como sugerencia 1 de esta ronda; no invalida la corrección de los dos términos señalados antes. |
| 6 | Sugerencia | Atendida | A.3 pasa de una oración a tres y distingue el descarte del estudio sobre *microbenchmarks* por alcance, en la Introducción, del de Ingo y Daly por datos de publicación incompletos, en el Planteamiento. Los ejemplos y sus motivos constan en los planes correspondientes. |
| 7 | Sugerencia | Atendida en el presupuesto | El plan actual ya no asigna una página de prosa a cada anexo: fija dos páginas totales, unas 250 palabras de prosa y el resto para cinco tablas. Las 254 palabras cumplen el margen 225–275. Existe una reserva conjunta para las tablas, aunque su ocupación efectiva queda pendiente de comprobar en la maquetación. No se mantiene la objeción anterior por falta de prosa. |

### Hallazgos de la ronda 2

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Sugerencia | Tabla B3, segunda fila, línea 88 | 13 — Terminología | La nueva forma «los *workflows*» usa cursiva. La entrada «Workflow» del glosario prescribe «workflow (sin cursiva, como en 5.7)». La forma de *quality gate* y «perfil de ejecución» sí cumple. | Escribir «los workflows», sin cursiva. Mantener la cursiva de *quality gate*, *push* y *pull requests*. |
| 2 | Sugerencia | B.3, primera oración, línea 79 | 8 — Legibilidad | En «la Introducción […] resultó saturada de citas […] y lenta», los dos adjetivos califican gramaticalmente a la Introducción. El origen dice que fue lento el proceso de producción, no el texto. La condensación conserva la cifra y el cambio de procedimiento, pero vuelve ambiguo ese resultado. | «La Introducción se produjo primero con cinco instrucciones permanentes (*skills*) que partían de la evidencia ya auditada. El texto quedó saturado de citas (17 en 880 palabras) y su producción fue lenta». Conservar a continuación la sustitución del procedimiento y la reescritura. |
| 3 | Sugerencia | `01 Plan.md`, afirmación interna 13; Tabla B3, segunda fila, línea 88 | 7 y 8 — Coherencia con el plan y precisión de la síntesis | El plan aún afirma que la compuerta corre «en cada push y pull request», aunque el borrador retiró esa generalización. Además, la posición de «que modifican…» en B3 puede leerse como una restricción solo de los *pull requests*. El YAML aplica los filtros de rutas a ambos eventos. No persiste la afirmación categórica anterior en el borrador; falta sincronizar el registro de control y hacer inequívoco el alcance compartido. | Para B3: «Las pruebas anteriores y la carga con el perfil de ejecución `ci`, en los *pushes* a `main` y los *pull requests*, en ambos casos con cambios en `Taller/**` o `.github/workflows/**`». Actualizar la afirmación 13 del plan con las mismas condiciones. Si se documenta también la ejecución manual, distinguirla: permite elegir variante, perfil y tasa. |

Las correcciones propuestas se dejan en este informe; no se aplicaron al plan ni al borrador. La discrepancia del plan se informa como coherencia del registro, no como un nuevo dato sin respaldo del borrador. Las tres sugerencias no impiden aprobar.

### Cotejo de las afirmaciones internas afectadas

Los números corresponden al orden de «Afirmaciones internas a verificar» de `01 Plan.md`.

| # del plan | Pasaje revisado | Origen cotejado | Resultado |
|---|---|---|---|
| 8 | A.3: motivos y ejemplos de descarte | Planes del Marco teórico, grupos A, B y D, apartados «Descartadas» y «Registro de búsqueda»; planes de Introducción y Planteamiento | Conforme. A registra copias y resúmenes de terceros, contenido comercial y falta de autoría. B registra los espejos y el acceso solo al resumen de *The Tail at Scale*. D descarta versiones anteriores y productos de la familia distintos de Professional, incluidos Enterprise y DevWeb. Introducción descarta Waller, Ehmke y Hasselbring por tratar un *microbenchmark* excluido; Planteamiento descarta Ingo y Daly por publicación incompleta y redundancia. El anexo puede sintetizar uno de los motivos registrados sin enumerarlos todos. |
| 9 | B1: título, agrupación del Marco teórico y cierre aprobado | Informes de los cuatro grupos del Marco teórico y recuento independiente conservado en la ronda 1 de este informe | Conforme. «Cuatro grupos» remite a 5.1–5.2, 5.3–5.4, 5.5–5.7 y 5.8. La fila sigue siendo el subtotal ya comprobado: 14 rondas, 7 no aprobadas, 14 bloqueantes y 25 sugerencias; no se suma de nuevo como otra parte. Las últimas rondas de esos grupos son R4, R4, R3 y R3, todas aprobadas. No cambia el conjunto de ocho partes ni sus totales 28/11/22/45. No procede incorporar las cuatro sugerencias de Conclusiones ni los hallazgos de estos anexos a ese corte. |
| 10 | B1: nota sobre la primera auditoría de Introducción | `02 Introducción/04 Auditoría.md`, R1 y seguimiento de R2 | Conforme. R1 auditó E1–E22: E1 y E2 se rechazaron por enlaces locales sin resolver y E13 por proceder solo de «Highlights». R2 registra las correcciones. La nueva nota abrevia «solo un resumen» a «un resumen» sin alterar el resultado ni convertir los tres rechazos en fuentes inexistentes. Se conserva la distinción de la ronda 1 entre esas filas rechazadas y los 22 hallazgos rotulados «Bloqueante». |
| 11 | B2: literalidad, nota de conteo y orden de las resoluciones de respaldo | Herramientas, R1 H4–H5 y seguimiento de R2; sección 6, R1 H3 y seguimiento de R2; correspondencias nominales conservadas en la ronda 1 de este informe | Conforme. Herramientas H4 trata títulos de metadatos y se resuelve con pasajes del cuerpo. H5 corrige la página de E33, además del problema de fidelidad seguido en rondas posteriores. La sección 6 H3 corrige el localizador de un pasaje literal al último párrafo de «Concepts». La nueva fila admite estas dos clases de corrección. La serie 15/9/5/3/1 sigue siendo un conteo de apariciones de rótulos, con solapamientos, no de defectos únicos ni una reclasificación por criterio numérico. Invertir el orden de «se acotó» y «se presentó como razonamiento propio» no añade una resolución. Se conserva el cotejo favorable anterior de los demás ejemplos y de la ausencia de obras inexistentes; no se recontaron las categorías. |
| 12 | B.3: cinco instrucciones, evidencia auditada, 17 citas en 880 palabras, lentitud y reescritura | `Alcance.md` §5.3, «Evolución del procedimiento»; Metodología §4.3 | Conforme en contenido. El alcance registra los cinco *skills*, la restricción de parafrasear evidencia ya auditada, las 17 citas en 880 palabras y un proceso lento. También registra la sustitución y la reescritura. §4.3 describe el procedimiento actual basado en plan, redacción y auditoría. La cifra se conserva como registro histórico, sin nuevo cómputo de aquella versión; «lenta» requiere la aclaración de prosa de la sugerencia 2. |
| 13 | B3: pruebas, control sin protección y ejecución automática | `Taller/docs/GUIA.md` §4; `Taller/docs/PLAN-DE-PRUEBAS.md` §§5–6.1; `.github/workflows/compuerta.yml` | Conforme en el borrador, con la precisión de la sugerencia 3. La guía documenta 38 pruebas que aprueban en ambas variantes y una prueba que reemplaza la protección y verifica la pérdida de visitas. «Debe fallar» se refiere a ese control deliberadamente defectuoso, no a un fallo esperado de la batería completa. El plan de pruebas documenta las 36 pruebas de herramientas. El workflow ejecuta funcionales, `unittest discover` para herramientas y luego carga. El cotejo de disparadores se detalla abajo. La frase universal aún presente en el plan no queda validada por este cotejo. |
| 14 | B3: ejecución interrumpida, inválida y repetida | `Taller/Taller.md` §7.1, nota de la campaña `calibracion-local`; plan de pruebas §§6.2 y 6.5 | Conforme. La nota registra interrupción por falta de memoria, invalidez por falta de `fases.json` y repetición. El anexo resume correctamente el incidente; no afirma que el detector diagnosticara la falta de memoria. El plan de pruebas considera inválida una medición sin esos datos y exige repetir las inválidas hasta completar las válidas previstas. |

**Disparadores y controles de B3.** En `compuerta.yml`, `push.branches: [main]` restringe los *pushes* a `main`; tanto `push.paths` como `pull_request.paths` contienen `Taller/**` y `.github/workflows/**`. Un cambio exclusivamente documental fuera de esas rutas no activa esos disparadores automáticos, tampoco por enviarse a `main`. «Taller/ o los workflows» sintetiza las dos rutas; la redacción propuesta precisa sus patrones y el alcance común del filtro. También existe `workflow_dispatch`, con entradas para variante, perfil y tasa: no contradice la descripción de los disparadores automáticos. En estos últimos, la carga usa `ci` por defecto; en una ejecución manual puede elegirse otro perfil. Los pasos de pruebas y carga dependen de que exista el sistema bajo prueba (`compose.yaml`).

El resultado «rechaza `regresion` y aprueba `corregida`» coincide con `Taller/Taller.md` §8 y con las campañas documentadas del perfil `ci`; no se deduce exclusivamente de que el YAML contenga un paso de carga. El archivo de configuración fija cuándo y cómo corre, mientras que los registros del taller sostienen el resultado observado. Las abreviaciones «cada cambio» o «cada push y pull request» que todavía figuran en otros documentos del taller no prevalecen sobre los filtros del workflow.

### Prosa, tablas y extensión

Los siete bloques del esquema conservan su función. Las nuevas entradas de A y B orientan hacia las tablas sin repetir sus celdas. A.3 separa los dos descartes antes confundidos y mantiene sus orígenes; B.3 conserva la evolución registrada, con la ambigüedad de redacción señalada. El modo ligero sigue siendo adecuado para esta síntesis interna. Se permite hablar del proceso en los anexos según la guía §5: *skills* se presenta mediante «instrucciones permanentes», y no se detecta un metacomentario prohibido por el criterio 11. No se introducen objetivos ni preguntas como listas copiadas, ni datos externos nuevos sin respaldo.

**Extensión:**

| Bloque | Plan actual | Borrador v4 |
|---|---|---|
| Apertura A | Sin presupuesto separado | 42 palabras |
| A.1 Herramientas | Sin presupuesto separado | 0 de prosa; Tabla A1 aparte |
| A.2 Consultas | Sin presupuesto separado | 42 palabras; Tabla A2 aparte |
| A.3 Descartes | Sin presupuesto separado | 78 palabras |
| **Anexo A, prosa** | **Sin cuota independiente** | **162 palabras** |
| Apertura B | Sin presupuesto separado | 44 palabras |
| B.1 Auditorías | Sin presupuesto separado | 0 de prosa; Tabla B1 aparte |
| B.2 Bloqueantes | Sin presupuesto separado | 0 de prosa; Tabla B2 aparte |
| B.3 Evolución | Sin presupuesto separado | 48 palabras |
| B.4 Código | Sin presupuesto separado | 0 de prosa; Tabla B3 aparte |
| **Anexo B, prosa** | **Sin cuota independiente** | **92 palabras** |
| **Total de prosa** | **Unas 250 palabras; margen 225–275** | **254; +1,6 %. Cumple.** |
| Tablas A1 y A2, con títulos y notas | Parte de la reserva conjunta de tablas | 70 y 144 palabras; total 214 |
| Tablas B1, B2 y B3, con títulos y notas | Parte de la reserva conjunta de tablas | 99, 153 y 121 palabras; total 373 |
| **Cinco tablas** | **Resto de las 2 páginas totales; sin reparto individual** | **587 palabras visibles; ocupación maquetada no comprobada** |

Se cuentan unidades separadas por espacios, sin encabezados, comentarios HTML ni marcas de formato. La prosa excluye tablas, títulos y notas de origen; las tablas incluyen sus celdas, encabezados, títulos y notas, sin barras ni filas separadoras. Este recuento mide extensión textual, no vuelve a contar los registros internos resumidos en A2, B1 y B2.

Con la equivalencia orientativa de 350 palabras por página, la prosa ocuparía unas 0,73 páginas y dejaría unas 1,27 de la reserva total para las cinco tablas. No se convierte su contenido tabular a páginas de texto corrido para declarar un exceso: la altura depende de columnas, anchos y saltos en el documento final. Sin esa maquetación no se acredita ni se descarta que las tablas excedan la reserva conjunta. No se aplica a cada anexo el presupuesto anterior de una página de prosa.

Se agregó esta ronda antes de la ronda 1, que se conserva íntegra. Se escribió únicamente `Investigación/Secciones/09 Anexos A y B/04 Auditoría.md`.

## Ronda 1 — 2026-11-11 — Borrador A v3 / B v2 · Evidencia sin versión (sin filas)

**Veredicto:** No aprobada | **Citas revisadas:** ninguna; no hay citas externas | **Afirmaciones internas revisadas:** las 14 del plan | **Plan:** v1, aprobado, modo ligero

Se aplicó la skill auditor con la adaptación solicitada: cotejo de las afirmaciones internas contra sus registros de origen y recuento independiente de A2, B1 y B2. Se revisaron el criterio 4 y los criterios 7–14; **el criterio 11 no aplica**, porque la guía §5 permite tratar el proceso en los anexos. No se exige añadir citas externas ni filas de evidencia a estos contenidos internos. Los criterios 5 y 6 no tienen objeto aquí.

Se consultaron los planes, registros de evidencia e informes de auditoría de las secciones 02–07, incluidas las cuatro partes del Marco teórico; la Metodología §§4.2–4.3; `Alcance.md` §5.3; `Investigación/Referencias.md`; el glosario y la guía; `Taller/Taller.md`; los tres documentos de `Taller/docs/`; `.github/workflows/compuerta.yml`; y el historial de Git. El cotejo corresponde a los archivos disponibles con HEAD `061554e`; la cifra histórica de coautorías conserva expresamente el corte `ceacb17`. No se ejecutaron las pruebas del taller: se verificaron los controles y resultados que documentan los orígenes indicados por el plan.

### Hallazgos

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante | Tabla B3, filas 1–2, líneas 87–88 | 4 — Respaldo de afirmaciones internas | «Corren en cada cambio» y «en cada *push* y *pull request*» exceden los disparadores reales. `compuerta.yml`, líneas 8–13, limita los *pushes* a `main` y aplica a ambos eventos los filtros `Taller/**` y `.github/workflows/**`. Un cambio exclusivamente documental fuera de esas rutas no dispara la compuerta. Que algunas descripciones del taller también abrevien los disparadores no sustituye la configuración efectiva. | En la primera fila, sustituir por «Las dos variantes aprueban las pruebas funcionales; ambas baterías se ejecutan cuando se activa la compuerta». En la segunda: «Las pruebas anteriores y la carga con el perfil de ejecución `ci`, en los *pushes* a `main` y los *pull requests* que modifican `Taller/**` o `.github/workflows/**`». Mantener el resultado observado de rechazo de `regresion` y aprobación de `corregida`. |
| 2 | Bloqueante | Tabla B2, fila «Literalidad», línea 72, y nota metodológica del recuento | 4 — Fidelidad de la síntesis interna | Los **3** casos se reproducen contando los rótulos originales «Literalidad», pero no son tres citas ausentes del cuerpo ni se resolvieron todos sustituyéndolas por pasajes del cuerpo. En Herramientas, R1 H5, la cita de E33 estaba en otra página; en la sección 6, R1 H3, el pasaje de E4 era literal y estaba al final del apartado, en vez de al principio. Ambos informes los rotulan «Literalidad y ubicación». Solo Herramientas R1 H4 trata títulos de metadatos usados como citas. La definición y la resolución de la fila generalizan ese único ejemplo a los tres casos. | Conservar el 3 si se explicita el método: «Literalidad, incluida ubicación cuando el informe las agrupa»; resolución: «Se usaron pasajes del cuerpo o se corrigió el localizador». Añadir a la nota: «Los casos cuentan apariciones de los rótulos en la columna “Criterio” de los informes; las categorías pueden solaparse». Si se prefiere una clasificación por defecto efectivo, reclasificar los casos y recalcular la tabla, sin mezclar ambos métodos. |
| 3 | Sugerencia | Tabla B1, título y nota, líneas 50–61 | 7 y 9 — Precisión del alcance del resumen | Los totales 28/11/22/45 son correctos para las ocho partes incluidas, pero el informe de Conclusiones ya existe: agrega una ronda aprobada y cuatro sugerencias. «Por parte del documento» no explicita ese corte. La propia auditoría de Conclusiones reconoce que el recuento histórico corresponde a las ocho partes anteriores. | Precisar el título como «Rondas de auditoría de las ocho partes incluidas» y añadir «No incluye Conclusiones ni la presente auditoría de los anexos». Alternativamente, incorporar Conclusiones y actualizar los totales a 29 rondas, 11 no aprobadas, 22 bloqueantes y 49 sugerencias, siempre antes de esta ronda. |
| 4 | Sugerencia | Antes de las tablas A1, A2, B1, B2 y B3 | 14 — Tablas y figuras | Las cinco tablas tienen número, título y origen, pero ninguna se menciona por su número en la prosa antes de aparecer. Los encabezados de subsección y los títulos de tabla no cumplen esa función de la guía §7. No hay duplicación extensa entre prosa y tablas ni figuras omitidas. | Añadir entradas breves: «La Tabla A1 identifica las herramientas y sus funciones»; «La Tabla A2 reúne las consultas y los registros por parte»; «La Tabla B1 resume las rondas de las ocho partes incluidas»; «La Tabla B2 agrupa los hallazgos según los rótulos de los informes»; «La Tabla B3 resume los controles aplicados al código». |
| 5 | Sugerencia | Tabla B3, segunda fila, línea 88 | 13 — Terminología | «Compuerta en CI» y «perfil `ci`» no siguen las formas obligatorias del glosario: *quality gate* y «perfil de ejecución». La forma abreviada «perfil» está expresamente desaconsejada para evitar confundirla con el perfil de carga. | Usar «*Quality gate* en CI» y «perfil de ejecución `ci`», también al aplicar el hallazgo 1. No cambiar el nombre literal del archivo `compuerta.yml`. |
| 6 | Sugerencia | A.3, único párrafo, línea 40 | 8 — Legibilidad | Una oración de 83 palabras encadena los cinco grupos de motivos y deja juntos dos descartes distintos: el estudio de *microbenchmarks* pertenece a la Introducción y la falta de datos de publicación corresponde a Ingo y Daly en el Planteamiento. Los motivos sí están documentados, pero el lector debe reconstruir qué ejemplo corresponde a cada uno. | Dividir el párrafo y explicitar el cierre: «También se descartó documentación de otros productos o versiones, como LoadRunner Enterprise frente a Professional. Por alcance se excluyó el estudio de Waller, Ehmke y Hasselbring sobre *microbenchmarks*; por datos de publicación incompletos, el de Ingo y Daly sobre MongoDB». Conservar en las oraciones anteriores los tres primeros grupos de motivos. |
| 7 | Sugerencia | Presupuesto de los anexos y distribución entre prosa y tablas | 12 — Extensión | El plan asigna una página de prosa a cada anexo, sin contar tablas, pero no fija palabras por subsección ni reserva espacio para las cinco tablas. Hay 156 palabras de prosa en A y 91 en B: con la equivalencia orientativa de `Alcance.md` de 350 palabras por página, ambas quedan por debajo del intervalo de una página ±10 %. No es una medición de páginas maquetadas. La petición de un resumen estructurado explica la concentración del contenido en tablas. | Ajustar el presupuesto al formato efectivamente elegido y asignar espacio aparte a las tablas; no ampliar la prosa solo para llenar páginas. Las entradas breves del hallazgo 4 aportan orientación sin repetir las celdas. No puede evaluarse el exceso de las tablas contra una reserva que el plan no define. |

### Cotejo de las afirmaciones del plan

La numeración siguiente sigue el orden de «Afirmaciones internas a verificar» de `01 Plan.md`.

| # | Afirmación | Origen cotejado | Resultado |
|---|---|---|---|
| 1 | Claude Code (Opus 5.5) planifica y redacta; Codex (GPT-6.1 Sol) audita en sesión independiente | Metodología §4.3, segundo párrafo y Figura 1; `Alcance.md` §5.3 | Conforme como descripción del procedimiento registrado. El taller y su documentación están registrados en el historial del repositorio. No se infiere el modelo de cada intervención exclusivamente de la coautoría. |
| 2 | Hasta `ceacb17`, 57 de 81 *commits* llevan coautoría de Claude | `git log ceacb17 --format=%H%x1f%B%x1e`, lectura de las líneas `Co-Authored-By` de cada mensaje | Conforme: 81 *commits* alcanzables, incluido `ceacb17`, y 57 con al menos una línea de coautoría de Claude. Son 56 con Claude Opus 5.5 y uno con Claude Sonnet 5.5; 57 es la cifra de Claude, no de Opus exclusivamente. |
| 3 | A2: 22 consultas, 238 resultados, 13 con fuente y 9 sin fuente; grupos 6/6/1/9; fecha común | Los cuatro «Registros de búsqueda» de los planes del Marco teórico, una fila por consulta | Conforme. Los totales independientes y el desglose se muestran abajo. Todas las filas tienen fecha 2026-11-07 y «Buscador web». La consulta 6 del grupo B confirma F4 y se cuenta entre las que tienen fuente; no equivale a una fuente nueva. |
| 4 | A2: 47 fuentes verificadas, con desglose 8/7/2/7/5/5/9/4 | Filas F de la tabla «Fuentes» de los ocho planes correspondientes | Conforme: 47 entradas de planes. No se deduplican entre secciones ni se equiparan estas entradas con obras distintas. |
| 5 | A2: 200 filas de evidencia, con desglose 29/30/5/26/31/31/44/4 | Filas E de los ocho `02 Evidencia.md` | Conforme: 200 filas, incluidas las conservadas bajo «Filas no usadas». No significa que el borrador final cite 200 filas. No hay IDs duplicados dentro de cada registro. |
| 6 | No se registraron las consultas de Introducción, Planteamiento y Metodología | Metodología §4.2 y los tres planes | Conforme con el estado del repositorio. §4.2 declara expresamente la ausencia de registro para Introducción y Planteamiento; el plan de Metodología tampoco tiene registro de consultas. La extensión a Metodología se comprueba en ese plan, no en una declaración expresa de §4.2. |
| 7 | 34 referencias distintas | `Investigación/Referencias.md`, una entrada bibliográfica por párrafo | Conforme: 34 entradas. Se cuentan por separado las obras o páginas con autor común y sufijos distintos; no se cuentan encabezados ni líneas en blanco. |
| 8 | A.3: motivos y ejemplos de descarte | Registros de búsqueda de los grupos A, B y D; apartados «Descartadas» de Introducción y Planteamiento | Conforme. A: consultas 1, 3–6; B: consultas 1–5, incluida *The Tail at Scale* en la 4; D: consultas 2–3 y 5–9, incluidos productos y versiones distintos. Introducción descarta Waller et al. por *microbenchmarks*; Planteamiento descarta Ingo y Daly por publicación incompleta y redundancia. Véase la sugerencia 6 para separar los ejemplos. |
| 9 | B1: 28 rondas, 11 no aprobadas, 22 bloqueantes, 45 sugerencias; última ronda aprobada | Los ocho informes correspondientes a las filas de B1, leyendo cada ronda y su tabla de hallazgos | Conforme para ese conjunto; véase el recuento y la sugerencia 3 sobre el corte. Las tres filas rechazadas de Introducción R1 se informan aparte y no se suman a los 22 hallazgos rotulados «Bloqueante». |
| 10 | Introducción R1 auditó evidencia y rechazó 3 de 22 filas | `02 Introducción/04 Auditoría.md`, R1, y seguimiento en R2 | Conforme: 19 aprobadas y 3 rechazadas. E1 y E2 tenían nombres de archivo sin enlaces resolubles; E13 usaba únicamente «Highlights». R2 da por corregidos los enlaces y sustituido el pasaje por texto del cuerpo. No eran fuentes inexistentes. |
| 11 | B2: 15/9/5/3/1 por tipo; ejemplos, resoluciones y ausencia de fuentes inexistentes | Columna «Criterio» de las 22 filas bloqueantes y sus seguimientos | Cifras nominales conformes, con el método y las correspondencias que se detallan abajo. **No conforme la descripción de los tres casos de literalidad y su resolución común**: hallazgo 2. Los cinco ejemplos existen y sus correcciones constan en rondas posteriores. Ninguno de los 22 bloqueantes ni de las tres filas rechazadas de Introducción R1 afirma que la obra citada sea inexistente. |
| 12 | Cinco instrucciones, evidencia auditada primero, 17 citas en 880 palabras, lentitud y reescritura | `Alcance.md` §5.3, «Evolución del procedimiento», y Metodología §4.3 para el procedimiento sustituto | Conforme con el relato interno. La cifra 880 se conserva tal como la registra el alcance; no se presenta como un nuevo conteo de aquella versión histórica. La lentitud es una valoración del proceso documentada allí, no una medición de productividad. |
| 13 | 38 pruebas funcionales y de concurrencia, control sin protección, 36 de herramientas y ejecución en CI | `Taller/docs/GUIA.md` §4; `PLAN-DE-PRUEBAS.md` §§5–6.1; pasos de `compuerta.yml` | Conforme para cantidades, funciones y perfil automático `ci`. La guía describe la prueba que verifica la pérdida de visitas al usar «leer, sumar y escribir» sin protección. El workflow ejecuta `funcionales`, las herramientas mediante `unittest discover` y después la carga. **No conforme el alcance «cada cambio / cada push y pull request»**: hallazgo 1. |
| 14 | Ejecución interrumpida por falta de memoria, inválida y repetida | `Taller/Taller.md` §7.1, campaña `calibracion-local`, nota de la tabla, línea 422; `PLAN-DE-PRUEBAS.md` §6.2; `INTERPRETACION.md` §§2–3 | Conforme. La ejecución se interrumpió a la mitad y se marcó inválida por ausencia de `fases.json`. La falta de memoria fue la causa de la interrupción; la ausencia del archivo fue la condición detectable de invalidez. Se repitió y no se contabilizó como rechazo de la API. |

### Recuento independiente de A2

Se contaron las filas numeradas del registro de búsqueda, las entradas F de cada plan y las filas E de cada registro de evidencia; no se usaron los totales del anexo como insumo. Para la columna de resultados se sumó el número inicial de cada celda, tal como lo registra el plan: no representa resultados únicos deduplicados.

| Parte | Consultas | Resultados | Con fuente | Sin fuente | Entradas F | Filas E |
|---|---:|---:|---:|---:|---:|---:|
| Introducción | — | — | — | — | 8 | 29 |
| Planteamiento | — | — | — | — | 7 | 30 |
| Metodología | — | — | — | — | 2 | 5 |
| 5.1–5.2 | 6 | 85 | 3 | 3 | 7 | 26 |
| 5.3–5.4 | 6 | 60 | 4 | 2 | 5 | 31 |
| 5.5–5.7 | 1 | 19 | 1 | 0 | 5 | 31 |
| 5.8 | 9 | 74 | 5 | 4 | 9 | 44 |
| Sección 6 | — | — | — | — | 4 | 4 |
| **Total** | **22** | **238** | **13** | **9** | **47** | **200** |

Sumas de resultados: grupo A, 20 + 10 + 17 + 10 + 18 + 10 = 85; B, 6 × 10 = 60; C, 19; D, 8 × 7 + 18 = 74. Las consultas sin fuente elegida son A3/A5/A6, B4/B5 y D3/D5/D8/D9. Se cuenta B6 como confirmación de F4; así se obtienen las 13 consultas restantes con fuente. La sección 6 declara consulta directa de documentación, sin búsquedas. Conclusiones y los anexos no aportan filas F o E a este total.

### Recuento independiente de B1

Se contó una ronda por encabezado `## Ronda`, un rechazo por veredicto «No aprobada» y una aparición por fila rotulada «Bloqueante» o «Sugerencia» en la tabla de hallazgos de esa ronda. No se recontaron las tablas de seguimiento. Una observación reiterada en otra ronda vuelve a contarse: son apariciones registradas, no problemas únicos.

| Parte | Rondas | No aprobadas | Bloqueantes | Sugerencias | Última ronda |
|---|---:|---:|---:|---:|---|
| Introducción | 6 | 2 | 4 | 3 | R6, aprobada |
| Planteamiento | 4 | 1 | 1 | 5 | R4, aprobada |
| Metodología | 2 | 0 | 0 | 5 | R2, aprobada |
| 5.1–5.2 | 4 | 2 | 5 | 6 | R4, aprobada |
| 5.3–5.4 | 4 | 1 | 1 | 6 | R4, aprobada |
| 5.5–5.7 | 3 | 2 | 2 | 5 | R3, aprobada |
| 5.8 | 3 | 2 | 6 | 8 | R3, aprobada |
| **Subtotal Marco teórico** | **14** | **7** | **14** | **25** | Cuatro grupos aprobados |
| Sección 6 | 2 | 1 | 3 | 7 | R2, aprobada |
| **Total de las ocho partes de B1** | **28** | **11** | **22** | **45** | Todas aprobadas al cierre |
| Conclusiones, fuera de B1 | 1 | 0 | 0 | 4 | R1, aprobada |
| **Total disponible antes de esta auditoría** | **29** | **11** | **22** | **49** | No incluye esta ronda |

El subtotal del Marco teórico no se suma dos veces. Introducción R1 aporta una de las 11 rondas no aprobadas, pero su tabla clasifica filas como «Rechazada», sin rotularlas «Bloqueante». Por eso sus tres rechazos no se añaden a los 22. Tampoco se convierten sugerencias repetidas en problemas nuevos por inferencia: se cuenta lo que cada informe registra.

### Recuento independiente de B2

La serie **15/9/5/3/1** se reproduce por los **rótulos escritos** en «Criterio», no mediante una reclasificación propia de los defectos. Cada fila bloqueante puede aportar a más de una columna. Las abreviaturas I, P, A, B, C, D y T indican Introducción, Planteamiento, grupos A–D del Marco teórico y sección 6; R es ronda y H el número de hallazgo en ella.

| Parte | Fidelidad | Respaldo | Ubicación | Literalidad | Trazabilidad |
|---|---:|---:|---:|---:|---:|
| Introducción | 4 | 1 | 0 | 0 | 0 |
| Planteamiento | 1 | 0 | 1 | 0 | 0 |
| Metodología | 0 | 0 | 0 | 0 | 0 |
| 5.1–5.2 | 2 | 1 | 2 | 0 | 1 |
| 5.3–5.4 | 1 | 1 | 0 | 0 | 0 |
| 5.5–5.7 | 2 | 2 | 0 | 0 | 0 |
| 5.8 | 5 | 2 | 1 | 2 | 0 |
| Sección 6 | 0 | 2 | 1 | 1 | 0 |
| **Total** | **15** | **9** | **5** | **3** | **1** |

Correspondencias para reproducir el recuento:

- **Fidelidad (15):** I R4 H1–H4; P R1 H1; A R1 H3 y R3 H1; B R2 H1; C R1 H1 y R2 H1; D R1 H1/H2/H3/H5 y R2 H1.
- **Respaldo (9):** I R4 H2; A R1 H4; B R2 H1; C R1 H1 y R2 H1; D R1 H3 y R2 H1; T R1 H1–H2. I R4 H4 menciona el criterio numérico 4, pero su rótulo dice «Fidelidad y atribución del razonamiento»: por eso no integra este conteo nominal. Contar el número 4 en lugar del rótulo daría **10**, no 9. El método debe quedar explícito.
- **Ubicación (5):** P R1 H1; A R1 H1–H2; D R1 H5; T R1 H3.
- **Literalidad (3):** D R1 H4–H5 y T R1 H3. D R1 H5 y T R1 H3 son los dos casos de localización que explican el hallazgo 2 de esta auditoría.
- **Trazabilidad (1):** A R1 H4. Ese hallazgo también incluye respaldo y formato; B2 selecciona solo cinco categorías y no pretende desglosar el criterio 6.

Las cinco columnas suman **33 apariciones** sobre **22 filas bloqueantes**. No incluyen las tres filas rechazadas de Introducción R1, coherentemente con B1. Los dos registros de C corresponden al mismo problema de atribución del SLO, inicialmente corregido solo de forma parcial; contarlos por ronda explica que aporten dos casos nominales.

**Ejemplos y resolución:** el límite aproximado y la atribución al ISTQB son I R4 H1/H4, resueltos en R5; el pasaje anterior al apartado es A R1 H1, corregido en R2; los metadatos son D R1 H4, corregido en R2; y los IDs sin cita autor–año son A R1 H4, resuelto en R2 mediante notas que reúnen autores, años e IDs. Las resoluciones de los ejemplos sí están documentadas. La corrección pendiente afecta la generalización de la fila de literalidad, no la existencia de esos ejemplos.

### Prosa, estructura y extensión

Los siete bloques del esquema están presentes y cumplen sus funciones: herramientas, consultas, descartes, auditorías, clases de hallazgo, evolución y controles del taller. El modo ligero admite la ausencia de citas externas en este resumen interno. No hay listas copiadas de objetivos o preguntas ni repetición innecesaria del alcance. B.3 presenta primero el equivalente «instrucciones permanentes» y luego *skills*; *commit*, *push*, *pull request* y *microbenchmarks* están en cursiva. Las desviaciones del glosario se limitan a las indicadas en el hallazgo 5. La revisión del proceso no constituye un hallazgo por metacomentarios.

**Extensión:**

| Bloque | Plan | Borrador |
|---|---|---|
| Apertura A | Sin presupuesto separado | 31 palabras |
| A.1 Herramientas | Sin presupuesto separado | 0 de prosa; Tabla A1 |
| A.2 Consultas | Sin presupuesto separado | 42 palabras; Tabla A2 aparte |
| A.3 Descartes | Sin presupuesto separado | 83 palabras |
| **Anexo A** | **1 página sin tablas; ≈350 palabras como orientación, intervalo 315–385** | **156 palabras; ≈0,45 páginas; −55,4 % frente a 350** |
| Apertura B | Sin presupuesto separado | 30 palabras |
| B.1 Auditorías | Sin presupuesto separado | 0 de prosa; Tabla B1 |
| B.2 Bloqueantes | Sin presupuesto separado | 0 de prosa; Tabla B2 |
| B.3 Evolución | Sin presupuesto separado | 61 palabras |
| B.4 Código | Sin presupuesto separado | 0 de prosa; Tabla B3 |
| **Anexo B** | **1 página sin tablas; ≈350 palabras como orientación, intervalo 315–385** | **91 palabras; ≈0,26 páginas; −74,0 % frente a 350** |
| **Total de prosa** | **2 páginas sin tablas; ≈700 palabras** | **247 palabras; ≈0,71 páginas** |
| Tablas A1–A2, con títulos y notas | Sin reserva de páginas definida | 214 palabras visibles |
| Tablas B1–B3, con títulos y notas | Sin reserva de páginas definida | 356 palabras visibles |

Conteo reproducible: unidades separadas por espacios; se excluyen encabezados, comentarios HTML y delimitadores Markdown. La prosa excluye las filas de tablas, sus títulos y sus notas de origen. Para las tablas se cuentan las palabras de las celdas, títulos y notas, sin barras ni filas separadoras. Las equivalencias de página usan las 350 palabras orientativas de `Alcance.md`; **no acreditan ocupación maquetada** ni permiten comprobar la altura de las tablas. No hay presupuestos por A.1–B.4 a los que aplicar individualmente ±10 %; el desajuste orientativo se informa por anexo y las tablas se reportan aparte.

Se escribió únicamente este informe. No se modificaron el borrador, el plan, la evidencia ni los archivos de origen.
