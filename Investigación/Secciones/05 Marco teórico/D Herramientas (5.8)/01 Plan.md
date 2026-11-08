# Plan — Marco teórico, grupo D: Herramientas (5.8)

**Estado:** Aprobado | **Modo:** Completo | **Versión:** 2 | **Fecha:** 2026-11-07 | **Presupuesto:** 400 palabras + 0,85 págs. de tabla (2 págs. en total)

> **Cambios en la versión 2:** aprobado por el usuario sin cambios. Las nueve fuentes se agregan a `Referencias.md`. Para APA 7, F2 pasa a «Apache Software Foundation» y las dos entradas de Perforce sin fecha se distinguen como «s. f.-a» (documentación) y «s. f.-b» (precios). No hay términos nuevos para el glosario.

## Objetivo y alcance

Subsección 5.8 del Marco teórico (`Alcance.md` §5.4 y §6; `Enunciado.md` §5, «catálogo y comparativa de herramientas comerciales y de código abierto disponibles en el mercado»). Responde a PI-4: cómo se comparan las herramientas según criterios técnicos definidos. Informa el costo de adopción de la pregunta-problema y justifica la elección de Gatling para el taller.

**Incluye:**

- Las seis herramientas fijadas en `Alcance.md` §6: Gatling (Community Edition), Apache JMeter, Grafana k6 y Locust, de código abierto, y OpenText Professional Performance Engineering (antes LoadRunner Professional) y BlazeMeter, comerciales. El usuario eligió BlazeMeter como plataforma SaaS el 2026-11-07.
- Los ocho criterios fijos de `Alcance.md` §6, sin agregar otros.
- Gatling Enterprise solo como contraste, dentro del mismo proveedor.
- Cada afirmación sobre una herramienta se verifica contra su documentación oficial vigente, con la versión consultada y la fecha de acceso.

**No incluye (lo cubren otras secciones o grupos):**

- Los modelos de carga, *coordinated omission*, los umbrales y los criterios de aceptación, ya definidos en los grupos B y C (5.3 y 5.7). Aquí se usan como criterios y se remite a ellos.
- El uso de Gatling en el taller (lenguaje del DSL, herramienta de build, plataforma de CI), que se define en la Fase 2.
- Otras herramientas, como Artillery, Vegeta o NeoLoad, y otros criterios.
- Las pruebas de frontend y de navegador, excluidas por el alcance (`Alcance.md` §4). Los protocolos de navegador de algunas herramientas no se comparan.

**Forma:** una subsección con subtítulo (5.8), con bloques sin subtítulo y la Tabla 3.

## Esquema argumental
| Bloque | Palabras | Idea central | Contenido | Insumos y fuentes |
|---|---|---|---|---|
| B1. Criterios de comparación | 110 | Las herramientas miden lo mismo; lo que las distingue, y lo que decide su costo de adopción, es cómo generan la carga, cómo se integran en un pipeline y cuánto cuestan. | Por qué estos ocho criterios: el modelo de carga y la arquitectura del generador vienen de 5.3 (*coordinated omission*); la integración con CI y los criterios de aprobación, de 5.7; el resto describe el costo de adopción. Remite a la Tabla 3. Sin fuentes externas: es contenido interno y razonamiento propio. | `Alcance.md` §6; grupos B y C |
| B2. Diferencias que importan | 170 | Las herramientas se separan en tres ejes: el modelo de carga que soportan, la arquitectura de su generador y si traen un criterio de aprobación que falle el pipeline sin piezas adicionales. | Modelo de carga: Gatling y k6 ofrecen abierto y cerrado; JMeter es cerrado por defecto, con un grupo de hilos de modelo abierto experimental; Locust y LoadRunner parten de usuarios virtuales en ciclo. Arquitectura: hilos por usuario (JMeter, LoadRunner como opción), mensajes o eventos (Gatling, Locust), un motor en Go (k6). CI: aserciones o umbrales que cambian el código de salida (Gatling, k6, Locust), frente a bibliotecas de terceros (JMeter) o un complemento con SLA (LoadRunner). BlazeMeter hereda estas propiedades del motor que ejecuta. | F1, F2, F3, F4, F5, F6 |
| B3. Licencia, costo y elección | 120 | El código abierto elimina el costo de licencia, pero no el de escalar: las versiones comerciales y SaaS cobran por generar carga a gran escala; para un taller con un entorno propio, Gatling Community cubre los criterios que la pregunta-problema exige. | Licencias abiertas (Apache 2.0, AGPL-3.0, MIT) frente a licencias comerciales con cuota gratuita limitada (LoadRunner Community, BlazeMeter Free Starter). Gatling Enterprise como contraste: mismo motor, con generación distribuida y de pago. La elección de Gatling, como razonamiento propio a partir de la tabla: modelo abierto, generador no basado en hilos, aserciones que fallan la ejecución y licencia abierta. Sus límites: algunos protocolos con licencia de componente propia y la generación distribuida reservada a Enterprise. | F1, F7, F3, F8, F5, F6, F9 |
| **Total** | **400** | | | |

**Presupuesto:** `Alcance.md` asigna 2 páginas a 5.8: 400 palabras y la tabla comparativa de 6 herramientas × 8 criterios. Con unas 350 palabras por página, la prosa ocupa unas 1,15 páginas, y la tabla, unas 0,85. Una tabla de 48 celdas solo cabe si las celdas son breves (unas 8 palabras) y la tabla va transpuesta, con los criterios en filas y las herramientas en columnas. Si al redactarla no cabe, puede tomar hasta media página del margen de 2 páginas de `Alcance.md` §5; si eso no alcanza, la alternativa es dividirla en dos tablas de cuatro criterios.

> **Notas para el redactor:**
>
> - **Versiones y fechas:** cada herramienta se cita con la versión verificada (ver «Verificación») y la fecha de acceso 2026-11-07. Si al redactar hay una versión más nueva, se actualiza la versión, se vuelve a verificar la celda afectada y se registra en la evidencia.
> - **Curva de aprendizaje:** ninguna documentación oficial la mide. La fila de la tabla es una síntesis propia, explícita en la nota de la tabla, a partir del lenguaje de scripting (criterio 1) y de si la herramienta exige una interfaz gráfica o un componente propietario. No se atribuye a ninguna fuente ni se presenta como medición.
> - **BlazeMeter:** ejecuta pruebas de otras herramientas mediante Taurus. En los criterios 2, 3 y 6 la celda dice que depende del motor ejecutado, sin repetir las otras columnas.
> - **Locust:** su modelo es cerrado (usuarios que esperan entre tareas). `constant_throughput` y `poisson` limitan o aleatorizan la tasa por usuario, pero no lo vuelven abierto: la documentación dice «at most». La celda lo dice así.
> - **LoadRunner:** el producto se llama ahora OpenText Professional Performance Engineering. El texto lo nombra así una vez, con «antes LoadRunner Professional», y después «LoadRunner», como `Alcance.md`. Sus escenarios orientados a objetivos fijan metas de tasa (por ejemplo, transacciones por segundo), pero se ejecutan con Vusers; la celda no lo presenta como modelo abierto.
> - **JMeter y CI:** la documentación oficial dice que la integración continua se logra con bibliotecas de terceros para Maven, Gradle y Jenkins. La celda no atribuye a JMeter un criterio de aprobación global integrado.
> - **Gatling, protocolos:** gRPC, MQTT y GraphQL se distribuyen con la Gatling Enterprise Component License, aunque se pueden usar con la Community Edition. La celda lo indica.
> - **Precios:** cambian con frecuencia. Se dan como «desde» y con la fecha de acceso; no se convierten de moneda.
> - **Enlace con el grupo B:** el modelo de carga es el criterio que conecta con *coordinated omission* (5.3); el texto lo dice en una frase, sin volver a explicarlo.

## Tablas y figuras
| ID | Tipo | Título | Bloque | Contenido | Fuentes | Espacio (págs.) |
|---|---|---|---|---|---|---|
| Tabla 3 | Tabla | Comparación de herramientas de pruebas de rendimiento | B1, B2, B3 | Ocho filas, una por criterio de `Alcance.md` §6, y seis columnas, una por herramienta, con su versión en el encabezado. Celdas breves, cada una con su fila de evidencia. La fila «Curva de aprendizaje» es una síntesis propia. Nota bajo la tabla con las fuentes, la fecha de acceso y la aclaración sobre la síntesis propia. | F1–F9 | 0,85 |

## Afirmaciones a respaldar
| ID | Pregunta | Bloque | Fuentes |
|---|---|---|---|
| A1 | ¿Qué modelos de carga (abierto, cerrado o ambos) soporta cada herramienta, según su documentación oficial? | B2, Tabla 3 | F1, F2, F3, F4, F5, F6 |
| A2 | ¿Cómo genera la carga cada herramienta: hilos, procesos, mensajes, eventos o un motor propio? | B2, Tabla 3 | F1, F2, F3, F4, F5, F6 |
| A3 | ¿Qué mecanismo ofrece cada herramienta para que una prueba falle en CI (aserciones, umbrales, código de salida, SLA o criterios de fallo) y cómo se integra con un pipeline? | B2, Tabla 3 | F1, F2, F3, F4, F5, F6 |
| A4 | ¿Qué licencia y qué costo tiene cada herramienta, y qué agregan Gatling Enterprise y los planes de pago de Grafana Cloud k6 y BlazeMeter? | B3, Tabla 3 | F1, F2, F3, F4, F5, F6, F7, F8, F9 |

Los demás datos de la tabla (lenguaje, protocolos, informes) no son afirmaciones del texto, pero cada celda lleva su fila de evidencia (guía, §7).

## Fuentes
| ID | Referencia y enlace | Acceso | Disponibilidad |
|---|---|---|---|
| F1 | Gatling Corp. (2026). *Gatling* (Versión 3.16.0) [Software]. https://docs.gatling.io/ | Abierta | https://docs.gatling.io/ |
| F2 | Apache Software Foundation. (2024). *Apache JMeter* (Versión 5.6.3) [Software]. https://jmeter.apache.org/ | Abierta | https://jmeter.apache.org/usermanual/index.html |
| F3 | Grafana Labs. (2026). *Grafana k6* (Versión 2.3.0) [Software]. https://grafana.com/docs/k6/latest/ | Abierta | https://grafana.com/docs/k6/latest/ |
| F4 | Locust. (2026). *Locust* (Versión 2.47.0) [Software]. https://docs.locust.io/en/stable/ | Abierta | https://docs.locust.io/en/stable/ |
| F5 | OpenText. (2026). *OpenText Professional Performance Engineering* (Versión 26.3) [Software]. https://admhelp.microfocus.com/lr/en/latest/help/WebHelp/Content/WelcomeContent/c_Welcome.htm | Abierta (documentación pública; el software es comercial) | https://admhelp.microfocus.com/lr/en/latest/ y https://admhelp.microfocus.com/vugen/en/26.1-26.3/ |
| F6 | Perforce Software. (s. f.-a). *BlazeMeter documentation*. Recuperado el 7 de noviembre de 2026, de https://help.blazemeter.com/ | Abierta (documentación pública; el servicio es comercial) | https://help.blazemeter.com/docs/guide/intro.html |
| F7 | Gatling Corp. (s. f.). *Gatling pricing*. Recuperado el 7 de noviembre de 2026, de https://gatling.io/pricing | Abierta | https://gatling.io/pricing |
| F8 | Grafana Labs. (s. f.). *Pricing*. Recuperado el 7 de noviembre de 2026, de https://grafana.com/pricing/ | Abierta | https://grafana.com/pricing/ |
| F9 | Perforce Software. (s. f.-b). *BlazeMeter pricing*. Recuperado el 7 de noviembre de 2026, de https://www.blazemeter.com/pricing | Abierta | https://www.blazemeter.com/pricing |

**Verificación (2026-11-07):** fecha de acceso de todas las páginas.

- **Versiones y licencias de las cuatro herramientas abiertas:** última versión publicada y licencia, tomadas de la API de GitHub de cada repositorio oficial. Gatling v3.16.0 (29 de septiembre de 2026, Apache-2.0); JMeter 5.6.3 (9 de enero de 2024, Apache-2.0), que coincide con la página de descarga oficial, «Apache JMeter 5.6.3 (Requires Java 8+)»; k6 v2.3.0 (21 de septiembre de 2026, AGPL-3.0); Locust 2.47.0 (21 de octubre de 2026, MIT), que coincide con el título de su documentación.
- **F1 (Gatling):**
  - Lenguajes: guías para el SDK de Java y el de JavaScript/TypeScript en la página de inicio, y ejemplos en Java, JavaScript, Kotlin y Scala en «Injection».
  - Modelos de carga: `injectOpen` e `injectClosed` («Injection», apartados «Open model» y «Closed model»); el glosario define el perfil de inyección como tasa de usuarios iniciados (abierto) o número de usuarios concurrentes (cerrado).
  - Arquitectura: el glosario, en «Virtual User», dice que otras herramientas implementan los usuarios virtuales como hilos y que Gatling los implementa como mensajes.
  - Protocolos: HTTP, WebSocket, SSE, JMS, MQTT, gRPC y GraphQL en la referencia de scripts; gRPC, MQTT y GraphQL con la Gatling Enterprise Component License, utilizables también con la Community Edition (por ejemplo, «gRPC / Setup», apartado «License and limitations»).
  - CI: «Assertions» dice que, si al menos una aserción falla, la simulación falla, y que los resultados se exportan en formato compatible con JUnit; complementos para Maven, Gradle y sbt, y guías para Jenkins, GitHub Actions, GitLab CI y otros.
  - Informes: «Static HTML reports», con mínimos, máximos, promedio, desviación estándar y percentiles.
- **F2 (JMeter):** la página de inicio enumera los protocolos (HTTP/HTTPS, SOAP/REST, FTP, JDBC, LDAP, JMS, correo, TCP, objetos Java), el modo CLI, el informe HTML dinámico, el *framework* multihilo y la integración continua «through 3rd party Open Source libraries for Maven, Gradle and Jenkins». «Elements of a Test Plan»: cada hilo ejecuta el plan de prueba completo y de forma independiente, y varios hilos simulan conexiones concurrentes. «Component Reference», apartado «Open Model Thread Group»: experimental, genera usuarios según un programa de tasas. «Generating Dashboard Report»: APDEX y tres percentiles configurables. Scripting: plan de prueba en la interfaz gráfica, con *samplers* en lenguajes JSR223 como Groovy (página de inicio).
- **F3 (k6):** «Open and closed models»: algunos *executors* usan el modelo cerrado y los de *arrival rate*, el abierto. «Thresholds»: son los criterios de aprobación; si no se cumplen, k6 termina con un código de salida distinto de cero, y la página dice que se usan para codificar SLO. «Protocols»: HTTP/1.1, HTTP/2, WebSockets y gRPC, y otros mediante extensiones xk6. «Running large tests»: k6 es «heavily multi-threaded», su máquina virtual de JavaScript corre sobre Go y un script simple usa entre 1 y 5 MB por usuario virtual. TypeScript habilitado por defecto desde v0.57 («JavaScript and TypeScript compatibility mode»). «Web dashboard»: panel en tiempo real integrado.
- **F4 (Locust):** «What is Locust»: pruebas en Python normal; cada usuario en su propio *greenlet*; basado en eventos con gevent, de modo que un proceso maneja miles de usuarios concurrentes. «Writing a locustfile»: `wait_time` después de cada tarea; `constant_throughput` («at most X times per second»), `constant_pacing` y `poisson`. «Testing other systems/protocols»: solo HTTP/HTTPS de fábrica; otros protocolos envolviendo sus bibliotecas. «Running without the web UI»: código de salida 1 si hubo fallos, y `process_exit_code` para criterios propios. «Configuration»: `--headless`, `--csv`, `--html`, `--exit-code-on-error`.
- **F5 (LoadRunner):** «What's new» identifica la versión 26.3 de OpenText Professional Performance Engineering. «Get started»: componentes VuGen, Controller y Analysis. «Design load test scenarios»: escenarios manuales u orientados a objetivos, con metas como Vusers simultáneos, páginas por minuto, *hits* por segundo o transacciones por segundo. VuGen, «Editor pane»: scripts grabados en C, y manuales en Java, JavaScript, C# y VB.NET. VuGen, «Vuser types»: protocolos como .NET, Citrix, DevWeb (HTTP y WebSocket), Java, Kafka, MQTT, LLM y TruClient, y licencias por protocolo. VuGen, «Run a Vuser as a process or thread»: con hilos, un proceso conductor por cada 50 Vusers, por defecto; con procesos, uno por Vuser, con mayor consumo de memoria. Controller, «Continuous integration with Jenkins»: complemento Application Automation Tools, y solo se integran escenarios con SLA, para decidir si la prueba pasó o falló; hay páginas equivalentes para Azure DevOps y TeamCity. «About licenses»: la licencia Community es gratuita y permite 50 Vusers en todos los protocolos, incluidos Gatling y JMeter, salvo los paquetes COM/DCOM, Templates y GUI.
- **F6 (BlazeMeter):** «Taurus testing»: Taurus define y ejecuta pruebas con YAML o JSON usando *executors* como JMeter, Gatling, Locust, Selenium, Playwright y k6. «Create Performance tests (k6)»: los motores de BlazeMeter corren sobre Taurus. «Add BlazeMeter testing to your CI/CD pipeline»: un paso del CI ejecuta la CLI de Taurus, que sube los scripts y lanza la prueba; hay complementos para Jenkins, Bamboo y TeamCity, y funciones para GitHub Actions. «Failure criteria»: criterios de aprobación o fallo sobre tiempos de respuesta, errores, *hits* por segundo y otros, también relativos a una línea base. «Introduction to Performance test reporting»: informes en la aplicación web, con comparación de informes y de línea base.
- **F7 (Gatling Enterprise):** planes Basic desde 89 € al mes con facturación anual (99 € mensual) y Team desde 356 € al mes; Enterprise a pedido. Los planes de pago incluyen generadores de carga gestionados, y la prueba distribuida aparece desde Team.
- **F8 (Grafana Cloud k6):** en el plan gratuito, hasta 500 horas de usuario virtual al mes; después, 0,15 USD por hora de usuario virtual.
- **F9 (BlazeMeter):** Free Starter con hasta 50 usuarios virtuales y un generador compartido; Basic, 149 USD al mes o 1 188 USD al año, con 1 000 usuarios concurrentes; Pro, 649 USD al mes o 5 988 USD al año, con 5 000; Unleashed, a pedido.
- **Descartadas:**
  - Blogs y tutoriales de terceros sobre LoadRunner (softwaretestinghelp, blogspot, Guru99, consultoras): no son documentación oficial; se usaron solo para encontrar las páginas oficiales.
  - Páginas comparativas de proveedores (blog de BlazeMeter, blog de Gatling «BlazeMeter alternative», StackShare): contenido comercial o de terceros, sin datos verificables (`Alcance.md` §5.3).
  - PeerSpot (opiniones de usuarios sobre precios de LoadRunner): no es fuente oficial, y el precio de las licencias de pago no es público; la celda dice «comercial, a cotización», con la licencia Community.
  - Wikipedia (LoadRunner): fuente secundaria.

## Registro de búsqueda
| # | Fecha | Buscador o base | Cadena | Resultados revisados | Elegidas / descartadas (motivo) |
|---|---|---|---|---|---|
| 1 | 2026-11-07 | Buscador web | `OpenText LoadRunner Professional documentation admhelp latest release Vuser protocols scripting languages C JavaScript` | 7: «What's new» del centro de ayuda (versiones latest, 25.1, 24.1-24.3 y 2021), *readmes* de 24.1 y 2023.1 y Wikipedia | Elegida: el centro de ayuda «latest» (F5), que resultó ser la versión 26.3. Descartada: Wikipedia (secundaria). |
| 2 | 2026-11-07 | Buscador web | `admhelp.microfocus.com vugen "script language" C JavaScript Vuser script languages supported` | 7: «Editor pane» (26.1 y 26.1-26.3), «C Vuser scripts» (2021 R2), «Protocol-specific Vuser functions» y «Record scripts» | Elegida: «Editor pane» 26.1-26.3 (F5), versión vigente. Descartadas: versiones anteriores. |
| 3 | 2026-11-07 | Buscador web | `admhelp.microfocus.com lr latest "Run Vuser as a process" thread multithreading Controller runtime settings` | 7: blogs y tutoriales de terceros (softwaretestinghelp, blogspot, Alibaba Cloud) | Ninguna elegida: sin documentación oficial. |
| 4 | 2026-11-07 | Buscador web | `site:admhelp.microfocus.com vugen runtime settings miscellaneous multithreading "Run Vuser as a thread"` | 7: «Run a Vuser as a process or thread» (26.1, 26.1-26.3 y 12.62) y «Configure runtime settings» (varias versiones) | Elegida: «Run a Vuser as a process or thread» 26.1-26.3 (F5). |
| 5 | 2026-11-07 | Buscador web | `site:admhelp.microfocus.com lr latest Jenkins plugin CI/CD integration Professional Performance Engineering SLA pass fail` | 7: páginas de Jenkins de LoadRunner Enterprise y de Performance Center, e integración con CI de DevWeb | Ninguna elegida: son de otros productos de la familia (Enterprise, DevWeb), no de LoadRunner Professional. |
| 6 | 2026-11-07 | Buscador web | `site:admhelp.microfocus.com/lr "Application Automation Tools" Jenkins Professional Performance Engineering scenario SLA` | 7: «Continuous integration with Jenkins» de Professional (26.1 y 26.1-26.3), páginas de Enterprise y de Service Virtualization | Elegida: «Continuous integration with Jenkins» 26.1-26.3 (F5). Descartadas: otros productos. |
| 7 | 2026-11-07 | Buscador web | `OpenText Professional Performance Engineering LoadRunner Professional Community Edition free virtual users license pricing` | 18: «About licenses» de LoadRunner (24.1 y 2021.2), folleto de paquetes de licencias, página de producto de OpenText, PeerSpot, Guru99, consultoras y blogs | Elegida: «About licenses», verificada en la versión 26.1-26.3 (F5). Descartados: PeerSpot, Guru99, consultoras y blogs (no oficiales o desactualizados). |
| 8 | 2026-11-07 | Buscador web | `help.blazemeter.com supported open source tools JMeter Gatling Locust k6 Taurus performance test failure criteria` | 7: blog y páginas comerciales de BlazeMeter, blog de Gatling | Ninguna elegida: contenido comercial. Las páginas oficiales se ubicaron en el índice del centro de ayuda de BlazeMeter (ver «Verificación»). |
| 9 | 2026-11-07 | Buscador web | `help.blazemeter.com "supported" "Gatling" "Locust" "k6" performance testing scripts create test` | 7: Medium, página comparativa de BlazeMeter y comparaciones de StackShare | Ninguna elegida: terceros o comerciales. |
