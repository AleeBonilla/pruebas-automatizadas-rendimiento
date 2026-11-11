# Auditoría — 07 Conclusiones

## Ronda 1 — 2026-11-11 — Borrador v5 · Evidencia sin versión (sin filas)

**Veredicto:** Aprobada | **Citas revisadas:** ninguna; no hay citas externas | **Afirmaciones internas verificadas:** las 11 del plan | **Plan:** v1, aprobado, modo ligero

Se aplicó la skill auditor al borrador completo. El cotejo de citas se sustituyó, conforme al encargo, por la comprobación de las afirmaciones internas de `01 Plan.md` contra sus orígenes. Se revisaron también la síntesis de las secciones 3 y 5, el criterio 4 y los criterios 7 a 14. No se exigieron citas ni filas de evidencia para contenido interno o razonamiento propio. Los criterios 1–3, 5 y 6 no tienen citas externas sobre las que operar en esta sección.

No existía una auditoría anterior de Conclusiones. Los cinco párrafos del borrador corresponden, en orden, a B1–B5.

### Hallazgos y excepción aplicada

| # | Tipo | Ubicación | Criterio | Hallazgo | Corrección sugerida |
|---|---|---|---|---|---|
| 1 | Sugerencia | B5 completo | 11 — Metacomentarios; excepción expresa del plan | El párrafo trata la IA y las auditorías, materias excluidas por la regla general. Se aplica la excepción explícita de `01 Plan.md`: `Enunciado.md`, sección 7, pide reflexiones metodológicas, y `Alcance.md` §5.6 pide la reflexión sobre el uso y la validación de la IA. La propia guía permite que el plan declare una excepción. Por eso esta observación no es bloqueante ni obliga a suprimir B5. | Conservar el bloque y su remisión al anexo B. Mantener la entrada «En lo metodológico…»; reservar para ese anexo el detalle operativo del procedimiento. |
| 2 | Sugerencia | B2–B5, un párrafo por bloque | 12 — Extensión | El total cumple, pero B2 y B3 tienen 66 palabras cada uno frente al mínimo de 68; B4 tiene 77 frente al mínimo de 81; B5 tiene 76 frente al mínimo de 77. El criterio exige revisar cada bloque por separado, aunque las diferencias sean pequeñas. | Ampliar con precisiones que aporten al argumento: en B2, cerrar con «en los entornos medidos»; en B3, precisar los requisitos y el costo inicial según el hallazgo 3; en B4, añadir «El resultado depende, por tanto, de las condiciones medidas»; en B5, acotar el recuento con «en las ocho partes auditadas hasta ese momento». Estas adiciones, consideradas por separado, permiten entrar en los márgenes sin repetir definiciones. |
| 3 | Sugerencia | B3, «bastan Git y Docker y entre cuatro y seis minutos por ejecución» | 7 y 9 — Precisión de la respuesta y selección | Los programas y la duración están respaldados, pero «bastan» puede leerse como un costo total de adopción. La sección 6.2 y `GUIA.md` §1 exigen Docker con Compose y recursos suficientes; §3 distingue la preparación inicial, y §9 estima cerca de una hora para calibrar y validar. El borrador exige calibrar en la oración siguiente, de modo que no oculta ese paso, pero conviene distinguir su costo del de una carga individual. | Reformular: «Con los recursos de 6.2, Git y Docker con Compose permiten reproducirlo; tras la preparación y la calibración iniciales, cada ejecución dura entre cuatro y seis minutos». Conservar después las condiciones del veredicto confiable. |
| 4 | Sugerencia | B2, «la compuerta rechazó siempre…» | 13 — Terminología | El glosario fija *quality gate* como forma en el texto y utiliza «compuerta» en su explicación. La sección emplea solo esta última denominación. Se entiende, pero no sigue la forma obligatoria registrada. | Sustituir por «la *quality gate* rechazó siempre a `regresion` y aprobó siempre a `corregida`». La expresión ya está presentada en las secciones anteriores y no requiere otra definición aquí. |

### Cotejo de las afirmaciones internas

Las ubicaciones de esta tabla identifican las fuentes internas consultadas; no son nuevas filas de evidencia externa.

| # | Afirmación del plan y ubicación en Conclusiones | Origen comprobado | Resultado |
|---|---|---|---|
| 1 | Ambas implementaciones aprueban las mismas 38 pruebas funcionales — B2 | Sección 6.1, segundo párrafo; `Taller/docs/GUIA.md` §4; `Taller/docs/PLAN-DE-PRUEBAS.md` §5, PF | Conforme. Se trata de las dos variantes del contador, `regresion` y `corregida`, y las pruebas incluyen concurrencia. La comparación no atribuye la misma funcionalidad a `sana`. |
| 2 | `regresion` colapsa entre 75 y 100 solicitudes/s; `corregida` mantiene un p95 de unos 10 ms hasta 300 — B2 | `Taller/Taller.md` §5.2, tabla del piloto y explicación posterior; §7.1 | Conforme. En el piloto local, `regresion` pasa de 14 ms a 75 solicitudes/s a 8 027 ms a 100; `corregida` registra 12, 11, 10, 9 y 10 ms entre 50 y 300. «Unos 10 ms» conserva la aproximación. Es el resultado del piloto con la configuración final, no una garantía para cualquier entorno. |
| 3 | 19 ejecuciones de validación, todas válidas, en dos entornos, siempre con rechazo de `regresion` y aprobación de `corregida` — B2 | Sección 6.6 y Tabla 6; `Taller/Taller.md` §7.2, las tres campañas | Conforme. `validacion-ci-1` aporta 7 ejecuciones, `validacion-ci-2`, 6, y `validacion-local`, 6: 19 en total. Los dos entornos son GitHub Actions y la computadora de desarrollo. Hay 9 ejecuciones de `regresion` rechazadas y 10 de `corregida` aprobadas. No se incorporó a este total la ejecución inválida de calibración local. |
| 4 | Git y Docker; cuatro a seis minutos por ejecución — B3 | Secciones 6.2 y 6.5; `Taller/docs/GUIA.md` §§1, 3 y 9 | Conforme como requisitos de software y duración de una ejecución completa de carga: unos cuatro minutos para `corregida` y seis para `regresion`. Docker requiere Compose. No es el tiempo de preparación ni el de la campaña de calibración y validación; véase la sugerencia 3. |
| 5 | Calibrar por entorno, validar con una campaña nueva y comprobar la validez de cada medición — B3 | Sección 6.4; `Taller/Taller.md` §§6.4 y 7; `Taller/docs/PLAN-DE-PRUEBAS.md` §§6 y 8; `GUIA.md` §9 | Conforme. Primero se comprueba que la medición sea interpretable y después se aplican las aserciones. La validación usa el perfil congelado y datos nuevos; si falla, se abre otra calibración. Un fallo del generador no se interpreta como regresión de la API. |
| 6 | Con 1 CPU por contenedor y la base de datos en la misma máquina, las variantes no se separaban — B4 | `Taller/Taller.md` §5.2, descripción de la primera configuración | Conforme. A 300 solicitudes/s, `regresion` aprobó con 88 ms y `corregida` fue rechazada con 482 ms. El párrafo sintetiza el resultado sin atribuirlo a una sola causa: el origen documenta tanto las cuotas de CPU como el costo reducido de las idas y vueltas a PostgreSQL. |
| 7 | El p95 de `corregida` varió hasta 28 veces entre corridas idénticas en GitHub Actions — B4 | `Taller/Taller.md` §7.1, primera calibración de `ci`; sección 6.6 | Conforme como redondeo: 250/9 = 27,78. La segunda calibración varió 60/9 = 6,67. El máximo pertenece a la primera calibración, no a las 19 ejecuciones de validación. El borrador no afirma haber identificado su causa. |
| 8 | Una regresión pequeña aprobaría porque se calibró con una que lleva el p95 a decenas de segundos — B4 | Sección 6.7; `Taller/Taller.md` §7.1 | Conforme como límite del diseño. La sección 6.7 precisa que incluso duplicar el tiempo de `corregida` quedaría bajo el umbral. Conclusiones conserva el carácter hipotético y no afirma haber ejecutado un experimento con una regresión pequeña. |
| 9 | 28 rondas, 11 no aprobadas, 22 bloqueantes; predominan fidelidad y respaldo; ninguno señala una fuente inexistente — B5 | Los ocho `04 Auditoría.md` anteriores a esta ronda; anexo B, §§B.1–B.2 | Conforme para ese conjunto de informes. El recuento independiente se detalla abajo. La lectura de los bloqueantes y de las tres filas rechazadas en la primera auditoría de evidencia de la Introducción no muestra una fuente inexistente: los problemas fueron de formulación, atribución, localización, registro o acceso. |
| 10 | Partir de la evidencia ya auditada saturó el texto de citas — B5 | `Alcance.md` §5.3, «Evolución del procedimiento»; anexo B, §B.3 | Conforme. Ambos documentan el procedimiento anterior y el resultado de 17 citas en 880 palabras; `Alcance.md` explica además que el redactor estaba limitado a parafrasear evidencia aprobada. Es una reflexión sobre ese proceso concreto, no una conclusión general sobre cualquier uso de evidencia. |
| 11 | Claude Code produce, Codex audita y la última decisión es humana — B5 | Sección 4.3, segundo párrafo y Figura 1 | Conforme. El origen asigna planificación y redacción a Claude Code y auditoría a Codex, de otro proveedor, con revisión humana final. Conclusiones resume las funciones sin repetir nombres de modelos ni los pasos operativos. «Funcionó separar…» y «aceleró la producción» se leen como balance cualitativo del autor; no se presenta una medición de productividad ni una comparación experimental entre procedimientos. |

### Recuento de los informes de auditoría

Se contaron los encabezados de ronda, sus veredictos y las filas identificadas como «Bloqueante» en los ocho informes que sustentan el anexo B. Esta ronda de Conclusiones queda fuera de ese conjunto histórico.

| Parte | Rondas | No aprobadas | Hallazgos bloqueantes |
|---|---:|---:|---:|
| Introducción | 6 | 2 | 4 |
| Planteamiento del problema | 4 | 1 | 1 |
| Metodología | 2 | 0 | 0 |
| Marco teórico, 5.1–5.2 | 4 | 2 | 5 |
| Marco teórico, 5.3–5.4 | 4 | 1 | 1 |
| Marco teórico, 5.5–5.7 | 3 | 2 | 2 |
| Marco teórico, 5.8 | 3 | 2 | 6 |
| Sección 6 | 2 | 1 | 3 |
| **Total** | **28** | **11** | **22** |

El total coincide con la Tabla B1. Las tres filas de evidencia rechazadas en la ronda 1 de la Introducción no están rotuladas como hallazgos bloqueantes y el anexo las informa aparte; por eso no se sumaron nuevamente a los 22. Las reiteraciones de un problema en rondas distintas sí se cuentan como registros distintos, como hace el anexo.

Para comprobar «sobre todo de fidelidad y de respaldo», se revisaron los criterios de las 22 filas: 15 mencionan el criterio 3 y 10 mencionan el criterio 4. Son los dos más frecuentes y pueden coincidir en una fila. La Tabla B2 asigna 9 casos a «Respaldo», sin explicar esa diferencia de clasificación; el borrador de Conclusiones no reproduce ese desglose y su afirmación sobre el predominio se sostiene con ambos recuentos. La ausencia de fuentes inexistentes se refiere a lo señalado en estos informes, tal como dice el borrador.

### Revisión de prosa y respaldo

- **Criterio 4 — Respaldo:** no se detectaron datos externos nuevos, definiciones normativas ni hallazgos empíricos externos introducidos sin cita. Las cifras del taller y de las auditorías tienen los orígenes internos comprobados arriba. Las conclusiones interpretativas se presentan como balance del trabajo.
- **Criterio 7 — Argumento:** B1 sintetiza PI-1 a PI-4; B2 responde PI-5; B3 responde la pregunta-problema; B4 desarrolla las tres lecciones técnicas; B5 formula el balance metodológico previsto. La respuesta afirmativa está condicionada y B4 conserva el límite sobre regresiones pequeñas.
- **Criterio 8 — Legibilidad:** cada párrafo tiene una idea central y las transiciones enlazan revisión, demostración, respuesta y balance. No hay encadenamiento de citas ni anuncios sobre lo que hará el texto.
- **Criterio 9 — Densidad y selección:** la ausencia de citas externas es compatible con el modo ligero y con una síntesis de contenido ya desarrollado. Las cifras elegidas sostienen el argumento; la precisión sobre el costo inicial se recoge en la sugerencia 3.
- **Criterio 10 — Contenido interno:** las preguntas se integran en la argumentación, sin copiar listas de objetivos o de alcance. PI-1 a PI-4 aparecen una vez en B1; PI-5, una vez en B2; la pregunta-problema, en B3.
- **Criterio 11 — Metacomentarios:** excepción aplicada exclusivamente a B5 y registrada como sugerencia 1. El comentario HTML de versión es un registro editorial oculto y no se cuenta como prosa del documento.
- **Criterio 13 — Terminología:** p95, *throughput*, tasa de error, línea base, umbral, candado y los nombres en código de las variantes conservan las formas del glosario. Sus primeras definiciones están en las secciones anteriores; no hace falta reintroducirlas en Conclusiones. La única sugerencia terminológica es la denominación de la *quality gate*.
- **Criterio 14 — Tablas y figuras:** el plan no prevé ninguna y el borrador no incluye ninguna. No falta material gráfico ni corresponde exigir numeración, título u origen. Las remisiones a 3.1–3.3, 5.3–5.8 y al anexo B llegan a contenido existente.

**Extensión:**

| Bloque | Plan | Margen ±10 % | Borrador | Diferencia | Resultado |
|---|---:|---:|---:|---:|---|
| B1. Hallazgos por pregunta de investigación | 125 | 112,5–137,5 | 135 | +8,0 % | Dentro del margen |
| B2. Respuesta a PI-5 | 75 | 67,5–82,5 | 66 | −12,0 % | Por debajo |
| B3. Respuesta a la pregunta-problema | 75 | 67,5–82,5 | 66 | −12,0 % | Por debajo |
| B4. Balance técnico | 90 | 81–99 | 77 | −14,4 % | Por debajo |
| B5. Reflexión sobre el uso de la IA | 85 | 76,5–93,5 | 76 | −10,6 % | Por debajo |
| **Total** | **450 en los bloques; 460 en la cabecera del plan** | **405–495; 414–506, respectivamente** | **420** | **−6,7 %; −8,7 %** | **Dentro de ambos márgenes totales** |

Conteo reproducible: unidades separadas por espacios en el texto visible de cada párrafo, incluidas las remisiones internas; se excluyen el título y los comentarios HTML y se retiran las marcas de cursiva y código. El plan tiene una diferencia interna de 10 palabras entre su cabecera y la suma de los bloques; no altera el resultado global. No hay tablas ni figuras cuyo espacio deba informarse aparte. El ajuste a una página depende de la maquetación y no se deduce solo del conteo.

La aprobación se sostiene en la ausencia de hallazgos bloqueantes. Se escribió únicamente este informe; no se corrigieron el borrador, el plan, la evidencia, los anexos ni los demás archivos de origen.
