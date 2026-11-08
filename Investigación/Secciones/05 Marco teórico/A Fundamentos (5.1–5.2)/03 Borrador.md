# Marco teórico — 5.1 y 5.2

<!-- Borrador v4 | Plan v5 | Evidencia v3 | 2026-11-07 -->
<!-- v4: corrige el hallazgo bloqueante 1 y aplica la sugerencia 2 de la auditoría, ronda 3. v3: condensación al nuevo presupuesto (550 palabras), según el plan v4. Se conservan todas las fuentes, la Figura 1 y la Tabla 1; dejan de citarse E7 y E8. v2: corrige los hallazgos bloqueantes 1–4 y aplica las sugerencias 5–8 de la auditoría, ronda 1. -->

## 5.1 Aseguramiento de la calidad en la fase de implementación

<!-- B1. Ciclo de vida y niveles de prueba -->

El aseguramiento de la calidad y las pruebas no son sinónimos: el primero es un enfoque preventivo, orientado al proceso; las pruebas, un enfoque correctivo, orientado al producto (ISTQB, 2024) <!-- E1 -->. Las pruebas de rendimiento son del segundo tipo, pero dependen de que el proceso las prevea. El modelo en V, un modelo secuencial, hace visible una buena práctica válida para cualquier modelo: a cada actividad de desarrollo le corresponde una actividad de prueba. El ISTQB distingue cinco niveles: de componentes, de integración de componentes, de sistema, de integración de sistemas y de aceptación (ISTQB, 2024) <!-- E2, E3, E4 -->. En rendimiento, el nivel de sistema evalúa el comportamiento de extremo a extremo bajo distintas condiciones de carga, y el de integración de sistemas, los flujos de datos y de trabajo entre sistemas (ISTQB, 2018) <!-- E5, E6 -->; la Figura 2 los sitúa en el modelo en V.

<!-- B2. DevOps, CI/CD y quality gates -->

CI/CD agrupa tres prácticas: en la integración continua, el equipo integra su trabajo con frecuencia; en la entrega continua, la aplicación queda siempre lista para producción tras superar pruebas automatizadas y controles de calidad, y en el despliegue continuo se despliega a producción automáticamente (Shahin et al., 2017) <!-- E9 -->. Las une el pipeline de despliegue (*deployment pipeline*), la manifestación automatizada del proceso que lleva el software desde el control de versiones hasta los usuarios. Sus etapas incluyen compuertas, como la de *commit*, y los resultados de las pruebas de capacidad pueden ser una compuerta o solo informar una decisión humana (Humble & Farley, 2010) <!-- E10, E11, E13 -->. Bezemer et al. (2019) <!-- E14 --> mencionan los *quality gates*, citando a esos autores, entre los medios de automatización de DevOps; aquí, el término designa esas compuertas.

<!-- B3. Shift-left y shift-right -->

El ISTQB llama *shift-left* al principio de probar antes, aclara que no implica descuidar las pruebas posteriores y propone ejecutar pruebas no funcionales desde el nivel de componentes cuando sea posible (ISTQB, 2024) <!-- E15, E16 -->. *Shift-right*, en cambio, traslada parte de las pruebas a producción (Microsoft, 2022) <!-- E17 -->, donde pueden monitorearse umbrales fijados a partir de los límites de escalabilidad conocidos (ISTQB, 2018) <!-- E18 -->. Este trabajo se ubica entre ambos extremos: valida el sistema integrado antes del despliegue y usa la ejecución en CI desde el desarrollo como puente, porque una prueba breve con cada cambio da una señal temprana y la validación completa confirma si se cumplen los requisitos.

<!-- FIGURA: Figura 2. Las pruebas de rendimiento en el modelo en V y en el pipeline de CI/CD. A la izquierda, el modelo en V: actividades de desarrollo en el brazo izquierdo (requisitos, diseño del sistema, diseño de componentes, código) y los cinco niveles de prueba en el brazo derecho (componentes, integración de componentes, sistema, integración de sistemas, aceptación). No se presupone una relación uno a uno entre las cuatro actividades y los cinco niveles: las líneas horizontales solo indican que a cada actividad de desarrollo le corresponde actividad de prueba. Sistema e integración de sistemas aparecen resaltados como foco del trabajo; componentes, marcado como posible shift-left de las pruebas no funcionales. A la derecha, el pipeline de despliegue: commit → pruebas de aceptación → pruebas de rendimiento (compuerta o información) → despliegue → producción, con producción y su monitoreo marcados como shift-right. Elaboración propia a partir de ISTQB (2024, 2018) y Humble y Farley (2010). -->

**Figura 2.** Las pruebas de rendimiento en el modelo en V y en el pipeline de CI/CD.

*Fuente:* elaboración propia. Modelo en V, niveles de prueba y *shift-left*: ISTQB (2024) <!-- E2, E3, E4, E16 -->. Rendimiento por nivel y monitoreo en producción: ISTQB (2018) <!-- E5, E6, E18 -->. Pipeline de despliegue y compuertas: Humble y Farley (2010) <!-- E10, E11, E12, E13 -->. *Shift-right*: Microsoft (2022) <!-- E17 -->.

## 5.2 Eficiencia de desempeño en ISO/IEC 25010

<!-- B4. Subcaracterísticas de la eficiencia de desempeño -->

ISO/IEC 25010:2023 descompone la eficiencia de desempeño en tres subcaracterísticas, comportamiento temporal, utilización de recursos y capacidad, las mismas que ya tenía la edición de 2011 (ISO & IEC, 2023) <!-- E19, E20, E21, E22 -->. Las tres se definen frente a requisitos especificados, no frente a una idea abstracta de rapidez. La Tabla 1 recoge la definición de cada una y el objetivo de prueba que el syllabus del ISTQB le asocia.

Distinguirlas no es un ejercicio de clasificación. Una respuesta lenta, un consumo excesivo de recursos y un límite de capacidad insuficiente son problemas distintos, que se detectan con mediciones distintas: en una API, los tiempos de respuesta y el *throughput*, el consumo de CPU y memoria del servidor y la carga máxima que admite sin incumplir sus requisitos. Por eso la selección de medidas debe partir del requisito que se quiere comprobar, y una prueba sin requisitos explícitos no puede decir si el sistema cumple. El comportamiento temporal es, en general, el objetivo más común de las pruebas de rendimiento (ISTQB, 2018) <!-- E23 -->, pero una prueba que solo mira los tiempos de respuesta puede pasar por alto un servidor que se acerca a su límite. Las métricas con que se observa cada subcaracterística se tratan en la sección siguiente.

**Tabla 1.** Subcaracterísticas de la eficiencia de desempeño

| Subcaracterística | Definición en ISO/IEC 25010:2023 | Objetivo de prueba asociado | Qué se observa |
|---|---|---|---|
| Comportamiento temporal | Capacidad de un producto de ejecutar su función especificada, en condiciones especificadas, de modo que los tiempos de respuesta y las tasas de *throughput* cumplan los requisitos <!-- E20 --> | En general, el objetivo más común de las pruebas de rendimiento <!-- E23 --> | Tiempos de respuesta y *throughput* (5.3) |
| Utilización de recursos | Capacidad de un producto de no usar más que la cantidad especificada de recursos para ejecutar su función, en condiciones especificadas <!-- E21 --> | Se investiga con pruebas específicas cuando la disponibilidad de los recursos es un riesgo <!-- E24 --> | Consumo de recursos del servidor, como CPU y memoria <!-- E26 --> |
| Capacidad | Capacidad de un producto de cumplir los requisitos sobre los límites máximos de un parámetro, como el número de usuarios concurrentes o el *throughput* de transacciones <!-- E22 --> | Se evalúa cuando el riesgo está en el comportamiento del sistema en sus límites requeridos, como el número de usuarios o el volumen de datos <!-- E25 --> | Carga máxima que el sistema admite sin incumplir sus requisitos |

*Fuente:* elaboración propia. Definiciones: ISO e IEC (2023) <!-- E20, E21, E22 -->. Objetivos de prueba: ISTQB (2018) <!-- E23, E24, E25 -->. Ejemplos de recursos: ISO e IEC (2023) <!-- E26 -->. La columna «Qué se observa» aplica esas definiciones al objeto de este trabajo.
