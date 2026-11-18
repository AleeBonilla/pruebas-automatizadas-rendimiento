# Falsa pérdida de tasa por saltos UTC

El 13 de noviembre de 2026 se reprodujo el problema incluso contra `/salud`,
sin consultas SQL. En `resultados/diagnostico-carga/fases.json`, la instrumentación
anterior registró las 1200 solicitudes previstas pero una inyección de 62,960 s
para una fase de 60 s. Gatling informó p95 de 3 ms y cero errores.

Una sonda independiente dentro del contenedor midió 90,005 s monotónicos frente
a 94,478 s UTC, sin intervalos de ejecución superiores a 100 ms. Esto demuestra
ajustes del reloj UTC durante el experimento; no identifica el servicio concreto
del anfitrión o de WSL responsable de ajustarlo.

`Fases` calculaba inyección, duración y bloques con `System.currentTimeMillis()`.
`metricas.py` calcula la tasa como `(iniciadas - 1) / inyeccion_s`, y `veredicto.py`
exige al menos el 98 % de la tasa prevista. Por eso un salto UTC positivo de
aproximadamente 1,5 s en una fase de 60 s provoca un falso resultado inválido,
independientemente de la variante. Un salto negativo también podía sobreestimar
la tasa y distorsionar bloques y latencias.

La corrección usa `System.nanoTime()` para el tiempo transcurrido y proyecta
las marcas UTC desde un ancla común. `desajuste_reloj_ms` registra la diferencia
entre el UTC real al finalizar y esa proyección. Las marcas proyectadas sirven
como referencia; los saltos UTC pueden desalinearlas de fuentes externas como
Prometheus. No se han relajado las reglas de validez.

Validación confirmada: `20261113T084416Z-carga-corregida`, perfil piloto original,
1200 solicitudes de medición en 59,951 s de inyección, tasa de aproximadamente
20/s, p95 de 13 ms, cero errores y veredicto aprobado. El desajuste UTC fue de
4819 ms durante esa misma ejecución. Las 36 pruebas de herramientas aprobaron,
y la construcción de Gatling ejecuta una regresión determinista con saltos UTC
positivos y negativos, que comprueba duración, bloques y desajuste.

La sonda se puede repetir desde PowerShell:

```powershell
Get-Content herramientas/diagnostico_reloj.py | docker compose exec -T api python -
```

La corrección elimina el error de instrumentación para las simulaciones que
comparten `Fases`; no elimina la saturación deliberada del candado en `regresion`.
Los informes antiguos se conservan: no se reinterpretan como mediciones nuevas.
