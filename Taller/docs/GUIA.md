# Guía del taller

Esta guía lleva de una computadora con Docker a ver una prueba de rendimiento rechazar un cambio defectuoso que las pruebas funcionales dejan pasar. Primero se reproduce el caso en local, después se lee lo que pasó desde Gatling y desde Grafana, y al final se repite en GitHub Actions como compuerta de un *pull request*. El diseño completo y sus razones están en [`Taller.md`](../Taller.md); aquí solo está el procedimiento.

El caso es una API de productos con un contador de visitas. La variante `regresion` protege el contador con un candado compartido por todas las solicitudes; la variante `corregida` lo incrementa con una sola instrucción SQL atómica. Las dos cuentan bien las visitas, así que las pruebas funcionales aprueban ambas. La diferencia solo aparece cuando llegan muchas solicitudes a la vez.

## 1. Requisitos

| Requisito | Detalle |
|---|---|
| Git | Cualquier versión reciente |
| Docker con Compose v2 | Docker Desktop en Windows o macOS; Docker Engine con el *plugin* de Compose en Linux |
| Núcleos | Al menos 4: la API y PostgreSQL usan los núcleos 2 y 3 de forma exclusiva |
| Recursos para Docker | Unas 5 CPU y 5,5 GB de memoria. En Docker Desktop se ajustan en *Settings → Resources*; con WSL2, en `%UserProfile%\.wslconfig` |
| Puertos libres | 8000 (API), 9090 (Prometheus) y 3000 (Grafana) |
| Línea de comandos | PowerShell 5.1 o 7 en Windows; `sh` en Linux y macOS |

No hace falta instalar Python, Java ni Maven: todo corre en contenedores. El procedimiento con `taller.sh` es el mismo que usa GitHub Actions en Linux; en macOS todavía no se ha comprobado.

Durante las mediciones conviene no usar la computadora para tareas pesadas. Otro programa que compita por la CPU cambia los resultados, y eso es justamente el ruido que la prueba intenta controlar.

## 2. Obtener el código

```sh
git clone https://github.com/AleeBonilla/pruebas-automatizadas-rendimiento.git
cd pruebas-automatizadas-rendimiento/Taller
```

Todos los comandos de esta guía se ejecutan dentro de `Taller/`. Cada uno aparece en sus dos formas: PowerShell para Windows y `sh` para Linux y macOS.

En Windows, si PowerShell no permite ejecutar scripts, se habilitan solo para la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## 3. Preparar el entorno

```powershell
.\taller.ps1 preparar
```

```sh
./taller.sh preparar
```

`preparar` construye las imágenes, levanta la API, PostgreSQL, Prometheus y Grafana, espera a que todos superen su *healthcheck* y deja los datos en su estado inicial: 10 000 productos con las visitas en cero. La primera vez tarda varios minutos, porque descarga las imágenes y compila la simulación de Gatling; las siguientes, segundos. Termina con `Entorno listo. API: healthy.`

Para comprobarlo:

| Dirección | Qué se ve |
|---|---|
| <http://localhost:8000/productos/1> | Un producto en JSON; cada recarga suma una visita |
| <http://localhost:3000> | Grafana con el panel «API del taller», sin iniciar sesión |
| <http://localhost:9090/targets> | Prometheus leyendo las métricas de la API |

## 4. Pruebas funcionales

```powershell
.\taller.ps1 funcionales
```

```sh
./taller.sh funcionales
```

Las 38 pruebas de pytest comprueban el contrato de la API, que una falla deshace la transacción y que, con solicitudes concurrentes, el contador final coincide con las visitas hechas. Lo comprueba en las dos variantes del contador, y las dos aprueban. Una de las pruebas reemplaza el candado por un «leer, sumar y escribir» sin protección y verifica que esa versión sí pierde visitas: así se sabe que la prueba de concurrencia es capaz de fallar.

Este es el punto de partida del taller: si solo existieran estas pruebas, `regresion` pasaría.

## 5. Prueba de carga

La prueba de carga envía solicitudes a un ritmo fijo, sin esperar las respuestas, como llegan los clientes de un servicio real. Primero hay un calentamiento de 60 s que no se evalúa y después 180 s de medición, sobre los que se calculan el p95 (el tiempo que no supera el 95 % de las solicitudes) y el porcentaje de errores.

El ritmo y el umbral salen de un perfil en `config/perfiles/`. El perfil `local` se calibró en la computadora de desarrollo y no vale para otra sin calibrarlo de nuevo, así que esta guía usa el perfil `ci`: 150 solicitudes por segundo, p95 menor que 3 000 ms y como máximo 1 % de errores. Esa tasa separa las variantes en cualquier computadora que cumpla los requisitos, porque el límite de `regresion` no depende del procesador: con el candado, cada visita retiene a las demás mientras espera a la base de datos, y eso limita la API a menos de 100 visitas por segundo. La sección 9 explica cómo calibrar un perfil propio.

### 5.1 `corregida`

```powershell
.\taller.ps1 ejecutar -Perfil ci -Variante corregida
```

```sh
./taller.sh ejecutar --perfil ci --variante corregida
```

La ejecución dura unos 4 minutos. Mientras corre, el panel de Grafana muestra unas 150 respuestas por segundo, una o dos solicitudes en curso y la CPU de la API en torno a un cuarto de núcleo. Al final aparece el veredicto:

```text
### ✅ Aprobado
```

### 5.2 `regresion`

```powershell
.\taller.ps1 ejecutar -Perfil ci -Variante regresion
```

```sh
./taller.sh ejecutar --perfil ci --variante regresion
```

Esta tarda más, unos 6 minutos, porque al terminar la inyección todavía quedan solicitudes en la fila. En Grafana, las solicitudes en curso suben a 7 y se quedan ahí: son los 8 hilos de la API menos el que atiende a Prometheus mientras lee la métrica. De esos 7, uno tiene el candado y 6 lo esperan. Las respuestas bajan a unas 85 por segundo y la CPU queda en un quinto de núcleo, menos que con `corregida`: la API no está ocupada calculando, está esperando. El veredicto:

```text
### ❌ Rechazado por rendimiento
```

| Variante | p50 | p95 | Errores | Veredicto |
|---|---:|---:|---:|---|
| `corregida` | 9 ms | 10 ms | 0 % | Aprobado |
| `regresion` | 29,1 s | 60 s | 32,7 % | Rechazado por rendimiento |

*Resultados de referencia en la computadora de desarrollo, con el perfil `ci`. Los milisegundos de otra computadora serán distintos; lo que debe repetirse es el veredicto. El p95 de `regresion` es exactamente 60 s porque más del 5 % de sus solicitudes llegó al límite de espera de Gatling.*

Las dos variantes devolvieron los mismos productos y contaron bien las visitas. Lo único que cambió es cuánto esperó cada cliente.

## 6. Leer los resultados

Cada ejecución deja una carpeta `resultados/<fecha UTC>-<tipo>-<variante>/`:

| Archivo | Contenido |
|---|---|
| `resumen.md` | Veredicto y motivo, percentiles, errores, tasa lograda y valor actual de cada aserción |
| `veredicto.json` | El veredicto, para leerlo desde un programa |
| `metricas.json` | Conteos, tasa lograda, *throughput* y percentiles de cada fase |
| `gatling/cargasimulation-*/index.html` | Informe HTML de Gatling |
| `fases.json` | Inicio y fin UTC del calentamiento y de la medición |
| `ejecucion.env` · `perfil.env` | Parámetros usados, revisión del código y equipo |
| `gatling.log` · `servicios.log` | Salida de Gatling y registros de la API y PostgreSQL |

`ejecutar` termina con un código que distingue tres resultados:

| Código | Resultado | Significado |
|---:|---|---|
| 0 | Aprobado | La medición cumple todas las aserciones |
| 1 | Rechazado por rendimiento | La medición incumple el p95 o el límite de errores |
| 2 | Inválido | La medición no se puede interpretar: la API no estaba sana, el generador no sostuvo la tasa, la configuración no era la pedida o faltan datos. No dice nada de la variante |

Estrés y picos no aprueban ni rechazan: su resultado es informativo y terminan con 0, o con 2 si la medición es inválida (sección 8).

### Informe de Gatling

En el informe, las solicitudes se llaman `calentamiento` y `medicion`, según la fase, y lo que cuenta es la página de `medicion`. Las estadísticas globales mezclan las dos fases, y las aserciones solo miran la medición. Conviene fijarse en tres cosas:

- **La tabla de percentiles.** En `corregida`, p50 y p95 están cerca. En `regresion`, el p50 ya está en decenas de segundos: no son unas pocas solicitudes lentas, es toda la fila.
- **El gráfico de tiempo de respuesta a lo largo de la ejecución.** En `regresion` crece sin parar, porque llegan más solicitudes de las que la API puede atender.
- **Los errores.** Los de `regresion` no son respuestas de error de la API, sino esperas agotadas. La mayoría son conexiones que la API no llegó a aceptar en 10 s, porque todos sus hilos estaban ocupados; otras son solicitudes que pasaron 60 s en la fila sin respuesta, y unas pocas, conexiones cerradas antes de responder.

### Grafana

En el panel «API del taller», el intervalo de tiempo se ajusta a las horas de `fases.json` (Grafana muestra la hora local; `fases.json`, UTC).

| Panel | `corregida` | `regresion` |
|---|---|---|
| Respuestas por segundo | Unas 150: todas las que llegan | Unas 85: el límite del candado |
| Solicitudes en curso | 1 o 2 | 7, todos los hilos disponibles |
| Espera del candado | En cero: no hay candado | 6 hilos esperando |
| CPU de la API | Un cuarto de núcleo | Un quinto: la API espera, no calcula |

Las solicitudes en curso se interpretan con la ley de Little: en promedio, en el sistema hay tantas solicitudes como la tasa de llegada por el tiempo de respuesta medio. Con 150 por segundo y unos 7 ms dentro de la API, es 1. Con `regresion`, el número se queda en 7 porque no hay más hilos: la fila que sigue creciendo está afuera, en las conexiones que esperan un hilo libre, y esa espera solo la ve Gatling.

Gatling mide desde afuera y decide el veredicto; Grafana muestra por qué. Los tiempos de uno y otro no coinciden, porque Gatling incluye la espera en la fila y la red, y el histograma de la API mide desde que un hilo toma la solicitud.

## 7. Repetir

`ejecutar` restablece los datos y los contadores antes de cada medición, así que se puede repetir sin volver a preparar. Las ejecuciones van de a una: dos mediciones a la vez compiten por la misma computadora y ninguna sirve.

Repetir es la forma de ver el ruido. El p95 de una misma variante cambia de una ejecución a otra; lo que importa es que la distancia entre las variantes sea mucho mayor que esa variación.

## 8. Estrés y picos

La prueba de carga responde si la API cumple a una tasa fija. Las otras dos preguntan otra cosa, y su resultado es informativo: no aprueban ni rechazan.

**Estrés: ¿dónde empieza la degradación?** Cada nivel es una ejecución aparte, con el calentamiento y la medición del perfil, y dice si a esa tasa se cumple el criterio. `-Tasas` (o `--tasas`) corre un nivel por tasa y resume la serie en `resultados/campana-estres-<variante>-<fecha>.md`:

```powershell
.\taller.ps1 ejecutar -Tipo estres -Perfil piloto -Variante regresion -Tasas 50,75,100,150
```

```sh
./taller.sh ejecutar --tipo estres --perfil piloto --variante regresion --tasas 50,75,100,150
```

Con el perfil `piloto`, cada nivel dura menos de 2 minutos. En la computadora de desarrollo, `regresion` cumple a 75 por segundo, con un p95 de 15 ms, y a 100 ya no: el p95 sube a 14,6 s y las respuestas correctas se quedan en unas 80 por segundo, el límite del candado. La columna «Correctas/s» del resumen muestra ese techo.

**Picos: ¿cómo responde a una ráfaga y cuánto tarda en recuperarse?** La carga sube de golpe de la tasa del perfil a la del pico, la mantiene `-DuracionPico` segundos (30 si no se indica) y vuelve a la base. La base dura lo que el calentamiento del perfil, y la vuelta, lo que la medición: esa es la ventana en la que se espera la recuperación.

```powershell
.\taller.ps1 ejecutar -Tipo picos -Perfil local -Variante regresion -Tasa 50 -Pico 150
```

```sh
./taller.sh ejecutar --tipo picos --perfil local --variante regresion --tasa 50 --pico 150
```

El resumen da el p95 de la base, del pico y de la ventana, y dice si la API se recuperó y cuándo. La simulación agrupa las solicitudes en bloques de 5 s y considera recuperada la API desde el bloque a partir del cual todos cumplen el criterio del perfil hasta el final de la ventana. La serie de bloques está en `fases.json`, y el gráfico de tiempos del informe de Gatling muestra la misma curva. Con `regresion`, a 50 por segundo la API va holgada, pero durante el pico la fila crece: el p95 sube unos 3,7 s cada 5 s, y al volver a la base baja unos 2 s cada 5 s. Con la ventana de 60 s del perfil `piloto` no alcanza a recuperarse; con la de 180 s del perfil `local`, se recupera 55 s después del pico. `corregida` atraviesa un pico de 150 a 300 por segundo sin cambiar su p95.

La tasa del pico no debe pasar de lo que sostiene el generador, unas 350 por segundo: si no la sostiene, la ejecución es inválida.

## 9. Calibrar un perfil propio

El perfil `ci` se calibró en el *runner* de GitHub Actions. Para tener uno de la propia computadora se sigue el procedimiento de [`Taller.md`](../Taller.md) §7.1. Antes de medir se decide cuántas repeticiones se harán y qué margen mínimo se exigirá; aquí, 3 repeticiones por variante y un umbral al menos 3 veces lejos de cada variante.

1. **Comprobar el generador.** Gatling debe sostener la tasa antes de culpar a la API. Contra `/salud`, que no usa la base de datos, debe aprobar sin errores:

   ```powershell
   .\taller.ps1 ejecutar -Perfil piloto -Ruta salud -Tasa 150
   ```

   Por encima de unas 350 solicitudes por segundo, Gatling se queda sin puertos (`Cannot assign requested address`) y la medición no vale.

2. **Explorar.** Con una serie de estrés y el perfil `piloto`, de 20 s de calentamiento y 60 s de medición, se busca la tasa en la que `regresion` deja de cumplir (sección 8). Una ejecución por tasa basta:

   ```powershell
   .\taller.ps1 ejecutar -Tipo estres -Perfil piloto -Variante regresion -Tasas 50,75,100,150
   .\taller.ps1 ejecutar -Tipo estres -Perfil piloto -Variante corregida -Tasas 150,300
   ```

3. **Elegir la tasa.** Bien por encima del punto donde `regresion` colapsa y con `corregida` todavía holgada. En la computadora de desarrollo y en el *runner*, `regresion` colapsó entre 75 y 100, y se eligió 150.

4. **Repetir.** Tres ejecuciones por variante con las duraciones completas, alternando el orden (`corregida`, `regresion`, `regresion`, `corregida`, `corregida`, `regresion`). El p95 de cada una aparece en su `resumen.md`, apruebe o no:

   ```powershell
   .\taller.ps1 ejecutar -Perfil local -Variante corregida -Tasa 150
   ```

   `campana` reúne las seis ejecuciones en `resultados/campana-<nombre>.md`: todas en orden, incluidas las inválidas y su motivo, y por variante el rango, la mediana y el coeficiente de variación del p95. Recibe los nombres de las carpetas de `resultados/`:

   ```powershell
   .\taller.ps1 campana -Nombre calibracion-local 20261110T043246Z-carga-corregida 20261110T043705Z-carga-regresion ...
   ```

   ```sh
   ./taller.sh campana --nombre calibracion-local 20261110T043246Z-carga-corregida 20261110T043705Z-carga-regresion ...
   ```

   Las ejecuciones inválidas no cuentan para los rangos. Si hay alguna, se repite hasta tener tres válidas por variante.

5. **Elegir el umbral.** Debe quedar al menos 3 veces por encima del peor p95 de `corregida` y 3 veces por debajo del mejor de `regresion`. El resumen de la campaña ya calcula ese intervalo. Si no cabe, la calibración no es satisfactoria: hay que revisar la tasa o el entorno, no estirar el margen.

6. **Escribir el perfil** en `config/perfiles/local.env` con la tasa y el umbral elegidos.

7. **Validar.** Una campaña nueva de 3 ejecuciones por variante con el perfil ya escrito: todas las de `corregida` deben aprobar y todas las de `regresion` deben ser rechazadas. La columna «Veredictos esperados» del resumen de `campana` lo indica. Si alguna no lo hace, se vuelve a calibrar; el umbral no se ajusta con los datos de la validación, porque así cualquier umbral parecería funcionar.

Cada ejecución completa dura entre 4 y 6 minutos, así que la calibración y la validación llevan cerca de una hora entre las dos. Un perfil calibrado sirve para esa computadora: en otra, el procedimiento se repite.

## 10. La compuerta en GitHub Actions

En el repositorio, el workflow `Compuerta` (`.github/workflows/compuerta.yml`) corre en cada *push* y en cada *pull request* que toca `Taller/`. Prepara el entorno en una máquina nueva de GitHub, ejecuta las pruebas funcionales y la prueba de carga con el perfil `ci`, y falla si la variante es rechazada o si no se pudo medir. El *pull request* queda marcado en rojo o en verde, y el informe se guarda como artefacto de la ejecución.

La variante que mide la compuerta es la de `config/variante.env`. En `main` es siempre `corregida`; un cambio que la pasa a `regresion` simula un cambio de código defectuoso.

Los dos *pull requests* de demostración del repositorio muestran el resultado:

| *Pull request* | Cambio | Compuerta |
|---|---|---|
| [#6](https://github.com/AleeBonilla/pruebas-automatizadas-rendimiento/pull/6) | `corregida` → `regresion` | ❌ p95 de 46,3 s y 13,4 % de errores |
| [#7](https://github.com/AleeBonilla/pruebas-automatizadas-rendimiento/pull/7) | `regresion` → `corregida` | ✅ p95 de 9 ms y sin errores |

Para reproducirlos en una cuenta propia:

1. Hacer un *fork* del repositorio en GitHub y, en la pestaña *Actions* del *fork*, habilitar los workflows.
2. Clonar el *fork*, crear una rama y cambiar la variante:

   ```sh
   git switch -c demo/regresion
   ```

   En `Taller/config/variante.env`, cambiar `VARIANTE=corregida` por `VARIANTE=regresion`, y luego:

   ```sh
   git commit -am "Activar la variante regresion"
   git push -u origin demo/regresion
   ```

3. Abrir el *pull request* hacia el `main` del propio *fork*, no hacia el repositorio original. En la página de GitHub se elige el *fork* como repositorio base; con la CLI de GitHub:

   ```sh
   gh pr create --repo <usuario>/pruebas-automatizadas-rendimiento --base main --head demo/regresion --fill
   ```

4. Esperar unos 7 minutos. La comprobación «Compuerta de rendimiento» falla, y el resumen de la ejecución en *Actions* muestra el veredicto y las aserciones. El informe completo está en el artefacto `resultados-<id>`.
5. Para la corrección, crear `demo/corregida` desde `demo/regresion`, volver a `VARIANTE=corregida` y abrir un *pull request* hacia `demo/regresion`, de modo que su cambio sea la corrección. La compuerta aprueba.

Estos *pull requests* no se integran: existen para mostrar la compuerta. Y el perfil `ci` está calibrado para las máquinas de GitHub, que no son las de la computadora local, así que sus milisegundos no se comparan con los de la sección 5.

## 11. Detener

```powershell
.\taller.ps1 detener                # detiene los servicios y conserva los datos
.\taller.ps1 detener -BorrarDatos   # además borra la base de datos
```

```sh
./taller.sh detener
./taller.sh detener --borrar-datos
```

Los resultados de `resultados/` se conservan en ambos casos. Para guardar o enviar una ejecución, `exportar` la empaqueta en un `.tar.gz` (la última, o la que se indique con `-Ejecucion` o `--ejecucion`).

## 12. Problemas frecuentes

| Síntoma | Causa y solución |
|---|---|
| PowerShell no ejecuta `taller.ps1` | La política de ejecución lo impide: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` |
| `preparar` falla con `Requested CPUs are not available` | Docker tiene menos de 4 núcleos disponibles. Aumentarlos en la configuración de Docker Desktop o usar una computadora con más núcleos |
| Un servicio no arranca porque el puerto está en uso | Otro programa ocupa el 8000, el 3000 o el 9090. Cerrarlo antes de preparar |
| Resultado 2 (inválido) | El motivo está en `resumen.md`. Si es de preparación, basta con volver a `preparar`; si el generador no sostuvo la tasa, cerrar otros programas o bajar la tasa |
| `Cannot assign requested address` en `gatling.log` | La tasa supera lo que el generador sostiene, unas 350 por segundo. La ejecución no sirve: bajar la tasa |
| `corregida` rechazada | La computadora estaba ocupada, o el perfil no corresponde a este entorno. Repetir con la computadora libre y, si se mantiene, calibrar un perfil propio (sección 9) |
| Grafana no muestra datos | El intervalo de tiempo no cubre la ejecución. Ajustarlo con las horas de `fases.json` |
