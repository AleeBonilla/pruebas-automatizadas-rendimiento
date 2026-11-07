# Marco teórico — 5.1 y 5.2

<!-- Borrador v2 | Plan v3 | Evidencia v2 | 2026-11-07 -->
<!-- v2: corrige los hallazgos bloqueantes 1–4 y aplica las sugerencias 5–8 de la auditoría, ronda 1. Después de la ronda 2 (aprobada) se aplica su sugerencia 1: cambio de prosa sin citas, no requiere nueva auditoría. -->

## 5.1 Aseguramiento de la calidad en la fase de implementación

<!-- B1. Ciclo de vida y niveles de prueba -->

El aseguramiento de la calidad y las pruebas suelen usarse como sinónimos, pero no lo son. El aseguramiento de la calidad es un enfoque preventivo, orientado al proceso, que se ocupa de implantar y mejorar los procesos; las pruebas, en cambio, son un enfoque correctivo, orientado al producto, que busca alcanzar niveles adecuados de calidad en lo que se construye (ISTQB, 2024) <!-- E1 -->. Las pruebas de rendimiento pertenecen al segundo grupo, pero dependen del primero: solo se ejecutan a tiempo si el proceso las prevé.

El modelo de ciclo de vida determina cuándo ocurre cada prueba. El modelo en V, uno de los modelos secuenciales, hace visible una buena práctica que el ISTQB plantea para cualquier modelo: a cada actividad de desarrollo le corresponde una actividad de prueba. Del lado de las pruebas, el syllabus distingue cinco niveles: componentes, integración de componentes, sistema, integración de sistemas y aceptación. En el nivel de sistema se prueba el comportamiento del sistema completo, incluidas sus características no funcionales, y la integración de sistemas requiere entornos de prueba preferiblemente similares al de operación (ISTQB, 2024) <!-- E2, E3, E4 -->.

En las pruebas de rendimiento, estos dos niveles cumplen funciones distintas: el de sistema evalúa el comportamiento de extremo a extremo bajo distintas condiciones de carga, y el de integración de sistemas, los flujos de datos y de trabajo a través de las interfaces entre sistemas (ISTQB, 2018) <!-- E5, E6 -->. La Figura 1 sitúa estos niveles en el modelo en V.

<!-- B2. DevOps, CI/CD y quality gates -->

Si el ciclo de vida dice cuándo se prueba, DevOps cambia cómo: al promover la integración y la entrega continuas, da a las pruebas retroalimentación rápida sobre si cada cambio perjudica el código existente y más visibilidad de las características no funcionales, como la eficiencia de desempeño (ISTQB, 2024) <!-- E7, E8 -->. CI/CD agrupa tres prácticas: en la integración continua, el equipo integra su trabajo con frecuencia, incluso varias veces al día; en la entrega continua, la aplicación queda siempre lista para producción tras superar pruebas automatizadas y controles de calidad, y en el despliegue continuo se despliega a producción automáticamente (Shahin et al., 2017) <!-- E9 -->.

Las une el pipeline de despliegue (*deployment pipeline*). Humble y Farley (2010) <!-- E10, E11, E12, E13 --> lo definen como la manifestación automatizada del proceso que lleva el software desde el control de versiones hasta los usuarios, y describen sus etapas como compuertas, desde la de *commit* hasta la de pruebas de aceptación automatizadas: solo las versiones que superan esta última pueden avanzar a las etapas siguientes. También advierten que los resultados de las pruebas de capacidad pueden funcionar como compuerta o solo informar una decisión humana. Los *quality gates* aparecen, junto con los pipelines y con referencia a esos autores, entre los medios de automatización de DevOps (Bezemer et al., 2019) <!-- E14 -->; en este trabajo, el término designa esas compuertas.

<!-- B3. Shift-left y shift-right -->

Este modo de trabajar desplaza las pruebas hacia el inicio del ciclo. El ISTQB llama *shift-left* a ese principio de probar antes, aclara que no implica descuidar las pruebas posteriores y propone ejecutar pruebas no funcionales desde el nivel de componentes cuando sea posible, porque suelen dejarse para cuando ya existen el sistema completo y un entorno representativo (ISTQB, 2024) <!-- E15, E16 -->. En el extremo opuesto, *shift-right* traslada parte de las pruebas a producción (Microsoft, 2022) <!-- E17 -->; en rendimiento, eso incluye fijar umbrales a partir de los límites de escalabilidad conocidos y monitorearlos en producción para anticipar problemas (ISTQB, 2018) <!-- E18 -->. Este trabajo se ubica entre ambos extremos: valida el sistema integrado antes del despliegue, en los niveles de sistema y de integración de sistemas, y usa la ejecución en CI desde el desarrollo como puente hacia esa validación. Las dos piezas no compiten: una prueba breve con cada cambio da una señal temprana de que algo empeoró, y la validación completa del sistema integrado confirma, antes de desplegar, si se cumplen los requisitos.

<!-- FIGURA: Figura 1. Las pruebas de rendimiento en el modelo en V y en el pipeline de CI/CD. A la izquierda, el modelo en V: actividades de desarrollo en el brazo izquierdo (requisitos, diseño del sistema, diseño de componentes, código) y los cinco niveles de prueba en el brazo derecho (componentes, integración de componentes, sistema, integración de sistemas, aceptación). No se presupone una relación uno a uno entre las cuatro actividades y los cinco niveles: las líneas horizontales solo indican que a cada actividad de desarrollo le corresponde actividad de prueba. Sistema e integración de sistemas aparecen resaltados como foco del trabajo; componentes, marcado como posible shift-left de las pruebas no funcionales. A la derecha, el pipeline de despliegue: commit → pruebas de aceptación → pruebas de rendimiento (compuerta o información) → despliegue → producción, con producción y su monitoreo marcados como shift-right. Elaboración propia a partir de ISTQB (2024, 2018) y Humble y Farley (2010). -->

**Figura 1.** Las pruebas de rendimiento en el modelo en V y en el pipeline de CI/CD.

*Fuente:* elaboración propia. Modelo en V, niveles de prueba y *shift-left*: ISTQB (2024) <!-- E2, E3, E4, E16 -->. Rendimiento por nivel y monitoreo en producción: ISTQB (2018) <!-- E5, E6, E18 -->. Pipeline de despliegue y compuertas: Humble y Farley (2010) <!-- E10, E11, E12, E13 -->. *Shift-right*: Microsoft (2022) <!-- E17 -->.

## 5.2 Eficiencia de desempeño en ISO/IEC 25010

<!-- B4. Subcaracterísticas de la eficiencia de desempeño -->

ISO/IEC 25010:2023 no trata la eficiencia de desempeño como un atributo indivisible: la descompone en tres subcaracterísticas, comportamiento temporal, utilización de recursos y capacidad, las mismas que ya tenía la edición de 2011 (ISO & IEC, 2023) <!-- E19, E20, E21, E22, E26 -->. Las tres se definen frente a requisitos especificados, no frente a una idea abstracta de rapidez, y entre los recursos la norma cuenta la CPU, la memoria, el almacenamiento y los dispositivos de red. La Tabla 1 recoge la definición de cada una y el objetivo de prueba que el syllabus del ISTQB le asocia.

Distinguirlas no es un ejercicio de clasificación. Una respuesta lenta, un consumo excesivo de recursos y un límite de capacidad insuficiente son problemas distintos, que se detectan con mediciones distintas. En una API, estas diferencias pueden observarse, por ejemplo, en los tiempos de respuesta y el *throughput*, en el consumo de CPU y memoria del servidor, aunque las respuestas sigan llegando a tiempo, y en el cumplimiento de los requisitos con la carga exigida. Por eso la selección de medidas debe partir del requisito que se quiere comprobar, y una prueba sin requisitos explícitos no puede decir si el sistema cumple. De las tres, el comportamiento temporal es, en general, el objetivo más común de las pruebas de rendimiento (ISTQB, 2018) <!-- E23 -->, pero una prueba que solo mira los tiempos de respuesta puede pasar por alto un servidor que se acerca a su límite. Las métricas con que se observa cada subcaracterística se tratan en la sección siguiente.

**Tabla 1.** Subcaracterísticas de la eficiencia de desempeño

| Subcaracterística | Definición en ISO/IEC 25010:2023 | Objetivo de prueba asociado | Qué se observa |
|---|---|---|---|
| Comportamiento temporal | Capacidad de un producto de ejecutar su función especificada, en condiciones especificadas, de modo que los tiempos de respuesta y las tasas de *throughput* cumplan los requisitos <!-- E20 --> | En general, el objetivo más común de las pruebas de rendimiento <!-- E23 --> | Tiempos de respuesta y *throughput* (5.3) |
| Utilización de recursos | Capacidad de un producto de no usar más que la cantidad especificada de recursos para ejecutar su función, en condiciones especificadas <!-- E21 --> | Se investiga con pruebas específicas cuando la disponibilidad de los recursos es un riesgo <!-- E24 --> | Consumo de recursos del servidor, como CPU y memoria <!-- E26 --> |
| Capacidad | Capacidad de un producto de cumplir los requisitos sobre los límites máximos de un parámetro, como el número de usuarios concurrentes o el *throughput* de transacciones <!-- E22 --> | Se evalúa cuando el riesgo está en el comportamiento del sistema en sus límites requeridos, como el número de usuarios o el volumen de datos <!-- E25 --> | Carga máxima que el sistema admite sin incumplir sus requisitos |

*Fuente:* elaboración propia. Definiciones: ISO e IEC (2023) <!-- E20, E21, E22 -->. Objetivos de prueba: ISTQB (2018) <!-- E23, E24, E25 -->. Ejemplos de recursos: ISO e IEC (2023) <!-- E26 -->. La columna «Qué se observa» aplica esas definiciones al objeto de este trabajo.
