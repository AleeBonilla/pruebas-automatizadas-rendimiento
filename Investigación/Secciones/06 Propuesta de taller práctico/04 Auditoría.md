# Auditoría — 06 Propuesta de taller práctico

## Ronda 7 — 2026-11-16 — Borrador v7 · Evidencia v2

**Veredicto:** Aprobada | **Citas revisadas:** ninguna nueva; se conserva el cotejo de E1–E4 de la ronda 2 | **Plan:** v2, aprobado, modo ligero

Se revisaron los dos hallazgos de la ronda 6, las filas modificadas de la Tabla 6 y la adecuación del plan a esa tabla. Se cotejaron con `Taller/Taller.md` §6.3, §7 y §8 y con `Taller/api/pruebas/`, incluido `conftest.py`. La evidencia permanece en v2 y se conserva la revisión de las citas y del contenido no modificado. La rúbrica del curso pide valores mínimo, medio y máximo; la tabla conserva esos rótulos y define el conjunto de cada fila. No se encontraron hallazgos bloqueantes ni sugerencias nuevos en los cambios revisados.

**Seguimiento de la ronda 6:**

| Hallazgo anterior | Estado | Comprobación |
|---|---|---|
| 1. Tasa de llegada | Resuelto | La fila se limita ahora a las cargas de validación, el estrés y los picos de la Tabla 7. En ese conjunto, 50 y 300 solicitudes por segundo son los extremos y 150 es un valor intermedio; la comprobación del generador a 500 y el piloto a 350 quedan fuera de la delimitación. `Taller.md` §6.3, §7 y §8 respalda los valores de las pruebas incluidas. La nota aclara que no son límites del sistema. |
| 2. Solicitudes por caso de pytest | Resuelto | La fila comprende solo los casos que hacen solicitudes HTTP, por lo que excluye `test_datos_semilla`, que consulta la base directamente. Las pruebas de contrato incluyen casos con una solicitud; `test_reversion.py` programa 64, 32 con fallo provocado, y `test_concurrencia.py` programa 400. El ejecutor usa hasta 16 hilos en esos casos; 64 y 400 son totales por caso, no solicitudes simultáneas. |

**Plan:** La descripción de T6 en el plan v2 ahora corresponde a la tabla de valores por parámetro y a los extremos de cada conjunto delimitado; ya no describe la columna de fuera de rango retirada en v6. La tabla conserva los identificadores inexistentes y su resultado esperado. El cotejo se basa en el código y los registros disponibles; no se ejecutaron nuevamente las pruebas ni se descargaron los resultados originales.

**Extensión:**

| Bloque | Plan | Borrador v7 |
|---|---|---|
| B1. 6.1 | 230; margen 207–253 | 233; cumple. |
| B2. 6.2 | 150; margen 135–165 | 159; cumple. |
| B3. 6.3 | 150; margen 135–165 | 157; cumple. |
| B4. 6.4 | 300; margen 270–330 | 316; cumple. |
| B5. 6.5 | 200; margen 180–220 | 216; cumple. |
| B6. 6.6 | 200; margen 180–220 | 218; cumple. |
| B7. 6.7 | 120; margen 108–132 | 113; cumple. |
| Total de prosa | 1 350; margen 1 215–1 485 | 1 412; cumple. |
| Tablas 4–7 y figuras 4–5 | 2,7 páginas en conjunto | Ocupación pendiente de maquetación. |
| Anexo C, incluida Figura 6 | 1,5 páginas | Sin cambios; ocupación pendiente de maquetación. |

Se conserva el conteo de la ronda 6 porque los cambios de v7 están dentro de la tabla. A 350 palabras por página, la prosa ocupa unas 4,03 páginas; con las 2,7 asignadas a tablas y figuras, la previsión es de 6,73 páginas frente a seis. Es una estimación pendiente de maquetación; el plan prevé recortar la Figura 5 si hace falta.

## Ronda 6 — 2026-11-16 — Borrador v6 · Evidencia v2

**Veredicto:** No aprobada | **Citas revisadas:** ninguna nueva; se conserva el cotejo de E1–E4 de la ronda 2 | **Plan:** v2, aprobado, modo ligero

Se revisaron los cuatro hallazgos de la ronda 5 y los cambios de v6 en la Tabla 6, su presentación en 6.4 y la última oración de la nota de la Tabla 7. Se cotejaron con `Taller/Taller.md` §6.3, §7 y §8, los tres perfiles de ejecución, `Taller/base-datos/productos.csv` y las pruebas de `Taller/api/pruebas/`. La evidencia sigue en v2 y las citas aprobadas no cambiaron. La rúbrica del curso, criterio «Valores de prueba», pide valores mínimo, medio y máximo; por ello se conservan esos rótulos en las correcciones propuestas. La nueva nota define los extremos como valores usados por las pruebas de cada fila, pero dos filas aún no delimitan conjuntos que los sostengan.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante | Tabla 6, tasa de llegada y nota | 4. Respaldo | La fila comprende los niveles medidos de carga, estrés y picos y la nota define el máximo como el valor más alto usado en las pruebas de la fila. Sin embargo, la propia Tabla 7 informa la comprobación del generador mediante carga a 500 solicitudes por segundo; `Taller.md` §7.1 también registra un piloto a 350. Esas pruebas impiden presentar 300 como máximo de toda la carga medida sin otra delimitación. Que 500 fuera una ejecución inválida no lo excluye de «niveles medidos». | Conservar los rótulos y acotar la fila a un conjunto explícito que incluya 50, 150 y 300 y excluya la comprobación del generador y otros pilotos, por ejemplo los niveles de carga de validación, estrés y picos informados en las filas correspondientes de la Tabla 7. Mantener 500 como observación de la comprobación del generador en esa tabla, sin presentarlo como límite del sistema. |
| 2 | Bloqueante | Tabla 6, solicitudes HTTP por caso de pytest y nota | 4. Respaldo | La fila sigue abarcando los casos de pytest, pero `test_datos_semilla` consulta la base directamente y no hace solicitudes HTTP: el mínimo de ese conjunto es 0, no 1. Los 64 y 400 son totales por caso, con hasta 16 hilos, como indica correctamente la tabla. | Acotar la fila a «casos de pytest que hacen solicitudes HTTP» para que 1 sea el mínimo de ese conjunto; alternativamente, incluir 0 como mínimo y ajustar los demás valores. Conservar mínimo, medio y máximo. |

**Seguimiento de la ronda 5:**

| Hallazgo anterior | Estado | Comprobación |
|---|---|---|
| 1. Tasa y fuera de rango | Parcial | Se quitó la columna «Fuera de rango» y 6.4 ya no presenta 500 como límite. La definición de extremos sigue siendo demasiado amplia para el máximo de la fila de tasa (hallazgo 1). |
| 2. Solicitudes por caso | No resuelto | La fila conserva el alcance de los casos de pytest y el mínimo de 1, aunque hay un caso sin solicitudes HTTP (hallazgo 2). Las cantidades y la distinción entre total y concurrencia coinciden con el código. |
| 3. Duración de fase | Resuelto | La fila limita las duraciones a las mediciones informadas y especifica el pico de 10 s de `corregida` y las fases de 60 y 180 s de `ci` y `local`. La Tabla 7 informa además el pico de 30 s; dentro de las fases identificadas en 6.6, 10 y 180 son los extremos. Los perfiles confirman 60 y 180 s, y `Taller.md` §6.3, el pico de 10 s. No se afirman límites generales para fases configurables. |
| 4. Nota de la Tabla 7 | Resuelto | La nueva oración identifica 60 s como límite de espera y señala que no permite conocer cuánto habrían tardado las solicitudes afectadas; ya no afirma que el p95 real fuera mayor. |

**Constancias del cotejo:** El CSV contiene 10 000 identificadores del 1 al 10 000, incluido 4182; la prueba de contrato consulta 4182 y comprueba los cinco identificadores inexistentes enumerados en la nota. Los umbrales de 300, 1 000 y 3 000 ms y el máximo de 1 % de errores coinciden con los perfiles. La nota de la Tabla 7 conserva los resultados por campaña verificados en la ronda anterior. La eliminación de la columna de fuera de rango no elimina los casos de identificadores inexistentes: figuran en la Tabla 6 y en su nota. El plan aún describe esa columna; la adecuación del plan a la nueva presentación queda como cuestión editorial, sin afectar el respaldo de los casos. Se conserva la revisión anterior de lo no modificado. El cotejo se basa en los registros y el código disponibles, sin ejecutar nuevamente las pruebas ni descargar resultados originales.

**Extensión:**

| Bloque | Plan | Borrador v6 |
|---|---|---|
| B1. 6.1 | 230; margen 207–253 | 233; cumple. |
| B2. 6.2 | 150; margen 135–165 | 159; cumple. |
| B3. 6.3 | 150; margen 135–165 | 157; cumple. |
| B4. 6.4 | 300; margen 270–330 | 316; cumple. |
| B5. 6.5 | 200; margen 180–220 | 216; cumple. |
| B6. 6.6 | 200; margen 180–220 | 218; cumple. |
| B7. 6.7 | 120; margen 108–132 | 113; cumple. |
| Total de prosa | 1 350; margen 1 215–1 485 | 1 412; cumple. |
| Tablas 4–7 y figuras 4–5 | 2,7 páginas en conjunto | Ocupación pendiente de maquetación. |
| Anexo C, incluida Figura 6 | 1,5 páginas | Sin cambios; ocupación pendiente de maquetación. |

Se cuentan unidades separadas por espacios, sin encabezados, comentarios HTML, tablas, títulos ni notas, y sin el anexo. A 350 palabras por página, la prosa ocupa unas 4,03 páginas; con las 2,7 asignadas a tablas y figuras, la previsión es de 6,73 páginas frente a seis. Es una estimación pendiente de maquetación; el plan prevé recortar la Figura 5 si hace falta.


## Ronda 5 — 2026-11-16 — Borrador v5 · Evidencia v2

**Veredicto:** No aprobada | **Citas revisadas:** ninguna nueva; se conserva el cotejo de E1–E4 de la ronda 2 | **Plan:** v2, aprobado, modo ligero

Se revisaron los tres hallazgos de la ronda 4 y los cambios declarados en v5: las filas de tasa, solicitudes y duración de la Tabla 6 y la nota de la Tabla 7. Se cotejaron con `Taller/Taller.md` §6.3, §7 y §8, los tres perfiles y las pruebas de `Taller/api/pruebas/`, incluido `conftest.py`. La evidencia permanece en v2 y los usos de las citas no cambiaron. Persisten afirmaciones de extremos sin respaldo y la nota de la Tabla 7 afirma más de lo que permite el límite de espera.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante | Tabla 6, tasa y columna «Fuera de rango y efecto» | 4. Respaldo | La fila dice «en carga, estrés y picos», pero conserva «Mínimo» en 50 sin definir un conjunto de ejecuciones que lo justifique: `piloto.env` fija `TASA=20` para explorar. La nota reconoce tasas menores sin excluirlas de la fila. Ubicar 500 «fuera de rango» sigue sugiriendo un límite general, aunque §7.1 documenta el agotamiento de puertos en ese piloto. | Rotular 50, 150 y 300 como ejemplos seleccionados y presentar 500 en una nota como resultado de ese piloto, sin convertirlo en un límite admitido. Ajustar también la oración introductoria sobre «fuera de rango». |
| 2 | Bloqueante | Tabla 6, solicitudes por caso de pytest | 4. Respaldo | La descripción de 64 y 400 distingue correctamente el total de los 16 hilos, pero «Mínimo: 1» no abarca todos los casos de pytest: `test_datos_semilla` consulta la base directamente y no hace solicitudes HTTP. | Presentar 1, 64 y 400 como ejemplos de casos que hacen solicitudes HTTP, sin atribuirles extremos de toda la suite; o definir el conjunto y reflejar que también hay casos sin solicitudes HTTP. |
| 3 | Bloqueante | Tabla 6, duración de una fase | 4. Respaldo | Los 10, 60 y 180 s corresponden a las fases indicadas, pero la fila y las cabeceras los presentan como extremos generales sin delimitar las mediciones. Las duraciones dependen del perfil y la duración del pico es configurable; las fuentes no establecen 10 y 180 s como límites generales. | Identificar las tres duraciones como ejemplos seleccionados y aclarar las fases y perfiles, o delimitar las ejecuciones comparadas y justificar sus extremos. |
| 4 | Bloqueante | Tabla 7, última oración de la nota | 4. Respaldo | La nota conserva «Un p95 de 60 s es el límite de espera de Gatling: el tiempo real fue mayor». El límite recorta la observación de solicitudes afectadas; por sí solo no permite conocer su tiempo real ni afirmar que el p95 real de la distribución fuera mayor. | Sustituir por «Un p95 de 60 s alcanza el límite de espera de Gatling; la medición no permite conocer cuánto habrían tardado en completarse las solicitudes afectadas». |

**Seguimiento de la ronda 4:**

| Hallazgo anterior | Estado | Comprobación |
|---|---|---|
| 1. Tasa y encabezados | No resuelto | Cambió la denominación de la fila y se precisó el piloto a 500, pero permanecen las cabeceras de extremos y «fuera de rango» sin un conjunto que sostenga su interpretación (hallazgo 1). |
| 2. Solicitudes y concurrencia | Resuelto en concurrencia; queda otro problema de respaldo | `test_reversion.py` programa 64 rutas, 32 con fallo; `test_concurrencia.py`, 400. `conftest.py` usa por defecto 16 hilos y el ejecutor limita a 16 los hilos de esos casos. La nueva redacción distingue total y simultaneidad, pero el mínimo de toda la suite no es 1 (hallazgo 2). |
| 3. Rangos por campaña | Resuelto | La nota reproduce los p95 de ambas variantes y los errores de `regresion` para `validacion-ci-1`, `validacion-ci-2` y `validacion-local`, conforme a §7.2. Los errores de `corregida` son 0 % en las tres campañas y ya constan en la fila. La última oración sobre el límite de espera requiere precisión (hallazgo 4). |

La observación adicional de la ronda 4 sobre las duraciones sigue pendiente (hallazgo 3). Los umbrales de 300, 1 000 y 3 000 ms y el máximo de errores de 1 % coinciden con los perfiles. Se conserva la revisión anterior de los bloques, tablas, figuras y anexo que no cambiaron. Las tablas están numeradas, tituladas, mencionadas y con origen; no se añadieron citas externas ni metacomentarios visibles. El cotejo usa registros y código disponibles, sin volver a ejecutar las pruebas ni descargar los resultados originales.

**Extensión:**

| Bloque | Plan | Borrador v5 |
|---|---|---|
| B1. 6.1 | 230; margen 207–253 | 233; cumple. |
| B2. 6.2 | 150; margen 135–165 | 159; cumple. |
| B3. 6.3 | 150; margen 135–165 | 157; cumple. |
| B4. 6.4 | 300; margen 270–330 | 326; cumple. |
| B5. 6.5 | 200; margen 180–220 | 216; cumple. |
| B6. 6.6 | 200; margen 180–220 | 218; cumple. |
| B7. 6.7 | 120; margen 108–132 | 113; cumple. |
| Total de prosa | 1 350; margen 1 215–1 485 | 1 422; cumple. |
| Tablas 4–7 y figuras 4–5 | 2,7 páginas en conjunto | Ocupación pendiente de maquetación; la nota ampliada de la Tabla 7 aumenta el espacio necesario. |
| Anexo C, incluida Figura 6 | 1,5 páginas | Sin cambios; ocupación pendiente de maquetación. |

Se conserva el conteo de la ronda 4: unidades separadas por espacios, sin encabezados, comentarios HTML, tablas, sus títulos ni notas, y sin el anexo. A 350 palabras por página, la prosa ocupa unas 4,06 páginas; con las 2,7 asignadas a tablas y figuras, la previsión es de 6,76 páginas frente a seis. Es una estimación pendiente de maquetación; el plan prevé recortar la Figura 5 si hace falta.

## Ronda 4 — 2026-11-16 — Borrador v4 · Evidencia v2

**Veredicto:** No aprobada | **Citas revisadas:** ninguna nueva; se conserva el cotejo de E1–E4 de la ronda 2 | **Plan:** v2, aprobado, modo ligero

Se revisaron los seis hallazgos de la ronda 3 y los cambios declarados en v4: 6.1, el último párrafo de 6.4, las tablas 6 y 7 y la apertura de 6.6. Se contrastaron con `Taller/Taller.md` §6.3, §7 y §8, los tres perfiles, `productos.csv` y `api/pruebas/`. La evidencia sigue en v2 y los usos de las citas no cambiaron. Persisten dos problemas bloqueantes en la Tabla 6 y queda una sugerencia sobre el detalle por campaña.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante | Tabla 6, tasa y cabeceras «Mínimo», «Medio», «Máximo» y «Fuera de rango» | 4. Respaldo | «Tasa de llegada de las mediciones informadas» no delimita un conjunto cuyos extremos sean 50 y 300: la propia Tabla 7 informa una prueba a 500, y `Taller.md` §7.1 registra un piloto a 350 sin errores. Además, el agotamiento a 500 es una observación de ese generador y ejecución; no establece un límite general de tasas admitidas. La nota sobre `piloto` no corrige el alcance de la cabecera. | Sustituir los encabezados por «Ejemplo bajo», «intermedio» y «alto» y aclarar que son valores seleccionados; presentar 500 como caso observado de ejecución inválida, sin convertirlo en un límite universal. Si se quieren conservar extremos, definir el conjunto comparado y usar sus extremos reales. |
| 2 | Bloqueante | Tabla 6, solicitudes por caso de pytest | 4. Respaldo | «64 concurrentes» y «400 concurrentes, con 16 hilos» confunden la cantidad total de solicitudes con las simultáneas. Las pruebas programan 64 o 400 solicitudes mediante un ejecutor de 16 hilos como máximo; no lanzan las 64 o las 400 al mismo tiempo. | Escribir «64 solicitudes, con hasta 16 hilos; 32 con fallo provocado» y «400 solicitudes, con hasta 16 hilos». Distinguir el total del caso de la concurrencia. |
| 3 | Sugerencia | Tabla 7, filas de carga | 14. Tablas | Se identifican las tres campañas y el número de ejecuciones por variante, pero los rangos de p95 y errores siguen agrupados: no se pueden leer por campaña como pidió la ronda 3. La Figura 5 prevista muestra los p95 individuales, pero no los rangos de errores. | Añadir una nota con los rangos por campaña: `validacion-ci-1`, 8–114 ms y 58,4–58,9 s, 19,0–23,0 %; `validacion-ci-2`, 8–10 ms y 54,1–59,1 s, 16,9–18,8 %; `validacion-local`, 10 ms y 60 s, 31,6–33,0 % (primero `corregida`, luego `regresion` y sus errores). |

**Seguimiento de la ronda 3:**

| Hallazgo anterior | Estado | Comprobación |
|---|---|---|
| 1. Fuera de rango y efectos | Parcial | 6.4 limita la respuesta 404 a identificadores y distingue la invalidez por generador. Se retiraron de esa columna los fallos inyectados y el tiempo de espera. Queda la interpretación de 500 como límite general en la fila de tasa (hallazgo 1 de esta ronda). |
| 2. Extremos y concurrencia | Parcial | La fila de solicitudes ahora incluye el caso de una consulta, y los umbrales coinciden con los tres perfiles. La fila de tasa sigue sin acotar correctamente los extremos y la de solicitudes confunde total y simultaneidad (hallazgos 1 y 2). Las duraciones citadas existen; para evitar que los encabezados impliquen límites generales de fases configurables, también conviene presentarlas como ejemplos seleccionados. |
| 3. Las 38 pruebas por variante | Resuelto | 6.1 ya no atribuye las 38 a cada variante. La Tabla 7 habla de la suite total y distingue los casos de ambas variantes y el control negativo independiente, que instala `sin_candado`. |
| 4. Causa del quiebre en 6.6 | Resuelto | La nueva oración indica que cambiaron equipo y simulación, sin atribuir la variación a uno de ellos ni afirmar que las demás mediciones fueran invariables, conforme a `Taller.md` §8. |
| 5. Resultado del generador | Resuelto | La Tabla 7 incorpora 500 entre los valores e informa que sostuvo 150 y 300 sin errores y que a 500 se agotaron puertos; §7.1 respalda esas observaciones y §6.4 fija el criterio de 98 %. |
| 6. Campañas | Parcial | Se indican 4/3/3 ejecuciones de `corregida` y 3/3/3 de `regresion`, pero los rangos de resultados se mantienen agrupados (sugerencia 3). |

**Constancias del cotejo:** El CSV contiene 10 000 identificadores, del 1 al 10 000, incluido 4182. `test_contrato.py` prueba los identificadores de la tabla con 404 y total de visitas intacto; `test_reversion.py` programa 64 solicitudes, 32 con fallo, y `test_concurrencia.py` programa 400 con 16 hilos. Los perfiles fijan umbrales de 300, 1 000 y 3 000 ms y error máximo de 1 %; `ci` y `local` fijan 60 s de calentamiento y 180 s de medición. Las cantidades y rangos conjuntos de la Tabla 7 concuerdan con las 19 ejecuciones válidas de §7.2. La suite reúne 38 casos parametrizados en total; el control negativo es un caso independiente. La nota sobre el p95 de 60 s debe leerse como un límite de medición: la cifra no permite conocer el tiempo real de las solicitudes afectadas.

Las tablas 6 y 7 están numeradas, tituladas, mencionadas y con origen. No se añadieron citas externas ni metacomentarios visibles. Los restantes bloques y el anexo no cambiaron; se conserva la revisión previa. La comparación se basa en registros y código disponibles, sin volver a ejecutar las pruebas ni descargar las ejecuciones originales.

**Extensión:**

| Bloque | Plan | Borrador v4 |
|---|---|---|
| B1. 6.1 | 230; margen 207–253 | 233; cumple. |
| B2. 6.2 | 150; margen 135–165 | 159; cumple. |
| B3. 6.3 | 150; margen 135–165 | 157; cumple. |
| B4. 6.4 | 300; margen 270–330 | 326; cumple. |
| B5. 6.5 | 200; margen 180–220 | 216; cumple. |
| B6. 6.6 | 200; margen 180–220 | 218; cumple. |
| B7. 6.7 | 120; margen 108–132 | 113; cumple. |
| Total de prosa | 1 350; margen 1 215–1 485 | 1 422; cumple. |
| Tablas 4–7 y figuras 4–5 | 2,7 páginas en conjunto | Ocupación pendiente de maquetación; no se puede determinar su altura a partir del Markdown. |
| Anexo C, incluida Figura 6 | 1,5 páginas | Sin cambios; ocupación pendiente de maquetación. |

Se cuentan unidades separadas por espacios, sin encabezados, comentarios HTML, tablas, títulos ni notas de tabla, y sin el anexo. A 350 palabras por página, la prosa ocupa unas 4,06 páginas; con las 2,7 asignadas a tablas y figuras, la previsión es de 6,76 páginas frente a seis. Es una estimación: corresponde comprobarla al maquetar y aplicar si hace falta el recorte de la Figura 5 previsto por el plan.

## Ronda 3 — 2026-11-16 — Borrador v3 · Evidencia v2

**Veredicto:** No aprobada | **Citas revisadas:** ninguna nueva; se conserva el cotejo de E1–E4 de la ronda 2 | **Plan:** v2, aprobado, modo ligero

Se revisaron los cambios del plan y del borrador, en particular las tablas 6 y 7 y los párrafos que las presentan. La evidencia no cambió y las citas aprobadas mantienen su uso. Se cotejaron las cifras y los valores de ambas tablas con `Taller/Taller.md` §6.3, §7 y §8, los tres archivos de `config/perfiles/`, `base-datos/productos.csv` y las pruebas de `api/pruebas/`. Hay **tres hallazgos bloqueantes y tres sugerencias**.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante | 6.4, último párrafo y Tabla 6, columna «Fuera de rango» | 4. Respaldo | La frase afirma que todos esos valores comprueban que la API rechaza lo que no debe atender. Los ID inexistentes sí se prueban con 404, pero a 500 solicitudes/s se agotan puertos del generador y la medición se declara inválida; no es un rechazo de la API. Los 20 fallos provocados comprueban reversión y recuperación, y no son un número fuera del intervalo de 3 a 400 solicitudes. Los 60 s son un límite de espera de una solicitud, no un valor fuera del rango de umbrales de p95. Se mezclan magnitudes y resultados diferentes. | Limitar la afirmación de rechazo a los identificadores inexistentes. Separar los casos de saturación del generador, fallos inyectados y tiempo de espera en filas o notas con su propósito y resultado, sin presentarlos como valores fuera de rango del parámetro de la fila. |
| 2 | Bloqueante | Tabla 6, columnas «Mínimo», «Medio» y «Máximo» | 4. Respaldo | Las cabeceras presentan extremos generales que las fuentes no sostienen: `piloto.env` fija una tasa de 20 solicitudes/s, menor que 50; las pruebas de contrato también realizan consultas individuales, menos que las 3 indicadas como mínimo de solicitudes por prueba. Los valores 50, 150, 300, 3, 64 y 400 sí aparecen en escenarios o pruebas, pero no son los extremos de todos los valores del parámetro tal como está rotulado. | Acotar explícitamente cada fila al conjunto comparado y escoger extremos verdaderos de ese conjunto; o sustituir esas cabeceras por «Ejemplo bajo», «intermedio» y «alto», explicando que son ejemplos seleccionados y no límites admitidos. Para las pruebas funcionales distinguir solicitudes por caso y solicitudes concurrentes. |
| 3 | Bloqueante | Tabla 7, fila «Funcionales» | 4. Respaldo | «Las 38 aprueban en las dos, incluido el control» atribuye las 38 pruebas a cada variante. Los 38 casos parametrizados forman el total de la suite: hay casos para `sana`, otros solo para `corregida` o `regresion`, y un control negativo separado que instala `sin_candado` y comprueba pérdida de visitas. El código no ejecuta ese control en las dos variantes. La cifra de 38 es el total, no 38 por variante. | Escribir «La suite de 38 casos aprobó; los casos aplicables a `regresion` y `corregida` aprobaron y el control negativo independiente detectó pérdida de visitas». Ajustar también la celda de valores y, para evitar la misma lectura, la formulación de 6.1. |
| 4 | Sugerencia | 6.6, primera oración | 7. Argumento; 8. Precisión | «Solo la tasa exacta … varió con el equipo» atribuye la diferencia al equipo, aunque `Taller.md` §8 dice que cambiaron tanto el equipo como la simulación y no aísla la causa. Además, «solo» puede leerse como si las demás mediciones no variaran. | Sustituir por «Los resultados coincidieron con lo esperado; el punto de quiebre observado de `regresion` varió entre las ejecuciones, en las que cambiaron el equipo y la simulación». |
| 5 | Sugerencia | Tabla 7, fila del generador | 8. Legibilidad; 14. Tablas | El resultado esperado exige sostener al menos el 98 % de la tasa, pero la celda obtenida solo dice «sin errores»; la fuente §7.1 también indica que sostuvo 150 y 300 solicitudes/s. El resultado a 500 se añade sin estar en la celda de valores de la prueba. | Indicar «Sostuvo 150 y 300 solicitudes/s sin errores; a 500 se agotaron los puertos y la ejecución fue inválida» y añadir 500 a la celda de valores o ponerlo en una fila separada. |
| 6 | Sugerencia | Tabla 7, cargas de validación | 14. Tablas | Los totales y rangos agrupados son correctos, pero ya no identifican las tres campañas ni permiten ver sus resultados por separado, aunque el plan v2 pide incluirlas. | Añadir las campañas `validacion-ci-1`, `validacion-ci-2` y `validacion-local` con sus cantidades y rangos por variante, o desglosarlas en una nota breve bajo la tabla. |

**Constancias del cotejo:**

- **Tabla 6, tasa:** 50 se usó en estrés y como base del pico de `regresion`; 150 corresponde a la carga `ci` y `local` y a la cima de ese pico; 300 al estrés de `corregida` y a la cima de su pico. A 500 el piloto agotó puertos efímeros; es una observación de ese generador, no un límite universal ni una respuesta de la API. El perfil `piloto` fija además `TASA=20`.
- **Identificadores:** el CSV contiene 10 000 ID, con mínimo 1 y máximo 10 000, y contiene 4182. La prueba de contrato consulta 4182. La prueba de inexistentes verifica 404 y contador total intacto para 0, 10 001, 2^31−1, 2^31 y 10^20 en las tres variantes; los cuatro valores seleccionados en la tabla están incluidos. `2^31^` y `10^20^` no son sintaxis de superíndice estándar de Markdown: conviene escribir `2³¹` y `10²⁰` o código inequívoco.
- **Pruebas funcionales:** `test_contrato.py` comprueba tres consultas seguidas a 17 y visitas 1, 2 y 3 para las variantes con contador. `test_reversion.py` mezcla 64 solicitudes, 32 con fallo inyectado; también provoca 20 fallos consecutivos y comprueba la recuperación frente a un pool de 8 conexiones. `test_concurrencia.py` lanza 400 solicitudes con 16 hilos y comprueba los contadores en ambas variantes; el control sin protección es independiente. Las cifras son correctas en esos casos, con las salvedades de los hallazgos 1–3.
- **Perfiles y duraciones:** los umbrales de `piloto`, `local` y `ci` son 300, 1 000 y 3 000 ms; los tres admiten hasta 1 % de errores. `ci` y `local` fijan 60 s de calentamiento y 180 s de medición; `piloto` fija 20 y 60 s. Los picos citados duran 30 y 10 s, y §6.3 registra el límite de espera de 60 s en el comportamiento medido. El límite de espera y el umbral de p95 no son el mismo parámetro.
- **Tabla 7, funcionales y generador:** la suite contiene 38 casos parametrizados en total, con las salvedades del hallazgo 3. §7.1 registra que `/salud` sostuvo 150 y 300 solicitudes/s sin errores y que a 500 se agotaron puertos; §6.4 establece la condición de al menos 98 % para la tasa lograda. La tabla no aporta una tasa lograda concreta, pero la fuente sí afirma que se sostuvieron esos niveles.
- **Estrés:** §7.1 registra para `regresion` 13 ms a 75 en un *runner*, 15 ms a 50 y 75 en local, 514 ms a 100 en el primer *runner* y 14,0 s a 100 en local. §8 registra 36 ms a 100 y 31,7 s con unas 92 respuestas correctas/s a 150 en otro *runner*. Para `corregida`, §7.1 registra 10 ms a 150 y 16 ms a 300 en el primer *runner*; en local fueron 10 ms en ambos niveles. Las cifras de la tabla concuerdan con las ejecuciones identificables, aunque conviene indicar el entorno de la fila de `corregida`.
- **Carga:** las campañas `validacion-ci-1`, `validacion-ci-2` y `validacion-local` suman respectivamente 7, 6 y 6 ejecuciones válidas: 10 de `corregida` aprobadas y 9 de `regresion` rechazadas. Los extremos conjuntos son 8–114 ms y cero errores para `corregida`, y 54,1–60 s y 16,9–33,0 % para `regresion`. Los umbrales son 3 000 ms en `ci` y 1 000 ms en `local`; 3 000/114 ≈ 26 y 54 100/3 000 ≈ 18. El p95 de 60 s está recortado por el tiempo de espera; el tiempo real de las solicitudes afectadas no se conoce a partir de esa cifra.
- **Picos:** §8 registra para `regresion` un pico de 50 a 150 durante 30 s, p95 de 12,0 s y recuperación a los 20 s en el *runner*; §6.3 registra recuperación a los 55 s en local con ventana de 180 s. También registra para `corregida` el pico de 150 a 300 durante 10 s y p95 de 12 ms en local. El resultado con ventana de 60 s del perfil `piloto` no se recuperó dentro de ella; no contradice el resultado de la ventana de 180 s, pero conviene mantener explícitos perfil y entorno. Los resultados son informativos, no un veredicto de la compuerta.

**Seguimiento y prosa:** los hallazgos de la ronda 1 que la ronda 2 consideró resueltos siguen atendidos, salvo la precisión sobre campañas que se plantea como nueva sugerencia ante el cambio de tabla. La Figura 5 mantiene sus datos individuales y su origen. El plan incorpora las tablas 6 y 7, ambas numeradas, tituladas, mencionadas antes de aparecer y con origen; las observaciones anteriores afectan la interpretación y el respaldo de sus celdas. No se añadieron citas externas ni metacomentarios visibles del proceso de redacción. Las restantes subsecciones y el anexo no cambiaron.

**Extensión:**

| Bloque | Plan | Borrador v3 |
|---|---|---|
| B1. 6.1 | 230; margen 207–253 | 234; cumple. |
| B2. 6.2 | 150; margen 135–165 | 159; cumple. |
| B3. 6.3 | 150; margen 135–165 | 157; cumple. |
| B4. 6.4 | 300; margen 270–330 | 322; cumple. |
| B5. 6.5 | 200; margen 180–220 | 216; cumple. |
| B6. 6.6 | 200; margen 180–220 | 220; cumple en el límite. |
| B7. 6.7 | 120; margen 108–132 | 113; cumple. |
| Total de prosa | 1 350; margen 1 215–1 485 | 1 421; cumple. |
| Tablas 4–7 y figuras 4–5 | 2,7 páginas en conjunto; tablas 6 y 7: 0,35 y 0,55 páginas | Ocupación pendiente de maquetación. La Tabla 7 contiene ocho filas de resultados; no se puede establecer su altura final con el Markdown. |
| Anexo C, incluida Figura 6 | 1,5 páginas, 0,5 para la figura | Sin cambios; ocupación pendiente de maquetación. |

Se usa el método de las rondas anteriores: unidades separadas por espacios, incluidas citas visibles, sin encabezados, comentarios HTML, tablas, sus títulos ni notas, y sin el anexo. Con 350 palabras por página, la prosa ocupa unas 4,06 páginas; más las 2,7 asignadas a tablas y figuras da una previsión de 6,76 páginas frente a seis. Es una estimación, no una medición: al maquetar corresponde verificar el espacio y aplicar, si hace falta, el recorte de la Figura 5 previsto por el plan.

El cotejo usa los registros internos y el código disponibles; no se volvieron a ejecutar las pruebas ni se descargaron las ejecuciones originales. Las rondas anteriores se conservan a continuación.

## Ronda 2 — 2026-11-10 — Borrador v2 · Evidencia v2

**Veredicto:** Aprobada | **Citas revisadas:** E4 (nuevo cotejo); E1, E2 y E3 (trazabilidad y uso; cotejo literal conservado de la ronda 1) | **Plan:** v1, aprobado, modo ligero

Se revisaron los diez hallazgos de la ronda anterior y las correcciones del borrador y de la evidencia, contra el plan, la guía de redacción y el glosario actuales. Los tres bloqueantes están resueltos y no se detectan otros. Las siete sugerencias también quedan atendidas, incluida la excepción terminológica ahora explícita para «workflow». No quedan hallazgos que requieran corrección en esta ronda.

**Seguimiento de la ronda 1:**

| Hallazgo anterior | Estado | Comprobación en v2 |
|---|---|---|
| 1. Garantía de exclusividad de CPU | Resuelto | 6.3 se limita a indicar que la API y PostgreSQL se ejecutan en núcleos distintos, fijados en la configuración. `Taller/compose.yaml` asigna `cpuset: "2"` a la API y `cpuset: "3"` a PostgreSQL. Se retiró la garantía de que ningún otro proceso compita por esas CPU. No se amplía el respaldo general de E1. |
| 2. Calificación externa de las versiones | Resuelto | La nota de la Tabla 4 dice «Versiones usadas en el taller; las dependencias exactas están en el repositorio». Describe la configuración interna y ya no afirma que esas versiones sean las estables de una fecha. |
| 3. Localizador de E4 | Resuelto | E4 ubica el pasaje en «Concepts», último párrafo, inmediatamente antes de «Scope». El nuevo cotejo del cuerpo de la documentación oficial confirma tanto la literalidad como esa ubicación. |
| 4. Extensión de 6.5 | Resuelto | Se redujo de 239 a 216 palabras, dentro del intervalo 180–220. Conserva las cuatro operaciones, las dos variantes, la lectura de resultados y el procedimiento de CI. |
| 5. Extensión y selección de 6.6 | Resuelto | Se redujo de 249 a 220 palabras, en el límite superior permitido. La apertura presenta el resultado conjunto y los márgenes; la Tabla 6 conserva el detalle por campaña. |
| 6. Terminología | Resuelto con el glosario actual | El borrador usa «perfil de ejecución» en la prosa y las descripciones de figuras, sin alterar parámetros como `--perfil`. La entrada «Workflow», agregada al glosario, prescribe expresamente «workflow (sin cursiva, como en 5.7)». La falta de cursiva deja de ser una desviación: se aplica la forma obligatoria del glosario según la guía, §8. |
| 7. Datos de la Figura 5 | Resuelto | El origen remite a los valores individuales de las tres campañas de `Taller/Taller.md` §7.2. La descripción dispone desplazar horizontalmente los puntos coincidentes para mostrar todas las ejecuciones; ya no pretende reconstruirlos solo con los rangos de la Tabla 6. |
| 8. Margen mínimo por variante | Resuelto | 6.6 distingue el mínimo de `corregida` en `validacion-ci-1` y el de `regresion` en `validacion-ci-2`. Los cocientes son 3 000/114 ≈ 26,3 y 54 100/3 000 ≈ 18,0, respectivamente. |
| 9. Causa de la variación | Resuelto | 6.6 localiza la mayor variación en las ejecuciones de `corregida` en GitHub Actions y declara que su causa no quedó identificada, conforme a `Taller/Taller.md` §7.1. No atribuye causalidad demostrada al hardware del ejecutor. |
| 10. Siete consultas y ocho hilos | Resuelto | 6.6 distingue las siete consultas de productos de la lectura de `/metrics`, que completa la ocupación de los ocho hilos. La métrica `EN_CURSO` excluye `/metrics`, según `Taller/api/tienda/metricas.py`; los seis o siete hilos en espera y la comparación de CPU coinciden con `Taller/docs/INTERPRETACION.md` §5. |

**Citas, respaldo y argumento:**

- **E4:** el pasaje registrado aparece literalmente al final de [«Assertions», apartado «Concepts»](https://docs.gatling.io/concepts/assertions/#concepts), antes de «Scope». Respalda que las aserciones se evalúan al terminar la simulación y que el fallo de una hace fallar la simulación. Su uso en 6.3 es fiel; F1, Gatling Corp. (2026) y la entrada de referencias coinciden. Los demás criterios de selección se remiten expresamente a 5.8, como prevé el plan.
- **E1–E3:** se conserva el cotejo literal aprobado en la ronda 1, sin repetirlo. Las citas mantienen sus IDs existentes y la correspondencia de fuente, autor y año. Las correcciones no amplían las afirmaciones atribuidas a Docker, Prometheus ni GitHub Actions. La referencia a una máquina virtual nueva sigue situada en el entorno hospedado de este taller. Las cuatro fuentes están en `Investigación/Referencias.md`; no se incorporaron fuentes externas nuevas en v2.
- **Resultados internos:** la reformulación de los márgenes concuerda con las tablas de validación de `Taller/Taller.md` §7.2 y con los umbrales de `config/perfiles/ci.env` y `local.env`. Las campañas suman 19 ejecuciones válidas y sostienen los rangos de la Tabla 6. La variación de unas 28 veces sigue identificada como un resultado de calibración, distinto de las campañas de validación. Estas cifras son resultados propios del taller, conforme al tratamiento establecido en el plan; no requieren una referencia bibliográfica externa.
- **Prosa y alcance:** se mantienen las siete subsecciones y el anexo C, con el argumento y las remisiones al Marco teórico previstos. Las cuatro citas corresponden al modo ligero. No hay metacomentarios visibles sobre el proceso de producción del texto; los comentarios de versión son ocultos. No se detectan definiciones normativas, datos externos ni afirmaciones nuevas sin respaldo introducidos por las correcciones.
- **Tablas, figuras y anexo:** están las tablas 4–6 y las descripciones de las figuras 4–6, numeradas, tituladas, con origen y mencionadas en el texto. Las figuras mediante comentarios cumplen el formato exigido para el borrador. La nueva descripción de la Figura 5 añade la distribución individual a los rangos de la tabla. Los extractos del anexo mantienen el contenido revisado en la ronda 1; la corrección terminológica no altera su funcionamiento.

**Extensión:**

| Bloque | Plan | Borrador v2 |
|---|---|---|
| B1. 6.1 Contexto de aplicación | 230 palabras; margen 207–253 | 234; +1,7 %. Cumple. |
| B2. 6.2 Recursos y código | 150 palabras; margen 135–165 | 159; +6,0 %. Cumple. |
| B3. 6.3 Stack tecnológico | 150 palabras; margen 135–165 | 157; +4,7 %. Cumple. |
| B4. 6.4 Plan de pruebas | 300 palabras; margen 270–330 | 324; +8,0 %. Cumple. |
| B5. 6.5 Guía paso a paso | 200 palabras; margen 180–220 | 216; +8,0 %. Cumple. |
| B6. 6.6 Resultados e interpretación | 200 palabras; margen 180–220 | 220; +10,0 %. Cumple en el límite superior. |
| B7. 6.7 Límites | 120 palabras; margen 108–132 | 113; −5,8 %. Cumple. |
| Total de prosa de la sección 6 | 1 350 palabras; margen 1 215–1 485 | 1 423; +5,4 %. Cumple en conjunto y por bloque. |
| Tablas 4, 5 y 6 | 0,45 + 0,50 + 0,40 = 1,35 páginas | 134, 139 y 105 palabras, respectivamente, incluidos títulos y notas. Ocupación pendiente de maquetación. |
| Figuras 4 y 5 | 0,40 + 0,45 = 0,85 páginas | Descripciones completas; ocupación pendiente de maquetación. |
| B8. Anexo C, incluida Figura 6 | 1,5 páginas; 0,5 para la figura | Unas 144 palabras fuera de comentarios y código, y 39 líneas de extractos: 11 de estructura, 10 de Java y 18 de YAML. Ocupación pendiente de maquetación. |

Se mantiene el método de la ronda 1: unidades separadas por espacios, incluidas las citas visibles, sin encabezados ni comentarios HTML. La prosa excluye tablas, títulos y notas de tabla y el anexo C. En las tablas se excluyen los separadores y las marcas de formato. El conteo del anexo es orientativo e incluye sus rótulos visibles.

**Espacio de tablas y figuras:** no se puede determinar si exceden sus asignaciones sin maquetar el documento. Con la equivalencia orientativa del plan de 350 palabras por página, la prosa ocupa unas 4,07 páginas; sumadas las 2,2 previstas para tablas y figuras, la sección se aproxima a 6,27 páginas. Esta previsión mantiene pendiente el control de las seis páginas al integrar el documento y la posible reducción de la Figura 5 que ya contempla el plan; no demuestra por sí sola un exceso de espacio. El anexo se controla aparte.

Esta ronda verifica las correcciones documentales y sus insumos. No vuelve a ejecutar las pruebas ni descarga individualmente los 19 artefactos de validación; el cotejo de las campañas se apoya en los registros internos identificados en `Taller/Taller.md`, con el alcance de comprobación directa consignado en la ronda 1. La ronda anterior se conserva íntegra a continuación.

## Ronda 1 — 2026-11-10 — Borrador v1 · Evidencia v1

**Veredicto:** No aprobada | **Citas revisadas:** E1, E2, E3 y E4 | **Plan:** v1, aprobado, modo ligero

Se cotejaron las cuatro filas con el cuerpo de la documentación oficial, y se revisaron la prosa, las tablas, las descripciones de figuras y el anexo C contra el plan, la guía de redacción y el glosario. También se contrastaron el procedimiento y los resultados con los documentos, la configuración, el código y los resultados disponibles del taller. Quedan **tres hallazgos bloqueantes y siete sugerencias**. Este informe no modifica el borrador, la evidencia ni los demás archivos.

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Bloqueante | 6.3, primer párrafo: «ningún otro proceso del entorno les quita tiempo de CPU» | 4. Respaldo | Se atribuye a la afinidad de CPU una garantía de exclusividad que la configuración no demuestra. `compose.yaml` permite a la API ejecutarse en la CPU 2 y a PostgreSQL en la 3; Gatling, Prometheus y Grafana no tienen afinidad que los excluya de esas CPU. La [referencia oficial de `cpuset`](https://docs.docker.com/reference/compose-file/services/#cpuset) define las CPU en las que se permite ejecutar un contenedor, sin establecer la exclusión de los demás procesos. E1 solo respalda la función general de Compose. | Sustituir la garantía por la configuración efectivamente comprobable: «La API y PostgreSQL se ejecutan en CPU distintas, fijadas mediante la configuración del entorno». Retirar la afirmación de que otros procesos no pueden competir por ellas. Si se quiere explicar el funcionamiento general de `cpuset`, registrar ese pasaje oficial en la evidencia y citarlo. |
| 2 | Bloqueante | Tabla 4, nota: «Versiones estables al 8 de noviembre de 2026» | 4. Respaldo | Las versiones utilizadas son contenido interno y pueden comprobarse en las dependencias y los archivos de construcción. Sin embargo, calificarlas como estables en una fecha afirma un estado externo de publicación que ninguna fila E1–E4 documenta. Repetir esa calificación desde `Taller.md` §5.1 no sustituye el respaldo oficial. No se concluye que las versiones sean inestables: falta la evidencia de la calificación. | Cambiar la nota a «Versiones utilizadas en el taller; configuración y dependencias en el repositorio». Si se conserva «estables al…», aportar los registros oficiales de publicación y sus filas de evidencia. |
| 3 | Bloqueante | `02 Evidencia.md`, E4, columna «Ubicación» | 2. Literalidad y ubicación | El pasaje de E4 aparece literalmente en [«Assertions», apartado «Concepts»](https://docs.gatling.io/concepts/assertions/#concepts), pero al final de ese apartado, inmediatamente antes de «Scope»; no en el primer párrafo indicado en la fila. La afirmación y su uso en 6.3 sí son fieles. El defecto se limita al localizador exigido para el cotejo. | Sustituir «primer párrafo» por «apartado “Concepts”, último párrafo, inmediatamente antes de “Scope”». Conservar el pasaje y la cita del borrador. |
| 4 | Sugerencia | B5, 6.5 completo | 12. Extensión | Contiene 239 palabras frente a las 200 previstas; supera el máximo de 220. El procedimiento local y el detalle de los workflows compiten por el mismo presupuesto. | Reducir al menos 19 palabras. Por ejemplo, condensar el comienzo a «La práctica usa cuatro operaciones de `taller.ps1` o `taller.sh`: `preparar`, `funcionales`, `ejecutar` y `detener`»; mantener después las dos invocaciones de carga y sus resultados. Abreviar la explicación del cambio de variante a «Un archivo selecciona la variante: el cambio a `regresion` reproduce un defecto y el retorno a `corregida` demuestra su corrección». Conservar E3 y las cifras de los ejemplos. |
| 5 | Sugerencia | B6, 6.6 completo | 9. Selección; 12. Extensión | Contiene 249 palabras frente a las 200 previstas; supera el máximo de 220. El primer párrafo vuelve a enumerar resultados que ya ordena la Tabla 6. | Reducir al menos 29 palabras. Puede sustituirse el primer párrafo por «Las 19 ejecuciones de validación fueron válidas y dieron los veredictos esperados (Tabla 6). El menor margen de `corregida` fue de 26 veces; el de `regresion`, de 18 veces. La Figura 5 muestra la separación. `regresion` también superó el 1 % de errores permitido». Mantener la explicación posterior de la variación y la observabilidad, con las precisiones de los hallazgos 8 y 9. |
| 6 | Sugerencia | 6.4, tercer párrafo; 6.5, segundo; 6.6, apertura; anexo C.2 | 13. Terminología | Se alternan «perfil de ejecución» y «perfil» para el mismo concepto: «el perfil se congela», «Los dos perfiles», «con el perfil `ci`», «perfiles de ejecución ya congelados» y «del perfil de ejecución». El glosario prohíbe «perfil» solo para distinguirlo del perfil de carga. Además, «workflows» se escribe sin cursiva en la prosa de 6.2 y 6.5, pese a ser un término técnico en inglés. | Usar de forma uniforme «perfil de ejecución» y «perfiles de ejecución» en la prosa, también en las descripciones de figuras. Por ejemplo: «Después, el perfil de ejecución se congela» y «Los dos perfiles de ejecución quedaron en 150 solicitudes por segundo». Escribir «*workflows* de CI» y «Tres *workflows* manuales». No alterar nombres de rutas ni parámetros como `--perfil`. |
| 7 | Sugerencia | Figura 5, descripción y origen | 14. Tablas y figuras | Se pide un punto por ejecución, pero se declara como insumo «los datos de la Tabla 6», que solo contiene rangos y cantidades. Esos agregados no permiten reconstruir los 19 valores individuales ni su distribución. Los valores sí están en las tablas de `Taller.md` §7.2, la fuente prevista por el plan. | Reformular el origen como «Elaboración propia con los valores individuales de las campañas de validación de `Taller.md` §7.2». Dibujar los 19 puntos y hacer visibles las repeticiones coincidentes mediante un pequeño desplazamiento horizontal o su multiplicidad. Así la figura aporta información distinta de los rangos de la tabla. |
| 8 | Sugerencia | 6.6, primer párrafo: «El margen más estrecho apareció en `validacion-ci-1`» | 8. Legibilidad y precisión | El enunciado no distingue el margen de cada variante. Para `corregida`, el mínimo sí está en esa campaña: 3 000/114 ≈ 26,3. Para `regresion`, el mínimo está en `validacion-ci-2`: 54 100/3 000 ≈ 18,0, menor que 58 400/3 000 ≈ 19,5. Los valores de la tabla son correctos; la formulación global del margen resulta ambigua. | Precisar «El menor margen de `corregida` apareció en `validacion-ci-1`, con 114 ms frente a 3 000 ms; el menor de `regresion`, en `validacion-ci-2`, fue de 18 veces». La condensación del hallazgo 5 ya incorpora ambos mínimos. |
| 9 | Sugerencia | 6.6, párrafo que comienza «El ruido estuvo en el *runner*» | 7. Argumento; 8. Precisión | La apertura puede leerse como atribución causal al equipo de CI. `Taller.md` §7.1 registra la variación en ese entorno, pero declara que su causa no está identificada y ofrece hipótesis. El contraste con la computadora de desarrollo permite localizar la observación, sin aislar su causa. | Sustituir por «La mayor variación se observó en las ejecuciones de `corregida` en GitHub Actions; su causa no quedó identificada». Conservar después los factores de variación y el p50, que sí corresponden a los registros internos. |
| 10 | Sugerencia | 6.6, último párrafo: «siete solicitudes están en curso, todos los hilos disponibles» | 8. Legibilidad y precisión | La Tabla 4 y `gunicorn.conf.py` fijan ocho hilos. La métrica de solicitudes en curso excluye `/metrics`, según `api/tienda/metricas.py`; por eso observar siete solicitudes de productos durante la recolección no equivale a configurar siete hilos. La redacción puede hacer parecer contradictorios esos datos. | Escribir «Durante la recolección se observan siete solicitudes de productos en curso; la métrica excluye `/metrics`. Seis o siete hilos esperan el candado». Mantener la comparación de CPU y la pérdida posterior de muestras. |

**Extensión:**

| Bloque | Plan | Borrador |
|---|---|---|
| B1. 6.1 Contexto de aplicación | 230 palabras; margen 207–253 | 234; +1,7 %. Cumple. |
| B2. 6.2 Recursos y código | 150 palabras; margen 135–165 | 159; +6,0 %. Cumple. |
| B3. 6.3 Stack tecnológico | 150 palabras; margen 135–165 | 165; +10,0 %. Cumple en el límite superior. |
| B4. 6.4 Plan de pruebas | 300 palabras; margen 270–330 | 320; +6,7 %. Cumple. |
| B5. 6.5 Guía paso a paso | 200 palabras; margen 180–220 | 239; +19,5 %. Excede. |
| B6. 6.6 Resultados e interpretación | 200 palabras; margen 180–220 | 249; +24,5 %. Excede. |
| B7. 6.7 Límites | 120 palabras; margen 108–132 | 114; −5,0 %. Cumple. |
| Total de prosa de la sección 6 | 1 350 palabras; margen 1 215–1 485 | 1 480; +9,6 %. Cumple en conjunto, pero no sustituye el control por bloque. |
| Tablas 4, 5 y 6 | 0,45 + 0,50 + 0,40 = 1,35 páginas | 130, 139 y 105 palabras, respectivamente, incluidos títulos y notas. No hay maquetación para comprobar su ocupación. |
| Figuras 4 y 5 | 0,40 + 0,45 = 0,85 páginas | Ambas están descritas mediante comentarios, como exige la guía. Ocupación pendiente de maquetación. |
| B8. Anexo C, incluida Figura 6 | 1,5 páginas, de las cuales 0,5 son para la figura | Unas 140 palabras fuera de los bloques de código y 39 líneas de extractos: 11 de estructura, 10 de Java y 18 de YAML. Figura descrita. Ocupación pendiente de maquetación. |

Se cuentan unidades separadas por espacios, incluidas las citas visibles, sin encabezados ni comentarios HTML. La prosa excluye tablas, títulos y notas de tabla y el anexo C. El conteo de las tablas excluye sus separadores Markdown. Las marcas de cursiva, negrita y código no cuentan como palabras independientes. El total del anexo es orientativo e incluye sus rótulos visibles.

**Espacio de tablas y figuras:** no se puede afirmar que excedan sus asignaciones sin una versión maquetada. Con la equivalencia orientativa del plan de 350 palabras por página, la prosa actual ocupa unas 4,23 páginas; al sumar las 2,2 asignadas a tablas y figuras, la sección se aproxima a 6,43 páginas frente a las seis previstas. Es una previsión de ajuste, no una medición de diseño final. Las reducciones de B5 y B6 son necesarias por bloque; después corresponde comprobar la ocupación conjunta y, si hace falta, aplicar el recorte de la Figura 5 previsto en el plan. El anexo se controla aparte.

**Constancias del cotejo:**

- **E1 — Docker:** el pasaje aparece literalmente en el primer párrafo de [«Docker Compose»](https://docs.docker.com/compose/). F2, Docker Inc. y «s. f.» concuerdan entre plan, evidencia, cita y referencias. La oración sobre definir y ejecutar los servicios no amplía la fila. La garantía adicional de CPU se evalúa por separado en el hallazgo 1.
- **E2 — Prometheus:** se localizaron los tres fragmentos en [«Overview», «What is Prometheus?», «Features» y «Architecture»](https://prometheus.io/docs/introduction/overview/). La consulta de métricas mediante HTTP es fiel a la fila; autor, fecha y F3 coinciden. Las funciones concretas del panel y su configuración son contenido del taller, comprobable en `observabilidad/`.
- **E3 — GitHub Actions:** los tres fragmentos figuran en el cuerpo de [«Understanding GitHub Actions», «Workflows», «Events» y «Runners»](https://docs.github.com/en/actions/get-started/understand-github-actions). Los dos primeros están dentro del apartado superior «The components of GitHub Actions» indicado por la fila. F4, autor y año concuerdan. La referencia a máquinas nuevas se interpreta en el entorno hospedado `ubuntu-24.04` de este taller; no verifica una garantía para ejecutores propios.
- **E4 — Gatling:** el contenido sobre evaluación de aserciones y fallo de la simulación es literal y fiel a [«Assertions», «Concepts»](https://docs.gatling.io/concepts/assertions/#concepts). F1 y la entrada de Gatling Corp. (2026), versión 3.16.0, coinciden. Queda pendiente corregir su ubicación, según el hallazgo 3. Los otros criterios de selección se remiten expresamente a 5.8, como permite el plan.
- **Trazabilidad y fuentes:** las cuatro citas visibles llevan sus IDs existentes. F1–F4 están en `Investigación/Referencias.md`; F2–F4 son documentación oficial abierta, admisible según `Alcance.md` §5.3. Aunque la evidencia no las rotula «Nueva», están identificadas en el plan y sus entradas bibliográficas existen. El formato autor–año y los comentarios ocultos cumplen la convención del documento.
- **Resultados internos:** las tres tablas de validación de `Taller.md` §7.2 suman 7 + 6 + 6 = 19 ejecuciones y reproducen los rangos, errores y veredictos de la Tabla 6. Los umbrales de 3 000 y 1 000 ms y la tasa de 150 solicitudes por segundo concuerdan con `config/perfiles/ci.env` y `local.env`. El factor de variación de unas 28 veces corresponde a 250/9 en la primera calibración; no se confunde con las tres campañas de validación. Las cifras de los dos *pull requests* de demostración coinciden con `docs/GUIA.md` §10.
- **Anexo y procedimiento:** se contrastaron los extractos con `CargaSimulation.java` y `.github/workflows/compuerta.yml`: se conservan las fases, las aserciones limitadas a `medicion`, los disparadores mostrados y la conservación de resultados. Los dos ejemplos de la Figura 6 tienen resultados locales disponibles: `20261110T224259Z-carga-corregida` da p95 de 12 ms, 0 % de errores y aprobación; `20261110T224735Z-carga-regresion` da p95 de 60 s, 42,85 % de errores y rechazo. Sus tasas de respuestas correctas son aproximadamente 150,0 y 66,3 por segundo. No se vuelven a ejecutar las pruebas ni se modifica el entorno.
- **Argumento, modo y alcance:** están las siete subsecciones y el anexo previstos, con las tres tablas y las tres figuras numeradas, tituladas, con origen y mencionadas antes de aparecer. Las descripciones de figuras mediante comentarios son el formato requerido en esta etapa; no se exige dibujarlas en el borrador. Las cuatro citas externas corresponden al modo ligero. No se detectan metacomentarios visibles sobre IA, skills o auditorías. Las decisiones de diseño, las cifras de las campañas y los límites del experimento se tratan como contenido interno conforme al plan; no se exige agregarles citas bibliográficas externas.

El cotejo de las campañas completas se apoya en sus registros resumidos en `Taller.md`, con identificadores de corridas y revisiones. La comprobación directa de artefactos de ejecución se limita a los dos ejemplos locales indicados; no se presenta esta ronda como una repetición experimental ni como una descarga y comprobación individual de los 19 artefactos de validación.
