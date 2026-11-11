# Plan — 06 Propuesta de taller práctico

**Estado:** Aprobado | **Modo:** Ligero | **Versión:** 1 | **Fecha:** 2026-11-10 | **Presupuesto:** 1 350 palabras + tablas y figuras (6 páginas) · anexo C aparte (1,5 páginas)

## Objetivo y alcance

Sección 6 del documento (`Enunciado.md` §6; `Alcance.md` §5.5 y §7; diseño en `Taller/Taller.md` §10). Es un resumen ejecutivo del taller, que responde PI-5: cómo se demuestra experimentalmente, con Gatling, la detección de un problema de rendimiento y la verificación de su corrección. El enunciado exige cuatro elementos (contexto de aplicación, recursos y código, stack tecnológico y guía paso a paso), y el objetivo específico 5 pide un plan de pruebas ejecutable con los compañeros. La sección agrega los resultados y los límites, que las Conclusiones necesitan para responder PI-5.

**Incluye:**

- El caso de la tienda: el contador de visitas con un candado global y su corrección con una instrucción SQL atómica.
- El repositorio, su estructura, los requisitos y los entregables.
- El stack, con sus versiones y su función, y la arquitectura del entorno.
- El plan de pruebas: objetivos, escenario con modelo de carga abierto, tipos de prueba, criterios, validez, calibración y validación.
- La guía resumida: procedimiento local y *quality gate* en CI.
- Los resultados de las campañas de validación (`ci` y `local`) y lo que mostró la observabilidad.
- Los límites de lo demostrado.
- El anexo C: enlace al repositorio, extractos de la simulación y del workflow, y una captura del informe de Gatling.

**No incluye (lo cubren otras secciones o el repositorio):**

- Las definiciones de los conceptos (percentiles, modelo de carga abierto, *coordinated omission*, ley de Little, línea base, ruido, *quality gate*): se remite al Marco teórico por número de subsección (5.1–5.8), sin repetir sus citas (`Taller.md` §10).
- La comparativa de herramientas que justifica Gatling, que está en 5.8; aquí solo se nombra el criterio.
- La respuesta a PI-5 y a la pregunta-problema, que va en las Conclusiones (§7). Aquí se presentan los resultados sin valorarlos frente a las preguntas.
- El detalle técnico: tablas completas de cada campaña, reglas de validez, comandos, lectura de los paneles y del informe. Están en `Taller/Taller.md`, `docs/GUIA.md`, `docs/PLAN-DE-PRUEBAS.md` y `docs/INTERPRETACION.md`.
- El proceso con IA y su validación (Metodología y anexos A y B).

**Forma:** siete subsecciones con subtítulo (6.1 a 6.7), sin párrafo de apertura, con la distribución de `Taller.md` §10. Las cifras de los resultados son contenido interno del trabajo (salen de las campañas registradas en el repositorio) y no llevan cita; cada una indica la campaña de la que sale.

## Esquema argumental

| Bloque | Palabras | Idea central | Contenido | Insumos y fuentes |
|---|---|---|---|---|
| B1. 6.1 Contexto de aplicación | 230 | El taller reproduce una regresión de rendimiento realista que las pruebas funcionales no detectan: un contador de visitas protegido por un candado global cuenta bien, pero atiende las solicitudes de a una, y solo una prueba de carga lo distingue de su corrección. | La API de productos de una tienda; el contador; la variante `regresion` (candado de Python compartido por todos los hilos) y la `corregida` (`UPDATE ... RETURNING` atómico); `sana` como referencia. Por qué es realista: no hay pausas artificiales, y la latencia de 2 ms hacia PostgreSQL reproduce una base de datos en otro servidor. Las dos variantes del contador aprueban las mismas pruebas funcionales: el rendimiento es un atributo de calidad propio (5.1, 5.2). Hipótesis: `regresion` se degrada a tasas en las que `corregida` cumple. | `Taller.md` §1, §4 y §5.2 |
| B2. 6.2 Recursos y código | 150 | Todo lo necesario para reproducir el taller está en un repositorio público, y un participante solo necesita Git y Docker. | Enlace al repositorio y a la carpeta `Taller/`. Estructura: API, base de datos, simulaciones, observabilidad, perfiles, herramientas, scripts y workflows. Requisitos: Docker con Compose, al menos 4 núcleos y unas 5 CPU y 5,5 GB para Docker. Entregables: código, guía, plan de pruebas e interpretación; los resultados de cada ejecución como artefactos. Plataformas comprobadas. | `Taller.md` §9; `docs/GUIA.md` §1–§2 |
| B3. 6.3 Stack tecnológico | 150 | El stack fija versiones, recursos y procedimiento para que las mediciones se comparen entre variantes y se repitan, y elige Gatling por los criterios de 5.8. | La Tabla 4 resume componentes, versiones y función. Contenedores con versiones exactas y núcleos fijos (Docker Compose); Gatling como generador de carga con modelo abierto y aserciones que fallan la ejecución (5.8); Prometheus y Grafana para observar el servidor; GitHub Actions para la *quality gate*. La Figura 4 muestra la arquitectura. | `Taller.md` §2, §5 y §5.1; F1–F4 |
| B4. 6.4 Plan de pruebas | 300 | El plan fija antes de medir qué se prueba, con qué carga y con qué criterio, y separa la elección del umbral de su comprobación, para que el veredicto sea confiable y no un ajuste a los datos. | Objetivos. Escenario: modelo de carga abierto a tasa constante, una consulta por usuario virtual, identificadores fijos (5.3). Tipos de prueba en la Tabla 5: funcionales como condición previa, carga como *quality gate*, estrés y picos informativos; resistencia excluida (5.4). Criterios: p95 y tasa de error de la medición, sin el calentamiento (5.6). Ejecuciones inválidas: el generador no sostuvo la tasa, faltan datos o la configuración no es la pedida. Perfiles de ejecución por entorno: calibración con tres repeticiones por variante y margen de 3 veces, congelamiento y validación con una campaña nueva (5.5–5.7). | `Taller.md` §6–§7; `docs/PLAN-DE-PRUEBAS.md` |
| B5. 6.5 Guía paso a paso | 200 | Con cuatro comandos, un participante reproduce en su computadora lo mismo que la *quality gate* hace en cada cambio: `corregida` aprueba y `regresion` es rechazada. | Local: preparar, pruebas funcionales, carga sobre cada variante con el perfil `ci`, lectura del resumen, del informe y de Grafana, y detener. Duraciones aproximadas. CI: el workflow de la *quality gate* en cada *push* y *pull request*; los dos *pull requests* de demostración; los workflows manuales de escenarios, calibración y validación (5.7). | `docs/GUIA.md` §3–§11; `Taller.md` §8 |
| B6. 6.6 Resultados e interpretación | 200 | En todas las ejecuciones válidas de las campañas de validación, `corregida` aprobó y `regresion` fue rechazada, con márgenes muy superiores al ruido medido; la observabilidad confirma que la causa es la espera del candado y no el cálculo. | La Tabla 6 resume las tres validaciones (`validacion-ci-1`, `validacion-ci-2`, `validacion-local`). Márgenes mínimos (umbral sobre el peor `corregida` y bajo el mejor `regresion`). Ruido del *runner*: el p95 de `corregida` cambió hasta 28 veces entre corridas idénticas, con el p50 estable. `regresion` incumple también la tasa de error. Una segunda computadora con el perfil `ci` dio los mismos veredictos. Grafana: con `regresion`, hilos esperando el candado y CPU más baja que con `corregida`; bajo la sobrecarga, la propia lectura de métricas deja de responder. La Figura 5 muestra el p95 de cada ejecución frente al umbral. | `Taller.md` §7; `docs/INTERPRETACION.md`; campañas del repositorio |
| B7. 6.7 Límites | 120 | Lo demostrado vale para una regresión conocida y grande, en los entornos y perfiles medidos; no prueba que el umbral detecte regresiones pequeñas o desconocidas. | Regresión conocida y umbral elegido con ella; una regresión que solo duplique el tiempo de `corregida` aprobaría. Validez restringida al perfil y al entorno, y hardware del *runner* variable. Entorno reducido: se comparan versiones, no se estima capacidad (5.5). Sin prueba de resistencia. Pendientes: reproducción por una persona ajena al desarrollo y comprobación en macOS. | `Taller.md` §7 y §9; `docs/PLAN-DE-PRUEBAS.md` §10 |
| **Total** | **1 350** | | | |
| B8. Anexo C. Material del taller | — (1,5 págs.) | El anexo permite verificar que la demostración es ejecutable: da el acceso al repositorio y extractos del código que deciden el veredicto. | C.1 Enlace y estructura del repositorio. C.2 Extracto de la simulación de carga (fases y aserciones). C.3 Extracto del workflow de la *quality gate*. C.4 Captura del informe de Gatling (página de la medición) de una ejecución de cada variante. | `Taller/` del repositorio |

## Tablas y figuras

| ID | Tipo | Título | Bloque | Contenido | Fuentes | Espacio (págs.) |
|---|---|---|---|---|---|---|
| T4 | Tabla | Tabla 4. Stack tecnológico del taller | B3 | Componente, versión y función en el taller: Flask y Gunicorn, PostgreSQL, pytest, Gatling, Docker Compose, Prometheus, Grafana y GitHub Actions | `Taller.md` §2 y §5.1 (elaboración propia) | 0,45 |
| F4 | Figura | Figura 4. Arquitectura del entorno del taller | B3 | Gatling envía solicitudes HTTP a la API, que consulta PostgreSQL con 2 ms de latencia; Prometheus lee `/metrics` y Grafana lo muestra; los scripts y GitHub Actions orquestan. Recursos fijos de cada contenedor | `Taller.md` §5 (elaboración propia) | 0,4 |
| T5 | Tabla | Tabla 5. Pruebas del taller | B4 | Prueba, pregunta, inyección, resultado y cuándo se ejecuta: funcionales, comprobación del generador, carga, estrés y picos | `docs/PLAN-DE-PRUEBAS.md` §5 (elaboración propia) | 0,5 |
| T6 | Tabla | Tabla 6. Resultados de las campañas de validación | B6 | Por campaña: entorno, ejecuciones válidas, rango del p95 de cada variante, tasa de error de `regresion`, umbral y veredictos esperados | `Taller.md` §7.2 (elaboración propia) | 0,4 |
| F5 | Figura | Figura 5. p95 de cada ejecución de validación frente al umbral | B6 | Puntos por ejecución en escala logarítmica, `corregida` y `regresion`, con la línea del umbral de cada perfil (3 000 ms en `ci` y 1 000 ms en `local`) | `Taller.md` §7.2 (elaboración propia) | 0,45 |
| F6 | Figura | Figura 6. Informe de Gatling de la medición, por variante | B8 | Captura de la tabla de estadísticas y del gráfico de tiempos de la página `medicion`, de una ejecución de `corregida` y una de `regresion` | Ejecuciones del repositorio | 0,5 (dentro del anexo) |

Las tablas y figuras de la sección suman unas 2,2 páginas y el texto, unas 3,9: 6,1 páginas en total. Si al maquetar no caben, se recorta primero la Figura 5, porque la Tabla 6 da los mismos rangos.

## Términos nuevos

| Término | Inglés | Forma propuesta | Define |
|---|---|---|---|
| Candado | lock | candado (*lock*) la primera vez; después, candado | 6.1 |
| Variante | — | variante, con su nombre en código: `regresion`, `corregida`, `sana` | 6.1 |
| Perfil de ejecución | — | perfil de ejecución, con su nombre en código (`ci`, `local`). No se usa «perfil» solo, para no confundirlo con el perfil de carga (5.4) | 6.4 |
| Campaña | — | campaña de calibración, campaña de validación | 6.4 |
| Ejecución inválida | — | ejecución inválida | 6.4 |

## Fuentes

| ID | Referencia y enlace | Acceso | Disponibilidad |
|---|---|---|---|
| F1 | Gatling Corp. (2026). *Gatling* (Versión 3.16.0) [Software]. https://docs.gatling.io/ (ya en `Referencias.md`) | Abierta | https://docs.gatling.io/ |
| F2 | Docker Inc. (s. f.). *Docker Compose*. Docker Docs. Recuperado el 10 de noviembre de 2026, de https://docs.docker.com/compose/ | Abierta | https://docs.docker.com/compose/ |
| F3 | Prometheus Authors. (s. f.). *Overview*. Prometheus. Recuperado el 10 de noviembre de 2026, de https://prometheus.io/docs/introduction/overview/ | Abierta | https://prometheus.io/docs/introduction/overview/ |
| F4 | GitHub. (s. f.). *Understanding GitHub Actions*. GitHub Docs. Recuperado el 10 de noviembre de 2026, de https://docs.github.com/en/actions/get-started/understand-github-actions | Abierta | https://docs.github.com/en/actions/get-started/understand-github-actions |

**Verificación (2026-11-10):**

- **F1:** ya verificada en el plan del grupo D del Marco teórico. Aquí se usa para las aserciones que hacen fallar la ejecución, que 5.8 ya respalda; si el redactor necesita un pasaje nuevo, lo toma de la documentación de aserciones.
- **F2:** título «Docker Compose», sin fecha ni versión. Pasaje: «Docker Compose is a tool for defining and running multi-container applications.» (primer párrafo).
- **F3:** título «Overview | Prometheus», sin fecha. Pasajes: «Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud.» (*What is Prometheus?*); «time series collection happens via a pull model over HTTP» (*Features*); «Prometheus scrapes metrics from instrumented jobs» (*Architecture*).
- **F4:** título «Understanding GitHub Actions», sin fecha. Pasajes: «GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline.» (introducción); «Workflows are defined by a YAML file checked in to your repository» y «An event is a specific activity in a repository that triggers a workflow run.» (*The components of GitHub Actions*); «Each workflow run executes in a fresh, newly-provisioned virtual machine.» (*Runners*).
- Grafana, Flask, Gunicorn, PostgreSQL y pytest aparecen solo con su versión y su función en el taller, que es contenido interno; no se les atribuye ninguna característica que necesite cita.

## Registro de búsqueda

No hubo consultas de búsqueda: F2–F4 son la documentación oficial de herramientas ya elegidas, y se consultaron directamente en su dirección.
