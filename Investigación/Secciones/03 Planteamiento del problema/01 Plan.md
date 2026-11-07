# Plan — Planteamiento del problema

**Estado:** Aprobado | **Modo:** Completo | **Versión:** 3 | **Fecha:** 2026-11-07 | **Presupuesto:** 1 050 palabras

> **Cambios en la versión 3:** condensación al nuevo presupuesto de `Alcance.md` (documento de 30–35 páginas, aprobado por el usuario): de 1 550 a 1 050 palabras. Se conservan las siete fuentes y la pregunta-problema. Las afirmaciones bajan a 10 (tope de 1 por cada 100 palabras): A2 se funde con A1, A4 con A3, A7 con A6 y A8 con A9; los IDs vigentes se conservan. La sección «Condensación» indica qué se recorta del borrador aprobado.
>
> **Cambios en la versión 2:** aprobado por el usuario sin cambios, incluida la pregunta-problema. Las fuentes nuevas (F1, F2, F6 y F7) se agregan a `Referencias.md`.

## Objetivo y alcance

Sección 3 del documento (`Alcance.md` §5.2; `Enunciado.md` §3). Responde a PI-2: qué problemas existen en la industria y en la academia para adoptar y automatizar las pruebas de rendimiento. El enunciado pide «identificación y documentación de la problemática actual en la industria y en la academia respecto al uso, adopción o limitaciones de las pruebas automatizadas». El alcance exige evidencia empírica (estudios de práctica en proyectos *open source* y encuestas industriales) y prohíbe toda estadística sin fuente verificable.

**Incluye:**

- Industria: pruebas escasas, esporádicas o tardías y fuera de los pipelines; entornos poco representativos; costo de la infraestructura de carga; resultados ruidosos y difíciles de interpretar; complejidad de las herramientas.
- Academia: poca presencia del rendimiento en la formación y una agenda de investigación distinta de la que necesita la práctica.
- Cierre: la pregunta-problema y la justificación del taller.

**No incluye (lo cubren otras secciones):**

- Por qué importa el rendimiento y el caso HealthCare.gov contado en detalle, que ya están en la Introducción. Aquí el caso solo se retoma por el tiempo de pruebas que se recortó.
- Definiciones, tipos de prueba y métricas (Marco teórico §5.3 y §5.4).
- Las soluciones: buenas prácticas, umbrales en CI y detección de regresiones (Marco teórico §5.6 y §5.7). Aquí se plantean los obstáculos, no cómo se superan.
- El costo de licencias de cada herramienta, que se compara en el Marco teórico §5.8. Aquí solo se trata el costo de la infraestructura de carga.
- Los *microbenchmarks* como tema. F1 estudia proyectos donde predominan; se usa solo como evidencia del estado de la práctica.

**Forma:** un párrafo de apertura sin subtítulo y cuatro subsecciones con subtítulo (3.1 a 3.4).

## Esquema argumental
| Bloque | Palabras | Idea central | Contenido | Insumos y fuentes |
|---|---|---|---|---|
| B0. Apertura (sin subtítulo) | 70 | Aunque el rendimiento es un atributo de calidad reconocido, la evidencia muestra que se prueba poco y mal: hay una brecha entre su importancia y la práctica. | Puente desde la Introducción, sin repetirla, y anuncio de los dos frentes: industria y academia. | Razonamiento propio |
| B1. 3.1 La práctica en la industria | 300 | Las pruebas de rendimiento existen, pero son escasas, esporádicas y rara vez forman parte del flujo automatizado de entrega. | Proyectos Java *open source*: pocas pruebas, rara vez actualizadas y a cargo de pocos desarrolladores. Encuesta industrial: frecuencia de las evaluaciones, tiempo dedicado y falta de integración en los pipelines, aclarando el tamaño de la muestra. HealthCare.gov como ejemplo de pruebas comprimidas por el calendario. | F1, F2, F5 |
| B2. 3.2 Obstáculos para automatizarlas | 300 | No se prueba poco por descuido: automatizar estas pruebas choca con obstáculos técnicos concretos de entorno, costo, interpretación de resultados y complejidad de las herramientas. | Entorno realista difícil de montar. Infraestructura de carga propia o alquilada. Pruebas largas y con mucho volumen de datos que analizar. Ruido en las mediciones e insostenibilidad de la revisión manual. Herramientas complejas que exigen conocimiento experto. Dificultad para encajar en las herramientas estándar de CI y para fijar aserciones de rendimiento. | F3, F4, F2, F1 |
| B3. 3.3 La brecha en la academia | 200 | La formación y la investigación no compensan esa dificultad: el rendimiento ocupa poco lugar en los cursos, y lo que la investigación produce no llega a la práctica. | Cursos que descuidan los atributos de calidad transversales, como el rendimiento. Diferencia entre los temas de las conferencias industriales (donde *performance* figura) y los de las académicas. Desajuste entre lo que entrega la investigación en ingeniería de rendimiento y lo que buscan los profesionales. | F7, F6, F2 |
| B4. 3.4 Planteamiento del problema | 180 | El problema es la distancia entre la necesidad de evaluar el rendimiento de forma continua y la capacidad real de los equipos para automatizarlo; el taller ataca esa distancia con un caso práctico y reproducible. | La pregunta-problema (propuesta abajo). Justificación del taller: cada obstáculo de B2 y B3 se conecta con lo que el taller demuestra (entorno propio y controlado, herramienta con curva de aprendizaje acotada, umbrales en CI, aplicación con los compañeros). Sin anticipar decisiones de la Fase 2 que siguen pendientes. | `Alcance.md` §1, §3 (PI-5) y §7; `Enunciado.md` (objetivos 4 y 5) |
| **Total** | **1 050** | | | |

## Condensación (versión 3)

El borrador v3 aprobado tiene 1 520 palabras. Las ideas centrales no cambian; se recortan desarrollos y detalles:

- **B0:** dos o tres oraciones, sin la frase sobre lo que «cabría esperar».
- **B1:** de Leitner y Bezemer quedan los 111 proyectos, el peso pequeño de las pruebas, su escasa actualización, el 16 % y la conclusión (E1–E4); sale el párrafo sobre la mezcla con las pruebas funcionales y la comunicación de resultados (E26). De la encuesta quedan el tamaño de la muestra, la frecuencia, el tiempo dedicado y la falta de integración en los pipelines (E5–E8); sale el reparto entre personas dedicadas y no dedicadas (E27). HealthCare.gov queda en una oración (E9).
- **B2:** el entorno se dice en una oración con E10–E12 (desafío y hardware propio o nube). La interpretación junta E13–E16 en un párrafo: análisis largo, ruido a escala y la dificultad de fijar aserciones, que se conserva porque prepara la pregunta-problema. La complejidad conserva E17 y E19; salen el detalle de E18 y la imagen de la herramienta de referencia (E28).
- **B3:** Bondi y Xiao en dos oraciones (E20, E21). Garousi y Felderer en una (E22–E24). La transferencia queda en el desajuste (E25); sale el ejemplo de los modelos de rendimiento (E29, E30).
- **B4:** el párrafo de síntesis se acorta a tres oraciones y el del taller conserva una oración por obstáculo, incluida la estabilidad del veredicto.

Las filas que dejan de citarse (E18, E26, E27, E28, E29, E30) pasan a «Filas no usadas» de la evidencia. Todas las fuentes siguen citadas.

**Pregunta-problema propuesta:** ¿Cómo pueden integrarse pruebas de rendimiento automatizadas sobre una API REST en un pipeline de CI, con un costo de adopción bajo y con resultados que permitan decidir de forma confiable si un cambio degradó el desempeño?

## Afirmaciones a respaldar
| ID | Pregunta | Bloque | Fuentes |
|---|---|---|---|
| A1 | ¿Qué proporción del conjunto de pruebas representan las pruebas de rendimiento en los proyectos Java *open source* estudiados, con qué frecuencia se actualizan, quién las mantiene, qué proporción usa un *framework* dedicado y qué concluyen los autores? (incluye la antigua A2) | B1 | F1 |
| A3 | ¿Con qué frecuencia realizan evaluaciones de rendimiento los participantes de la encuesta, cuánto de su tiempo les dedican, cuántas respuestas tuvo la encuesta y están integradas esas evaluaciones en los pipelines de entrega? (incluye la antigua A4) | B1 | F2 |
| A5 | ¿Cómo afectaron los retrasos del calendario de HealthCare.gov al tiempo disponible para las pruebas? | B1 | F5 |
| A6 | ¿Qué dificultad plantea configurar un entorno de prueba realista para las pruebas de carga, y qué infraestructura requiere (hardware propio o nube alquilada)? (incluye la antigua A7) | B2 | F3 |
| A9 | ¿Por qué las pruebas con cargas realistas son más difíciles de analizar, qué papel juega el ruido de la infraestructura en la detección de cambios de rendimiento y por qué no basta la revisión manual de miles de resultados? (incluye la antigua A8) | B2 | F3, F4 |
| A10 | ¿Qué barrera identifica la encuesta en la complejidad de los enfoques y las herramientas de ingeniería de rendimiento, y qué conocimiento exigen? | B2 | F2 |
| A11 | ¿Qué señalan Leitner y Bezemer sobre la integración de las pruebas de rendimiento con las herramientas estándar de CI y sobre la fragilidad de las aserciones de rendimiento? | B2 | F1 |
| A12 | ¿Qué observan Bondi y Xiao sobre el lugar del rendimiento en los cursos de ingeniería de software y en el ciclo de desarrollo? | B3 | F7 |
| A13 | ¿Qué diferencia encuentran Garousi y Felderer entre los temas de las conferencias de pruebas industriales y las académicas, y dónde aparece el rendimiento? | B3 | F6 |
| A14 | ¿Qué desajuste señala la encuesta entre lo que entrega la investigación en ingeniería de rendimiento y lo que buscan los profesionales? | B3 | F2 |

> **Notas para el redactor:**
>
> - **A3:** la encuesta tiene 26 respuestas completas y 108 parciales. El texto debe decirlo para no generalizar las cifras a toda la industria.
> - **A4:** la frase más directa («automatic performance evaluations are usually not integrated into automatic delivery pipelines») está en el resumen. Hay que respaldarla con el cuerpo (§4 y §5.3); si el cuerpo no lo dice, no se usa.
> - **A12:** la afirmación de que los cursos descuidan el rendimiento está en el resumen de F7. En el cuerpo, la frase es que el rendimiento suele ser «an afterthought». Es una observación de los autores, no una medición, y el texto debe presentarla así.
> - **A5 y A9:** ya hay filas aprobadas en la evidencia de la Introducción (E13 de GAO-14-694 y E27 y E29 de Daly et al.). Pueden reutilizarse, pero se registran de nuevo en la evidencia de esta sección.
> - **F1:** el estudio es de proyectos Java *open source* y muchas de sus pruebas son *microbenchmarks*. Se usa solo para describir el estado de la práctica, sin tratar los *microbenchmarks* como tema.

## Fuentes
| ID | Referencia y enlace | Acceso | Disponibilidad |
|---|---|---|---|
| F1 | Leitner, P., & Bezemer, C.-P. (2017). An exploratory study of the state of practice of performance testing in Java-based open source projects. En *Proceedings of the 8th ACM/SPEC International Conference on Performance Engineering (ICPE '17)* (pp. 373–384). ACM. https://doi.org/10.1145/3030207.3030213 | Abierta | https://research.spec.org/icpe_proceedings/2017/proceedings/p373.pdf |
| F2 | Bezemer, C.-P., Eismann, S., Ferme, V., Grohmann, J., Heinrich, R., Jamshidi, P., Shang, W., van Hoorn, A., Villavicencio, M., Walter, J., & Willnecker, F. (2019). How is performance addressed in DevOps? A survey on industrial practices. En *Proceedings of the 2019 ACM/SPEC International Conference on Performance Engineering (ICPE '19)* (pp. 45–50). ACM. https://doi.org/10.1145/3297663.3309672 | Abierta | https://research.spec.org/icpe_proceedings/2019/proceedings/p45.pdf · https://arxiv.org/pdf/1808.06915 |
| F3 | Jiang, Z. M., & Hassan, A. E. (2015). A survey on load testing of large-scale software systems. *IEEE Transactions on Software Engineering, 41*(11), 1091–1118. https://doi.org/10.1109/TSE.2015.2445340 | Abierta (copia del autor) | https://www.eecs.yorku.ca/~zmjiang/publications/tse2015_jiang.pdf |
| F4 | Daly, D., Brown, W., Ingo, H., O'Leary, J., & Bradford, D. (2020). The use of change point detection to identify software performance regressions in a continuous integration system. En *Proceedings of the 2020 ACM/SPEC International Conference on Performance Engineering (ICPE '20)* (pp. 67–75). ACM. https://doi.org/10.1145/3358960.3375791 | Abierta (CC BY 4.0) | https://research.spec.org/icpe_proceedings/2020/proceedings/p67.pdf |
| F5 | U.S. Government Accountability Office. (2014). *Healthcare.gov: Ineffective planning and oversight practices underscore the need for improved contract management* (GAO-14-694). https://www.gao.gov/products/gao-14-694 | Abierta | https://www.gao.gov/assets/gao-14-694.pdf |
| F6 | Garousi, V., & Felderer, M. (2017). Worlds apart: Industrial and academic focus areas in software testing. *IEEE Software, 34*(5), 38–45. https://doi.org/10.1109/MS.2017.3641116 | Abierta (manuscrito aceptado, CC BY-NC-ND) | https://edepot.wur.nl/438223 |
| F7 | Bondi, A. B., & Xiao, L. (2023). Early progress on enhancing existing software engineering courses to cultivate performance awareness. En *Companion of the 2023 ACM/SPEC International Conference on Performance Engineering (ICPE '23 Companion)* (pp. 345–349). ACM. https://doi.org/10.1145/3578245.3584352 | Abierta | https://research.spec.org/icpe_proceedings/2023/companion/p345.pdf |

**Verificación (2026-11-07):**

- **F1, F2, F6 y F7:** título, autores, publicación, páginas y fecha comprobados en Crossref a partir del DOI, y texto completo leído en el enlace de disponibilidad.
  - **F1:** pasajes de A1, A2 y A11 localizados en el cuerpo, incluido el 16 % de proyectos con *framework* dedicado.
  - **F2:** pasajes de A3 (§4.1, con las frecuencias), A10 (§5.1) y A14 (§5) localizados en el cuerpo. Para A4, ver la nota para el redactor.
  - **F6:** el manuscrito aceptado incluye la tabla de palabras más frecuentes de cada tipo de conferencia; *performance* aparece en la de las industriales.
  - **F7:** el texto completo es de 5 páginas (ICPE '23 Companion).
- **F3, F4 y F5:** ya verificadas en el plan de la Introducción y presentes en `Referencias.md`. Los pasajes de F3 para A6–A8 se localizaron en el cuerpo de la copia del autor (diseño de la carga y ejecución de la prueba); el redactor debe precisar la sección y la página.
- **Descartadas:**
  - Garousi, Rainer, Lauvås y Arcuri (2020), *Software-testing education: A systematic literature mapping*: no trata el rendimiento de forma específica.
  - Ingo y Daly (2020), *Automated system performance testing at MongoDB*: la versión de arXiv no tiene datos de publicación completos, y lo que aporta sobre el ruido ya lo cubre F4.
  - Smith (2021), *Software performance engineering education: What topics should be covered?*: es el resumen de una presentación de una página, sin evidencia.
