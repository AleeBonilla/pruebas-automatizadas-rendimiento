# Alcance de la Investigación: Pruebas Automatizadas de Rendimiento

> Documento de control del alcance. Todo el contenido que se produzca para la investigación debe respetarlo. Si un contenido no cabe aquí, **no se incluye** sin aprobación explícita.

## 1. Enfoque central

**Pruebas de rendimiento automatizadas sobre APIs web (HTTP/REST) en la fase de IMPLEMENTACIÓN, integradas a un pipeline de CI, con Gatling como herramienta del taller.**

| Decisión | Definición |
|---|---|
| Fase del ciclo de vida | **Implementación**: validación pre-despliegue del sistema integrado. El *shift-left* (ejecución en CI desde desarrollo) se trata como puente, no como segundo eje. |
| Objeto bajo prueba | Backend / API REST. |
| Herramienta del taller | **Gatling**. Los detalles de uso (lenguaje del DSL, forma de ejecución, etc.) se definen en la Fase 2. |
| Extensión objetivo | **50–55 páginas Word en total, anexos incluidos.** |
| Formato de página asumido | Times New Roman / Calibri 12, interlineado 1.5, márgenes 2.5 cm ≈ **350 palabras por página** de texto corrido (las tablas y figuras cuentan dentro del presupuesto). |

## 2. Fases del trabajo

| Fase                              | Contenido                                          | Secciones del documento                                                                                                            | Estado                                         |
| --------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **Fase 1: Investigación**         | Investigación teórica y documental                 | 1 Portada, 2 Introducción, 3 Planteamiento del problema, 4 Metodología, 5 Marco teórico, 8 Referencias, anexos de validación de IA | **Alcance definido** (este documento)          |
| **Fase 2:       Taller y cierre** | Propuesta y construcción del taller + conclusiones | 6 Propuesta de taller práctico, 7 Conclusiones, anexos del taller                                                                  | **Por definir** mediante discusión de opciones |

La forma de trabajo con IA (skills) se definirá aparte y se incorporará a este documento cuando esté acordada.

## 3. Preguntas de investigación

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
| Métricas: tiempo de respuesta p50/p95/p99, *throughput*, tasa de error, concurrencia, usuarios virtuales | Observabilidad/APM (Prometheus, Grafana) como complemento | Microbenchmarks y *profiling* de código (JMH, perf, async-profiler) |
| ISO/IEC 25010 → eficiencia de desempeño | Generación de carga distribuida / en la nube | Ingeniería del caos |
| Proceso de pruebas de rendimiento (ISTQB CT-PT) | Ley de Little y nociones básicas de colas | Teoría de colas formal y modelado analítico de capacidad |
| Modelos de carga abiertos vs. cerrados; *coordinated omission* | *Shift-right* (pruebas en producción, *canary*) | Tuning de bases de datos, JVM o infraestructura como tema propio |
| Umbrales/SLO como *quality gates* automatizados en CI | Seguridad bajo carga (DoS) — solo para delimitar ética | Rendimiento móvil y de escritorio |
| Catálogo y comparativa de 6 herramientas | | Pruebas contra sistemas de terceros o sitios públicos |

## 5. Estructura y presupuesto de páginas

Total estimado: **~53 páginas, anexos incluidos** (rango aceptable 50–55).

| # | Sección | Fase | Páginas | Palabras aprox. | PI que responde |
|---|---|---|---|---|---|
| 1 | Portada + índice general (figuras y tablas en el mismo índice) | 1 | 2 | — | — |
| 2 | Introducción | 1 | 2.5 | 875 | — |
| 3 | Planteamiento del problema | 1 | 4.5 | 1 550 | PI-2 |
| 4 | Metodología | 1 | 3.5 | 1 200 | — |
| 5 | Marco teórico | 1 | 17 | 5 400 + tablas/figuras | PI-1, PI-3, PI-4 |
| 6 | Propuesta de taller práctico | 2 | 11.5 | por definir | PI-5 |
| 7 | Conclusiones | 2 | 2.5 | 875 | todas |
| 8 | Referencias | 1 | 3 | 25–35 entradas | — |
| 9 | Anexos | 1 y 2 | 6.5 | — | — |

### 5.1 Introducción (2.5 p.)

- Relevancia del rendimiento como atributo de calidad (impacto en negocio, experiencia de usuario, costos de infraestructura).
- Ubicación del tema en el ciclo de vida: fase de implementación.
- Motivación, objetivos y estructura del documento.

### 5.2 Planteamiento del problema (4.5 p.)

- **Industria:** pruebas de rendimiento ejecutadas tarde o nunca; entornos de prueba no representativos; costo de herramientas y de infraestructura de carga; falta de integración en CI/CD; resultados ruidosos y difíciles de interpretar.
- **Academia:** poca presencia en currículos frente a pruebas funcionales; brecha entre investigación (p. ej. detección de regresiones) y práctica.
- Evidencia empírica obligatoria (estudios de práctica en proyectos open source y encuestas industriales); **ninguna estadística sin fuente verificable**.
- Cierre: pregunta-problema y justificación del taller.

### 5.3 Metodología (3.5 p.)

- **Enfoque:** investigación teórico-aplicada: revisión de literatura semi-sistemática + estudio experimental (taller).
- **Fuentes:** IEEE Xplore, ACM Digital Library, Scopus/Google Scholar, normas ISO/IEC, syllabus ISTQB, documentación oficial de herramientas.
- **Cadenas de búsqueda** (ejemplos): `"performance testing" AND ("load testing" OR "stress testing")`, `"load testing" AND (survey OR "state of practice")`, `"performance regression" AND ("continuous integration" OR DevOps)`.
- **Criterios de inclusión:** 2010–2026 (excepto clásicos), revisado por pares, normas, o documentación oficial; en inglés o español.
- **Criterios de exclusión:** blogs sin autoría identificable, contenido de marketing sin datos, temas de la columna "Excluir".
- **Procedimiento de uso y validación de IA:** *por definir* (se trabajará con skills).

### 5.4 Marco teórico (17 p.)

| Subsección | Páginas | Contenido clave |
|---|---|---|
| 5.1 Aseguramiento de la calidad en la fase de implementación | 2 | Ciclo de vida, modelo en V, CI/CD, *quality gates*, *shift-left* vs *shift-right* |
| 5.2 Eficiencia de desempeño en ISO/IEC 25010 | 1 | Comportamiento temporal, utilización de recursos, capacidad |
| 5.3 Conceptos y métricas fundamentales | 3 | Latencia vs. tiempo de respuesta, *throughput*, percentiles (por qué no el promedio), concurrencia, usuarios virtuales, *think time*, ley de Little, modelos de carga abiertos vs. cerrados, *coordinated omission* |
| 5.4 Clasificación de las pruebas de rendimiento | 2.5 | Carga, estrés, *spike*, *soak*; mención de escalabilidad, volumen y capacidad. Tabla comparativa: objetivo, perfil de carga, duración, qué detecta |
| 5.5 Proceso de pruebas de rendimiento | 2 | Fases según ISTQB CT-PT: planificación, análisis/diseño (perfil operacional, modelo de carga), implementación (scripts, datos), ejecución, análisis y reporte; requisitos de entorno |
| 5.6 Principios, buenas prácticas y antipatrones | 2 | Línea base, aislamiento del generador de carga, calentamiento, repetibilidad, datos realistas; antipatrones (promedios, entorno compartido, probar sin objetivos) |
| 5.7 Automatización e integración en CI/CD | 1.5 | Umbrales como criterio pass/fail, detección de regresiones, frecuencia de ejecución, observabilidad como complemento |
| 5.8 Catálogo y comparativa de herramientas | 3 | Ver §6 |

### 5.5 Propuesta de taller práctico (11.5 p.) — Fase 2

Contenido mínimo exigido por el enunciado: contexto de aplicación, recursos y código, stack tecnológico y guía paso a paso, más el plan de pruebas ejecutable con los compañeros (objetivo específico 5). Las subsecciones y su distribución de páginas se definen en la Fase 2.

### 5.6 Conclusiones (2.5 p.) — Fase 2

- Hallazgos por pregunta de investigación.
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

## 7. Taller práctico — Fase 2 (por definir)

Esta sección se construirá mediante discusión de opciones. Solo está fijado lo siguiente:

- **Herramienta:** Gatling.
- **Objeto bajo prueba:** una API REST.
- **Restricción ética:** solo se prueba contra un entorno propio, nunca contra sistemas de terceros ni sitios públicos.
- **Extensión:** 11.5 páginas en el documento.

**Decisiones pendientes:**

- [ ] Sistema bajo prueba: qué API, qué lenguaje o framework, si se construye desde cero o se reutiliza una existente
- [ ] Problema de rendimiento a demostrar, si lo hay, y cómo se evidencia
- [ ] Forma de uso de Gatling (lenguaje del DSL, herramienta de build, ejecución)
- [ ] Entorno de ejecución y reproducibilidad para los compañeros
- [ ] Integración con CI: si se incluye y con qué plataforma
- [ ] Escenarios de prueba y criterios de aceptación (SLO)
- [ ] Estructura del plan de pruebas y de la guía paso a paso

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

## 9. Anexos previstos (6.5 páginas en total)

El material extenso (código completo, registros íntegros de IA) va en un **repositorio**; los anexos solo contienen el enlace y extractos representativos.

| Anexo | Contenido | Fase | Páginas |
|---|---|---|---|
| A | Registro resumido de consultas de IA | 1 | 1.5 |
| B | Resumen de la validación crítica de los productos de IA y su resolución | 1 | 1.5 |
| C | Material del taller (código, resultados, capturas); contenido por definir | 2 | 3.5 |
