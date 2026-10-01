# Una inversión que no era física

**Primer borrador · Charla del curso · 15–20 minutos**

Lautaro Silva Pizzi y Manuel Racca · FCEN-UBA · 2026

Propuesta: 12 diapositivas, unos 18 minutos, sin contar preguntas. Cada sección separa el texto breve para proyectar del guion oral. Los tiempos incluyen explicar las figuras y hacer pausas; deben ajustarse en un ensayo. Reparto entre expositores pendiente. Este archivo es el borrador editable del contenido, todavía no una presentación diagramada.

## 1. Una anomalía, dos agentes y una pregunta — 1 min

**En pantalla**

- Una inversión que no era física.
- ¿Cómo ayudó la IA a descubrir un sesgo de selección?
- Caso real de una tesis de física en el Observatorio Pierre Auger.

**Para decir**

Hoy vamos a contar una investigación en la que se buscó explicar un resultado extraño de unas simulaciones. Había una diferencia entre dos detectores y parecía exigir una explicación física. La respuesta terminó estando en la selección de los datos. Nos interesa especialmente cómo se llegó a esa respuesta: los agentes de inteligencia artificial propusieron ideas, escribieron código y se revisaron entre sí. También descartaron una hipótesis correcta y cometieron errores que tuvo que detectar el investigador.

La pregunta de nuestra presentación es qué podemos aprender de ese proceso para trabajar con IA en investigación.

Fuente: informe extendido, Introducción y Conclusiones.

## 2. La física mínima para seguir la historia — 1 min 30 s

**En pantalla**

- Un rayo cósmico produce una lluvia de partículas en la atmósfera.
- SD: detectores de superficie. UMD: detectores subterráneos de muones.
- En una lluvia inclinada, dos lados pueden recibir distintas densidades.
- En esta charla: resultados de **simulaciones**, no de datos reales.

**Para decir**

Los detectores toman muestras de una lluvia de partículas en distintos puntos. Para esta historia nos interesan los muones. El SD está en la superficie y el UMD está enterrado; no son detectores equivalentes y sus respuestas no tienen por qué coincidir exactamente.

El análisis compara regiones alrededor del eje de una lluvia inclinada. Se llaman temprana y tardía según cuál alcanza primero el frente. Un número, A uno, resume esa diferencia: con la convención usada, positivo significa exceso del lado temprano. No necesitamos seguir la derivación matemática, pero sí recordar que un cambio de signo cambia qué lado predomina.

Fuente: informe extendido, Contexto científico.

## 3. El resultado que queríamos explicar — 1 min 30 s

**En pantalla**

- Lejos del núcleo, la asimetría de los muones del SD se volvía negativa.
- La del UMD seguía siendo positiva.
- Primera interpretación: buscar un mecanismo físico.

**Visual:** [figura original de la anomalía](10_estudio_de_caso/figures/sd_desglose_componentes_vs_umd.pdf). Señalar la componente muónica del SD y el UMD; no confundir muones con señal total del tanque.

**Para decir**

En este gráfico, el eje horizontal es la distancia al núcleo de la lluvia y el vertical mide la asimetría. La curva de muones del SD cruza el cero a grandes distancias. La del UMD no. Esa diferencia motivó buscar explicaciones relacionadas con la propagación de muones, la geometría de los tanques y los umbrales de los detectores.

La investigación estaba orientada a explicar el fenómeno. La posibilidad de que el propio análisis produjera la inversión no se había comprobado adecuadamente. Ese punto de partida condicionó también las preguntas que recibieron los agentes.

Fuente: informe extendido, Contexto científico y Cronología.

## 4. Cómo se incorporaron los agentes — 1 min 30 s

**En pantalla**

- Claude Code y Codex leían archivos, proponían pruebas y escribían código.
- Contexto compartido: `CLAUDE.md` y `AGENTS.md`.
- El investigador discutía la física y revisaba los resultados.

**Visual:** [flujo de trabajo](10_estudio_de_caso/figures/workflow.pdf).

**Para decir**

No se usó solamente un chat al que se le pegaban preguntas. Los agentes podían trabajar sobre el repositorio y consultar el código y los documentos. Un archivo de contexto guardaba las reglas del proyecto, su organización y algunas lecciones de errores anteriores. Eso permitía retomar el trabajo en otra sesión.

Los agentes exploraron varias explicaciones físicas. El tesista corrigió errores de esas explicaciones y los agentes también corrigieron aspectos de su razonamiento. La memoria ayudaba a mantener continuidad, pero una conclusión equivocada guardada como cierta podía orientar mal el trabajo siguiente.

Fuente: informe extendido, Incorporación de agentes y Cómo trabajamos con los agentes; contexto histórico en `01_contexto_y_prompts/`.

## 5. La hipótesis correcta apareció el 7 de septiembre — 1 min 30 s

**En pantalla**

- Un subagente señaló el requisito `HasStation`.
- Pregunta clave: ¿qué estaciones llegan a la muestra?
- La hipótesis se descartó con una prueba que no la evaluaba.

**Para decir**

Un subagente de Claude encontró un requisito del código: la estación debía aparecer en el evento reconstruido. Señaló que esto podía seleccionar estaciones de manera distinta en las dos regiones y cambiar el promedio de muones entre las que sobrevivían.

La respuesta fue hacer una prueba estadística que igualaba el número de filas de los grupos. Como el resultado no cambiaba, se interpretó que la selección quedaba descartada. Pero esa prueba examinaba el efecto de tener diferentes cantidades de filas. No recuperaba las estaciones excluidas. Había una hipótesis relevante, pero la prueba elegida no podía refutarla.

Fuente: informe extendido, El casi-hallazgo del 7/09; `10_estudio_de_caso/notes/crosscheck_phase1.md`.

## 6. Por qué esa prueba no alcanzaba — 2 min

**En pantalla**

Ejemplo inventado para explicar la selección; **no son datos del experimento**:

| Grupo | Valores completos | Media completa | Valores conservados | Media seleccionada |
|---|---|---:|---|---:|
| A | 2, 4, 6, 8 | 5 | 2, 4, 6, 8 | 5 |
| B | 1, 3, 5, 7 | 4 | 5, 7 | 6 |

- Antes: media A > media B. Después: media A < media B.
- Igualar cantidades dentro de lo conservado no recupera lo perdido.

**Para decir**

Imaginemos dos grupos. En la población completa, el promedio de A es cinco y el de B es cuatro. Ahora supongamos que del grupo B sólo conservamos los valores altos. Su promedio pasa a seis y el orden se invierte.

Si tomamos al azar dos valores del grupo A para igualar tamaños, su promedio esperado sigue siendo cinco. El del B seleccionado sigue siendo seis. Repetir ese muestreo no devuelve los valores uno y tres que ya quedaron afuera.

Esta es la diferencia entre tener pocos datos y tener datos seleccionados. El problema de la prueba original es que trabajaba dentro de una muestra que ya había perdido información. Para comprobar la hipótesis había que volver a una población que incluyera las estaciones excluidas.

Fuente del argumento: informe extendido, párrafo posterior al casi-hallazgo. Tabla: ilustración didáctica nueva, no reproducción del bootstrap original.

## 7. Una duda se convirtió en una certeza heredada — 1 min 30 s

**En pantalla**

Hipótesis de selección → prueba insuficiente → informe que la descarta → prompt para otro agente.

**Para decir**

La falla no terminó en la prueba. El informe perdió el detalle concreto del requisito señalado por el subagente. Después, Claude escribió un prompt para Codex que presentaba ese descarte como algo establecido, aunque también pedía explorar una posible selección a nivel de detector.

Así, el agente siguiente recibió una conclusión con más seguridad de la que justificaba la evidencia. Esto nos parece uno de los aprendizajes principales del caso: cuando resumimos trabajo o lo pasamos a otro agente, debemos conservar qué se probó, con qué datos y qué quedó sin resolver. Un resumen puede ser muy claro y aun así transmitir una premisa falsa.

Fuente: informe extendido, Astra y el sesgo de selección; verificación del prompt en `10_estudio_de_caso/notes/crosscheck_phase1.md`.

## 8. El 10 de septiembre: comparar las dos poblaciones — 2 min

**En pantalla**

- Codex volvió al código y cuestionó el descarte.
- Comparó todas las estaciones simuladas disponibles con las seleccionadas.
- En 1200–1350 m: **+0,069 sin requisito → −0,124 con requisito**.
- UMD: +0,082; también es una población seleccionada.

**Visual:** [comparación después del reprocesamiento](10_estudio_de_caso/figures/SD_sin_corte_vs_UMD_reprocesado_v13.pdf).

**Para decir**

Codex, usando el modelo llamado Astra en este trabajo, leyó el código y advirtió que la prueba anterior no descartaba el sesgo. Luego comparó estaciones simuladas antes y después del requisito. La inversión aparecía al seleccionar la población.

El gráfico muestra la confirmación posterior con el reprocesamiento del pipeline del tesista. En la banda que destacamos, la asimetría del SD es positiva antes de seleccionar y negativa después. El valor del UMD sirve como referencia, pero no es una muestra libre de selección.

Hay un detalle importante: no bastaba con borrar una condición del código. El lector original recorría contadores UMD que ya dependían del disparo del SD. Hubo que guardar por separado las estaciones simuladas del SD para recuperar la población faltante. La conclusión es sobre las poblaciones comparadas en esta simulación.

Fuente: `05_revision_astra_codex_sesgo_seleccion/RESUMEN_PARA_DIRECCION.md`; `07_reprocesamiento_claude/README.md`; informe extendido. No mezclar estos números con +0,068 y −0,095 del primer control, que usa otra banda radial y otro procedimiento de estimación.

## 9. Encontrar el problema no eliminó los errores — 1 min 30 s

**En pantalla**

- Un lector de Codex perdía 63.747 filas.
- El tesista lo detectó contando filas.
- Claude corrigió el lector; Codex auditó el reprocesamiento.
- La revisión funcionó en ambas direcciones.

**Para decir**

Sería engañoso contar esta historia como un agente que se equivocó y otro que hizo todo bien. Codex también entregó un lector que perdía filas. El investigador lo detectó con una comprobación sencilla: comparar los conteos. Claude trabajó en la corrección y después Codex auditó los resultados.

Además, el primer control de Codex usaba un lector simplificado. Eso no equivalía a haber modificado solamente el pipeline original. La reproducción con el código del tesista fue un paso adicional importante. Encontrar una explicación prometedora y tener una implementación validada son avances distintos.

Fuente: informe extendido, Revisión cruzada; `07_reprocesamiento_claude/CAMBIOS.md` y `README.md`.

## 10. Qué nos llevamos para trabajar con IA — 1 min 30 s

**En pantalla**

1. Preguntar qué población representa cada resultado.
2. Preguntar si la prueba podría detectar el error buscado.
3. Guardar las dudas y los límites en la memoria del proyecto.
4. Reproducir resultados y vigilar conteos antes de extender código.

**Para decir**

Los agentes fueron útiles para explorar, programar y cuestionar argumentos. Pero una respuesta convincente no reemplazó una prueba adecuada. En este caso fueron decisivos tanto una lectura independiente como controles humanos muy concretos.

La memoria del proyecto también tiene que revisarse. Conviene registrar las conclusiones junto con su evidencia y su alcance. Si guardamos solamente el veredicto, una equivocación puede sobrevivir muchas sesiones. Y cuando pedimos una segunda opinión, esa revisión debe poder cuestionar las premisas, no limitarse a corregir el texto.

Fuente: informe extendido, Qué funcionó, Qué falló y Recomendaciones.

## 11. Qué demuestra este caso y qué queda abierto — 1 min

**En pantalla**

- La selección explica la inversión en la muestra simulada estudiada.
- No demuestra superioridad general de un modelo.
- Mecanismo físico detallado y controles adicionales: pendientes.
- La reconstrucción del caso también se hizo con ayuda de IA.

**Para decir**

Trabajamos con un solo caso. Los resultados se obtuvieron con veinte archivos simulados, protones, un modelo hadrónico y un rango angular específico. Persisten diferencias entre SD y UMD a distancias menores. No demostramos que toda la asimetría sea instrumental ni que un modelo sea mejor en general: cambiaron a la vez el modelo, el contexto y la forma de revisar el problema.

El informe reconstruyó el proceso a partir del historial y las sesiones, con verificaciones y una revisión adversarial. Aun así, también fue escrito con IA y tiene limitaciones. El testimonio del tesista es muy positivo, pero debe distinguirse de una comparación controlada de productividad.

Fuente: informe extendido, Cómo hicimos esta reconstrucción, La voz del tesista y Limitaciones; respuestas del 28/09.

## 12. Cierre — 30 s

**En pantalla**

**Antes de explicar un efecto, revisar cómo se construyó la muestra.**

Repositorio e informe: https://github.com/Lautaro-Silva/Proyecto-Final-OGyAI

**Para decir**

La hipótesis correcta apareció dos veces. Lo decisivo fue cómo se la puso a prueba. La IA ayudó a llegar al resultado, pero también propagó errores. Nuestra lección es combinar agentes capaces de cuestionar premisas con pruebas reproducibles y supervisión humana concreta.

Gracias.

## Preguntas posibles — material de apoyo, fuera del tiempo

**¿Fue un bug de Offline?** No se demostró eso. El resultado documentado es un sesgo respecto de la población de estaciones simuladas previa al requisito.

**¿Por qué no alcanza con igualar el número de datos?** Porque se muestrea entre los que sobrevivieron; no se restaura la distribución de los excluidos.

**¿Qué queda por comprobar?** El mecanismo ligado al disparo y a las componentes de señal; los directores pidieron, entre otros controles, revisar estaciones excluidas con un solo muon. El estado pendiente es el documentado al 28/09/2026, no una consulta nueva a los autores.

**¿El UMD demuestra cuál es el valor verdadero?** No. También está condicionado a la selección del SD; los resúmenes ausentes no pueden interpretarse como ceros físicos.

**¿Leyeron aquí las 49 sesiones originales?** El estudio previo las analizó. Para este borrador se consultaron los informes y las fuentes incluidas en el repositorio; los registros crudos de las sesiones no están publicados en él.

## Próxima revisión editorial

- Ensayar y ajustar tiempos; decidir quién presenta cada sección.
- Convertir el contenido aprobado en diapositivas y revisar la legibilidad de las figuras.
- Mantener el ejemplo inventado claramente separado de los resultados científicos.
- Actualizar los controles pendientes sólo si los autores aportan resultados nuevos.
