# Plan — Introducción

**Estado:** Aprobado | **Modo:** Ligero | **Versión:** 7 | **Fecha:** 2026-11-07 | **Presupuesto:** 875 palabras

> **Cambios en la versión 7:** migrado a la plantilla nueva. La tabla «Subsecciones» pasa a «Esquema argumental», con la idea central de cada bloque. Se quitan los puntos a investigar P1–P8 y la nota para el investigador, que el modo ligero no usa. Las fuentes y su verificación no cambian. Presupuesto ajustado según la auditoría, ronda 4: B1 375, B2 150, B3 225, B4 125.
>
> **Cambios en la versión 6:** se adopta el flujo de trabajo nuevo (ver `Workflow.md` y `Guía de redacción.md`); el estado «Final» pasa a «Aprobado». El borrador v3 se reescribió con voz propia y menos citas. B3 ya no enumera los objetivos específicos ni las preguntas de investigación, y no menciona el uso de IA. Las preguntas pasan a B4, junto a la sección que responde cada una. Presupuesto redistribuido: B1 350, B2 150, B3 225, B4 150.
>
> **Cambios en la versión 5:** el borrador v1 señaló que en B3 falta respaldo para la motivación de automatizar las pruebas e integrarlas en CI. Se agregan los puntos P7 y P8 y las fuentes F8 y F9. Se pasan 25 palabras de B1 a B3 para dar lugar a esa motivación. B1 ya tenía 385 palabras en el borrador.

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

## Esquema argumental
| Bloque | Palabras | Idea central | Contenido | Insumos y fuentes |
|---|---|---|---|---|
| B1. El rendimiento como atributo de calidad | 375 | El rendimiento es un atributo de calidad reconocido por la norma, y descuidarlo tiene costos concretos para el usuario, para la organización y para la infraestructura. | Definición de eficiencia de desempeño (sin subcaracterísticas). Umbrales de tiempo de respuesta de Nielsen. Fallas por incapacidad de escalar y el caso HealthCare.gov. Sobreaprovisionamiento como costo de no medir. | `Alcance.md` §5.1; F7, F4, F3, F5, F6 |
| B2. Ubicación en el ciclo de vida | 150 | El trabajo se concentra en la validación del sistema integrado antes del despliegue, porque es donde los resultados mejor anticipan el comportamiento en producción. | Fase de implementación. Recomendaciones del ISTQB: probar temprano y, en los niveles de sistema y de integración de sistemas, usar entornos, datos y cargas realistas. La CI desde desarrollo como puente, no como segundo eje. | `Alcance.md` §1; `Enunciado.md` (objetivo específico 3); F2 |
| B3. Motivación, enfoque y objetivo | 225 | Como cada versión puede alterar el desempeño, las pruebas deben automatizarse e integrarse en CI; de ahí el enfoque y el objetivo del trabajo. | Entregas frecuentes y evaluación continua del desempeño. La experiencia de Daly et al. con la revisión manual. Enfoque: API REST, CI y Gatling. Objetivo general, con el taller y el plan de pruebas para los compañeros. No enumera los objetivos específicos ni menciona el uso de IA. La detección de regresiones y los umbrales van en el Marco teórico §5.7. | `Enunciado.md` (objetivo general, objetivos específicos 4 y 5); `Alcance.md` §1; F8, F9 |
| B4. Estructura del documento y preguntas de investigación | 125 | El documento recorre cinco preguntas de investigación, y cada una se responde en una sección concreta. | Las preguntas PI-1 a PI-5, cada una una sola vez y junto a la sección que la responde; las secciones 3 a 9. | `Alcance.md` §2, §3 y §5 |
| **Total** | **875** | | | |

## Fuentes
| ID  | Referencia y enlace                                                                                                                                                                                                                                     | Acceso                    | Disponibilidad                                                                                                                                                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| F7  | ISO/IEC. (2023). *ISO/IEC 25010:2023 Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (2.ª ed.). https://www.iso.org/standard/78176.html                                   | Cerrada                   | Local (`Adjuntos/Local/ISO-IEC 25010-2023/ISO-IEC 25010-2023.pdf`)                                                                                                                       |
| F2  | ISTQB. (2018). *Certified Tester Foundation Level Specialist Syllabus — Performance Testing* (Versión 2018, 9 de diciembre de 2018). https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf                                | Abierta                   | https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf                                                                                   |
| F3  | Jiang, Z. M., & Hassan, A. E. (2015). A survey on load testing of large-scale software systems. *IEEE Transactions on Software Engineering, 41*(11), 1091–1118. https://doi.org/10.1109/TSE.2015.2445340                                                | Abierta (copia del autor) | https://www.eecs.yorku.ca/~zmjiang/publications/tse2015_jiang.pdf                                                                                                     |
| F4  | Nielsen, J. (1993). *Response times: The 3 important limits*. Nielsen Norman Group. Extracto del capítulo 5 de *Usability Engineering*, con actualización de 2014. https://www.nngroup.com/articles/response-times-3-important-limits/                  | Abierta                   | https://www.nngroup.com/articles/response-times-3-important-limits/                                                                                                   |
| F5  | U.S. Government Accountability Office. (2014). *Healthcare.gov: Ineffective planning and oversight practices underscore the need for improved contract management* (GAO-14-694). https://www.gao.gov/products/gao-14-694                                | Abierta                   | https://www.gao.gov/assets/gao-14-694.pdf                                                                                                                             |
| F6  | Amazon Web Services. (s. f.). *AWS Well-Architected Framework*: páginas «Performance efficiency» y «Cost optimization — Definition». Consultado el 2026-11-06. https://docs.aws.amazon.com/wellarchitected/latest/framework/performance-efficiency.html | Abierta                   | https://docs.aws.amazon.com/wellarchitected/latest/framework/performance-efficiency.html · https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-def.html |
| F8  | Brunnert, A., van Hoorn, A., Willnecker, F., Danciu, A., Hasselbring, W., Heger, C., Herbst, N., Jamshidi, P., Jung, R., von Kistowski, J., Koziolek, A., Kroß, J., Spinner, S., Vögele, C., Walter, J., & Wert, A. (2015). *Performance-oriented DevOps: A research agenda* (Informe técnico SPEC-RG-2015-01). SPEC Research Group — DevOps Performance Working Group, Standard Performance Evaluation Corporation. https://research.spec.org/publications/brunnert_performance_oriented_devops_2015 | Abierta | https://research.spec.org/fileadmin/user_upload/documents/wg_devops/endorsed_publications/SPEC-RG-2015-001-DevOpsPerformanceResearchAgenda.pdf · https://arxiv.org/pdf/1508.04752 |
| F9  | Daly, D., Brown, W., Ingo, H., O'Leary, J., & Bradford, D. (2020). The use of change point detection to identify software performance regressions in a continuous integration system. En *Proceedings of the 2020 ACM/SPEC International Conference on Performance Engineering (ICPE '20)* (pp. 67–75). ACM. https://doi.org/10.1145/3358960.3375791 | Abierta (CC BY 4.0) | https://research.spec.org/icpe_proceedings/2020/proceedings/p67.pdf |

**Verificación (2026-11-06):**

- **F7:** ficha de ISO: publicada, 2.ª edición, 2023-11, de pago. Copia local revisada (BS ISO/IEC 25010:2023, «UK implementation of ISO/IEC 25010:2023»):
  - 2.ª edición, 2023-11.
  - Definición de *performance efficiency* en §3.2.
  - Las nueve características del modelo en §4.1.
- **F2:** portada y fecha leídas en el PDF. Ubicación de las secciones: §1.1 en la p. 10 (corregido en v5 según la auditoría de evidencia, ronda 1) y §1.3.2 en las pp. 13–14.
- **F3:** volumen, número, páginas (1091–1118) y DOI leídos en la copia del autor. La afirmación de P3 está en la introducción y cita a Weyuker y Vokolos (2000), cuyo texto completo es cerrado.
- **F4:** autor, fecha y límites leídos en la página.
- **F5:** título, fecha y conclusión leídos en la ficha de la GAO.
- **F6:** las dos páginas fueron leídas; no tienen fecha de versión, por eso se usa la fecha de consulta.
- **F8:** la ficha del SPEC RG da el título, los 16 autores en orden, el número de informe y la fecha (agosto de 2015). El texto completo se leyó en la copia de arXiv (1508.04752v1). §4.4 «Performance Change Detection» está en las pp. 20–21. Es un informe técnico del grupo de investigación, no un artículo arbitrado.
- **F9:** el título, los autores, el congreso, el DOI y la licencia CC BY 4.0 se leyeron en el PDF de las actas de ICPE '20, pp. 67–75. §1 y §1.1 están en las pp. 67–68. La versión de arXiv (2003.00584) se titula *Change Point Detection in Software Performance Testing*. Se cita la versión publicada.
- **Descartada:** Waller, Ehmke y Hasselbring (2015), *ACM SIGSOFT Software Engineering Notes, 40*(2). El argumento coincide con el de P7, pero el caso es un *microbenchmark* (excluido por el alcance) y el repositorio la registra como no arbitrada. F8 la cita como antecedente.
