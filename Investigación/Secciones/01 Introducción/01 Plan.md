# Plan — Introducción

**Estado:** Final | **Versión:** 4 | **Fecha:** 2026-11-06 | **Presupuesto:** 875 palabras

## Objetivo y alcance

Sección 2 del documento («Introducción», `Alcance.md` §5 y §5.1; `Enunciado.md` §2). Debe presentar el tema, justificar su relevancia en la ingeniería de software y exponer la motivación, los objetivos y la estructura del documento. Responde a lo que pide el enunciado: «Presentación general del tema, relevancia en la ingeniería de software y motivación del estudio».

**Incluye:**

- El rendimiento como atributo de calidad y su impacto en el negocio, en la experiencia del usuario y en el costo de la infraestructura.
- La ubicación del tema en la fase de implementación.
- El enfoque (API REST, CI, Gatling), los objetivos, las preguntas de investigación y la estructura del documento.

**No incluye (lo cubren otras secciones):**

- Definiciones de las subcaracterísticas de ISO/IEC 25010, que van en el Marco teórico §5.2. Aquí solo se nombra la característica.
- Las causas por las que las pruebas se ejecutan tarde o en entornos no representativos, y la evidencia sobre adopción. Todo eso va en el Planteamiento del problema, igual que la pregunta-problema.
- *Shift-left*, *shift-right*, CI/CD y *quality gates* en detalle, que van en el Marco teórico §5.1 y §5.7.
- Fuentes, cadenas de búsqueda y procedimiento con IA, que van en Metodología.
- Métricas de frontend como Core Web Vitals, excluidas por el alcance. Los umbrales de percepción del usuario se usan solo para mostrar por qué importa el tiempo de respuesta de extremo a extremo.

**Forma:** los cuatro bloques son grupos de párrafos dentro de una sola sección. No llevan subtítulos en el documento, porque en 2.5 páginas los subtítulos fragmentarían el texto.

## Subsecciones
| Subsección | Palabras | Qué comunica | Insumos | Puntos |
|---|---|---|---|---|
| B1. El rendimiento como atributo de calidad | 350 | Que el rendimiento es una característica de calidad del producto según la norma, no un aspecto accesorio. Que tiene impacto en tres frentes: la experiencia del usuario (umbrales de tiempo de respuesta), el negocio (las fallas de sistemas a gran escala se deben con frecuencia a la incapacidad de escalar, como en el caso HealthCare.gov) y el costo de la infraestructura (el sobreaprovisionamiento compensa la ineficiencia). | `Alcance.md` §5.1; F2–F7 | P1, P2, P3, P4, P5 |
| B2. Ubicación en el ciclo de vida | 175 | Que el trabajo se sitúa en la fase de implementación: validación previa al despliegue del sistema integrado, en los niveles de sistema e integración de sistemas, donde el entorno, los datos y la carga deben ser realistas. Que la ejecución en CI desde desarrollo se trata como puente y no como segundo eje. | `Alcance.md` §1; `Enunciado.md` (fases de desarrollo e implementación, objetivo específico 3); F2 | P6 |
| B3. Motivación, enfoque y objetivos | 225 | Por qué automatizar estas pruebas sobre API REST y llevarlas a un pipeline de CI. La herramienta del taller, Gatling. El objetivo general, los objetivos específicos y las preguntas PI-1 a PI-5. El uso de IA como base inicial validada críticamente, mencionado en una sola oración porque el procedimiento va en Metodología. | `Enunciado.md` (objetivo general, objetivos específicos, nota metodológica); `Alcance.md` §1 y §3 | — |
| B4. Estructura del documento | 125 | Qué contiene cada sección (3 a 9) y qué pregunta de investigación responde cada una. | `Alcance.md` §2 y §5 (tabla de secciones y PI) | — |
| **Total** | **875** | | | |

## Puntos a investigar
| ID | Pregunta | Subsección | Fuentes |
|---|---|---|---|
| P1 | ¿Cómo define ISO/IEC 25010:2023 la eficiencia de desempeño (§3.2) y dónde la ubica dentro del modelo de calidad del producto (§4.1)? ¿Cómo relaciona el syllabus ISTQB CT-PT (§1.1) la eficiencia de desempeño con la experiencia del usuario? | B1 | F7, F2 |
| P2 | ¿Qué tres límites de tiempo de respuesta propone Nielsen (1993) para la percepción del usuario y qué significa cada uno? | B1 | F4 |
| P3 | ¿Qué afirman Jiang y Hassan (2015) sobre la causa predominante de las fallas en sistemas de gran escala (incapacidad de escalar frente a defectos funcionales) y qué casos públicos citan como ejemplo? | B1 | F3 |
| P4 | ¿Qué consecuencias del lanzamiento de HealthCare.gov (1 de octubre de 2013) documenta la GAO en GAO-14-694 y qué concluye sobre la verificación de los requisitos de desempeño antes del lanzamiento? | B1 | F5 |
| P5 | ¿Cómo define el AWS Well-Architected Framework la eficiencia de desempeño y cómo vincula el uso de los recursos con el costo, mediante el sobreaprovisionamiento? | B1 | F6 |
| P6 | ¿En qué niveles de prueba ubica el syllabus ISTQB CT-PT (§1.3.2) las pruebas dinámicas de rendimiento y qué exige en los niveles de sistema e integración de sistemas? | B2 | F2 |

> **Nota para el investigador:** en P1 basta con la definición y la ubicación. Las subcaracterísticas (§3.2.1–3.2.3) le corresponden al Marco teórico §5.2. La copia local de F7 es la adopción británica BS ISO/IEC 25010:2023, que implementa el texto de ISO/IEC 25010:2023. Se cita como ISO/IEC 25010:2023.
>
> En P4 basta con el impacto y la conclusión sobre la falta de verificación. Las causas detalladas (pruebas incompletas, capacidad no planificada) están en GAO-15-238 y le corresponden al Planteamiento del problema.

## Fuentes
| ID  | Referencia y enlace                                                                                                                                                                                                                                     | Acceso                    | Disponibilidad                                                                                                                                                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| F7  | ISO/IEC. (2023). *ISO/IEC 25010:2023 Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (2.ª ed.). https://www.iso.org/standard/78176.html                                   | Cerrada                   | Local (`Adjuntos/Local/ISO-IEC 25010-2023.pdf`)                                                                                                                       |
| F2  | ISTQB. (2018). *Certified Tester Foundation Level Specialist Syllabus — Performance Testing* (Versión 2018, 9 de diciembre de 2018). https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf                                | Abierta                   | https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf                                                                                   |
| F3  | Jiang, Z. M., & Hassan, A. E. (2015). A survey on load testing of large-scale software systems. *IEEE Transactions on Software Engineering, 41*(11), 1091–1118. https://doi.org/10.1109/TSE.2015.2445340                                                | Abierta (copia del autor) | https://www.eecs.yorku.ca/~zmjiang/publications/tse2015_jiang.pdf                                                                                                     |
| F4  | Nielsen, J. (1993). *Response times: The 3 important limits*. Nielsen Norman Group. Extracto del capítulo 5 de *Usability Engineering*, con actualización de 2014. https://www.nngroup.com/articles/response-times-3-important-limits/                  | Abierta                   | https://www.nngroup.com/articles/response-times-3-important-limits/                                                                                                   |
| F5  | U.S. Government Accountability Office. (2014). *Healthcare.gov: Ineffective planning and oversight practices underscore the need for improved contract management* (GAO-14-694). https://www.gao.gov/products/gao-14-694                                | Abierta                   | https://www.gao.gov/assets/gao-14-694.pdf                                                                                                                             |
| F6  | Amazon Web Services. (s. f.). *AWS Well-Architected Framework*: páginas «Performance efficiency» y «Cost optimization — Definition». Consultado el 2026-11-06. https://docs.aws.amazon.com/wellarchitected/latest/framework/performance-efficiency.html | Abierta                   | https://docs.aws.amazon.com/wellarchitected/latest/framework/performance-efficiency.html · https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-def.html |

**Verificación (2026-11-06):**

- **F7:** ficha de ISO: publicada, 2.ª edición, 2023-11, de pago. Copia local revisada (BS ISO/IEC 25010:2023, «UK implementation of ISO/IEC 25010:2023»):
  - 2.ª edición, 2023-11.
  - Definición de *performance efficiency* en §3.2.
  - Las nueve características del modelo en §4.1.
- **F2:** portada y fecha leídas en el PDF. Ubicación de las secciones: §1.1 en la p. 11 y §1.3.2 en las pp. 13–14.
- **F3:** volumen, número, páginas (1091–1118) y DOI leídos en la copia del autor. La afirmación de P3 está en la introducción y cita a Weyuker y Vokolos (2000), cuyo texto completo es cerrado.
- **F4:** autor, fecha y límites leídos en la página.
- **F5:** título, fecha y conclusión leídos en la ficha de la GAO.
- **F6:** las dos páginas fueron leídas; no tienen fecha de versión, por eso se usa la fecha de consulta.
