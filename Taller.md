# Diseño del taller práctico

> Documento de diseño de la Fase 2. Recoge las decisiones discutidas sobre el taller. Cuando se aprueben, pasan a `Alcance.md` §7, que sigue siendo el documento de control. Los números marcados como *ilustrativos* son ejemplos: los valores reales salen de la calibración (§7).

**Estado:** Borrador | **Fecha:** 2026-11-07

## 1. Objetivo

Demostrar experimentalmente, con Gatling, cómo una prueba de rendimiento automatizada en un pipeline de CI detecta una regresión de rendimiento y verifica su corrección (PI-5), con un veredicto confiable entre ejecuciones repetidas (`Alcance.md` §7).

La idea que el taller debe dejar clara: **existe un tipo de defecto que ninguna prueba funcional detecta y que solo aparece con carga.** Una prueba de rendimiento automatizada es la que lo atrapa antes de llegar a producción.

## 2. Formato

| Aspecto | Decisión |
|---|---|
| Tipo | **Demostrativo.** Quien presenta ejecuta y explica; los compañeros observan y entienden cómo se hacen las pruebas. No necesitan computadora ni cuenta de GitHub. |
| Duración | 20–30 min (guion de 25 min, §8) |
| Público | Unos 20 compañeros |
| Ejecución | En vivo, en GitHub Actions, proyectado en pantalla. Con plan B grabado. |
| Reproducibilidad | El repositorio es público, y cualquiera puede repetir el taller después: hace un *fork* y ejecuta el workflow. No necesita instalar nada. |

**Relación con el objetivo específico 5** («plan de pruebas ejecutable a través del taller práctico y aplicable con los compañeros del curso»): en la sesión, el plan de pruebas se ejecuta de forma demostrativa frente a los compañeros. Para que también sea *aplicable* por ellos, el repositorio incluye la guía paso a paso para ejecutarlo por su cuenta. **Pendiente:** confirmar que este formato satisface el enunciado.

## 3. Sistema bajo prueba

| Elemento | Decisión |
|---|---|
| Aplicación | API REST propia de una tienda (productos), construida desde cero |
| Stack | Java, Spring Boot y PostgreSQL |
| Entorno | Docker Compose (API + base de datos) |
| Endpoint principal | `GET /productos/{id}`: devuelve el producto y suma una visita a su contador |
| Datos | Unos 1 000 productos sembrados al iniciar (*ilustrativo*) |
| Ética | Solo se prueba contra este entorno propio, nunca contra sistemas de terceros ni sitios públicos |

## 4. Las tres versiones

La historia: un desarrollador agrega un **contador de visitas** por producto. La versión ingenua (leer → sumar → escribir) pierde visitas cuando llegan dos solicitudes a la vez. Para evitarlo, el desarrollador serializa el método con `synchronized`. El contador queda correcto, pero toda la API pasa a atender las solicitudes de una en una.

| Versión | Qué tiene | ¿Contador correcto con concurrencia? | ¿Pasan las pruebas funcionales? | Quién espera a quién |
|---|---|---|---|---|
| `sana` | API sin contador (línea base) | No aplica | Sí | Nadie |
| `regresion` | Contador con `synchronized` | Sí | **Sí** | **Todas las solicitudes, en una fila global** |
| `corregida` | Contador con `UPDATE` atómico en la base de datos | Sí | Sí | Solo dos solicitudes al mismo producto, por un instante |

**Regresión:**

```java
public synchronized Producto verProducto(Long id) {
    Producto p = repo.findById(id).orElseThrow();   // 1. leer de la BD
    p.setVisitas(p.getVisitas() + 1);               // 2. sumar en Java
    repo.save(p);                                   // 3. escribir en la BD
    return p;
}
```

**Corrección:**

```java
@Modifying @Transactional
@Query("UPDATE Producto p SET p.visitas = p.visitas + 1 WHERE p.id = :id")
void sumarVisita(@Param("id") Long id);

public Producto verProducto(Long id) {      // sin synchronized
    repo.sumarVisita(id);
    return repo.findById(id).orElseThrow();
}
```

**La corrección no consiste en quitar el `synchronized` y nada más.** Si solo se quitara, volvería la pérdida de visitas: la API sería rápida pero contaría mal. La corrección cambia **quién controla la concurrencia**: en lugar de un candado global en la aplicación, la base de datos bloquea solo la fila del producto, por un instante.

**Por qué la regresión solo aparece con carga** (*ilustrativo*): si cada solicitud ocupa el bloque unos 25 ms, la API atiende como máximo unas 40 solicitudes por segundo. Con un usuario no se nota nada. Si llegan 50 por segundo, se forma una fila que crece durante toda la prueba y el p95 se dispara. Es la ley de Little en acción (5.3).

## 5. Las pruebas

### 5.1 Escenario común

Las tres pruebas usan el **mismo escenario**: cada usuario virtual pide un producto elegido al azar entre los sembrados, mediante un *feeder* de Gatling, y verifica que la respuesta sea `200`. El azar importa: si todos pidieran el mismo producto, también la versión corregida competiría por la misma fila.

La carga se genera con un **modelo de carga abierto**, es decir, a una tasa de llegadas fija e independiente de las respuestas. Así, todas las ejecuciones reciben la misma carga, la fila de la regresión se hace visible y se evita *coordinated omission* (5.3).

### 5.2 Tipos de prueba

Cada tipo es una clase corta de Gatling que comparte el escenario y declara solo su perfil de carga. Los nombres de los métodos se verifican en la documentación vigente de Gatling (grupo D).

| Tipo | Pregunta que responde | Perfil de carga (*ilustrativo*) | Papel en el pipeline |
|---|---|---|---|
| **Carga** | ¿Cumple los criterios con la carga esperada? | `constantUsersPerSec(R).during(60)` | **Quality gate:** sus aserciones dejan el job en verde o en rojo |
| **Estrés** | ¿Dónde se rompe y cómo se degrada? | Escalones crecientes: `incrementUsersPerSec(10).times(6).eachLevelLasting(20)...` | Informativa: curva del p95 según la carga |
| **Picos** | ¿Aguanta una ráfaga súbita y se recupera? | Base 30 s → subida en 2 s → pico 10 s → bajada → base 30 s | Informativa (criterio propio pendiente, §12) |

**Criterios de la prueba de carga** (*ilustrativos*; los valores reales salen de §7):

```java
.assertions(
    global().responseTime().percentile(95.0).lt(UMBRAL_MS),   // p95 < umbral
    global().failedRequests().percent().lt(1.0)               // errores < 1 %
)
```

**Fuera del taller:** la prueba de resistencia (*soak*). Su sentido es durar horas, y no cabe en una sesión en vivo. Comprimirla a minutos y llamarla así sería engañoso. Se trata solo en el Marco teórico (5.4).

## 6. Pipeline (GitHub Actions)

El workflow se lanza a mano (`workflow_dispatch`), con una entrada `version`: `sana`, `regresion`, `corregida` o `todas`.

```
[Run workflow: version = X]
        │
        ├── Pruebas funcionales (JUnit)        → verdes en las tres versiones
        ├── Carga     × N repeticiones         → quality gate (verde/rojo)
        ├── Estrés    × 1                      → curva p95 según la carga
        └── Picos     × 1                      → p95 y errores antes, durante y después de la ráfaga
        │   (cada job, en su propio runner, levanta su propia API + BD)
        ▼
  Job final: junta las métricas → tabla y gráficos → GitHub Pages
```

**Pasos de cada job de rendimiento:**

1. Descargar la versión elegida del código.
2. Levantar la API y la base de datos con Docker Compose, con la CPU de cada contenedor limitada (por ejemplo, `cpus: 1`). Así se satura la API y no el generador de carga.
3. Esperar a que la API esté lista y enviarle una carga corta de calentamiento, que no se mide.
4. Ejecutar la simulación con Maven. En la de carga, si una aserción falla, el comando termina con error y el job queda en rojo.
5. Guardar las métricas y el reporte HTML como artefactos.

**Job final:** junta las métricas de todos los jobs y publica en GitHub Pages:
- la tabla de versión por tipo de prueba;
- el p95 de cada repetición de la carga;
- la curva de estrés;
- la línea de tiempo del pico;
- los reportes de Gatling.

**Dos usos del mismo workflow:**

- **En vivo:** una versión por ronda (§8). Las tres pruebas corren en paralelo, así que una ronda dura lo que tarda la más larga.
- **Antes de la clase:** con `version` en `todas`, una sola ejecución prueba las 3 versiones con los 3 tipos de prueba. Sirve para calibrar (§7) y para los resultados del documento.

**Optimización para la sesión:** las imágenes de las tres versiones se construyen de antemano y se publican en GitHub Container Registry. Los jobs de rendimiento no compilan la API: descargan la imagen de la versión elegida. Las dependencias de Maven quedan en caché.

## 7. Calibración y confiabilidad del veredicto

La calibración se hace antes de la clase y es la parte metodológica central del taller.

1. **Encontrar la capacidad de cada versión** con la prueba de estrés: hasta qué tasa responde sin que el p95 se dispare.
2. **Elegir la tasa de la prueba de carga (R)** por **encima** de la capacidad de `regresion` y por **debajo** de la de `sana` y `corregida`. Si la tasa queda por debajo de ambas, la regresión no se nota.
3. **Repetir la prueba de carga** unas 20 veces por versión (*ilustrativo*) y registrar el p95 de cada ejecución.
4. **Fijar el umbral** en el hueco entre las distribuciones: por encima del peor p95 de `sana` y `corregida`, por debajo del mejor p95 de `regresion` y con margen hacia los dos lados.
5. **Comprobar** que, con ese umbral, todas las repeticiones de `sana` y `corregida` pasan y todas las de `regresion` fallan.
6. **Reportar** cuánto varían las métricas entre ejecuciones (rango y coeficiente de variación) y justificar el umbral con ese margen.

```
sana / corregida:  p95 entre 35 y 55 ms      (ilustrativo)
regresión:         p95 entre 600 y 900 ms
                   ──────────┼──────────
                           umbral, lejos de los dos rangos
```

## 8. Guion de la sesión (25 min)

Quien presenta maneja la computadora y el proyector. El público observa; en algunos momentos se le hace una pregunta en voz alta para que piense la respuesta antes de ver el resultado.

| Min | Qué se hace | Qué se ve en pantalla |
|---|---|---|
| **0–3: Contexto** | El problema: un sistema puede funcionar bien y fallar con carga. Se presentan la API y las tres versiones. | Diagrama de la API y tabla de versiones |
| **3–6: Cómo es una prueba de rendimiento** | Escenario, carga y criterios en el código de Gatling. Modelo abierto. Los tres tipos de prueba y sus perfiles. Se lanza la ronda 0. | La clase de Gatling y los perfiles de carga |
| **6–10: Ronda 0, `sana`** | Mientras corre, se explica el pipeline y el *quality gate*. Después se leen los resultados. | Actions en vivo; luego, carga en verde, curva de estrés y pico con recuperación |
| **10–17: Ronda 1, `regresion`** | Se muestra el cambio y que las pruebas funcionales siguen verdes. Pregunta: «¿qué va a pasar con carga?». Se lanza. Mientras corre, se explica la fila con la ley de Little. | Pruebas funcionales en verde y carga **en rojo**; el estrés se rompe antes; el pico no se recupera; la CPU baja aunque la API vaya lenta |
| **17–22: Ronda 2, `corregida`** | Pregunta: «¿y si solo quitamos el `synchronized`?». Se explica por qué no basta y se muestra la corrección. Se lanza. | De nuevo en verde, con el p95 cerca de la línea base |
| **22–25: Cierre** | Resultados de la calibración: variación entre repeticiones y umbral justificado. Comparación de las 3 versiones (ejecución `todas`, previa). Qué no demuestra el taller (§10). Enlace al repositorio. | Tabla y gráficos comparativos; QR del repositorio |

Quedan 5 minutos de holgura dentro de los 30. Si GitHub o la red fallan, se pasa a las ejecuciones grabadas sin cortar el hilo.

## 9. Respaldo en la investigación

Cada decisión del taller remite a una subsección del Marco teórico y a su fuente. Lo que no tenga respaldo se declara como decisión propia del trabajo, sin atribuirlo a una fuente. Esta tabla pasa como requisito al plan de la sección 06.

| Decisión del taller | Subsección | Fuente | Estado |
|---|---|---|---|
| La regresión pasa las pruebas funcionales y se detecta con carga | 5.1, 5.7 | ISTQB CTFL (2024); grupo C | A cubrir en C |
| Prueba en CI como *quality gate* | 5.1 | Humble y Farley (2010); Bezemer et al. (2019) | Redactado (A) |
| La carga actúa de compuerta; el estrés y los picos informan | 5.1 | Humble y Farley (2010, p. 128) | Redactado (A) |
| Criterios sobre tiempo de respuesta, *throughput* y recursos | 5.2 | ISO/IEC 25010:2023; CT-PT §1.1 | Redactado (A) |
| p95 en lugar del promedio | 5.3 | CT-PT §4.4 | Planificado (B) |
| Por qué el candado crea una fila que crece | 5.3 | Lazowska et al. (1984), ley de Little | Planificado (B) |
| Modelo de carga abierto con tasa fija | 5.3 | Schroeder et al. (2006) | Planificado (B) |
| Evitar *coordinated omission* con el modelo abierto | 5.3 | Friedrich et al. (2017) | Planificado (B) |
| Tipos de prueba: carga, estrés y picos; la resistencia, solo en el Marco teórico | 5.4 | CT-PT §1.2 | Planificado (B) |
| Plan de pruebas por fases | 5.5 | CT-PT; ISO/IEC/IEEE 29119-3 | **A cubrir en C** |
| Línea base, calentamiento y repeticiones | 5.6 | — | **A cubrir en C** |
| Generador y API en la misma máquina (antipatrón declarado) | 5.6 | Jiang y Hassan (2015) | **A cubrir en C** |
| Umbral con margen frente a la variación | 5.7 | Leitner y Bezemer (2017); Daly et al. (2020) | Citado en el Planteamiento; a desarrollar en C |
| Frecuencia distinta para cada tipo de prueba | 5.7 | — | **A cubrir en C** |
| Perfiles de inyección y aserciones de Gatling | 5.8 | Documentación oficial de Gatling | **A cubrir en D** |

**Para el plan del grupo C:** antes de planificarlo, el planificador recibe la lista de lo que el taller necesita respaldar: línea base, calentamiento, repeticiones, aislamiento del generador de carga, umbrales con margen y frecuencia de ejecución por tipo de prueba. Esa lista sirve para que el Marco teórico no deje sin respaldo lo que el taller usa, no para orientarlo hacia el taller.

## 10. Límites que se declaran

- El taller detecta si un cambio **empeoró** el rendimiento frente a la versión anterior. **No mide** cuánto aguantaría un sistema real en producción.
- El generador de carga y la API comparten la máquina del runner de CI. Es un antipatrón (5.6), mitigado con el límite de CPU y una carga moderada, y se declara.
- El runner de CI no se parece a un entorno de producción. Es el problema del entorno no representativo del Planteamiento del problema (3.2).
- La regresión es una sola, de un tipo concreto (contención por un candado). Otros tipos, como las consultas N+1 o las fugas de memoria, no se demuestran.

## 11. Productos para el documento

**Sección 6, Propuesta de taller práctico (6 págs.).** La distribución es tentativa y se fija en el plan de la sección:

| Subsección | Págs. | Contenido |
|---|---|---|
| Contexto de aplicación | 0,75 | El problema, la API y las tres versiones |
| Recursos, código y stack | 0,5 | Repositorio, tecnologías y versiones |
| Plan de pruebas | 1,5 | Objetivos, alcance, tipos, criterios, entorno y calibración (estructura según ISO/IEC/IEEE 29119-3) |
| Guía paso a paso | 1,25 | Cómo ejecutar el taller desde un *fork*; el detalle completo va en el repositorio |
| Resultados | 1,5 | Variación por versión, umbral justificado, tabla de versión por tipo de prueba y curvas |
| Límites | 0,5 | §10 |

**Anexo C (1,5 págs.):** capturas del pipeline y de los reportes, y el enlace al repositorio.

**Conclusiones:** el balance técnico del taller y la respuesta a PI-5.

## 12. Preparación y pendientes

**Antes de la clase:** la construcción, la calibración, la comparación final y el plan B están automatizados (§13). Lo único manual es el ensayo de la presentación con cronómetro.

**Por decidir:**

- [ ] El criterio de la prueba de picos (por ejemplo: errores < X % y recuperación del p95 en < Y s), o dejarla solo informativa
- [ ] Número de repeticiones de la carga en vivo (N) y en la calibración
- [ ] Tasa de carga (R), umbral y escalones del estrés, según la calibración
- [ ] Confirmar que el formato demostrativo cumple el objetivo específico 5 (§2)

**Por verificar:**

- [ ] Límite de jobs en paralelo de GitHub Actions en el plan gratuito, para dimensionar N y la ejecución `todas`
- [ ] Recursos de los runners públicos (CPU y memoria) para fijar los límites de los contenedores
- [ ] Cómo extraer el p95 por escalón en la prueba de estrés a partir de los archivos de Gatling
- [ ] Nombres y comportamiento de los métodos de inyección y de las aserciones en la versión vigente de Gatling
- [ ] Duración real de una ronda en vivo
- [ ] Existencia y acceso de ISO/IEC/IEEE 29119-3 (`Alcance.md` §8: «verificar existencia antes de usar»)

## 13. Plan de implementación

El taller lo construye Claude Code completo. Todo lo que se repite queda automatizado: construir las imágenes, ejecutar las pruebas, juntar las métricas, publicar los resultados, calibrar y comprobar que la demostración se comporta como se espera. Las únicas acciones humanas son las aprobaciones (§13.6) y, en la sesión, apretar «Run workflow».

### 13.1 Principios

- **Un clic por acción.** Cada operación (preparar, ejecutar una ronda, calibrar, verificar) es un workflow con `workflow_dispatch`, sin pasos manuales en medio.
- **Sin secretos.** Solo se usa el `GITHUB_TOKEN` del propio workflow. Así, un *fork* funciona sin configurar nada (§2).
- **Todo fijado.** Las versiones de Java, Spring Boot, Gatling, PostgreSQL y las *actions* de GitHub se fijan en una versión exacta, y no se actualizan solas. Así, una ejecución de hoy y una de la semana de la clase usan lo mismo.
- **Parámetros fuera del código.** La tasa de carga, el umbral, los escalones del estrés y el perfil del pico viven en `config/parametros.json`. La calibración los propone y una persona los aprueba (§13.4).
- **La demostración se prueba a sí misma.** Un workflow de verificación comprueba que `sana` y `corregida` pasan y `regresion` falla (§13.4).

### 13.2 Repositorio

**Ubicación (por confirmar):** propongo un **repositorio público propio del taller**, separado del de la investigación, por ejemplo `taller-rendimiento-gatling`.

- Quien lo copie se lleva solo el taller.
- GitHub Pages y Actions quedan dedicados a él.
- Los cambios de la investigación no disparan workflows.

La alternativa es una carpeta `taller/` en este repositorio, con los workflows filtrados por ruta.

```
taller-rendimiento-gatling/
├── api/                          API de la tienda (Spring Boot, Maven Wrapper)
│   ├── src/main/...              controlador, servicio, repositorio, datos semilla
│   ├── src/test/...              pruebas funcionales (JUnit + Spring Boot Test)
│   └── Dockerfile
├── rendimiento/                  proyecto Gatling (DSL de Java, Maven Wrapper)
│   └── src/test/java/...
│       ├── TiendaBase.java       protocolo, feeder y escenario común
│       ├── CargaSimulation.java  perfil de carga + aserciones (quality gate)
│       ├── EstresSimulation.java perfil en escalones
│       └── PicosSimulation.java  perfil base → pico → base
├── config/parametros.json        tasa, umbral, escalones, perfil del pico, repeticiones
├── docker-compose.yml            API + PostgreSQL, con límites de CPU y memoria
├── scripts/
│   ├── esperar_api.sh            espera a que la API responda
│   ├── calentar.sh               carga corta de calentamiento, no medida
│   ├── muestrear_recursos.sh     docker stats cada segundo → CSV de CPU y memoria
│   ├── extraer_metricas.py       reporte de Gatling → metricas.json por job
│   ├── agregar.py                todas las métricas → tabla, gráficos, resumen e índice HTML
│   └── calibrar.py               capacidades → tasa y umbral propuestos + informe
├── .github/workflows/
│   ├── preparar.yml              construye y publica las imágenes de las tres versiones
│   ├── rendimiento.yml           ronda en vivo o `todas` (§6)
│   ├── calibracion.yml           calibración (§7) → pull request con parámetros
│   └── verificacion.yml          ensayo automático de la demostración
└── docs/
    ├── GUIA.md                   cómo repetir el taller desde un fork
    └── PLAN-DE-PRUEBAS.md        plan de pruebas (estructura según ISO/IEC/IEEE 29119-3)
```

**Las tres versiones como historia de *commits*:** la API se escribe en tres *commits* sucesivos, marcados con *tags*. Así, la regresión y la corrección son cambios de código reales, y en la sesión se muestran con la vista de comparación de GitHub.

| Tag | Commit | Imagen |
|---|---|---|
| `v1-sana` | API sin contador | `ghcr.io/<dueño>/tienda-api:sana` |
| `v2-regresion` | Agrega el contador con `synchronized` | `ghcr.io/<dueño>/tienda-api:regresion` |
| `v3-corregida` | Reemplaza el candado por el `UPDATE` atómico | `ghcr.io/<dueño>/tienda-api:corregida` |

Las pruebas funcionales evolucionan con cada *commit*. Desde `v2` incluyen una prueba concurrente del contador (varios hilos suman visitas y el total debe cuadrar), que pasa en `v2` y en `v3`. Esa prueba es la que demuestra que la regresión es funcionalmente correcta.

### 13.3 Workflows

| Workflow | Disparo | Entradas | Qué hace | Resultado |
|---|---|---|---|---|
| `preparar.yml` | Manual y al crear un tag | — | Compila cada tag, corre sus pruebas funcionales, construye la imagen y la publica en GHCR | Las tres imágenes listas |
| `rendimiento.yml` | Manual | `version`: `sana`, `regresion`, `corregida` o `todas` | Pruebas funcionales del tag; carga × N, estrés y picos por versión (§6); agregación y publicación | Veredicto, tabla y gráficos en Pages |
| `calibracion.yml` | Manual | — | Estrés escalonado amplio para las tres versiones; capacidades; tasa propuesta; carga × 20 por versión con esa tasa; umbral propuesto | Pull request que actualiza `config/parametros.json` y agrega el informe de calibración |
| `verificacion.yml` | Manual y programado (por ejemplo, cada noche la semana de la clase) | — | Ejecuta `todas` y compara con lo esperado: `sana` y `corregida` pasan la carga; `regresion` la falla en todas las repeticiones | Verde si la demostración se comporta como debe; rojo, con el detalle, si no |

**Detalles de `rendimiento.yml`:**

- Cada job de rendimiento corre en su propio runner. Descarga la imagen de su versión y levanta `docker-compose.yml`. Después, en segundo plano, arranca `muestrear_recursos.sh`, espera a la API, calienta y ejecuta su simulación con los parámetros de `config/parametros.json`.
- En la ronda de `regresion`, el job de carga **debe** quedar en rojo: es la demostración. Con `todas`, los jobs de carga usan `continue-on-error`, y el job final informa el veredicto de cada versión sin que el workflow completo falle.
- El job final se ejecuta siempre (`if: always()`). Descarga los artefactos, ejecuta `agregar.py`, escribe el resumen en la página de la ejecución (`$GITHUB_STEP_SUMMARY`) y publica en Pages.

**Publicación en Pages con historial:** cada ejecución se guarda en una carpeta propia, `ejecuciones/<fecha>-<versión>-<id>/`, en una rama `resultados`, y el índice se regenera con la lista de ejecuciones. Así, las ejecuciones anteriores siguen disponibles, y el **plan B es automático**: si en clase falla una ronda, se abre la última ejecución publicada de esa versión.

### 13.4 Calibración y verificación automáticas

**Regla de calibración**, fijada antes de ver los datos (es una decisión propia del trabajo, y así se declara):

1. **Capacidad de una versión:** la mayor tasa del estrés escalonado en la que el p95 no supera *k* veces el p95 del primer escalón y los errores no pasan del 1 %. El valor de *k* se fija en el plan de la sección 06.
2. **Tasa de carga:** un valor entre la capacidad de `regresion` y la menor capacidad de `sana` y `corregida`, con margen respecto de ambas. Si no hay margen suficiente, la calibración falla y lo informa; no se fuerza un valor.
3. **Umbral:** un valor en el hueco entre el peor p95 de `sana` y `corregida` y el mejor p95 de `regresion`, con margen hacia los dos lados. Si los rangos se tocan, la calibración falla y lo informa.
4. **Informe:** capacidades, rangos de p95, coeficiente de variación por versión, tasa y umbral propuestos, con sus márgenes. Va en el pull request, y sus tablas y gráficos alimentan los Resultados de la sección 6.

El pull request no se fusiona solo. Una persona revisa el informe y lo aprueba (§13.6).

**Verificación:** `verificacion.yml` repite la demostración completa y falla si alguna repetición da un veredicto distinto del esperado. Programada en los días previos a la clase, detecta si los runners de GitHub cambiaron lo suficiente como para invalidar la calibración. Sus ejecuciones también suman datos de variación para el documento.

### 13.5 Etapas de construcción

Cada etapa termina con un criterio que se comprueba antes de pasar a la siguiente.

- **Etapas 1–4:** se desarrollan y prueban en local. Java, Docker y Docker Compose están disponibles en esta máquina, y Maven llega con el Maven Wrapper.
- **Etapas 5–9:** se comprueban en GitHub Actions, porque la calibración solo vale en el entorno donde se ejecuta la demostración.

| # | Etapa | Entregables | Criterio de terminado |
|---|---|---|---|
| 1 | Esqueleto | Repositorio, Maven Wrapper en `api/` y `rendimiento/`, `docker-compose.yml`, versiones fijadas | `docker compose up` levanta PostgreSQL y una API vacía que responde |
| 2 | Versión `sana` | Endpoint, datos semilla, pruebas funcionales, Dockerfile, tag `v1-sana` | Pruebas funcionales en verde; la imagen arranca y responde con los datos sembrados |
| 3 | Versiones `regresion` y `corregida` | Contador con candado; prueba concurrente; corrección atómica; tags `v2-regresion` y `v3-corregida` | La prueba concurrente pasa en `v2` y `v3`. En local, con carga, `v2` es claramente más lenta que `v1` y `v3` |
| 4 | Simulaciones de Gatling | `TiendaBase` y las tres simulaciones, leyendo `parametros.json` | En local, contra cada versión, las tres simulaciones terminan y generan su reporte; la de carga falla con `v2` |
| 5 | Imágenes en CI | `preparar.yml` | Las tres imágenes quedan en GHCR desde una ejecución limpia |
| 6 | Ronda en CI | `rendimiento.yml` con una versión, muestreo de recursos y `extraer_metricas.py` | Una ronda de cada versión termina con el veredicto esperado y sus métricas en artefactos |
| 7 | Resultados publicados | `agregar.py`, publicación con historial, modo `todas` | La página muestra la tabla de versión por tipo de prueba, las curvas y los reportes; las ejecuciones anteriores siguen disponibles |
| 8 | Calibración | `calibrar.py` y `calibracion.yml` | El pull request trae parámetros con margen en los dos lados y su informe |
| 9 | Verificación | `verificacion.yml` | Tres ejecuciones seguidas, en días distintos, sin un solo veredicto distinto del esperado |
| 10 | Documentación | `README`, `docs/GUIA.md`, `docs/PLAN-DE-PRUEBAS.md` | Una persona que no participó puede hacer un *fork* y repetir el taller siguiendo solo la guía |

### 13.6 Aprobaciones humanas

| Momento | Qué se aprueba | Por qué no se automatiza |
|---|---|---|
| Antes de la etapa 1 | Dónde vive el repositorio y con qué cuenta | Crear un repositorio público es una acción visible hacia afuera |
| Etapa 5 | Activar Pages y dejar públicas las imágenes de GHCR | Son configuraciones de la cuenta |
| Etapa 8 | Fusionar el pull request de calibración | El umbral es el criterio del *quality gate*: una persona debe revisarlo |
| Antes de la clase | Revisar el último informe de verificación | Es la última comprobación de que la demostración funciona |

### 13.7 Riesgos

| Riesgo | Mitigación |
|---|---|
| El ruido de los runners es mayor que la diferencia entre versiones | La regresión se diseña para multiplicar el p95, no para empeorarlo un poco; la calibración falla de forma explícita si no hay margen |
| La base de datos es tan rápida que el candado no se nota | Se ajusta el trabajo dentro del bloque o la tasa de carga en la calibración, sin agregar esperas artificiales |
| El generador de carga se satura antes que la API | Límite de CPU para los contenedores y muestreo de recursos del runner completo; si el generador se satura, se ve en los datos |
| Límite de jobs en paralelo | Con N moderado en vivo y la cola aceptada en `todas` y en la calibración, que corren antes de la clase |
| GitHub o la red fallan en clase | Plan B automático en Pages (§13.3) |
| Cambian las versiones de las herramientas | Todo fijado (§13.1) |
