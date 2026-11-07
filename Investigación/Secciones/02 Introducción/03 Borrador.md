# Introducción

<!-- Borrador v6 | Plan v8 | Evidencia v6 | 2026-11-07 -->
<!-- v6: aplica la sugerencia 1 de la auditoría, ronda 6 (división de una oración, sin cambiar la cita; no requiere nueva auditoría). v5: condensación al nuevo presupuesto (700 palabras), según el plan v8. Se conservan las ocho citas y todas sus fuentes. v4: corrige los hallazgos 1–5 de la auditoría, ronda 4. v3: reescrito según la Guía de redacción. Los bloques no llevan subtítulos en el documento; se marcan con comentarios. -->

<!-- B1. El rendimiento como atributo de calidad -->

Un sistema de software puede cumplir todas sus funciones y, aun así, fallarles a sus usuarios: basta con que responda demasiado lento o deje de responder cuando aumenta la demanda. Por eso el rendimiento es un atributo de calidad y no un aspecto accesorio. La norma ISO/IEC 25010:2023 lo incluye, con el nombre de eficiencia de desempeño, entre las nueve características de su modelo de calidad del producto. Lo define como la capacidad de ejecutar las funciones dentro de parámetros especificados de tiempo y de *throughput*, con un uso eficiente de los recursos en condiciones especificadas (International Organization for Standardization [ISO] & International Electrotechnical Commission [IEC], 2023) <!-- E1, E2 -->.

Descuidarlo tiene costos en varios frentes. Para el usuario, Nielsen (1993) <!-- E7, E8, E9 --> describió umbrales aproximados de percepción que, según él mismo, valen también para la web: alrededor de un segundo está el límite para que conserve el hilo de lo que hace, aunque note la demora, y alrededor de diez, el límite para mantener su atención. En una aplicación web, cada demora del *backend* bajo carga se suma a esa espera.

Para la organización, las fallas de los sistemas de gran escala tienden a deberse a su incapacidad de escalar ante la demanda, más que a defectos funcionales, y con frecuencia son catastróficas (Jiang & Hassan, 2015) <!-- E10, E11 -->. HealthCare.gov, el portal de seguros de salud del Gobierno estadounidense, se puso en operación sin la verificación requerida de sus requisitos de desempeño y, cuando abrió la inscripción el 1 de octubre de 2013, muchos usuarios no pudieron usarlo por fallas, errores y tiempos de respuesta lentos (U.S. Government Accountability Office [GAO], 2014) <!-- E12, E14 -->.

En la infraestructura, por último, no saber cuánta carga soporta un sistema invita a aprovisionar recursos de más «por si acaso»; Amazon Web Services (AWS, s. f.-a) <!-- E17 --> advierte que hacerlo, en lugar de medir para encontrar el despliegue de menor costo, puede conducir a despliegues sobreaprovisionados.

<!-- B2. Ubicación en el ciclo de vida -->

Este trabajo ubica las pruebas de rendimiento en la fase de implementación, entendida como la validación del sistema integrado antes de su despliegue. El syllabus del ISTQB recomienda empezar a probar el rendimiento lo antes posible y, en los niveles de sistema y de integración de sistemas, contar con entornos, datos y cargas realistas para obtener resultados precisos (International Software Testing Qualifications Board [ISTQB], 2018) <!-- E19, E22 -->. Este estudio se concentra en esos dos niveles, porque son los que ejercitan el sistema completo con sus integraciones. La ejecución temprana de las pruebas en un pipeline de integración continua (CI) se aborda como un puente hacia esa validación y no como un segundo eje.

<!-- B3. Motivación, enfoque y objetivos -->

El ritmo actual de entrega explica por qué automatizar esas pruebas. Reaccionar con rapidez a los cambios del negocio exige publicar con frecuencia, en muchas versiones pequeñas, y como cada una puede alterar el desempeño de la aplicación, este debe evaluarse de forma continua antes de que llegue a producción (Brunnert et al., 2015) <!-- E23, E24 -->. Una prueba de carga que se ejecuta a mano, de vez en cuando, no puede seguir ese ritmo. El equipo de MongoDB integró las pruebas de rendimiento en su sistema de CI para identificar qué *commits* cambiaban el desempeño y pronto comprobó que revisar los resultados a mano no era sostenible, por lo que automatizó la detección (Daly et al., 2020) <!-- E26, E28, E29 -->.

Con esa motivación, este trabajo estudia las pruebas de rendimiento automatizadas sobre API web HTTP/REST, integradas en un pipeline de CI y con Gatling como herramienta. El objetivo general es reunir el estado del arte de estas pruebas en una investigación teórico-aplicada y demostrar sus conceptos en un taller práctico, acompañado de un plan de pruebas que los compañeros del curso puedan ejecutar.

<!-- B4. Estructura del documento y preguntas de investigación -->

El documento se organiza en torno a cinco preguntas de investigación. La sección 3 examina qué dificulta adoptar y automatizar las pruebas de rendimiento (PI-2), y la 4 describe la metodología. La sección 5, Marco teórico, explica qué son estas pruebas, cómo se clasifican y qué métricas las definen (PI-1); qué principios y prácticas rigen su diseño, su ejecución y su integración en CI/CD (PI-3), y cómo se comparan las herramientas (PI-4). La sección 6 presenta el taller con Gatling, que muestra cómo se detecta un problema de rendimiento y se verifica su corrección (PI-5). La 7 reúne las conclusiones, y la 8 y la 9, las referencias y los anexos.
