# Alcance de la Investigación: Pruebas Automatizadas de Rendimiento

> Documento de control del alcance. Todo el contenido que se produzca para la investigación debe respetarlo. Si un contenido no cabe aquí, **no se incluye** sin aprobación explícita.

## 1. Enfoque central

**Pruebas de rendimiento automatizadas sobre APIs web (HTTP/REST) en la fase de IMPLEMENTACIÓN, integradas a un pipeline de CI, con Gatling como herramienta del taller.**

| Decisión | Definición |
|---|---|
| Fase del ciclo de vida | **Implementación**: validación pre-despliegue del sistema integrado. El *shift-left* (ejecución en CI desde desarrollo) se trata como puente, no como segundo eje. |
| Objeto bajo prueba | Backend / API REST. |
| Herramienta del taller | **Gatling**. Los detalles de uso (lenguaje del DSL, forma de ejecución, etc.) se definen en la Fase 2. |
| Extensión objetivo | **30–35 páginas Word en total, con portada, índice, referencias y anexos incluidos.** Se redujo de 50–55 páginas el 2026-11-07; los borradores ya aprobados se condensan conservando todas sus fuentes (§5). |
| Formato de página asumido | Times New Roman / Calibri 12, interlineado 1.5, márgenes 2.5 cm ≈ **350 palabras por página** de texto corrido (las tablas y figuras cuentan dentro del presupuesto). |

## 2. Fases del trabajo

| Fase                              | Contenido                                          | Secciones del documento                                                                                                            | Estado                                         |
| --------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **Fase 1: Investigación**         | Investigación teórica y documental                 | 1 Portada, 2 Introducción, 3 Planteamiento del problema, 4 Metodología, 5 Marco teórico, 8 Referencias, anexos de validación de IA | **Alcance definido** (este documento)          |
| **Fase 2: Taller y cierre** | Propuesta y construcción del taller + conclusiones | 6 Propuesta de taller práctico, 7 Conclusiones, anexos del taller | **Taller construido y validado** (`Taller/Taller.md`, estado al 2026-11-10); sección 6, Conclusiones y anexos A, B y C redactados y montados en el documento de Word (35 páginas); pendientes: reproducción externa (T20), comprobación en macOS y auditoría independiente de los anexos A y B |

La forma de trabajo con IA está definida en §5.3, en el procedimiento de uso y validación de IA. El detalle operativo está en `Investigación/Workflow.md` y en `Investigación/Guía de redacción.md`.

## 3. Preguntas de investigación

**Pregunta-problema** (formulada en el Planteamiento del problema, §3.4): ¿Cómo pueden integrarse pruebas de rendimiento automatizadas sobre una API REST en un pipeline de CI, con un costo de adopción bajo y con resultados que permitan decidir de forma confiable si un cambio degradó el desempeño?

Las preguntas de investigación la descomponen. PI-2 justifica el problema; PI-1 y PI-3 dan la base conceptual y práctica (incluida la integración en CI y la interpretación de resultados); PI-4 informa el costo de adopción mediante la comparativa de herramientas, y PI-5 lo demuestra en el taller.

| PI | Pregunta | Fase |
|---|---|---|
| PI-1 | ¿Qué son las pruebas de rendimiento, cómo se clasifican y qué métricas las definen según ISTQB e ISO/IEC 25010? | 1 |
| PI-2 | ¿Qué problemas existen en la industria y la academia para su adopción y automatización (ejecución tardía, entornos no representativos, resultados poco reproducibles, costo, brecha de habilidades)? | 1 |
| PI-3 | ¿Qué principios, buenas prácticas y antipatrones rigen el diseño, ejecución e interpretación de pruebas de rendimiento, y cómo se integran en CI/CD? | 1 |
| PI-4 | ¿Cómo se comparan las herramientas comerciales y de código abierto disponibles según criterios técnicos definidos? | 1 |
| PI-5 | ¿Cómo se demuestra experimentalmente, con Gatling, la detección y verificación de la corrección de un problema de rendimiento? | 2 |

## 4. Inclusiones y exclusiones

| Incluir (a fondo) | Mencionar (≤ 1 párrafo) | Excluir explícitamente |
|---|---|---|
| Tipos: carga, estrés, picos (*spike*), resistencia (*soak*) | Escalabilidad, volumen y capacidad como variantes | Rendimiento de frontend (Lighthouse, Core Web Vitals) |
| Métricas: tiempo de respuesta p50/p95/p99, *throughput*, tasa de error, concurrencia, usuarios virtuales | Observabilidad/APM como complemento teórico; Prometheus y Grafana se implementan en el taller para interpretar las pruebas | Microbenchmarks y *profiling* de código (JMH, perf, async-profiler) |
| ISO/IEC 25010 → eficiencia de desempeño | Generación de carga distribuida / en la nube | Ingeniería del caos |
| Proceso de pruebas de rendimiento (ISTQB CT-PT) | Ley de Little y nociones básicas de colas | Teoría de colas formal y modelado analítico de capacidad |
| Modelos de carga abiertos vs. cerrados; *coordinated omission* | *Shift-right* (pruebas en producción, *canary*) | Tuning de bases de datos, JVM o infraestructura como tema propio |
| Umbrales/SLO como *quality gates* automatizados en CI | Seguridad bajo carga (DoS) — solo para delimitar ética | Rendimiento móvil y de escritorio |
| Catálogo y comparativa de 6 herramientas | | Pruebas contra sistemas de terceros o sitios públicos |

## 5. Estructura y presupuesto de páginas

Total estimado: **~33 páginas, todo incluido** (rango aceptable 30–35). Las 2 páginas de margen hasta el tope quedan para el Marco teórico o el taller, si al redactarlos lo necesitan.

**Condensación de lo ya aprobado:** la Introducción, el Planteamiento del problema, la Metodología y el grupo A del Marco teórico se escribieron con el presupuesto anterior y se condensan al nuevo. Se pueden quitar filas de evidencia, pero cada fuente de `Investigación/Referencias.md` debe seguir citada al menos una vez en el documento; las filas que dejen de citarse pasan a «Filas no usadas».

| #   | Sección                                                        | Fase  | Páginas | Palabras aprox.        | PI que responde  |
| --- | -------------------------------------------------------------- | ----- | ------- | ---------------------- | ---------------- |
| 1   | Portada + índice general (figuras y tablas en el mismo índice) | 1     | 2       | —                      | —                |
| 2   | Introducción                                                   | 1     | 2       | 700                    | —                |
| 3   | Planteamiento del problema                                     | 1     | 3       | 1 050                  | PI-2             |
| 4   | Metodología                                                    | 1     | 2       | 700                    | —                |
| 5   | Marco teórico                                                  | 1     | 10.5    | 2 670 + tablas/figuras | PI-1, PI-3, PI-4 |
| 6   | Propuesta de taller práctico                                   | 2     | 6       | por definir            | PI-5             |
| 7   | Conclusiones                                                   | 2     | 1.5     | 525                    | todas            |
| 8   | Referencias                                                    | 1     | 2.5     | 25–35 entradas         | —                |
| 9   | Anexos                                                         | 1 y 2 | 3.5     | —                      | —                |

### 5.1 Introducción (2 p.)

- Relevancia del rendimiento como atributo de calidad (impacto en negocio, experiencia de usuario, costos de infraestructura).
- Ubicación del tema en el ciclo de vida: fase de implementación.
- Motivación, objetivos y estructura del documento.

### 5.2 Planteamiento del problema (3 p.)

- **Industria:** pruebas de rendimiento ejecutadas tarde o nunca; entornos de prueba no representativos; costo de herramientas y de infraestructura de carga; falta de integración en CI/CD; resultados ruidosos y difíciles de interpretar.
- **Academia:** poca presencia en currículos frente a pruebas funcionales; brecha entre investigación (p. ej. detección de regresiones) y práctica.
- Evidencia empírica obligatoria (estudios de práctica en proyectos open source y encuestas industriales); **ninguna estadística sin fuente verificable**.
- Cierre: pregunta-problema y justificación del taller.

### 5.3 Metodología (2 p.)

- **Enfoque:** investigación teórico-aplicada: revisión de literatura semi-sistemática + estudio experimental (taller).
- **Tipos de fuente, por orden de preferencia:** normas ISO/IEC, syllabus ISTQB, artículos arbitrados (sobre todo de ACM e IEEE) y documentación oficial de herramientas.
- **Estrategia de búsqueda:** búsquedas dirigidas a las afirmaciones que necesita cada plan, en buscadores web y en bases bibliográficas abiertas (Crossref, OpenAlex, arXiv, ACM Digital Library, IEEE Xplore). Cada fuente se verifica en la página del editor y por su DOI en Crossref, y se lee en texto completo, en una copia abierta y legal (actas de SPEC, arXiv, copia de autor o repositorio institucional) o en una copia local si es cerrada. No se usa Scopus.
- **Cadenas de búsqueda** (ejemplos): `"performance testing" AND ("load testing" OR "stress testing")`, `"load testing" AND (survey OR "state of practice")`, `"performance regression" AND ("continuous integration" OR DevOps)`.
- **Registro de búsqueda:** a partir del Marco teórico, cada plan registra sus consultas: fecha, buscador o base, cadena, resultados y fuentes elegidas o descartadas con su motivo. En la Introducción y en el Planteamiento del problema solo se registraron las fuentes verificadas y las descartadas, y la Metodología lo declara así.
- **Criterios de inclusión:** 2010–2026 (excepto clásicos), revisado por pares, normas, o documentación oficial; en inglés o español.
- **Criterios de exclusión:** blogs sin autoría identificable, contenido de marketing sin datos, temas de la columna "Excluir".
- **Procedimiento de uso y validación de IA** (la Metodología lo resume; el detalle de los criterios del auditor, las rondas y la evolución del procedimiento va en el anexo B):
  - **Principio:** un modelo produce y otro, de un proveedor distinto, audita. Claude Code (Opus 5.5) planifica y redacta; Codex (GPT-6.1 Sol) audita. Ninguna sección avanza sin la aprobación humana del plan, y ningún texto se integra al documento sin revisión humana.
  - **Flujo por sección**, mediante tres skills:
    1. **Planificador:** define el modo de la sección (ligero o completo), un esquema argumental con la idea central de cada bloque, las afirmaciones que requieren respaldo y las fuentes. Cada fuente se verifica en su página de publicación (título, autores, fecha o versión y enlace) y se clasifica por acceso. El usuario aprueba el plan de forma explícita.
    2. **Redactor:** lee las fuentes en texto completo, nunca solo el resumen, y redacta con voz propia según la guía de redacción. Registra cada cita del texto en una tabla de evidencia con la cita textual literal, en el idioma original, y su ubicación (sección y página). Cada cita del borrador lleva oculto el ID de su fila de evidencia.
    3. **Auditor:** el redactor lo ejecuta de forma automática (`codex exec`), en una sesión nueva en cada ronda. Coteja cada cita con su fuente (trazabilidad, literalidad, ubicación y fidelidad), verifica que ningún dato externo aparezca sin cita y revisa la prosa contra la guía. Sus hallazgos son **bloqueantes** (citas infieles o no trazables, datos sin respaldo, metacomentarios) o **sugerencias** (argumento, legibilidad, densidad de citas, extensión). El redactor corrige los bloqueantes y decide sobre las sugerencias, con un máximo de dos rondas por invocación.
  - **Criterios de redacción:** primero el argumento; la evidencia lo respalda. Se cita lo que proviene de fuentes externas (definiciones, datos, casos, hallazgos) y no el razonamiento propio ni el contenido interno. La densidad de citas depende del modo, y el texto no habla del proceso con que se produjo, salvo en la Metodología y en los anexos.
  - **Registro:** los planes, la evidencia, los borradores y las auditorías de cada sección se versionan en el repositorio. Los informes de auditoría conservan todas sus rondas. Este material alimenta los anexos A y B.
  - **Evolución del procedimiento:** la Introducción se produjo primero con una versión de cinco skills que partía de la evidencia: el redactor solo podía parafrasear filas de evidencia ya auditadas. El resultado fue un texto saturado de citas (17 en 880 palabras) y poco desarrollado, en un proceso lento. Esa versión se sustituyó por la actual y la Introducción se reescribió con ella. La comparación entre ambas versiones es un insumo para la reflexión metodológica (§5.6).

### 5.4 Marco teórico (10.5 p.)

Las páginas incluyen las tablas y figuras de cada subsección; las palabras son solo de texto corrido.

| Subsección | Páginas (palabras + tablas/figuras) | Contenido clave |
|---|---|---|
| 5.1 Aseguramiento de la calidad en la fase de implementación | 1.5 (350 palabras + Figura 2) | Ciclo de vida, modelo en V, CI/CD, *quality gates*, *shift-left* vs *shift-right* |
| 5.2 Eficiencia de desempeño en ISO/IEC 25010 | 1 (200 palabras + Tabla 1) | Comportamiento temporal, utilización de recursos, capacidad |
| 5.3 Conceptos y métricas fundamentales | 2 (550 palabras + figura de modelos de carga abierto y cerrado) | Latencia vs. tiempo de respuesta, *throughput*, percentiles (por qué no el promedio), concurrencia, usuarios virtuales, *think time*, ley de Little, modelos de carga abiertos vs. cerrados, *coordinated omission* |
| 5.4 Clasificación de las pruebas de rendimiento | 1.5 (300 palabras + tabla comparativa) | Carga, estrés, *spike*, *soak*; mención de escalabilidad, volumen y capacidad. Tabla comparativa: objetivo, perfil de carga, duración, qué detecta |
| 5.5 Proceso de pruebas de rendimiento | 0.75 (260 palabras) | Fases según ISTQB CT-PT: planificación, análisis/diseño (perfil operacional, modelo de carga), implementación (scripts, datos), ejecución, análisis y reporte; requisitos de entorno |
| 5.6 Principios, buenas prácticas y antipatrones | 1 (350 palabras) | Línea base, aislamiento del generador de carga, calentamiento, repetibilidad, datos realistas; antipatrones (promedios, entorno compartido, probar sin objetivos) |
| 5.7 Automatización e integración en CI/CD | 0.75 (260 palabras) | Umbrales como criterio pass/fail, detección de regresiones, frecuencia de ejecución, observabilidad como complemento |
| 5.8 Catálogo y comparativa de herramientas | 2 (400 palabras + tabla comparativa de 6 herramientas × 8 criterios) | Ver §6 |

### 5.5 Propuesta de taller práctico (6 p.) — Fase 2

Contenido mínimo exigido por el enunciado: contexto de aplicación, recursos y código, stack tecnológico y guía paso a paso, más el plan de pruebas ejecutable con los compañeros (objetivo específico 5). Las subsecciones y su distribución de páginas se definen en la Fase 2.

### 5.6 Conclusiones (1.5 p.) — Fase 2

- Hallazgos por pregunta de investigación.
- Respuesta a la pregunta-problema, a partir de esos hallazgos.
- Balance técnico del taller.
- Reflexión metodológica sobre el uso y la validación de la IA.

## 6. Catálogo de herramientas

**Herramientas a comparar (6):**

- **Código abierto:** Gatling (Community), Apache JMeter, Grafana k6, Locust.
- **Comerciales:** OpenText LoadRunner, y una plataforma SaaS (BlazeMeter **o** Tricentis NeoLoad). Mencionar Gatling Enterprise como contraste dentro del mismo proveedor.

**Criterios fijos de comparación** (no agregar otros):

1. Lenguaje / forma de scripting
2. Modelo de carga soportado (abierto, cerrado o ambos)
3. Protocolos soportados
4. Integración con CI/CD y criterios pass/fail
5. Reportes y análisis de resultados
6. Eficiencia del generador de carga (arquitectura: hilos vs. asíncrona)
7. Curva de aprendizaje
8. Licencia y costo

Toda afirmación sobre una herramienta debe verificarse contra su **documentación oficial vigente**, indicando la versión consultada y la fecha de acceso.

## 7. Taller práctico — Fase 2

**Decisiones actualizadas el 2026-11-08, aprobadas por el usuario.** El diseño operativo se desarrolla en `Taller/Taller.md`; la implementación y la validación experimental están pendientes.

- **Modalidad:** el equipo presenta y aplica el taller en clase; los compañeros pueden clonar el repositorio y ejecutar las pruebas en sus computadoras mediante una guía reproducible.
- **Sistema bajo prueba:** API REST propia de productos, construida con Flask, Gunicorn y PostgreSQL.
- **Problema a demostrar:** contención por un candado global al incorporar un contador de visitas. La comparación principal es entre la implementación con regresión y la corregida, ambas con la misma funcionalidad; la versión sin contador es una referencia adicional.
- **Herramienta:** Gatling Community con DSL de Java y Maven Wrapper, ejecutado en un contenedor.
- **Entorno:** Docker Compose para API, base de datos, generador y observabilidad. La práctica local requiere Git y Docker con Compose; no requiere una cuenta de GitHub. Las plataformas y requisitos mínimos se comprobarán durante la implementación.
- **Observabilidad:** Prometheus y Grafana se incluyen en el entorno reproducible para interpretar las pruebas, con métricas de aplicación y consumo frente a los límites de CPU y memoria de los contenedores. Gatling determina el veredicto automático. Su incorporación práctica, aprobada por el usuario, no convierte la observabilidad en un segundo eje del Marco teórico.
- **Integración con CI:** GitHub Actions reutiliza el procedimiento local y ejecuta pruebas funcionales y carga ante cambios relevantes; estrés, picos y campañas completas disponen de ejecución manual.
- **Confiabilidad del veredicto:** calibrar por entorno, congelar los parámetros y validarlos con ejecuciones nuevas. Se espera que todas las repeticiones válidas de la implementación corregida aprueben y las de la regresión sean rechazadas por rendimiento. Se reportan variación, márgenes y ejecuciones inválidas; no se ajusta el umbral sobre los mismos datos usados para validar.
- **Reproducibilidad:** conservar código, dependencias, datos y procedimiento; calibrar perfiles distintos para cada equipo y para CI. No se exige igualdad de tiempos entre computadoras diferentes.
- **Restricción ética:** solo se prueba contra el entorno propio, nunca contra sistemas de terceros ni sitios públicos.
- **Extensión:** 6 páginas en el documento; código, paneles, resultados completos y guía extendida en el repositorio.

**Pendientes de implementación y medición** (actualizado el 2026-11-10):

- [x] Ubicación del repositorio, versiones exactas y plataformas soportadas (`Taller.md` §5.1; `docs/GUIA.md` §1). Falta comprobar macOS.
- [x] Recursos mínimos, configuración del servidor, conexiones y límites de contenedores (`Taller.md` §5.2).
- [x] Perfiles, duraciones, repeticiones, reglas de calibración y márgenes, fijados antes de recoger los datos correspondientes (`Taller.md` §7; `docs/PLAN-DE-PRUEBAS.md`).
- [x] Instrumentación, extracción de métricas y exportación de evidencias (`Taller.md` §6.4–§6.5; `docs/INTERPRETACION.md`).
- [x] Validación independiente por entorno (`Taller.md` §7.2) y reproducción del veredicto `ci` en una segunda computadora del equipo. La reproducción por una persona ajena al desarrollo sigue pendiente (T20).
- [ ] Comprobación de la guía por una persona ajena al desarrollo y ajuste de la presentación al tiempo asignado por el curso (T20).

## 8. Fuentes ancla (verificar existencia antes de usar)

- ISTQB. *Certified Tester Performance Testing (CT-PT) Syllabus*.
- ISO/IEC 25010 — *Systems and software Quality Requirements and Evaluation (SQuaRE): Product quality model* (versión vigente).
- ISO/IEC/IEEE 29119-3 — *Software testing: Test documentation*.
- Jiang, Z. M., & Hassan, A. E. (2015). A survey on load testing of large-scale software systems. *IEEE Transactions on Software Engineering*.
- Molyneaux, I. *The Art of Application Performance Testing* (2.ª ed.). O'Reilly.
- Schroeder, B., Wierman, A., & Harchol-Balter, M. (2006). Open versus closed: A cautionary tale. *NSDI*.
- Leitner, P., & Bezemer, C.-P. (2017). An exploratory study of the state of practice of performance testing in Java-based open source projects. *ICPE*.
- Bezemer, C.-P., et al. (2019). How is performance addressed in DevOps? A survey on industrial practices. *ICPE*.
- Little, J. D. C. (1961). A proof for the queuing formula L = λW. *Operations Research*.
- Documentación oficial: Gatling, Apache JMeter, Grafana k6, Locust, LoadRunner, BlazeMeter/NeoLoad.

**Meta:** 25–35 referencias en total, con al menos 50 % artículos revisados por pares o normas.

## 9. Anexos previstos (3.5 páginas en total)

El material extenso (código completo, registros íntegros de IA) va en un **repositorio**; los anexos solo contienen el enlace y extractos representativos.

| Anexo | Contenido | Fase | Páginas |
|---|---|---|---|
| A | Registro resumido de consultas de IA | 1 | 1 |
| B | Resumen de la validación crítica de los productos de IA y su resolución, con el detalle del procedimiento que la Metodología resume | 1 | 1 |
| C | Material del taller: enlace y estructura del repositorio, extractos de la simulación y de la *quality gate*, y captura del informe de Gatling (redactado y montado) | 2 | 1.5 |

**Estado al 2026-11-11:** las secciones 6 y 7 y los anexos A, B y C están en el documento de Word, que tiene 35 páginas. El anexo C está en `Investigación/Secciones/06 Propuesta de taller práctico/03 Borrador.md`, con las Figuras 4 a 6 en `figuras/` (la 6, de las ejecuciones de `validacion-ci-2`); las Conclusiones, en `07 Conclusiones/`, y los anexos A y B, en `09 Anexos A y B/03 Borrador.md`. Las Conclusiones pasaron por el auditor (`07 Conclusiones/04 Auditoría.md`, aprobada en la primera ronda); los anexos A y B, no. En el Word, la Tabla 6 no tiene la columna «Veredictos esperados» y la Figura 5 va antes de la Tabla 6; el borrador de la sección 6 conserva el orden original.
