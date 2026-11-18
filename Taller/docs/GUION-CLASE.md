# Guion para presentar el taller

Duración sugerida: 15–20 minutos, con las imágenes preparadas antes de clase.
Los comandos son para PowerShell, desde la carpeta `Taller`.

## Antes de clase

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\taller.ps1 preparar
docker compose ps
```

Preparar descarga y construye las imágenes, levanta los servicios y restablece
los datos. Hacerlo antes evita consumir la exposición descargando dependencias.
Guardar también informes de una ejecución previa de cada variante.

## 1. Objetivo y arquitectura — 2 minutos

Decir: «Vamos a demostrar que una aplicación puede funcionar correctamente y
aun así introducir una regresión de rendimiento. Compararemos dos implementaciones
de la misma operación, con iguales datos, recursos y carga».

```powershell
Invoke-RestMethod http://localhost:8000/salud
Invoke-RestMethod http://localhost:8000/productos/1
Start-Process http://localhost:3000
Start-Process http://localhost:9090/targets
```

Explicar: Gatling genera solicitudes; Flask/Gunicorn atiende; PostgreSQL guarda
productos y visitas; Prometheus recoge métricas; Grafana las visualiza.
Cada consulta al producto incrementa sus visitas, por contrato didáctico.

## 2. Mostrar el cambio que causa la regresión — 2 minutos

Abrir `api/tienda/variantes.py` y comparar `visitar_regresion` y
`visitar_corregida`.

Decir: «La regresión usa un candado global. Una solicitud conserva el candado
mientras consulta y actualiza PostgreSQL; las demás esperan incluso cuando
consultan productos distintos. La corregida utiliza un UPDATE atómico: la base
coordina las actualizaciones de cada fila, sin serializar todos los productos».

No proponer simplemente quitar el candado al algoritmo de leer, sumar y escribir:
eso permitiría perder incrementos concurrentes. Se comparan las implementaciones
completas; también cambia el número de consultas SQL.

## 3. Demostrar corrección funcional — 1–2 minutos

```powershell
.\taller.ps1 funcionales
```

Decir: «Estas pruebas comprueban contrato, transacciones y exactitud del contador
con concurrencia. Ambas implementaciones deben aprobar: el problema que buscamos
es cuánto esperan los clientes bajo carga».

Esperar a que terminen antes de generar carga: las pruebas restablecen la base.

## 4. Definir el experimento — 1 minuto

Para una demostración corta se usa `piloto` con tasa y umbral explícitos:

| Parámetro | Valor de la demostración |
|---|---:|
| Llegadas | 150 solicitudes/s |
| Calentamiento | 20 s |
| Medición | 60 s |
| p95 exigido | menor de 3000 ms |
| Errores permitidos | como máximo 1 % |

Decir: «Es un modelo abierto: las llegadas no esperan a que termine la solicitud
anterior. El p95 es el tiempo que no supera el 95 % de las solicitudes. Las
aserciones se calculan solo sobre la medición».

La versión de carga espera a que terminen las solicitudes del calentamiento
antes de iniciar la medición. Bajo saturación puede existir una pausa entre
ambas fases; no presentar esta prueba como una llegada continua entre fases.

Estos ajustes son para exposición, no una nueva calibración de los perfiles.

## 5. Ejecutar corregida — aproximadamente 90 segundos

```powershell
.\taller.ps1 ejecutar -Tipo carga -Perfil piloto -Variante corregida -Tasa 150 -Umbral 3000
$codigoCorregida = $LASTEXITCODE
$idCorregida = (Get-ChildItem .\resultados -Directory -Filter '*-carga-corregida' |
    Sort-Object Name | Select-Object -Last 1).Name
Get-Content ".\resultados\$idCorregida\resumen.md"
```

Mientras corre, mostrar Grafana con actualización automática y los últimos
5–15 minutos. Observar respuestas por segundo, solicitudes en curso y recolección.

Esperado: tasa generada cercana a 150/s, p95 bajo, pocos o ningún error y
veredicto aprobado. Usar los valores obtenidos; no prometer milisegundos exactos.

## 6. Ejecutar regresion — puede tardar varios minutos

```powershell
.\taller.ps1 ejecutar -Tipo carga -Perfil piloto -Variante regresion -Tasa 150 -Umbral 3000
$codigoRegresion = $LASTEXITCODE
$idRegresion = (Get-ChildItem .\resultados -Directory -Filter '*-carga-regresion' |
    Sort-Object Name | Select-Object -Last 1).Name
Get-Content ".\resultados\$idRegresion\resumen.md"
```

Decir: «La tasa ofrecida es la misma, pero el servidor procesa más lentamente.
La cola crece y aparecen latencias altas y posiblemente tiempos de espera
agotados. El candado puede causar saturación sin una CPU al 100 %: los hilos
están esperando».

Esperado: rechazo por rendimiento. Puede continuar después de acabar la
inyección, porque quedan solicitudes pendientes. No lanzar otra prueba a la vez.
Si Grafana deja de mostrar datos, mirar la recolección: `/metrics` comparte los
hilos del servidor y también puede quedar esperando. Un hueco no significa
cero solicitudes ni cero latencia.

## 7. Leer y comparar la evidencia — 2 minutos

```powershell
.\taller.ps1 campana -Nombre demostracion-clase $idCorregida $idRegresion
Get-Content .\resultados\campana-demostracion-clase.md

$informe = Get-ChildItem ".\resultados\$idRegresion\gatling" -Recurse -Filter index.html |
    Select-Object -First 1
Invoke-Item $informe.FullName
```

En Gatling abrir la solicitud `medicion`. Mostrar p95, errores y evolución del
tiempo de respuesta. Distinguir tasa generada de respuestas correctas por segundo:
el generador puede sostener 150/s aunque la API no las termine a ese ritmo.

| Código | Interpretación |
|---:|---|
| 0 | Cumple el criterio de carga |
| 1 | La medición es válida y falla el criterio de rendimiento |
| 2 | La medición es inválida: no permite juzgar la variante |

Un resultado inválido se investiga o se repite; no se presenta como una regresión
detectada. `campana` resume las ejecuciones, pero dos pruebas no constituyen una
calibración ni una validación formal.

## 8. Explicar automatización en CI — 1 minuto

Mostrar `.github/workflows/compuerta.yml` y `config/variante.env`.

Decir: «En CI ejecutamos pruebas funcionales y de rendimiento. Un cambio que
conserve la función pero empeore la latencia puede dejar el job en rojo. Esto
automatiza la detección antes de integrar el cambio. Para exigirlo al fusionar,
el repositorio debe configurar ese check como obligatorio».

Para presentar el perfil completo utilizado en CI, en lugar de la demostración
corta, ejecutar por separado:

```powershell
.\taller.ps1 ejecutar -Perfil ci -Variante corregida
.\taller.ps1 ejecutar -Perfil ci -Variante regresion
```

Este perfil usa 150/s, calentamiento de 60 s, medición de 180 s y p95 menor de
3000 ms. Reservar aproximadamente 10–12 minutos para ambas, con margen según
el equipo. El perfil local usa la misma carga y duraciones con umbral de 1000 ms.

## 9. Cierre

Decir: «La corrección funcional y el rendimiento son criterios distintos.
Gatling cuantifica la experiencia del cliente, Grafana ayuda a explicar la
causa y CI convierte el criterio en una comprobación repetible».

```powershell
.\taller.ps1 exportar -Ejecucion $idRegresion
.\taller.ps1 detener
```

## Preguntas previsibles

- **¿Por qué p95?** Expone la experiencia de las solicitudes lentas que el
  promedio puede ocultar. También se examinan errores y distribución.
- **¿Por qué no quitar solo el candado?** El incremento debe seguir siendo
  correcto con concurrencia; el UPDATE atómico evita actualizaciones perdidas.
- **¿Por qué misma carga y recursos?** Para comparar variantes bajo condiciones
  equivalentes. Los valores de este entorno no predicen capacidad de producción.
- **¿Qué aporta repetir?** Permite separar una diferencia persistente del ruido
  del equipo. Una demostración ilustra; una campaña aporta evidencia repetida.
- **¿Qué pasó con «no sostuvo la tasa»?** La instrumentación restaba horas UTC
  ajustables. Se observaron saltos del reloj del contenedor que inflaban el
  intervalo. Ahora las duraciones, bloques y tasa usan reloj monotónico y se
  registra el desajuste UTC. No se modificaron las tolerancias ni los umbrales.
