# Introducción

<!-- Borrador v2 | Plan v5 | Evidencia v4 | 2026-11-07 -->

<!-- Según el plan, los cuatro bloques no llevan subtítulos en el documento. Se marcan con comentarios para la trazabilidad. -->

<!-- B1. El rendimiento como atributo de calidad -->

La norma ISO/IEC 25010:2023 define la eficiencia de desempeño como la capacidad de un producto de ejecutar sus funciones dentro de parámetros especificados de tiempo y de *throughput*, y de ser eficiente en el uso de los recursos en condiciones especificadas (International Organization for Standardization [ISO] & International Electrotechnical Commission [IEC], 2023) <!-- E1 -->. Es una de las nueve características del modelo de calidad del producto (ISO & IEC, 2023) <!-- E2 -->, de carácter no funcional (International Software Testing Qualifications Board [ISTQB], 2018) <!-- E5 -->.

Su relevancia se manifiesta en tres frentes. En la experiencia del usuario, el rendimiento es esencial para ofrecer una buena experiencia (ISTQB, 2018) <!-- E3 -->. Nielsen (1993) <!-- E6, E7, E8 --> propone tres límites: hasta 0,1 segundos la reacción se percibe instantánea; hasta 1 segundo el flujo de pensamiento no se interrumpe, y hacia los 10 segundos se pierde la atención del usuario. Estas pautas valen también para las aplicaciones web (Nielsen, 1993) <!-- E9 -->.

En el negocio, según los estudios que reseñan Jiang y Hassan (2015) <!-- E10, E11 -->, las fallas de los sistemas de gran escala tienden a deberse a la incapacidad de escalar ante la demanda, más que a defectos funcionales, y esa incapacidad suele provocar fallas catastróficas y cobertura mediática desfavorable, como ocurrió con el sitio de salud del Gobierno estadounidense, HealthCare.gov. Al abrirse la inscripción, el 1 de octubre de 2013, muchos usuarios no pudieron usarlo por fallas, errores y tiempos de respuesta lentos (U.S. Government Accountability Office [GAO], 2014) <!-- E12 -->. Se había lanzado sin la verificación requerida de los requisitos de desempeño, y luego se destinaron más de 708 000 dólares a expertos en desempeño y 1,5 millones a ampliar la capacidad (GAO, 2014) <!-- E14, E15 -->.

En la infraestructura, Amazon Web Services (AWS, s. f.-b) <!-- E16 --> vincula la eficiencia de desempeño con el uso eficiente de los recursos de la nube y advierte que la tentación de sobrecompensar por si acaso, en vez de hacer pruebas comparativas para hallar el despliegue de menor costo, puede producir despliegues sobreaprovisionados (AWS, s. f.-a) <!-- E17 -->.

<!-- B2. Ubicación en el ciclo de vida -->

Este trabajo sitúa las pruebas de rendimiento en la fase de implementación, entendida como la validación previa al despliegue del sistema integrado. Así se atiende el objetivo de contextualizar el aseguramiento de la calidad del producto dentro de una etapa del ciclo de vida. El syllabus del ISTQB recomienda iniciar las pruebas dinámicas de rendimiento lo antes posible, conforme se construye el sistema, y las contempla desde las pruebas unitarias hasta las de aceptación (ISTQB, 2018) <!-- E19 -->. En el nivel de sistema, evalúan el comportamiento de extremo a extremo bajo distintas condiciones de carga; en el de integración de sistemas, se enfocan en los flujos de datos y de trabajo a través de las interfaces clave entre sistemas (ISTQB, 2018) <!-- E20, E21 -->. En ambos niveles, en los que se concentra este estudio, es crítico usar entornos, datos y cargas realistas para obtener resultados precisos (ISTQB, 2018) <!-- E22 -->. La ejecución de las pruebas en un pipeline de integración continua (CI) desde el desarrollo se trata como un puente hacia esa validación, no como un segundo eje.

<!-- B3. Motivación, enfoque y objetivos -->

Esa relevancia motiva el estudio de las pruebas de rendimiento automatizadas. Según Brunnert et al. (2015) <!-- E23, E24 -->, reaccionar con rapidez a los cambios del negocio exige entregas frecuentes, y como el desempeño puede cambiar con cada versión nueva, debe evaluarse de forma continua antes de que esta pase a producción. En la industria, Daly et al. (2020) <!-- E26, E29 --> describen un sistema de CI que registra cada *commit* y también ejecuta las pruebas de rendimiento, con el fin de detectar qué *commits* cambian el desempeño; como revisar manualmente los gráficos no era sostenible, automatizaron la detección (Daly et al., 2020) <!-- E28 -->. Por ello, este trabajo estudia esas pruebas sobre API web HTTP/REST, en un pipeline de CI y con Gatling como herramienta del taller.

El objetivo general es realizar una investigación teórico-aplicada sobre estas pruebas, con su estado del arte, y demostrar sus conceptos en un taller práctico. Los objetivos específicos son emplear la IA para generar el marco teórico y auditar críticamente sus productos, contextualizar la calidad en la fase de implementación, diseñar el taller y formular un plan de pruebas aplicable con los compañeros.

Las preguntas de investigación indagan qué son estas pruebas, cómo se clasifican y qué métricas las definen (PI-1); qué problemas dificultan su adopción (PI-2); qué prácticas las rigen y cómo se integran en CI/CD (PI-3); cómo se comparan las herramientas (PI-4), y cómo se demuestra con Gatling la detección de un problema y la verificación de su corrección (PI-5). La IA aporta una base inicial que se valida críticamente, como detalla la Metodología.

<!-- B4. Estructura del documento -->

El resto del documento se organiza así. La sección 3, Planteamiento del problema, documenta las limitaciones para adoptar y automatizar estas pruebas y responde a PI-2. La sección 4, Metodología, describe el enfoque, las fuentes, los criterios de búsqueda y el uso y la validación de la IA. La sección 5, Marco teórico, responde a PI-1, PI-3 y PI-4 con los conceptos, métricas y tipos de prueba, el proceso, las buenas prácticas, la integración en CI/CD y la comparativa de herramientas. La sección 6 presenta el taller con Gatling y responde a PI-5. La sección 7 reúne las conclusiones de todas las preguntas; la 8, las referencias, y la 9, los anexos sobre el uso de la IA y el taller.
