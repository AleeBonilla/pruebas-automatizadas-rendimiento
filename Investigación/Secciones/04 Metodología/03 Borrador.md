# Metodología

<!-- Borrador v5 | Plan v3 | Evidencia v2 | 2026-11-07 -->
<!-- v5: reescribe el segundo párrafo de 4.2 a pedido del usuario, sin referencias internas al flujo de trabajo (prosa sin citas). Si en el Marco teórico se usan bases bibliográficas además del buscador web, hay que nombrarlas en ese párrafo. v4: aplica las sugerencias 1 y 2 de la auditoría, ronda 2 (prosa sin citas; no requiere nueva auditoría). v3: condensación al nuevo presupuesto (700 palabras), según el plan v3. Se conservan las dos fuentes; deja de citarse E5. v2: aplica las sugerencias 1 y 2 de la auditoría, ronda 1. -->
<!-- Las cifras de 4.3 tienen fecha de corte 2026-11-07 y deben actualizarse al terminar la Fase 1. -->

## 4.1 Enfoque metodológico

Esta investigación es de tipo teórico-aplicado y combina dos componentes. Una revisión de literatura construye la base conceptual y el diagnóstico, y responde las preguntas PI-1 a PI-4; un componente experimental, el taller práctico, pone esa base a prueba en un caso concreto y responde PI-5. Entre los dos abordan la pregunta-problema: la revisión explica qué hace falta para automatizar estas pruebas de forma confiable, y el taller muestra si es posible hacerlo con un costo de adopción bajo.

La revisión es semisistemática. Snyder (2019) <!-- E1, E2, E3 --> describe este enfoque como el adecuado para temas que distintos grupos de investigadores han conceptualizado y estudiado de maneras diferentes; su búsqueda puede ser sistemática o no, pero el proceso debe ser transparente y seguir una estrategia definida, de modo que el lector pueda juzgar si las decisiones fueron razonables. Las pruebas de rendimiento encajan en esa descripción: se estudian desde la ingeniería de rendimiento, desde las pruebas de software y desde la práctica industrial.

## 4.2 Fuentes y estrategia de búsqueda

Las fuentes se eligieron por su cercanía al origen de cada afirmación. Se prefirieron, en este orden, las normas y los syllabus del ISTQB; los artículos revisados por pares, sobre todo de ACM e IEEE, y la documentación oficial de las herramientas. Se incluyeron trabajos de 2010 a 2026, en inglés o en español, salvo algunos clásicos anteriores, y se excluyeron los blogs sin autoría identificable, el contenido comercial sin datos y los temas que el alcance deja fuera.

Las búsquedas fueron dirigidas: cada una buscó respaldo para una afirmación concreta que la sección necesitaba, y se hicieron en un buscador web. A partir del Marco teórico, cada consulta se registró con su fecha, el buscador, la cadena de búsqueda y las fuentes elegidas o descartadas. Las consultas de la Introducción y del Planteamiento del problema no se registraron; de esas secciones solo consta qué fuentes se verificaron y cuáles se descartaron, con su motivo.

Los datos bibliográficos se comprobaron en la página de publicación o en la propia copia consultada, y el DOI en Crossref cuando lo había; cada fuente se leyó en texto completo. Se usaron copias abiertas y legales, como las actas que publica SPEC, arXiv, copias de autor o repositorios institucionales, y las fuentes cerradas se consultaron en copias locales. La búsqueda no pretende ser exhaustiva: busca la fuente más directa para cada afirmación y deja constancia de por qué se eligió. El anexo A resume las consultas y las fuentes descartadas.

## 4.3 Uso y validación crítica de la inteligencia artificial

El documento se elaboró con herramientas de inteligencia artificial, y eso exige controles específicos, porque los modelos de lenguaje pueden citar obras que no existen. En un estudio con textos generados por ChatGPT, el 55 % de las obras citadas por GPT-3.5 eran inventadas, frente al 18 % con GPT-4 (Walters & Wilder, 2023) <!-- E4 -->. Son modelos anteriores a los usados aquí, pero el riesgo basta para no aceptar ninguna cita sin cotejarla con su fuente.

El procedimiento separa la producción del control: Claude Code, con el modelo Opus 5.5, planifica y redacta, y Codex, con el modelo GPT-6.1 Sol, de otro proveedor, audita. Cada sección pasa por tres pasos. Un plan define la idea central de cada bloque, las afirmaciones que requieren respaldo y las fuentes verificadas, y ninguna sección avanza sin la aprobación humana de su plan. La redacción lee las fuentes en texto completo y registra cada cita en una tabla de evidencia, con el pasaje literal y su ubicación. El auditor, en una sesión independiente, coteja cada cita con su fuente y revisa la prosa; la aprobación exige resolver sus hallazgos bloqueantes, como una cita infiel o un dato sin respaldo, y los que queden tras dos rondas se entregan a revisión humana, que es siempre la última.

Hasta el 7 de noviembre de 2026, este control detectó errores que la redacción no había visto, como afirmaciones que decían más que su fuente o una interpretación atribuida a un hallazgo distinto del que la originaba. El procedimiento mismo se corrigió a partir de sus resultados: una primera versión, en la que la redacción solo podía parafrasear evidencia auditada de antemano, produjo una introducción de 882 palabras con 17 citas; con la versión actual, la reescritura de esa introducción, de extensión similar, quedó con 8. El anexo B detalla cada hallazgo y su resolución.
