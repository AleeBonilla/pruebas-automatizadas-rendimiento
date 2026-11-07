# Plan — Marco teórico, grupo B: Conceptos y tipos (5.3–5.4)

**Estado:** Aprobado | **Modo:** Completo | **Versión:** 3 | **Fecha:** 2026-11-07 | **Presupuesto:** 850 palabras + 1 pág. de tabla y figura (3,5 págs. en total)

> **Cambios en la versión 3:** aprobado por el usuario sin cambios. Las fuentes nuevas (F2, F3 y F4) se agregan a `Referencias.md`, y los términos nuevos, a `Glosario.md`.
>
> **Cambios en la versión 2:** ajuste al nuevo presupuesto de `Alcance.md` (documento de 30–35 páginas): de 1 500 a 850 palabras y de 5,5 a 3,5 páginas. Se conservan las cinco fuentes. Se elimina la Figura 3: los perfiles de carga se describen en la columna «Perfil de carga» de la Tabla 2. Las afirmaciones bajan a 8 (tope de 1 por cada 100 palabras): A2 se funde con A1, A4 con A8, A7 con A6 y A10 con A9; los IDs vigentes se conservan. La ley del tiempo de respuesta y el tiempo transcurrido salen del texto y de los términos nuevos.

## Objetivo y alcance

Subsecciones 5.3 y 5.4 del Marco teórico (`Alcance.md` §5.4; `Enunciado.md` §5, «clasificación, principios y mejores prácticas del tipo de prueba elegido»). Responden a PI-1 (qué son las pruebas de rendimiento, cómo se clasifican y qué métricas las definen). Fijan el vocabulario que usan los grupos C y D y el taller.

**Incluye:**

- 5.3: tiempo de respuesta, *throughput*, tasa de error, concurrencia, usuarios virtuales y *think time*; por qué los percentiles y no el promedio; la ley de Little; los modelos de carga abierto y cerrado; *coordinated omission*. La latencia se trata como decisión de terminología (ver la nota).
- 5.4: las pruebas de carga, de estrés, de picos y de resistencia, con su tabla comparativa (objetivo, perfil de carga, duración, qué detecta), y la mención de las pruebas de escalabilidad, de volumen y de capacidad.

**No incluye (lo cubren otras secciones o grupos):**

- Las subcaracterísticas de ISO/IEC 25010, que ya están en el grupo A (5.2). 5.3 las retoma solo como lo que miden las métricas, con una remisión.
- El proceso de prueba (planificación, perfil operacional, scripts, entorno), las buenas prácticas y antipatrones, y los umbrales en CI/CD, que van en el grupo C (5.5–5.7). 5.3 define las métricas y los modelos de carga; cómo se fijan los objetivos y los umbrales va en C.
- Qué modelo de carga soporta cada herramienta, que es un criterio de la comparativa del grupo D (5.8).
- La teoría de colas formal y el modelado analítico de capacidad (`Alcance.md` §4, «Excluir»). La ley de Little se menciona en dos oraciones, sin derivaciones.
- La prueba de concurrencia del CT-PT, que el alcance no incluye.

**Forma:** dos subsecciones con subtítulo (5.3 y 5.4). Dentro de cada una, bloques sin subtítulo.

## Esquema argumental
| Bloque | Palabras | Idea central | Contenido | Insumos y fuentes |
|---|---|---|---|---|
| B1. 5.3, bloque 1: métricas básicas | 160 | Una prueba de rendimiento mide tres cosas distintas (lo que espera el usuario, lo que procesa el sistema y lo que consume), y genera la carga con usuarios virtuales que imitan el ritmo humano mediante el *think time*. | El tiempo de respuesta, el *throughput* y la utilización de recursos como preocupaciones del usuario, del negocio y del sistema. La tasa de error. Los usuarios virtuales, la concurrencia y el *think time*. La decisión sobre «latencia», en una oración (ver la nota). | F1 |
| B2. 5.3, bloque 2: percentiles frente al promedio | 110 | El promedio esconde la experiencia de los usuarios que más esperan; por eso los objetivos de tiempo de respuesta se fijan en percentiles. | El promedio, sesgado por valores atípicos. El percentil 90 como objetivo habitual. El p95 y el p99 del alcance, como extensión del mismo razonamiento (razonamiento propio). | F1 |
| B3. 5.3, bloque 3: ley de Little y modelos de carga | 170 | Carga, *throughput* y tiempo de respuesta están ligados por una ley simple, y la forma de generar la carga (modelo cerrado o abierto) cambia lo que se mide, al punto de que el mismo sistema da resultados distintos. | La ley de Little (N = XR) en dos oraciones, sin derivaciones, y su equivalente en el CT-PT. Los modelos cerrado y abierto: definiciones, resultados significativamente distintos con la misma carga y el predominio del modelo cerrado en los generadores. Remite a la Figura 2. | F2, F1, F3 |
| B4. 5.3, bloque 4: *coordinated omission* | 110 | Un generador de modelo cerrado puede omitir justo las mediciones que importan, porque deja de enviar solicitudes mientras el sistema está detenido; el resultado subestima los peores tiempos. | Cómo se produce y por qué agrava el problema del promedio (enlace con B2). Cómo se evita: enviar solicitudes de forma asíncrona, según un modelo abierto. Conexión con la comparativa de herramientas (grupo D), en una frase. | F4 |
| B5. 5.4, bloque 1: tipos principales | 200 | Los tipos de prueba no se distinguen por la herramienta, sino por la pregunta que responden, y eso se refleja en el perfil de carga y la duración; la terminología, además, no es uniforme en la literatura. | Qué pregunta responde cada tipo (carga, estrés, picos, resistencia) y un ejemplo de lo que detecta (por ejemplo, las fugas de memoria en la de resistencia). La diversidad de interpretaciones de los términos. Las definiciones, los perfiles y las duraciones van en la Tabla 2; el texto no las repite. | F1, F5 |
| B6. 5.4, bloque 2: variantes | 100 | La escalabilidad, la capacidad y el volumen son variantes que miden límites, no comportamiento bajo una carga dada. | La prueba de escalabilidad y la de capacidad, en una oración cada una. El volumen como la dimensión de datos de la capacidad: el CT-PT no define una prueba de volumen aparte (ver la nota). | F1 |
| **Total** | **850** | | | |

**Presupuesto:** `Alcance.md` asigna 3,5 páginas al grupo: 5.3, 2 páginas (550 palabras y la Figura 2), y 5.4, 1,5 páginas (300 palabras y la Tabla 2). Con unas 350 palabras por página, 850 palabras ocupan unas 2,4 páginas; la Figura 2, unas 0,4, y la Tabla 2, unas 0,6. Para entrar en ese espacio, B5 delega en la Tabla 2 las definiciones de los cuatro tipos y la prosa se queda con el argumento.

> **Notas para el redactor:**
>
> - **Latencia y tiempo de respuesta (decisión de terminología):** no se encontró una definición arbitrada ni normativa que los distinga; las fuentes técnicas usan «latency» y «response time» de maneras distintas, a veces como sinónimos (ver el registro de búsqueda). El CT-PT (F1) usa «response time» para lo que percibe el usuario y «network latency» como dato de recursos. El texto sigue esa convención, que el glosario recoge: tiempo de respuesta para lo que mide el cliente; latencia solo para la latencia de red. Cuando una fuente dice «latency» para referirse al tiempo de respuesta (F4), se traduce como tiempo de respuesta. Esta decisión se presenta como del trabajo, en una oración, sin atribuirla a una fuente.
> - **Ley de Little:** `Alcance.md` la limita a nociones básicas y excluye la teoría de colas formal. Dos oraciones: la ley y su lectura intuitiva, sin derivaciones ni redes de colas. Little (1961) es la fuente ancla del alcance, pero es cerrada; F2 enuncia la ley en un libro clásico que sus autores ofrecen en acceso abierto.
> - **Percentiles:** F1 habla del percentil 90. El alcance menciona p50, p95 y p99. El texto puede explicar que se eligen percentiles más altos cuando importa la cola de la distribución, como razonamiento propio y sin atribuir valores concretos a F1.
> - **F4, prevalencia del problema:** la frase «occurs in almost all load generators and monitoring tools» está solo en el resumen y no se usa. Del cuerpo sirven la explicación (§2) y la forma de evitarlo (§3).
> - **F4, versión:** la copia abierta es la versión de los autores previa a la publicación. Las páginas de la evidencia son las de esa copia (1–12); la referencia lleva las páginas publicadas (215–226).
> - **Volumen:** el CT-PT no tiene una prueba de volumen propia. La capacidad incluye explícitamente los volúmenes de datos (§1.1 y §1.2). El texto lo dice así, sin inventar una definición.
> - **Tabla 2:** carga lo que antes iba en la Figura 3. La columna «Perfil de carga» describe la forma de la carga en el tiempo (rampa y meseta, escalones hasta superar el límite, ráfagas súbitas, meseta prolongada). La columna «Duración» se formula en términos relativos y con su respaldo (por ejemplo, para la resistencia: «un período propio del contexto operacional del sistema»), porque el CT-PT no da duraciones en horas. Nada de cifras sin fuente.

## Tablas y figuras
| ID | Tipo | Título | Bloque | Contenido | Fuentes | Espacio (págs.) |
|---|---|---|---|---|---|---|
| Figura 2 | Diagrama | Modelos de carga cerrado y abierto | B3, B4 | Dos esquemas lado a lado. Cerrado: N usuarios virtuales en ciclo (enviar → esperar respuesta → *think time* → enviar). Abierto: llegadas a una tasa, independientes de las respuestas, con cola en el servidor. | Adaptado de F3 (figura 1) | 0,4 |
| Tabla 2 | Tabla | Comparación de los tipos de prueba de rendimiento | B5 | Cuatro filas (carga, estrés, picos, resistencia) y cuatro columnas (objetivo, perfil de carga, duración, qué detecta). | F1; elaboración propia en la síntesis de las columnas «perfil» y «duración» | 0,6 |

## Afirmaciones a respaldar
| ID | Pregunta | Bloque | Fuentes |
|---|---|---|---|
| A1 | ¿Cómo asocia el CT-PT el tiempo de respuesta, el *throughput* y la utilización de recursos a las preocupaciones del usuario, del negocio y del sistema, y qué son los usuarios virtuales y el *think time*? (incluye la antigua A2) | B1 | F1 |
| A3 | ¿Por qué el CT-PT advierte contra el promedio y qué percentil indica como objetivo habitual? | B2 | F1 |
| A5 | ¿Cómo enuncian Lazowska et al. la ley de Little, y cómo la expresa el CT-PT para el *throughput*? | B3 | F2, F1 |
| A6 | ¿Cómo definen Schroeder et al. los modelos cerrado y abierto, qué diferencia encuentran en los resultados con la misma carga y qué modelo asumen la mayoría de los generadores que revisan? (incluye la antigua A7) | B3 | F3 |
| A8 | ¿Cómo se produce *coordinated omission* en un generador de modelo cerrado, qué efecto tiene sobre el tiempo de respuesta medio y cómo se evita? (incluye la antigua A4) | B4 | F4 |
| A9 | ¿Cómo define el CT-PT las pruebas de carga, de estrés, de picos y de resistencia, qué problemas busca cada una (por ejemplo, fugas de memoria) y con qué perfiles de carga se construyen? (incluye la antigua A10) | B5, Tabla 2 | F1 |
| A11 | ¿Qué muestran Jiang y Hassan sobre la diversidad de interpretaciones de las pruebas de carga, de rendimiento y de estrés? | B5 | F5 |
| A12 | ¿Cómo define el CT-PT las pruebas de escalabilidad y de capacidad, y dónde incluye los volúmenes de datos? | B6 | F1 |

## Términos nuevos
| Término | Inglés | Forma propuesta | Define |
|---|---|---|---|
| Latencia (cambio) | latency | latencia: solo latencia de red; para lo que mide el cliente, tiempo de respuesta | 5.3 |
| Promedio | average, mean | promedio | — (evitar «media» para no mezclar) |
| Perfil de carga | load profile | perfil de carga | 5.4 |
| Rampa de subida / de bajada | ramp-up / ramp-down | rampa de subida (*ramp-up*), rampa de bajada (*ramp-down*) | 5.4 |
| Prueba de resistencia (cambio) | soak / endurance testing | prueba de resistencia (*soak* o *endurance*): el CT-PT usa *endurance* | 5.4 |

Además, al aprobarse el plan, en el glosario se marca 5.3 como sección que define el tiempo de respuesta, el *throughput*, la tasa de error, el percentil, la concurrencia, el usuario virtual, el *think time*, los modelos de carga, *coordinated omission* y la ley de Little; y 5.4, los tipos de prueba.

## Fuentes
| ID | Referencia y enlace | Acceso | Disponibilidad |
|---|---|---|---|
| F1 | International Software Testing Qualifications Board. (2018). *Certified Tester Foundation Level Specialist syllabus: Performance testing* (Versión 2018). https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf | Abierta | https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-PT_Syllabus_v1.0_2018.pdf |
| F2 | Lazowska, E. D., Zahorjan, J., Graham, G. S., & Sevcik, K. C. (1984). *Quantitative system performance: Computer system analysis using queueing network models*. Prentice-Hall. https://homes.cs.washington.edu/~lazowska/qsp/ | Abierta (los autores recuperaron los derechos y la publican) | https://homes.cs.washington.edu/~lazowska/qsp/Images/Chap_03.pdf |
| F3 | Schroeder, B., Wierman, A., & Harchol-Balter, M. (2006). Open versus closed: A cautionary tale. En *Proceedings of the 3rd Symposium on Networked Systems Design and Implementation (NSDI '06)* (pp. 239–252). USENIX Association. https://www.usenix.org/conference/nsdi-06/open-versus-closed-cautionary-tale | Abierta | https://www.usenix.org/legacy/events/nsdi06/tech/full_papers/schroeder/schroeder.pdf |
| F4 | Friedrich, S., Wingerath, W., & Ritter, N. (2017). Coordinated omission in NoSQL database benchmarking. En B. Mitschang et al. (Eds.), *Datenbanksysteme für Business, Technologie und Web (BTW 2017) – Workshopband* (Lecture Notes in Informatics, P-266, pp. 215–226). Gesellschaft für Informatik. https://dl.gi.de/items/780bef9a-d6df-4776-80e3-e85ae0158e63 | Abierta (copia de los autores) | https://vsis-www.informatik.uni-hamburg.de/getDoc.php/publications/569/Coordinated_Omission_in_NoSQL_Database_Benchmarking-Friedrich.pdf |
| F5 | Jiang, Z. M., & Hassan, A. E. (2015). A survey on load testing of large-scale software systems. *IEEE Transactions on Software Engineering, 41*(11), 1091–1118. https://doi.org/10.1109/TSE.2015.2445340 | Abierta (copia del autor) | https://www.eecs.yorku.ca/~zmjiang/publications/tse2015_jiang.pdf |

**Verificación (2026-11-07):**

- **F1:** ya estaba en `Referencias.md`. Pasajes nuevos localizados en el cuerpo:
  - Tipos de prueba (carga, estrés, escalabilidad, picos, resistencia, capacidad), incluidas las fugas de memoria en la de resistencia y los volúmenes de datos en la de capacidad: §1.2, pp. 12–13.
  - El tiempo de respuesta, el *throughput* y la utilización de recursos como preocupaciones del usuario, el negocio y el sistema: §4.1, p. 34.
  - El *think time* y el tiempo transcurrido: §4.2.2, p. 39.
  - Los usuarios virtuales y los perfiles de carga (rampas, escalones): §4.2.4, pp. 42–43.
  - El *throughput* en función de los usuarios virtuales, el tiempo de procesamiento y el *think time*, y la concurrencia modelada con usuarios virtuales: §4.2.5, p. 44.
  - Los promedios engañosos en estados transitorios: §4.3, p. 50.
  - El promedio sesgado por valores atípicos y el percentil 90 como objetivo: §4.4, p. 52.
- **F2:** la página de los autores en la Universidad de Washington confirma que el editor les devolvió los derechos y que publican el libro en PDF (Prentice-Hall, 1984). Capítulo 3, «Fundamental Laws», leído completo. La ley de Little (N = XR) está en §3.3, p. 43, y la ley del tiempo de respuesta, con su ejemplo, en p. 46. Es un clásico anterior a 2010, admitido por `Alcance.md` §5.3.
- **F3:** la página de USENIX da el título, los autores y el congreso (NSDI '06). Los pies de página del PDF dan las páginas 239–252 de las actas. Las definiciones de los modelos cerrado y abierto, los resultados distintos con la misma carga y el predominio del modelo cerrado en los generadores están en §1, pp. 239–240. Es una fuente ancla del alcance, anterior a 2010 y admitida como clásico.
- **F4:** la Biblioteca Digital de la GI registra los autores, el año, el volumen (BTW 2017 Workshopband, LNI P-266, taller SCDM 2017), las páginas (215–226), los editores, la ciudad (Bonn) y el ISBN 978-3-88579-660-2. La copia abierta es la de los autores, de la Universidad de Hamburgo. La explicación de *coordinated omission* está en §2 (pp. 2–4 de la copia), y la forma de evitarlo con solicitudes asíncronas, en §3 (p. 5). No está en Crossref.
- **F5:** ya estaba en `Referencias.md`. Tabla 1 («Interpretations of Load Testing, Performance Testing and Stress Testing») y §2, pp. 1092–1093.
- **Descartadas:**
  - Little (1961): es la fuente ancla del alcance para la ley, pero es cerrada (*Operations Research*). F2 la enuncia en acceso abierto.
  - Molyneaux, *The Art of Application Performance Testing*: es una fuente ancla del alcance, pero es un libro cerrado y no está en `Adjuntos/Local`. F1 cubre lo que este grupo necesita de ella.
  - Dean y Barroso (2013), «The Tail at Scale»: pertinente para la latencia de cola, pero solo se encontró el resumen (ver el registro de búsqueda), y F1 ya cubre los percentiles.
  - Blogs y páginas de proveedores sobre latencia y tiempo de respuesta, y sobre *coordinated omission*: sin autoría identificable, comerciales o contradictorios entre sí (`Alcance.md` §5.3).

## Registro de búsqueda
| # | Fecha | Buscador o base | Cadena | Resultados revisados | Elegidas / descartadas (motivo) |
|---|---|---|---|---|---|
| 1 | 2026-11-07 | Buscador web | `Schroeder Wierman Harchol-Balter "Open versus closed: a cautionary tale" NSDI 2006 pdf` | 10: páginas de USENIX (registro, HTML y PDF), Caltech, researchr, Toronto | Elegida: F3, desde USENIX. Las demás repiten el mismo artículo. |
| 2 | 2026-11-07 | Buscador web | `"coordinated omission" latency measurement load generator open-loop peer-reviewed paper` | 10: Friedrich et al. (Hamburgo), blogs (dev.to, Artillery, Brooker, devbytes, velobot), una charla (Today Software Magazine), un póster | Elegida: F4, artículo de taller arbitrado. Descartados: blogs y charla (sin revisión o comerciales). |
| 3 | 2026-11-07 | Buscador web | `Lazowska Zahorjan Graham Sevcik "Quantitative System Performance" free online pdf Little's law response time law` | 10: página de los autores (Washington), espejos (Pavía, Temple, Dortmund) y catálogos de libros libres | Elegida: F2, desde la página de los autores. Descartados los espejos, por no ser la fuente original. |
| 4 | 2026-11-07 | Buscador web | `Dean Barroso "The Tail at Scale" Communications of the ACM 2013 tail latency percentiles pdf` | 10: variantes de idioma de la misma página de Google Research, solo con el resumen | Descartada: solo resumen accesible, y F1 cubre los percentiles. |
| 5 | 2026-11-07 | Buscador web | `definition "response time" versus "latency" difference queueing time service time client-perceived performance engineering` | 10: blogs, preguntas de foros, una patente y páginas de proveedores (Loadster, Cirrus Data) | Ninguna elegida: sin autoría identificable o comerciales, y con definiciones contradictorias. Se resuelve como decisión de terminología. |
| 6 | 2026-11-07 | Buscador web | `"Coordinated Omission in NoSQL Database Benchmarking" BTW 2017 Workshopband dl.gi.de Friedrich Wingerath Ritter` | 10: registro de la GI, páginas de la Universidad de Hamburgo, researchr | Confirma la publicación de F4. Los datos se tomaron del registro de la GI (ver «Verificación»). |
