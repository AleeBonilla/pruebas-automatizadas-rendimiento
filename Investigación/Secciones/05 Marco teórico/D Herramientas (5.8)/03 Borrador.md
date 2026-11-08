# Marco teórico — 5.8

<!-- Borrador v3 | Plan v2 | Evidencia v2 | 2026-11-07 -->
<!-- v3: corrige el hallazgo bloqueante 1 y aplica las sugerencias 2 y 3 de la auditoría, ronda 2. v2: corrige los hallazgos bloqueantes 1–5 y aplica las sugerencias 6–10 de la auditoría, ronda 1. -->

## 5.8 Catálogo y comparativa de herramientas

<!-- B1. Criterios de comparación -->

Las seis herramientas comparadas miden, en lo esencial, lo mismo: tiempos de respuesta, *throughput* y errores. Lo que las distingue, y lo que define su costo de adopción, es cómo generan la carga, cómo entran en un pipeline y cuánto cuesta usarlas a escala. Por eso la Tabla 3 las compara con ocho criterios que salen de las secciones anteriores. El modelo de carga se relaciona con *coordinated omission* (5.3), y la arquitectura del generador, con el riesgo de que este limite la carga; la integración con CI y el criterio de aceptación importan porque una prueba solo funciona como *quality gate* si puede hacer fallar el pipeline (5.7). Los demás criterios describen el resto del costo de adopción.

**Tabla 3.** Comparación de herramientas de pruebas de rendimiento

| Criterio | Gatling 3.16.0 | JMeter 5.6.3 | k6 2.3.0 | Locust 2.47.0 | LoadRunner 26.3 | BlazeMeter (SaaS) |
|---|---|---|---|---|---|---|
| Lenguaje o forma de *scripting* | SDK en Java, Kotlin, Scala y JavaScript/TypeScript <!-- E1 --> | Plan de prueba en interfaz gráfica; *samplers* en Groovy u otros lenguajes JSR223 <!-- E10 --> | JavaScript y TypeScript <!-- E17 --> | Python <!-- E25 --> | C al grabar; también Java, JavaScript, C# y VB.NET <!-- E32 --> | YAML o JSON (Taurus), con *scripts* de las herramientas que ejecuta <!-- E39 --> |
| Modelo de carga | Abierto y cerrado <!-- E2 --> | Cerrado; abierto con un grupo de hilos experimental <!-- E11 --> | Abierto y cerrado, según el *executor* <!-- E18 --> | Cerrado; puede limitar la tasa por usuario <!-- E26 --> | Usuarios virtuales (Vusers); escenarios manuales o por objetivos <!-- E33 --> | Depende del motor y de la configuración de BlazeMeter <!-- E40 --> |
| Protocolos | HTTP, WebSocket, SSE, JMS, MQTT, gRPC y GraphQL¹ <!-- E3, E4 --> | HTTP(S), SOAP/REST, FTP, JDBC, LDAP, JMS, correo y TCP <!-- E12 --> | HTTP/1.1, HTTP/2, WebSockets y gRPC; otros con extensiones <!-- E19 --> | HTTP(S); otros envolviendo sus bibliotecas <!-- E27 --> | Decenas, con licencia por protocolo <!-- E34 --> | Los del motor que ejecuta <!-- E40 --> |
| Integración con CI/CD y criterio de aceptación | Aserciones que hacen fallar la simulación; complementos de *build* y exportación JUnit <!-- E5 --> | Modo CLI; CI mediante bibliotecas de terceros <!-- E13 --> | Umbrales; código de salida distinto de cero si fallan <!-- E20 --> | Modo sin interfaz; código de salida ante fallos o criterio propio <!-- E28 --> | Complemento para Jenkins, solo con escenarios con acuerdos de nivel de servicio (SLA) <!-- E35 --> | Criterios de fallo; CLI de Taurus en el pipeline <!-- E41, E42 --> |
| Informes y análisis | Informe HTML estático con percentiles <!-- E6 --> | Informe HTML con APDEX y percentiles <!-- E14 --> | Panel web integrado, en tiempo real <!-- E21 --> | Interfaz web en tiempo real; CSV e informe HTML <!-- E29 --> | Componente Analysis <!-- E36 --> | Informes web; comparación con línea base <!-- E42, E43 --> |
| Eficiencia del generador | Usuarios virtuales como mensajes, no como hilos <!-- E7 --> | Un hilo por usuario virtual <!-- E15 --> | Motor multihilo en Go <!-- E22 --> | Un *greenlet* por usuario (gevent) <!-- E30 --> | Procesos o hilos, según el protocolo <!-- E37 --> | Depende del motor <!-- E40 --> |
| Curva de aprendizaje² | Media: DSL propio sobre un lenguaje general | Baja con la interfaz gráfica; mayor al programar en Groovy | Baja si se conoce JavaScript | Baja si se conoce Python | Alta: tres componentes propietarios y *scripts* en C | Baja si ya se conoce la herramienta que ejecuta |
| Licencia y costo | Apache 2.0, gratuita; Enterprise desde 89 €/mes (anual) <!-- E8, E9 --> | Apache 2.0, gratuita <!-- E16 --> | AGPL-3.0, gratuita; nube: Free, o Pro a 19 USD/mes y exceso desde 0,15 USD/h³ <!-- E23, E24 --> | MIT, gratuita <!-- E31 --> | Comercial; Community gratuita hasta 50 Vusers <!-- E38 --> | Comercial; gratis hasta 50 usuarios virtuales; Basic, 149 USD/mes <!-- E44 --> |

*Fuente:* elaboración propia a partir de la documentación oficial, consultada el 7 de noviembre de 2026: Gatling Corp. (2026, s. f.), Apache Software Foundation (2024), Grafana Labs (2026, s. f.), Locust (2026), OpenText (2026) y Perforce Software (s. f.-a, s. f.-b) <!-- E1–E44 -->. LoadRunner: OpenText Professional Performance Engineering (antes LoadRunner Professional). ¹ Licencia de componente propia; en la Community Edition, hasta 5 usuarios y 5 minutos por prueba. ² Valoración propia según lenguaje e interfaz; no medida. ³ h = hora de usuario virtual; Free y Pro incluyen 500 h/mes.

<!-- B2. Diferencias que importan -->

Las diferencias de fondo están en tres ejes. El primero es el modelo de carga: Gatling y k6 ofrecen de forma estable ambos modelos; en JMeter el abierto es experimental; Locust genera la carga con usuarios que esperan entre tareas, y LoadRunner, con usuarios virtuales en escenarios manuales o por objetivos. Ante una API con llegadas independientes de las respuestas, un generador cerrado puede subestimar los peores tiempos (5.3).

El segundo eje es la arquitectura del generador. JMeter dedica un hilo a cada usuario virtual, y LoadRunner ejecuta sus usuarios virtuales como procesos o como hilos, según el protocolo. Gatling, en cambio, los implementa como mensajes, lo que según su documentación escala mucho mejor (Gatling Corp., 2026) <!-- E7 -->; Locust usa corrutinas, y k6, un motor multihilo propio. El tercero es el criterio de aceptación. Gatling, k6 y Locust pueden terminar con un código de salida que hace fallar el pipeline sin piezas adicionales, mientras que JMeter delega la CI en bibliotecas de terceros (Apache Software Foundation, 2024) <!-- E13 --> y LoadRunner, en un complemento que solo admite escenarios con SLA (OpenText, 2026) <!-- E35 -->.

<!-- B3. Licencia, costo y elección -->

El código abierto elimina el costo de licencia, pero no el de escalar. Las cuatro herramientas abiertas son gratuitas, y las comerciales ofrecen cuotas gratuitas de unos 50 usuarios virtuales; lo que se paga es generar carga a gran escala. En Gatling Enterprise, los planes de pago agregan generadores de carga gestionados y, desde el plan Team, la prueba distribuida (Gatling Corp., s. f.) <!-- E9 -->. Un taller con un entorno propio no necesita esa escala, y Gatling Community reúne lo que la pregunta-problema exige: modelo abierto, un generador que no depende de un hilo por usuario, aserciones que hacen fallar la ejecución y licencia abierta. Sus límites, la prueba distribuida de pago y la licencia propia de algunos protocolos, no afectan a una API REST probada por HTTP.
