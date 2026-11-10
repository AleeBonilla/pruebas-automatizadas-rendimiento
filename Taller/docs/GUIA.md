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

El ritmo y el umbral salen de un perfil en `config/perfiles/`. El perfil `local` todavía tiene valores provisionales, demasiado bajos para separar las variantes, así que esta guía usa el perfil `ci`: 150 solicitudes por segundo, p95 menor que 3 000 ms y como máximo 1 % de errores. Esa tasa separa las variantes en cualquier computadora que cumpla los requisitos, porque el límite de `regresion` no depende del procesador: con el candado, cada visita retiene a las demás mientras espera a la base de datos, y eso limita la API a menos de 100 visitas por segundo. La sección 8 explica cómo calibrar un perfil propio.

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

Cada ejecución deja una carpeta `resultados/<fecha UTC>-carga-<variante>/`:

| Archivo | Contenido |
|---|---|
| `resumen.md` | Veredicto, motivo y valor actual de cada aserción |
| `veredicto.json` | Lo mismo, para leerlo desde un programa |
| `gatling/cargasimulation-*/index.html` | Informe HTML de Gatling |
| `fases.json` | Inicio y fin UTC del calentamiento y de la medición |
| `ejecucion.env` · `perfil.env` | Parámetros usados, revisión del código y equipo |
| `gatling.log` · `servicios.log` | Salida de Gatling y registros de la API y PostgreSQL |

`ejecutar` termina con un código que distingue tres resultados:

| Código | Resultado | Significado |
|---:|---|---|
| 0 | Aprobado | La medición cumple todas las aserciones |
| 1 | Rechazado por rendimiento | La medición incumple el p95 o el límite de errores |
| 2 | Error de infraestructura | No se pudo medir: la API no estaba sana, Gatling falló o falta el informe. No dice nada de la variante |

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

## 8. Calibrar un perfil propio

El perfil `ci` se calibró en el *runner* de GitHub Actions. Para tener uno de la propia computadora se sigue el procedimiento de [`Taller.md`](../Taller.md) §7.1. Antes de medir se decide cuántas repeticiones se harán y qué margen mínimo se exigirá; aquí, 3 repeticiones por variante y un umbral al menos 3 veces lejos de cada variante.

1. **Comprobar el generador.** Gatling debe sostener la tasa antes de culpar a la API. Contra `/salud`, que no usa la base de datos, debe aprobar sin errores:

   ```powershell
   .\taller.ps1 ejecutar -Perfil piloto -Ruta salud -Tasa 150
   ```

   Por encima de unas 350 solicitudes por segundo, Gatling se queda sin puertos (`Cannot assign requested address`) y la medición no vale.

2. **Explorar.** Con el perfil `piloto`, de 20 s de calentamiento y 60 s de medición, se busca la tasa en la que `regresion` deja de cumplir. Una ejecución por tasa basta:

   ```powershell
   foreach ($t in 50, 75, 100, 150) { .\taller.ps1 ejecutar -Perfil piloto -Variante regresion -Tasa $t }
   .\taller.ps1 ejecutar -Perfil piloto -Variante corregida -Tasa 300
   ```

3. **Elegir la tasa.** Bien por encima del punto donde `regresion` colapsa y con `corregida` todavía holgada. En la computadora de desarrollo y en el *runner*, `regresion` colapsó entre 75 y 100, y se eligió 150.

4. **Repetir.** Tres ejecuciones por variante con las duraciones completas, alternando el orden (`corregida`, `regresion`, `regresion`, `corregida`, `corregida`, `regresion`). El p95 de cada una aparece en su `resumen.md`, apruebe o no:

   ```powershell
   .\taller.ps1 ejecutar -Perfil local -Variante corregida -Tasa 150
   ```

5. **Elegir el umbral.** Debe quedar al menos 3 veces por encima del peor p95 de `corregida` y 3 veces por debajo del mejor de `regresion`. Si no cabe, la calibración no es satisfactoria: hay que revisar la tasa o el entorno, no estirar el margen.

6. **Escribir el perfil** en `config/perfiles/local.env` con la tasa y el umbral elegidos.

7. **Validar.** Una campaña nueva de 3 ejecuciones por variante con el perfil ya escrito: todas las de `corregida` deben aprobar y todas las de `regresion` deben ser rechazadas. Si alguna no lo hace, se vuelve a calibrar; el umbral no se ajusta con los datos de la validación, porque así cualquier umbral parecería funcionar.

Cada ejecución completa dura entre 4 y 6 minutos, así que la calibración y la validación llevan cerca de una hora entre las dos. Un perfil calibrado sirve para esa computadora: en otra, el procedimiento se repite.

## 9. La compuerta en GitHub Actions

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

## 10. Detener

```powershell
.\taller.ps1 detener                # detiene los servicios y conserva los datos
.\taller.ps1 detener -BorrarDatos   # además borra la base de datos
```

```sh
./taller.sh detener
./taller.sh detener --borrar-datos
```

Los resultados de `resultados/` se conservan en ambos casos. Para guardar o enviar una ejecución, `exportar` la empaqueta en un `.tar.gz` (la última, o la que se indique con `-Ejecucion` o `--ejecucion`).

## 11. Problemas frecuentes

| Síntoma | Causa y solución |
|---|---|
| PowerShell no ejecuta `taller.ps1` | La política de ejecución lo impide: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` |
| `preparar` falla con `Requested CPUs are not available` | Docker tiene menos de 4 núcleos disponibles. Aumentarlos en la configuración de Docker Desktop o usar una computadora con más núcleos |
| Un servicio no arranca porque el puerto está en uso | Otro programa ocupa el 8000, el 3000 o el 9090. Cerrarlo antes de preparar |
| Resultado 2 (error de infraestructura) | No se pudo medir. El motivo está en `resumen.md`; muchas veces basta con volver a `preparar` |
| `Cannot assign requested address` en `gatling.log` | La tasa supera lo que el generador sostiene, unas 350 por segundo. La ejecución no sirve: bajar la tasa |
| `corregida` rechazada | La computadora estaba ocupada, o el perfil no corresponde a este entorno. Repetir con la computadora libre y, si se mantiene, calibrar un perfil propio (sección 8) |
| Grafana no muestra datos | El intervalo de tiempo no cubre la ejecución. Ajustarlo con las horas de `fases.json` |
