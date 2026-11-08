# Marco teórico — 5.3 y 5.4

<!-- Borrador v4 | Plan v3 | Evidencia v3 | 2026-11-07 -->
<!-- v4: define la tasa de error con Jones et al. (2016), fuente ya incluida en las referencias por el grupo C (E31). v3: corrige el hallazgo bloqueante 1 y aplica las sugerencias 2 y 3 de la auditoría, ronda 2. v2: aplica las sugerencias 1–4 de la auditoría, ronda 1. -->

## 5.3 Conceptos y métricas fundamentales

<!-- B1. Métricas básicas -->

Una prueba de rendimiento observa tres magnitudes. El tiempo de respuesta es lo que espera el usuario; el *throughput*, las transacciones procesadas por unidad de tiempo, y la utilización de recursos, lo que el sistema consume. En general, el primero preocupa al usuario; el segundo, al negocio, y la tercera, al sistema. Una transacción fallida, la que no se completó, dura mucho menos que una completada y puede falsear el *throughput* (ISTQB, 2018) <!-- E1, E2, E3 -->. Por eso se mide aparte la tasa de error, que suele expresarse como fracción de las solicitudes recibidas (Jones et al., 2016) <!-- E31 -->. Aquí, «latencia» designa solo la de red; lo que mide el cliente es tiempo de respuesta.

La carga la generan usuarios virtuales, instancias que repiten las acciones de un tipo de usuario. Su número modela la concurrencia, cuántos usuarios actúan en paralelo, y el tiempo de espera entre acciones (*think time*) imita el ritmo humano. Pero el número de usuarios no mide bien la carga: falta saber qué hace cada uno y con qué intensidad (ISTQB, 2018) <!-- E4, E5, E6, E7 -->.

<!-- B2. Percentiles frente al promedio -->

La forma de resumir los tiempos de respuesta cambia lo que se ve en ellos. El promedio suele sesgarse por valores atípicos, y por eso el CT-PT propone el percentil 90 como objetivo habitual: representa a la mayoría de los usuarios que alcanzan un umbral de rendimiento dado (ISTQB, 2018) <!-- E8 -->. El mismo razonamiento lleva a percentiles más altos cuando importa la cola de la distribución. El percentil 95 (p95) y el percentil 99 (p99) muestran la cola de los tiempos de respuesta, que el promedio diluye: un sistema puede tener un promedio aceptable mientras una de cada veinte solicitudes tarda varias veces más.

<!-- B3. Ley de Little y modelos de carga -->

Las métricas están ligadas. La ley de Little establece que el número promedio de solicitudes en un sistema es igual a su *throughput* por el tiempo promedio que cada una pasa en él, N = XR. Para todos los usuarios, con el *think time* Z sumado al tiempo de respuesta, toma la forma N = X(R + Z) (Lazowska et al., 1984) <!-- E9, E10 -->. La fórmula del CT-PT para el *throughput* tiene esa misma forma: si el procesamiento se alarga, el *throughput* puede caer aunque nada más cambie (ISTQB, 2018) <!-- E11 -->.

También importa cómo se genera la carga. En el modelo de carga cerrado, cada usuario virtual envía una solicitud nueva solo tras recibir la respuesta anterior y su *think time*; en el abierto, las solicitudes llegan sin esperar a que terminen las anteriores (Figura 3). Ambos dan resultados significativamente distintos aun con la misma carga, y la mayoría de los generadores de carga web revisados asumía el cerrado (Schroeder et al., 2006) <!-- E12, E13, E14 -->. Los montajes de prueba típicos usan un modelo de carga cerrado, aunque muchos sistemas públicos se comportan como uno abierto (ISTQB, 2018) <!-- E15 -->.

<!-- B4. Coordinated omission -->

El modelo cerrado tiene, además, un efecto menos visible: puede omitir justo las mediciones que importan. Un generador que envía cada solicitud de forma síncrona y espera la respuesta antes de enviar la siguiente deja de enviar mientras el sistema está detenido. Las solicitudes que debieron salir durante esa pausa nunca se miden, y los resultados no reflejan bien las detenciones; el efecto empeora si solo se informa el tiempo de respuesta promedio. Ese problema se conoce como *coordinated omission*, y se evita implementando un modelo abierto, con solicitudes enviadas de forma asíncrona (Friedrich et al., 2017) <!-- E16, E17, E18 -->. Por eso, qué modelo de carga admite cada herramienta es uno de los criterios con que se comparan en 5.8.

<!-- FIGURA: Figura 3. Modelos de carga cerrado y abierto. Dos esquemas lado a lado. A la izquierda, el modelo cerrado: un número fijo N de usuarios virtuales, cada uno en ciclo (enviar → cola → servidor → recibir → think time → enviar); cada usuario envía su siguiente solicitud solo después de recibir la respuesta anterior y completar su think time. A la derecha, el modelo abierto: llegadas nuevas a una tasa dada, independientes de las respuestas, que entran a la cola del servidor y salen del sistema al completarse. Adaptado de Schroeder et al. (2006), figura 1 (a) y (b); se omite el modelo parcialmente abierto (c). -->

**Figura 3.** Modelos de carga cerrado y abierto.

*Fuente:* adaptado de Schroeder et al. (2006) <!-- E12 -->.

## 5.4 Clasificación de las pruebas de rendimiento

<!-- B5. Tipos principales -->

Los tipos de prueba de rendimiento no se distinguen por la herramienta, sino por la pregunta que responden, y esa pregunta fija el perfil de carga, es decir, la forma de la carga en el tiempo, y la duración. Un mismo escenario puede responder preguntas distintas, y la pregunta determina qué comportamiento hay que observar y, por tanto, cómo se diseña la prueba. La prueba de resistencia (*soak* o *endurance*), por ejemplo, busca problemas que se acumulan con el tiempo, como las fugas de memoria (ISTQB, 2018) <!-- E20 -->. Una duración insuficiente puede ocultarlos; del mismo modo, para explorar los límites, una prueba de estrés tiene que acercarse a ellos, con más carga o con menos recursos. La Tabla 2 compara los cuatro tipos principales.

Esa clasificación es menos estable de lo que parece. Jiang y Hassan (2015) <!-- E21 --> encontraron muchas interpretaciones distintas de la prueba de carga, tanto en la investigación como en la práctica industrial, y observaron que el término suele usarse como sinónimo de prueba de rendimiento y de prueba de estrés. Por eso este documento adopta las definiciones del CT-PT y las mantiene en todas sus secciones. Al leer otra fuente, el perfil de carga dice más que el nombre de la prueba.

**Tabla 2.** Comparación de los tipos de prueba de rendimiento

| Tipo | Objetivo | Perfil de carga | Duración | Qué detecta |
|---|---|---|---|---|
| Carga | Comprobar que el sistema soporta niveles crecientes de la carga realista prevista, generada por un número controlado de usuarios o procesos concurrentes <!-- E19 --> | Rampa de subida (*ramp-up*) hasta la carga prevista y meseta en estado estable (*steady state*) <!-- E22, E27 --> | La necesaria para observar el estado estable después de la rampa de subida <!-- E27 --> | Respuesta que se degrada con cargas moderadas o altas, aun dentro de los rangos esperados, por saturación de recursos <!-- E24 --> |
| Estrés | Evaluar el sistema con cargas en el límite de lo previsto o por encima, o con menos recursos disponibles <!-- E19 --> | Escalones o rampa hasta alcanzar o superar el máximo esperado <!-- E22, E23 --> | Lo bastante para observar el comportamiento en el límite y más allá | Manejo de errores deficiente bajo carga alta o superior al límite: *pools* de recursos insuficientes, colas pequeñas, tiempos de espera demasiado cortos <!-- E25 --> |
| Picos (*spike*) | Comprobar que el sistema responde bien a ráfagas súbitas de carga máxima y vuelve después a un estado estable <!-- E19 --> | Ráfagas súbitas sobre una carga de base, con cambios instantáneos de carga <!-- E19, E22 --> | Ráfagas breves, seguidas del tiempo necesario para comprobar la vuelta al estado estable | Caídas o falta de respuesta ante un número grande y repentino de solicitudes, como en la venta de entradas para un gran evento <!-- E26 --> |
| Resistencia | Comprobar la estabilidad del sistema a lo largo del tiempo <!-- E20 --> | Meseta prolongada con carga constante | Un período propio del contexto operacional del sistema <!-- E20 --> | Respuesta que se degrada con el tiempo por problemas de capacidad de los recursos, como fugas de memoria o agotamiento de conexiones y de *pools* de hilos <!-- E20 --> |

*Fuente:* elaboración propia a partir de ISTQB (2018) <!-- E19, E20, E22, E23, E24, E25, E26, E27 -->. Las columnas «Objetivo» y «Qué detecta» resumen las definiciones y los modos de falla del CT-PT; la asignación de cada modo de falla a un tipo es propia. Las columnas «Perfil de carga» y «Duración» son una síntesis propia a partir de los perfiles que describe el CT-PT, que no fija duraciones en horas.

<!-- B6. Variantes -->

Otras pruebas miden límites más que el comportamiento bajo una carga dada. La de escalabilidad determina si el sistema puede crecer, con más usuarios o más datos almacenados, sin violar los requisitos de rendimiento vigentes. La de capacidad determina cuántos usuarios o transacciones soporta sin dejar de cumplir sus objetivos de rendimiento, que pueden expresarse también en volúmenes de datos. El CT-PT no define una prueba de volumen aparte (ISTQB, 2018) <!-- E28, E29, E30 -->, de modo que aquí el volumen se trata como la dimensión de datos de la capacidad. En una API, esa dimensión importa: una consulta que responde bien con mil registros puede no hacerlo con un millón.
