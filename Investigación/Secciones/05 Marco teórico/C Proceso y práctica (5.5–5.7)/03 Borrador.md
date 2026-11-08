# Marco teórico — 5.5, 5.6 y 5.7

<!-- Borrador v3 | Plan v2 | Evidencia v3 | 2026-11-07 -->
<!-- v3: corrige el hallazgo bloqueante 1 y aplica las sugerencias 3 y 4 de la auditoría, ronda 2. v2: corrige el hallazgo bloqueante 1 y aplica las sugerencias 2–4 de la auditoría, ronda 1. -->

## 5.5 Proceso de pruebas de rendimiento

<!-- B1. Actividades del proceso -->

Las pruebas de rendimiento siguen las actividades del proceso de pruebas general, pero cada una con tareas propias. La planificación es especialmente importante, porque debe asignar entornos, datos, herramientas y personas, y el monitoreo y control prevé acciones ante desvíos y evalúa los criterios de salida. El análisis fija condiciones, como los niveles de carga, y decide los tipos de prueba. El diseño produce casos modulares que se combinan en pruebas mayores, y la implementación prepara el entorno antes de cada ejecución, con datos representativos de producción en volumen y tipo. La ejecución evalúa si se cumplen los requisitos, y el cierre entrega los resultados en un informe (ISTQB, 2018) <!-- E1, E30, E2 -->.

El conjunto, además, es iterativo: cada prueba aporta información para corregir u optimizar el sistema, y la siguiente muestra el efecto de esos cambios. La carga también se construye por partes: los perfiles operacionales, que describen cómo usa el sistema cada tipo de usuario, se agregan en un perfil de carga (ISTQB, 2018) <!-- E3, E4 -->.

<!-- B2. Entorno y datos -->

El entorno es lo más delicado del proceso. Debe parecerse a producción tanto como sea posible, porque el rendimiento es una función no lineal del entorno: cuanto más se aleja de producción, menos fiables son las proyecciones. El tamaño y la estructura de los datos pueden alterar los resultados de forma drástica (ISTQB, 2018) <!-- E5, E6 -->. Humble y Farley (2010) <!-- E31, E7 --> llaman pruebas de capacidad a un conjunto más amplio que el tipo de 5.4, y advierten que, en hardware menos potente, revelan los problemas graves, pero no demuestran que la aplicación cumpla sus objetivos. Por eso, en un entorno propio y reducido como el del taller, lo útil es comparar versiones del sistema en el mismo entorno, no su capacidad absoluta.

## 5.6 Principios, buenas prácticas y antipatrones

<!-- B3. Línea base y repetibilidad -->

De ahí el principio del que dependen los demás: una prueba de rendimiento vale sobre todo como comparación. La línea base es el conjunto de métricas con que se comparan las mediciones actuales con las anteriores (ISTQB, 2018) <!-- E8 -->. Cuando faltan requisitos no funcionales, el criterio de aceptación suele derivarse del principio de «no peor que antes»: la versión nueva no debe rendir menos que la anterior (Jiang & Hassan, 2015) <!-- E9 -->.

Y comparar exige resultados que se repitan. Para lograrlo, Humble y Farley (2010) <!-- E10 --> recomiendan aislar el entorno y dedicarlo solo a medir. Aun así, el ruido, la variación entre ejecuciones ajena al cambio evaluado, no desaparece: en un sistema de CI industrial, la peor variación era menor del 10 % en la mayoría de las pruebas y llegaba al 20 % o más en algunas (Daly et al., 2020) <!-- E11 -->.

<!-- B4. Realismo de la ejecución -->

Una ejecución debe medir el sistema, no sus artefactos. Un conjunto de datos pequeño, o de complejidad distinta a la de producción, puede dar resultados engañosos, y las máquinas que generan la carga deben monitorearse, por si una, más lenta, no sostiene la carga (ISTQB, 2018) <!-- E12, E13 -->. En plataformas que optimizan en tiempo de ejecución, como .NET y Java, los resultados sensatos solo llegan tras varios minutos de período de calentamiento (*warm-up*). Antes de confiar en un fallo, conviene comprobar contra un sustituto vacío (*stub*) que la propia prueba alcanza la tasa necesaria, porque, en su experiencia, muchas pruebas atribuyen a la aplicación un fallo que es de la prueba (Humble & Farley, 2010) <!-- E14, E15 -->. Por eso conviene separar el estado inicial del estable (5.4) y justificar cuándo empieza a medirse.

<!-- B5. Antipatrones -->

Los antipatrones más comunes no son errores técnicos, sino de criterio. El primero es probar sin objetivos: no debe emprenderse una prueba de rendimiento sin entender antes qué mediciones y métricas hacen falta (ISTQB, 2018) <!-- E16 -->. El segundo es resumir con promedios, que esconden la cola de la distribución (5.3). Humble y Farley (2010) <!-- E17, E18, E19 --> describen otros tres: los requisitos vagos, como «lo más rápido posible», que no ponen límite al esfuerzo; el entorno compartido, en el que una versión puede fallar porque otras pruebas automatizadas corrían a la vez, y la medición sin criterio de aceptación, que deja el veredicto a un análisis humano largo.

## 5.7 Automatización e integración en CI/CD

<!-- B6. Umbrales y regresiones -->

Como *quality gate*, una prueba de rendimiento necesita un umbral explícito. Un objetivo de nivel de servicio (SLO) es un valor o rango objetivo para un nivel de servicio medido por un indicador de nivel de servicio (SLI), una medida cuantitativa del servicio (Jones et al., 2016) <!-- E20, E21 -->. Si existe un SLO, es un buen punto de partida para el umbral. Fijarlo es delicado: Humble y Farley (2010) <!-- E22, E23 --> señalan que un umbral demasiado exigente produce fallos intermitentes y uno demasiado holgado no detecta un cambio que reduce el *throughput* casi a la mitad, y proponen subirlo progresivamente cuando ya pasa. Un umbral estático, además, confunde cambio y ruido: en un sistema de CI, uno fijo del 10 % daba muchas falsas alarmas en las pruebas ruidosas y dejaba pasar regresiones menores; la detección de puntos de cambio las redujo drásticamente (Daly et al., 2020) <!-- E24, E25 -->. Su margen debe justificarse con la variación medida.

<!-- B7. Frecuencia, etapa y observabilidad -->

No todas las pruebas de rendimiento caben en cada *commit*. El objetivo principal de las que corren en CI es asegurar que un cambio no empeore el rendimiento, y por el poco tiempo disponible pueden limitarse a un subconjunto de pruebas más extensas (ISTQB, 2018) <!-- E26 -->. Humble y Farley (2010) <!-- E27, E28 --> distinguen dos niveles: pruebas de humo de rendimiento en la etapa de *commit*, que vigilan puntos críticos conocidos, y una etapa propia para las pruebas largas, que en algunos proyectos funciona como compuerta: si no pasan, no se despliega sin una intervención manual.

Lo que el pipeline no ve lo completa la observabilidad. Tras la entrega, el rendimiento debe monitorearse para saber si la aplicación alcanza los niveles deseados en el uso real (ISTQB, 2018) <!-- E29 -->, el complemento *shift-right* de 5.1.
