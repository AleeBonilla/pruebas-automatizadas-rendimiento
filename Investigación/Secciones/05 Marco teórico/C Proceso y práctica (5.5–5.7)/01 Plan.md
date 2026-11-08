# Plan — Marco teórico, grupo C: Proceso y práctica (5.5–5.7)

**Estado:** Aprobado | **Modo:** Completo | **Versión:** 2 | **Fecha:** 2026-11-07 | **Presupuesto:** 870 palabras (2,5 págs.; sin tablas ni figuras)

> **Cambios en la versión 2:** aprobado por el usuario sin cambios. La fuente nueva (F5) se agrega a `Referencias.md`, y los términos nuevos, a `Glosario.md`. Por decisión del usuario, se elimina de `Referencias.md` la entrada de Amazon Web Services (s. f.-b), *Performance efficiency*, que ningún borrador cita; la otra entrada de AWS pasa de «s. f.-a» a «s. f.».

## Objetivo y alcance

Subsecciones 5.5, 5.6 y 5.7 del Marco teórico (`Alcance.md` §5.4; `Enunciado.md` §5, «clasificación, principios y mejores prácticas del tipo de prueba elegido»). Responden a PI-3: qué principios, buenas prácticas y antipatrones rigen el diseño, la ejecución y la interpretación de las pruebas de rendimiento, y cómo se integran en CI/CD. Son el puente directo hacia el taller: justifican el entorno propio, la línea base, las repeticiones y los umbrales que el taller deberá aplicar (`Alcance.md` §7).

**Incluye:**

- 5.5: las actividades del proceso según el CT-PT (planificación, análisis, diseño, implementación, ejecución y cierre con reporte), su carácter iterativo, el paso de los perfiles operacionales al perfil de carga y los requisitos del entorno y de los datos.
- 5.6: la línea base y el principio de «no peor que antes»; la repetibilidad y el aislamiento del entorno; el calentamiento, los datos realistas y la verificación del generador de carga; los antipatrones (probar sin objetivos, informar solo promedios, entorno compartido, medir sin criterio de aprobación).
- 5.7: los umbrales como criterio de aprobación (SLI, SLO y *quality gates*), el riesgo de fijarlos mal, la detección de regresiones en presencia de ruido, la frecuencia y la etapa del pipeline en que se ejecutan, y la observabilidad como complemento.

**No incluye (lo cubren otras secciones o grupos):**

- Las métricas, los percentiles, los modelos de carga, *coordinated omission* y los tipos de prueba, ya definidos en el grupo B (5.3–5.4). Este grupo los usa y remite a ellos; no los redefine.
- El pipeline de despliegue, las compuertas y el *shift-right*, ya presentados en el grupo A (5.1). 5.7 los aplica a las pruebas de rendimiento.
- Los obstáculos para automatizar (entornos, ruido, umbrales delicados, complejidad), ya argumentados en el Planteamiento del problema (3.2). 5.6 y 5.7 responden a esos obstáculos con prácticas; no los vuelven a presentar como problema.
- Las herramientas y su soporte para criterios de aprobación, que son criterios de la comparativa del grupo D (5.8).
- Los detalles del taller (plataforma de CI, escenarios, valores de los umbrales, número de repeticiones), que se definen en la Fase 2.
- La observabilidad y el APM a fondo: el alcance solo admite mencionarlos (`Alcance.md` §4).

**Forma:** tres subsecciones con subtítulo (5.5, 5.6 y 5.7). Dentro de cada una, bloques sin subtítulo.

## Esquema argumental
| Bloque | Palabras | Idea central | Contenido | Insumos y fuentes |
|---|---|---|---|---|
| B1. 5.5, bloque 1: actividades del proceso | 150 | Las pruebas de rendimiento siguen las actividades del proceso de pruebas general, pero cada una tiene tareas propias, y el conjunto es iterativo: cada ejecución informa una corrección que la siguiente verifica. | Las actividades del CT-PT y lo propio de cada una: la planificación asigna entornos, datos y herramientas; el análisis decide condiciones y tipos de prueba; el diseño es modular; la implementación combina perfiles operacionales en un perfil de carga y prepara datos representativos; la ejecución y el cierre con reporte. El carácter iterativo. | F1 |
| B2. 5.5, bloque 2: entorno y datos | 110 | El entorno es la variable más delicada del proceso, porque el rendimiento no escala de forma lineal con él: una prueba en un entorno reducido detecta problemas graves, pero no demuestra que se cumplan los objetivos de producción. | El entorno lo más parecido posible a producción y la pérdida de fiabilidad de las proyecciones a medida que se aleja. El tamaño y la estructura de los datos. Lo que una prueba en hardware de menor capacidad puede y no puede mostrar. Conexión con el taller, como razonamiento propio: en un entorno propio y reducido, el resultado útil es la comparación entre versiones, no la capacidad absoluta. | F1, F2 |
| B3. 5.6, bloque 1: línea base y repetibilidad | 130 | Una prueba de rendimiento vale sobre todo como comparación, y una comparación solo es válida si los resultados se repiten: por eso la línea base y el aislamiento del entorno son las prácticas de las que dependen las demás. | La línea base como conjunto de métricas para comparar ejecuciones. El principio de «no peor que antes» cuando faltan requisitos. Resultados estables y reproducibles mediante un entorno aislado y dedicado. La variación real entre ejecuciones en un sistema de CI industrial, como orden de magnitud del ruido. | F1, F4, F2, F3 |
| B4. 5.6, bloque 2: realismo de la ejecución | 120 | Una ejecución solo es representativa si mide al sistema en condiciones reales y no a sus artefactos: datos de tamaño realista, un período de calentamiento antes de medir y un generador de carga que no sea el cuello de botella. | Los datos pequeños o de distinta complejidad, que engañan. El calentamiento en plataformas con optimización en tiempo de ejecución, enlazado con el estado estable (5.4). Monitorear el generador de carga y validar que la prueba puede sostener la tasa necesaria antes de confiar en un fallo. | F1, F2 |
| B5. 5.6, bloque 3: antipatrones | 100 | Los antipatrones más comunes no son errores técnicos, sino de criterio: probar sin objetivos medibles, resumir con promedios, compartir el entorno o medir sin decidir qué cuenta como aprobado. | Probar sin definir antes métricas y objetivos; los requisitos vagos («lo más rápido posible»). El promedio, con remisión a 5.3. El entorno compartido con otras pruebas. La medición sin criterio de aprobación, que convierte la prueba en un ejercicio de análisis manual. | F1, F2 |
| B6. 5.7, bloque 1: umbrales y regresiones | 140 | Para que una prueba de rendimiento funcione como *quality gate*, su resultado debe compararse con un umbral explícito; fijarlo es el punto delicado, porque un umbral ajustado produce fallos intermitentes, uno holgado deja pasar regresiones, y uno estático no distingue el cambio del ruido. | El SLI y el SLO (SLI ≤ objetivo) como origen de los umbrales. El umbral demasiado ajustado o demasiado holgado, y su ajuste progresivo (*ratcheting*). Los umbrales estáticos frente al ruido: falsos positivos y regresiones pequeñas no detectadas; la detección de puntos de cambio como alternativa. Conexión con el taller (razonamiento propio): el margen del umbral se justifica con la variación medida entre ejecuciones. | F5, F2, F3 |
| B7. 5.7, bloque 2: frecuencia, etapa y observabilidad | 120 | No todas las pruebas de rendimiento caben en cada *commit*: en CI corre un subconjunto breve, orientado a detectar que un cambio no empeore el rendimiento, y las pruebas largas van en una etapa propia; la observabilidad en producción completa lo que el pipeline no puede ver. | El objetivo de las pruebas de rendimiento en CI y por qué son un subconjunto. Las pruebas de humo de rendimiento en la etapa de *commit* y la etapa de capacidad separada, como compuerta o con intervención manual. El monitoreo tras la entrega como complemento, con remisión al *shift-right* de 5.1. | F1, F2 |
| **Total** | **870** | | | |

**Presupuesto:** `Alcance.md` asigna al grupo 2,5 páginas y 870 palabras: 5.5, 0,75 páginas (260 palabras); 5.6, 1 página (350), y 5.7, 0,75 páginas (260). Con unas 350 palabras por página, 870 palabras ocupan unas 2,5 páginas, de modo que no queda espacio para tablas ni figuras. Si el redactor necesita recortar, B5 puede apoyarse más en remisiones (el promedio ya está en 5.3 y el entorno compartido en B3).

> **Notas para el redactor:**
>
> - **No repetir el Planteamiento:** 3.2 ya usa a Daly et al. (2020) para el ruido en CI y a Leitner y Bezemer (2017) para las aserciones conservadoras o agresivas. Aquí Daly et al. aporta otros pasajes (la magnitud de la variación entre ejecuciones y el fracaso de los umbrales estáticos) y la dificultad de fijar el umbral se apoya en Humble y Farley (2010). El texto presenta prácticas que responden a esos obstáculos, no los obstáculos de nuevo.
> - **Humble y Farley, terminología:** el libro habla de *capacity tests* y *capacity test stage*. En el texto se traducen como «pruebas de capacidad» solo cuando la fuente se refiere a ese conjunto; si el pasaje vale para las pruebas de rendimiento en general, se dice así y se aclara la equivalencia una vez. No se confunde con la prueba de capacidad del CT-PT (5.4).
> - **Humble y Farley, páginas:** se citan por la paginación impresa (etiqueta) de la copia local convertida a Markdown, no por la del PDF.
> - **Daly et al., cifras:** la variación entre ejecuciones («less than 10%», «as much as 20% or more») describe su sistema; se presenta como un ejemplo industrial, no como un valor general. Las páginas son las de las actas (67–75), en la copia abierta de SPEC.
> - **SLO:** la fuente (F5) es un capítulo de libro sobre operación de servicios, no de pruebas. Se usa solo para definir SLI y SLO; que el umbral de una prueba en CI se derive de un SLO es una conexión del texto.
> - **Calentamiento:** Humble y Farley lo mencionan para plataformas con compiladores que optimizan en tiempo de ejecución (.NET y Java). No se generaliza a todas las plataformas; el texto puede razonar por qué importa para cualquier sistema con cachés o conexiones que se inicializan al principio, sin atribuirlo a la fuente.
> - **Proceso del CT-PT:** las actividades se integran en prosa, no como lista copiada del syllabus (guía, §4).

## Afirmaciones a respaldar
| ID | Pregunta | Bloque | Fuentes |
|---|---|---|---|
| A1 | ¿Qué actividades del proceso distingue el CT-PT para las pruebas de rendimiento, qué tareas propias tiene cada una, por qué las describe como iterativas y cómo se forma el perfil de carga a partir de los perfiles operacionales? | B1 | F1 |
| A2 | ¿Qué exige el CT-PT del entorno y de los datos, por qué la distancia respecto de producción reduce la fiabilidad de las proyecciones y qué puede y qué no puede mostrar una prueba en hardware de menor capacidad, según Humble y Farley? | B2 | F1, F2 |
| A3 | ¿Cómo define el CT-PT la línea base y cómo describen Jiang y Hassan el principio de «no peor que antes»? | B3 | F1, F4 |
| A4 | ¿Qué recomiendan Humble y Farley para obtener resultados estables y reproducibles, qué problema causa un entorno compartido con otras pruebas, y cuánto varían los resultados entre ejecuciones en el sistema de CI que describen Daly et al.? | B3, B5 | F2, F3 |
| A5 | ¿Qué dicen las fuentes sobre el calentamiento antes de medir, el tamaño y la estructura de los datos, y la verificación de que el generador de carga sostiene la carga prevista? | B4 | F1, F2 |
| A6 | ¿Por qué el CT-PT desaconseja probar sin definir antes métricas y objetivos, y cómo critican Humble y Farley los requisitos vagos y la medición sin criterio de aprobación? | B5 | F1, F2 |
| A7 | ¿Cómo definen Jones et al. el SLI y el SLO, qué ocurre según Humble y Farley si el umbral es demasiado alto o demasiado bajo y cómo lo ajustan, y qué problemas encontraron Daly et al. con un umbral estático? | B6 | F5, F2, F3 |
| A8 | ¿Qué pruebas de rendimiento recomiendan el CT-PT y Humble y Farley ejecutar en CI y en qué etapa del pipeline, y qué papel le da el CT-PT al monitoreo después de la entrega? | B7 | F1, F2 |

## Términos nuevos
| Término | Inglés | Forma propuesta | Define |
|---|---|---|---|
| Perfil operacional | operational profile | perfil operacional | 5.5 |
| Calentamiento | warm-up | período de calentamiento (*warm-up*); después, calentamiento | 5.6 |
| Ruido | noise | ruido (variación entre ejecuciones que no se debe al cambio evaluado) | 5.6 |
| Antipatrón | antipattern | antipatrón | 5.6 |
| Umbral | threshold | umbral | 5.7 |
| Indicador de nivel de servicio (SLI) | service level indicator | indicador de nivel de servicio (SLI); después, SLI | 5.7 |
| Prueba de humo de rendimiento | performance smoke test, guard test | prueba de humo de rendimiento | 5.7 |
| Detección de puntos de cambio | change point detection | detección de puntos de cambio | 5.7 |

Además, al aprobarse el plan, en el glosario se marca 5.5 como sección que define el sistema bajo prueba, el entorno de prueba y el generador de carga; 5.6, la línea base y el criterio de aceptación, y 5.7, la regresión de rendimiento, la aserción de rendimiento, el SLO y la observabilidad.

## Fuentes
| ID | Referencia y enlace | Acceso | Disponibilidad |
|---|---|---|---|
| F1 | International Software Testing Qualifications Board. (2018). *Certified Tester Foundation Level Specialist syllabus: Performance testing* (Versión 2018). https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf | Abierta | https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf |
| F2 | Humble, J., & Farley, D. (2010). *Continuous delivery: Reliable software releases through build, test, and deployment automation*. Addison-Wesley. | Cerrada | Local: `Adjuntos/Local/Continuous-Delivery - Jez Humble & David Farley/` |
| F3 | Daly, D., Brown, W., Ingo, H., O'Leary, J., & Bradford, D. (2020). The use of change point detection to identify software performance regressions in a continuous integration system. En *Proceedings of the 2020 ACM/SPEC International Conference on Performance Engineering (ICPE '20)* (pp. 67–75). ACM. https://doi.org/10.1145/3358960.3375791 | Abierta (CC BY 4.0) | https://research.spec.org/icpe_proceedings/2020/proceedings/p67.pdf |
| F4 | Jiang, Z. M., & Hassan, A. E. (2015). A survey on load testing of large-scale software systems. *IEEE Transactions on Software Engineering, 41*(11), 1091–1118. https://doi.org/10.1109/TSE.2015.2445340 | Abierta (copia del autor) | https://www.eecs.yorku.ca/~zmjiang/publications/tse2015_jiang.pdf |
| F5 | Jones, C., Wilkes, J., Murphy, N., & Smith, C. (2016). Service level objectives. En B. Beyer, C. Jones, J. Petoff, & N. R. Murphy (Eds.), *Site reliability engineering: How Google runs production systems* (cap. 4). O'Reilly Media. https://sre.google/sre-book/service-level-objectives/ | Abierta (CC BY-NC-ND 4.0) | https://sre.google/sre-book/service-level-objectives/ |

**Verificación (2026-11-07):**

- **F1:** ya estaba en `Referencias.md`. Pasajes localizados en el cuerpo, con la paginación impresa:
  - El carácter iterativo y las actividades del proceso (planificación, monitoreo y control, análisis, diseño, implementación, ejecución y cierre): §3.1, pp. 23–24.
  - Las pruebas de rendimiento en CI, como subconjunto y con el objetivo de asegurar que un cambio no empeore el rendimiento: §3.4, p. 30. El monitoreo tras la entrega: §3.4, p. 31.
  - No probar sin entender antes qué mediciones y métricas hacen falta: §2.1.1, p. 17. La falta de oráculos y de requisitos de rendimiento bien formulados: §2.4, p. 21. Las herramientas de monitoreo continuo: §2.3, p. 21.
  - La línea base: §4.1.2, apartado «Acceptance Criteria», p. 34. Los perfiles operacionales que se agregan en un perfil de carga: §4.1.2, apartado «Profiles», p. 35.
  - El entorno lo más parecido posible a producción, el rendimiento como función no lineal del entorno y el tamaño y la estructura de los datos: §4.2.8, p. 48. El laboratorio aislado para ver variaciones pequeñas: p. 49. Monitorear las máquinas que generan la carga y validar el montaje antes de ejecutar: p. 49.
  - Las comprobaciones automáticas cuando la prueba corre en CI: §4.3, p. 51.
- **F2:** ya estaba en `Referencias.md`, con copia local. Capítulo 9, «Testing Nonfunctional Requirements», leído completo en la copia convertida a Markdown (pp. 225–248 impresas). Pasajes clave:
  - Los requisitos vagos («as fast as possible», «two seconds»): pp. 227–228.
  - La medición frente a la prueba, y el umbral demasiado alto (fallos intermitentes) o demasiado bajo (no detecta una caída a la mitad), con el aislamiento del entorno y el ajuste progresivo del umbral: pp. 232–233.
  - El entorno de capacidad y la extrapolación especulativa; las pruebas en hardware de menor capacidad detectan problemas graves, pero no demuestran que se cumplan los objetivos: pp. 234–236.
  - Validar con un *stub* que la prueba puede sostener la tasa necesaria, y ejecutar pruebas automáticas de capacidad para cada cambio que supera las etapas anteriores: p. 244.
  - El calentamiento de .NET y Java, las *guard tests* como pruebas de humo de rendimiento en la etapa de *commit* y el entorno compartido con otras pruebas automatizadas: p. 245.
  - La etapa de capacidad separada, como compuerta con intervención manual o no: p. 246.
- **F3:** ya estaba en `Referencias.md`. La copia abierta de las actas en SPEC (licencia CC BY 4.0) coincide con la referencia (ICPE '20, pp. 67–75, DOI 10.1145/3358960.3375791). La variación entre ejecuciones de su sistema (menos del 10 % en la mayoría de las pruebas y hasta 20 % o más en algunas): §1, p. 67. Los falsos positivos y las regresiones pequeñas no detectadas con un umbral estático del 10 %: §1.1, p. 68. También se revisó la versión de arXiv (2003.00584), que tiene el mismo texto; se cita la de las actas.
- **F4:** ya estaba en `Referencias.md`. El principio de «no peor que antes» para derivar criterios de aprobación cuando faltan requisitos no funcionales: §2.1.1, p. 1092.
- **F5:** nueva. La página de sre.google identifica el capítulo 4, «Service Level Objectives», escrito por Chris Jones, John Wilkes y Niall Murphy con Cody Smith, y editado por Betsy Beyer. El prefacio del libro en el mismo sitio da los editores (Betsy Beyer, Chris Jones, Jennifer Petoff y Niall Richard Murphy), la editorial (O'Reilly), el año (2016) y el ISBN 978-1-491-92912-4; el sitio publica el texto bajo licencia CC BY-NC-ND 4.0. Las definiciones de SLI y de SLO, y la estructura «SLI ≤ target», están en los apartados «Indicators» y «Objectives». Es un libro de referencia de la práctica industrial, no arbitrado, admitido como documentación de autoría identificable (`Alcance.md` §5.3); hay una edición nueva, reescrita, pero se cita la de 2016, que es la que el sitio publica en abierto.
- **Descartadas:**
  - Ingo y Daly (2020), *Automated system performance testing at MongoDB*: sigue descartada por lo mismo que en el Planteamiento (sin datos de publicación completos en arXiv, y F3 cubre el ruido).
  - Leitner y Bezemer (2017): ya sostiene en 3.2 la dificultad de fijar aserciones; repetirla aquí duplicaría el argumento.
  - Amazon Web Services (s. f.-b), *Performance efficiency*: se revisó la página por si servía para 5.6 o 5.7, pero es solo un índice del pilar, sin contenido que respalde las afirmaciones de este grupo El usuario decidió eliminarla de `Referencias.md` al aprobar el plan.
  - Molyneaux, *The Art of Application Performance Testing*: fuente ancla del alcance, pero cerrada y sin copia local; F1 y F2 cubren el proceso y las prácticas.

## Registro de búsqueda
| # | Fecha | Buscador o base | Cadena | Resultados revisados | Elegidas / descartadas (motivo) |
|---|---|---|---|---|---|
| 1 | 2026-11-07 | Buscador web | `Google "Site Reliability Engineering" book chapter "Service Level Objectives" SLI SLO definition sre.google` | 19: el capítulo en sre.google (dos variantes de idioma), el capítulo «Implementing SLOs» del *workbook*, blogs y resúmenes (Medium, Substack, dev.to, Coralogix, Squadcast, Blameless), un capítulo de Manning y páginas comerciales | Elegida: F5, el capítulo original en sre.google. Descartados: resúmenes de terceros (no son la fuente) y el *workbook* (más extenso de lo necesario para dos definiciones). |
