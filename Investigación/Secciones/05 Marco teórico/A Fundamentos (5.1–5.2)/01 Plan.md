# Plan — Marco teórico, grupo A: Fundamentos (5.1–5.2)

**Estado:** Aprobado | **Modo:** Completo | **Versión:** 5 | **Fecha:** 2026-11-07 | **Presupuesto:** 550 palabras + 0,9 págs. de tabla y figura (2,5 págs. en total)

> **Cambios en la versión 5:** corrige el espacio de la Figura 1 y la Tabla 1 para que sumen las 0,9 páginas del encabezado, como señaló la auditoría (rondas 3 y 4): 0,5 y 0,4 páginas, según el reparto de `Alcance.md` §5.4 (5.1: 350 palabras + Figura 1 en 1,5 páginas; 5.2: 200 palabras + Tabla 1 en 1 página). No cambia el contenido ni las afirmaciones.
>
> **Cambios en la versión 4:** condensación al nuevo presupuesto de `Alcance.md` (documento de 30–35 páginas, aprobado por el usuario): de 850 a 550 palabras. Se conservan las siete fuentes, la Figura 1 y la Tabla 1. Las afirmaciones bajan a 5 (tope de 1 por cada 100 palabras): A2 se funde con A1, A6 con A5 y A8 con A7; los IDs vigentes se conservan. La sección «Condensación» indica qué se recorta.
>
> **Cambios en la versión 3:** aprobado por el usuario sin cambios. Las fuentes nuevas (F1, F3, F4 y F6) se agregan a `Referencias.md`, y los términos nuevos, a `Glosario.md`.
>
> **Cambios en la versión 2:** el usuario aportó Humble y Farley (2010) en copia local (F6). Los *quality gates* dejan de ser síntesis propia: se apoyan en las compuertas (*gates*) del *deployment pipeline* de F6, y el término «quality gates» en Bezemer et al. (2019, F7), que cita F6. Se quitan los criterios de salida del CTFL (A4), que ya no hacen falta. Por preferencia del usuario, el texto usa «CI/CD» siempre que se pueda. Se actualiza la ruta local de F5.

## Objetivo y alcance

Subsecciones 5.1 y 5.2 del Marco teórico (`Alcance.md` §5.4; `Enunciado.md` §5, «fundamentación teórica sobre el aseguramiento de la calidad en la etapa del ciclo de vida seleccionada»). Contribuyen a PI-1 (qué métricas definen las pruebas según ISTQB e ISO/IEC 25010) y a PI-3 (cómo se integran en CI/CD). Ubican el rendimiento en dos marcos: el ciclo de vida, donde está la actividad de prueba, y el modelo de calidad, donde está el atributo que se prueba.

**Incluye:**

- 5.1: la distinción entre aseguramiento de la calidad y pruebas; el ciclo de vida y el modelo en V; los niveles de prueba y dónde se concentran las pruebas de rendimiento; DevOps y CI/CD; los *quality gates*; *shift-left* y *shift-right*.
- 5.2: la eficiencia de desempeño en ISO/IEC 25010:2023 y sus tres subcaracterísticas: comportamiento temporal, utilización de recursos y capacidad.

**No incluye (lo cubren otras secciones o grupos):**

- Por qué importa el rendimiento y la definición general de eficiencia de desempeño, que ya están en la Introducción. 5.2 no repite la definición: la da por conocida y desarrolla las subcaracterísticas.
- La justificación de concentrarse en la fase de implementación, que ya está en la Introducción (B2). Aquí solo se describe el marco que la sostiene.
- Las métricas (tiempo de respuesta, *throughput*, percentiles) y los tipos de prueba, que van en el grupo B (5.3–5.4). 5.2 las nombra solo como lo que observa cada subcaracterística.
- El proceso de pruebas de rendimiento y su automatización en CI/CD (umbrales, detección de regresiones), que van en el grupo C (5.5–5.7). 5.1 presenta CI/CD y los *quality gates* como marco general, sin entrar en cómo se aplican al rendimiento.
- Las herramientas, que van en el grupo D (5.8).
- *Shift-right* más allá de una mención (`Alcance.md` §4: «Mencionar, ≤ 1 párrafo»).

**Forma:** dos subsecciones con subtítulo (5.1 y 5.2). Dentro de 5.1, tres bloques sin subtítulo.

## Esquema argumental
| Bloque | Palabras | Idea central | Contenido | Insumos y fuentes |
|---|---|---|---|---|
| B1. 5.1, bloque 1: ciclo de vida y niveles de prueba | 130 | Asegurar la calidad es un enfoque de proceso que acompaña todo el ciclo de vida; las pruebas son una de sus formas de control, y las de rendimiento rinden más en los niveles superiores, donde el sistema está integrado y el entorno se parece al de operación. | La diferencia entre aseguramiento de la calidad y pruebas. Los modelos de ciclo de vida y el modelo en V, en el que cada actividad de desarrollo tiene una de prueba. Los cinco niveles de prueba. Los niveles de sistema y de integración de sistemas, y el entorno que necesitan. Remite a la Figura 2. | F1, F2 |
| B2. 5.1, bloque 2: DevOps, CI/CD y *quality gates* | 120 | CI/CD convierte las pruebas en un paso automático de cada cambio, y un *quality gate* es la forma de que ese paso decida si el cambio avanza. | DevOps y sus beneficios para las pruebas, incluida la visibilidad de las características no funcionales. Qué abarca CI/CD: integración continua, entrega continua y despliegue continuo. El pipeline de despliegue como modelo automatizado del camino de cada cambio hasta producción. Sus etapas como compuertas: la de *commit*, la de pruebas de aceptación y la de pruebas de capacidad, cuyos resultados pueden funcionar como compuerta o solo informar una decisión humana. El término *quality gate*. | F1, F3, F6, F7 |
| B3. 5.1, bloque 3: *shift-left* y *shift-right* | 100 | Probar antes (*shift-left*) no reemplaza las pruebas posteriores, y probar en producción (*shift-right*) las complementa. Este trabajo se sitúa entre ambos: valida el sistema integrado antes del despliegue y usa CI como puente. | *Shift-left* según el CTFL, incluidas las pruebas no funcionales desde el nivel de componente y la advertencia de no descuidar las posteriores. *Shift-right* como mención: pruebas en producción y umbrales de rendimiento monitoreados en producción. La ubicación de este trabajo, con remisión a `Alcance.md` §1. | F1, F4, F2; `Alcance.md` §1 |
| B4. 5.2 Eficiencia de desempeño en ISO/IEC 25010 | 200 | La norma descompone la eficiencia de desempeño en tres subcaracterísticas, y cada una corresponde a un objetivo distinto de las pruebas de rendimiento; por eso la norma sirve para decidir qué medir. | Las tres subcaracterísticas y su definición. La edición de 2023 conserva las tres de la de 2011. El objetivo de prueba que el CT-PT asocia a cada una (el comportamiento temporal es el más común). Qué observa cada una, como puente a 5.3. Remite a la Tabla 1. | F5, F2 |
| **Total** | **550** | | | |

## Condensación (versión 4)

El borrador v2 aprobado tiene 886 palabras. Las ideas centrales no cambian; la Figura 2 y la Tabla 1 se mantienen sin cambios y cargan más contenido:

- **B1:** la distinción entre aseguramiento de la calidad y pruebas (E1), el modelo en V y los cinco niveles (E2–E4) y el papel de los niveles de sistema y de integración de sistemas en rendimiento (E5, E6), en un párrafo.
- **B2:** sale la oración sobre los beneficios de DevOps para las pruebas (E7, E8). Quedan CI/CD (E9), el pipeline de despliegue y sus compuertas (E10, E11, E13) y el término *quality gate* (E14). E12 sigue citada en la fuente de la Figura 2.
- **B3:** *shift-left* (E15, E16), *shift-right* (E17, E18) y la ubicación del trabajo, más breve.
- **B4:** la descomposición en tres subcaracterísticas (E19–E22) y el argumento de por qué distinguirlas (E23), con un ejemplo en una API. La oración sobre los recursos que cuenta la norma sale de la prosa; E26 sigue citada en la Tabla 1.

E7 y E8 pasan a «Filas no usadas». Todas las fuentes siguen citadas.

**Presupuesto:** `Alcance.md` asigna 3 páginas a 5.1 y 5.2 (2 + 1) y 5 400 palabras «+ tablas/figuras» a todo el Marco teórico. Con unas 350 palabras por página, 850 palabras ocupan unas 2,4 páginas, y la tabla y la figura completan las 3. Las palabras que este grupo deja libres frente a la proporción del Marco teórico (unas 950) se reservan para los grupos B y C.

> **Notas para el redactor:**
>
> - ***Quality gate*:** F6 no usa esa expresión: habla de compuertas (*gates*) del *deployment pipeline*. El término «quality gates» aparece en la introducción de F7 (§1, p. 45), que cita F6. El texto puede decir que lo que Humble y Farley describen como compuertas del pipeline es lo que la literatura posterior llama *quality gates*, con las dos citas. La etapa de pruebas de capacidad como compuerta (F6, p. 128) es el pasaje clave para el resto del Marco teórico.
> - **CI/CD (preferencia del usuario):** el texto usa «CI/CD» siempre que se hable de estas prácticas en conjunto, y «CI» cuando sea solo la integración continua. La diferencia entre entrega continua y despliegue continuo se explica una sola vez, con las palabras completas; «CD» no se usa sola, porque F1 la usa para la entrega y F3 para el despliegue. Al citar F3 no se reproducen sus siglas.
> - **F6 en Markdown:** la copia local en `.md` marca cada página con `<!-- Pagina PDF: n; etiqueta: m -->`. En la ubicación de la evidencia se usa la etiqueta, que es la página impresa del libro. El capítulo 9 («Testing Nonfunctional Requirements») queda anotado para el grupo C.
> - **F4:** es literatura gris (documentación de Microsoft). Se usa solo para la definición de *shift-right*, en una oración.
> - **Filas reutilizables:** E20 y E21 de la evidencia de la Introducción (F2, §1.3.2) respaldan qué evalúan las pruebas de rendimiento en los niveles de sistema y de integración de sistemas. Se registran de nuevo en esta sección. E22 ya se citó en la Introducción; si se usa aquí, no se repite la misma idea.

## Tablas y figuras
| ID | Tipo | Título | Bloque | Contenido | Fuentes | Espacio (págs.) |
|---|---|---|---|---|---|---|
| Figura 2 | Diagrama | Las pruebas de rendimiento en el modelo en V y en el pipeline de CI | B1, B3 | A la izquierda, el modelo en V con los cinco niveles de prueba, marcando sistema e integración de sistemas como foco de este trabajo y el nivel de componente como opción de *shift-left*. A la derecha, el pipeline (integración → entrega → despliegue) con el *quality gate* de rendimiento antes del despliegue. Producción, con su monitoreo, como *shift-right*. | Elaboración propia a partir de F1, F2 y F3 | 0,5 |
| Tabla 1 | Tabla | Subcaracterísticas de la eficiencia de desempeño | B4 | Tres filas (comportamiento temporal, utilización de recursos, capacidad) y tres columnas: definición en ISO/IEC 25010:2023, objetivo de prueba según el CT-PT y qué se observa (puente a 5.3). | F5, F2; la última columna es elaboración propia | 0,4 |

## Afirmaciones a respaldar
| ID | Pregunta | Bloque | Fuentes |
|---|---|---|---|
| A1 | ¿Cómo distingue el CTFL el aseguramiento de la calidad de las pruebas, qué lugar da al modelo en V y a la correspondencia entre actividades de desarrollo y de prueba, y qué evalúan los niveles de sistema y de integración de sistemas, en general (CTFL) y para el rendimiento (CT-PT)? (incluye la antigua A2) | B1 | F1, F2 |
| A3 | ¿Cómo definen Shahin et al. la integración continua, la entrega continua y el despliegue continuo, y qué beneficios para las pruebas atribuye el CTFL a DevOps y a CI/CD? | B2 | F3, F1 |
| A4 | ¿Cómo definen Humble y Farley el *deployment pipeline*, qué papel cumplen sus compuertas (*commit*, pruebas de aceptación, pruebas de capacidad) y dónde aparece el término «quality gates»? | B2 | F6, F7 |
| A5 | ¿Cómo define el CTFL el *shift-left* y qué dice sobre las pruebas no funcionales; qué es *shift-right* según la guía de Microsoft, y qué propone el CT-PT sobre umbrales de rendimiento monitoreados en producción? (incluye la antigua A6) | B3 | F1, F4, F2 |
| A7 | ¿Cómo define ISO/IEC 25010:2023 cada subcaracterística de la eficiencia de desempeño, se mantienen respecto de la edición de 2011, y qué objetivo de las pruebas de rendimiento asocia el CT-PT a cada una? (incluye la antigua A8) | B4, Tabla 1 | F5, F2 |

## Términos nuevos
| Término | Inglés | Forma propuesta | Define |
|---|---|---|---|
| Aseguramiento de la calidad | quality assurance (QA) | aseguramiento de la calidad; sin sigla en el texto | 5.1 |
| Modelo en V | V-model | modelo en V | 5.1 |
| Nivel de prueba | test level | nivel de prueba; niveles: prueba de componentes, de integración de componentes, de sistema, de integración de sistemas y de aceptación | 5.1 |
| CI/CD | CI/CD | CI/CD: integración continua junto con entrega o despliegue continuos. Es el término preferido cuando se habla de estas prácticas en conjunto | 5.1 |
| Despliegue continuo | continuous deployment | despliegue continuo, sin sigla | 5.1 |
| Pipeline de despliegue | deployment pipeline | pipeline de despliegue (*deployment pipeline*) la primera vez; después, pipeline | 5.1 |
| DevOps | DevOps | DevOps (sin cursiva, asimilado) | 5.1 |
| Comportamiento temporal | time behaviour | comportamiento temporal | 5.2 |
| Utilización de recursos | resource utilization | utilización de recursos | 5.2 |
| Capacidad | capacity | capacidad (subcaracterística de ISO/IEC 25010; no confundir con la prueba de capacidad de 5.4) | 5.2 |

Además, al aprobarse el plan, en el glosario se marca 5.1 como sección que define la entrega continua, el *quality gate*, *shift-left* y *shift-right*, y la forma de la entrega continua pasa a «entrega continua», sin sigla propia (la sigla CD deja de usarse sola).

## Fuentes
| ID | Referencia y enlace | Acceso | Disponibilidad |
|---|---|---|---|
| F1 | International Software Testing Qualifications Board. (2024). *Certified Tester Foundation Level syllabus* (Versión 4.0.1). https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf | Abierta | https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf |
| F2 | International Software Testing Qualifications Board. (2018). *Certified Tester Foundation Level Specialist syllabus: Performance testing* (Versión 2018). https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf | Abierta | https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf |
| F3 | Shahin, M., Ali Babar, M., & Zhu, L. (2017). Continuous integration, delivery and deployment: A systematic review on approaches, tools, challenges and practices. *IEEE Access, 5*, 3909–3943. https://doi.org/10.1109/ACCESS.2017.2685629 | Abierta (acceso abierto de IEEE; preprint en arXiv) | https://arxiv.org/pdf/1703.07019 |
| F4 | Microsoft. (2022, 21 de julio). *Shift right to test in production*. Microsoft Learn. Consultado el 2026-11-07. https://learn.microsoft.com/en-us/devops/deliver/shift-right-test-production | Abierta | https://learn.microsoft.com/en-us/devops/deliver/shift-right-test-production |
| F5 | ISO/IEC. (2023). *ISO/IEC 25010:2023 Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (2.ª ed.). https://www.iso.org/standard/78176.html | Cerrada | Local (`Adjuntos/Local/ISO-IEC 25010-2023/ISO-IEC 25010-2023.pdf`, con copia en `.md`) |
| F6 | Humble, J., & Farley, D. (2010). *Continuous delivery: Reliable software releases through build, test, and deployment automation*. Addison-Wesley. ISBN 978-0-321-60191-9 | Cerrada | Local (`Adjuntos/Local/Continuous-Delivery - Jez Humble & David Farley/`, PDF y copia en `.md`), aportada por el usuario |
| F7 | Bezemer, C.-P., Eismann, S., Ferme, V., Grohmann, J., Heinrich, R., Jamshidi, P., Shang, W., van Hoorn, A., Villavicencio, M., Walter, J., & Willnecker, F. (2019). How is performance addressed in DevOps? A survey on industrial practices. En *Proceedings of the 2019 ACM/SPEC International Conference on Performance Engineering (ICPE '19)* (pp. 45–50). ACM. https://doi.org/10.1145/3297663.3309672 | Abierta | https://research.spec.org/icpe_proceedings/2019/proceedings/p45.pdf |

**Verificación (2026-11-07):**

- **F1:** PDF oficial descargado de istqb.org. La portada y el historial de revisiones indican la versión 4.0.1 del 15 de septiembre de 2024, una corrección de erratas de la v4.0 de abril de 2023. Pasajes localizados en el cuerpo:
  - Testing y aseguramiento de la calidad: §1.2.2, p. 17.
  - Modelos de ciclo de vida, con el modelo en V como ejemplo de modelo secuencial, y buenas prácticas de prueba (una actividad de prueba por cada actividad de desarrollo): §2.1.1–2.1.2, pp. 25–26.
  - DevOps y CI/CD, incluida la mayor visibilidad de las características no funcionales: §2.1.4, pp. 26–27.
  - *Shift left*, con las pruebas no funcionales desde el nivel de componente y la advertencia de no descuidar las posteriores: §2.1.5, p. 27.
  - Niveles de prueba, incluido el entorno «preferably similar to the operational environment» para la integración de sistemas: §2.2.1, pp. 28–29.
  - Criterios de entrada y de salida: §5.1.3, p. 49, y su uso entre niveles: p. 28.
- **F2:** ya estaba en `Referencias.md`. Pasajes nuevos en el cuerpo:
  - Objetivos de prueba por subcaracterística: §1.1, p. 11.
  - Umbrales monitoreados en producción: §1.2, p. 12.
  - E20 y E21 (§1.3.2, p. 14) ya están aprobadas en la evidencia de la Introducción.
- **F3:** título, autores, revista, volumen, páginas y licencia (acceso abierto de IEEE) comprobados en Crossref a partir del DOI. Texto completo leído en arXiv (1703.07019), cuya portada lo identifica como el artículo de IEEE Access. Definiciones de CI, entrega continua y despliegue continuo: §I, p. 2.
- **F4:** página leída en Microsoft Learn; sus metadatos dan la fecha (21 de julio de 2022) y el autor de la página. Definición de *shift-right* en el primer párrafo. Es literatura gris.
- **F5:** copia local, ya verificada en el plan de la Introducción. Subcaracterísticas: §3.2.1–3.2.3, p. 2. Comparación con la edición de 2011: tabla A.1, p. 13.
- **F6:** aportada por el usuario como PDF con conversión a `.md`. La página de créditos da el título, los autores, la editorial (Addison-Wesley), el ISBN 978-0-321-60191-9 y la primera impresión (agosto de 2010); el registro de la Biblioteca del Congreso es de 2010. La página de créditos dice «Copyright © 2011», pero se cita como 2010, que es el año de primera impresión y el que usa la literatura, incluida F7. Pasajes localizados (páginas impresas):
  - Definición del *deployment pipeline*: cap. 5, «What Is a Deployment Pipeline?», pp. 106–107.
  - La etapa de *commit* como compuerta: cap. 5, «The Commit Stage», p. 122.
  - La compuerta de pruebas de aceptación automatizadas: cap. 5, «The Automated Acceptance Test Gate», p. 124.
  - Los resultados de las pruebas de capacidad como compuerta o como información para una decisión humana: cap. 5, «Subsequent Test Stages», p. 128.
- **F7:** ya estaba en `Referencias.md`. «quality gates [16]» está en el cuerpo (§1 «Introduction», p. 45), y su referencia [16] es F6.
- **Descartadas:**
  - Guías de proveedores sobre *quality gates* (SonarSource, Perforce, testRigor, Codefresh): son contenido comercial, excluido por `Alcance.md` §5.3.
  - TechTarget (definición de *shift-right*): glosario comercial; Microsoft Learn es más directo.
  - Glosario del ISTQB (*quality gate*): la página oficial es una aplicación que no se pudo leer, y las copias de terceros no muestran la definición. Con F6 y F7 ya no hace falta.

## Registro de búsqueda
| # | Fecha | Buscador o base | Cadena | Resultados revisados | Elegidas / descartadas (motivo) |
|---|---|---|---|---|---|
| 1 | 2026-11-07 | Buscador web | `ISTQB Certified Tester Foundation Level syllabus v4.0 pdf shift-left test levels DevOps` | 20: PDF oficial de istqb.org (v4.0.1), notas de versión, resúmenes y cursos de terceros (Scribd, Udemy, softwaretestpilot y otros) | Elegida: F1, PDF oficial. Descartadas: copias y resúmenes de terceros (no oficiales). |
| 2 | 2026-11-07 | Buscador web | `"continuous integration, delivery and deployment" systematic review approaches tools challenges practices IEEE Access` | 10: arXiv, registros de catálogos y repositorios (Monash, RMIT, DOAJ) del mismo artículo | Elegida: F3, revisión sistemática arbitrada y de acceso abierto. |
| 3 | 2026-11-07 | Buscador web | `"quality gates" continuous delivery pipeline definition software engineering paper` | 17: blogs y guías de proveedores (testRigor, SonarSource, Perforce, Codefresh), Microsoft Docs, InfoQ y otros | Ninguna elegida: contenido comercial o sin revisión. Se resuelve con una síntesis propia a partir de F1 y F3. |
| 4 | 2026-11-07 | Buscador web | `"shift-right" testing in production definition software testing peer-reviewed study` | 10: TechTarget, Microsoft Learn (varias traducciones), zetcode, CM Crossroads | Elegida: F4, documentación con autor y fecha. Descartadas: TechTarget (glosario comercial) y zetcode (sin autoría identificable). |
| 5 | 2026-11-07 | Buscador web | `ISTQB glossary "quality gate" definition` | 18: copias del glosario en sitios de terceros, glosarios de empresas, glosario del gobierno de California | Ninguna elegida: no muestran la definición oficial, y la de California es de gestión de proyectos, no de pruebas. |
| 6 | 2026-11-07 | Buscador web | `"testing in production" OR "shift-right" continuous deployment canary empirical study ICSE OR FSE OR EMSE` | 10: blogs de práctica (Microsoft Learn, Gremlin, GlobalLogic y otros) | Ninguna elegida: sin estudios arbitrados. *Shift-right* queda como mención, con F4. |
