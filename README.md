# Una inversión que no era física: un estudio de caso de investigación asistida por IA

**Curso:** *Investigación asistida por inteligencia artificial: aplicación en ondas gravitacionales* (M. Zaldarriaga), FCEN-UBA, 2026
**Autores:** Lautaro Silva Pizzi y Manuel Racca

Este repositorio documenta cómo se usaron agentes de IA para programación (**Claude Code** y **OpenAI Codex**) en un problema de investigación real y en curso: la tesis de licenciatura de L. Silva Pizzi (FCEN-UBA / ITeDA) sobre las asimetrías azimutales de la densidad de muones medidas con el Detector Subterráneo de Muones (UMD) del Observatorio Pierre Auger. Reconstruimos el proceso a partir de evidencia primaria (149 *commits*, 49 registros de sesiones de los agentes y todos los documentos que produjeron) y nos hicimos una pregunta: **¿los agentes ayudaron o entorpecieron el descubrimiento de que un efecto aparentemente físico era un artefacto de selección?**

➡️ **Empezar por el informe breve (4 páginas): [`informe/informe_breve.pdf`](informe/informe_breve.pdf)**
La versión extendida (16 páginas, con la cronología completa y la metodología) es [`informe/informe.pdf`](informe/informe.pdf).

---

## La historia en breve

- **El problema.** En simulaciones Monte Carlo, la amplitud del primer armónico azimutal $A_1$ en $\rho(\varphi)=\rho_0(1+A_1\cos\varphi)$ del número de muones en los tanques de agua del detector de superficie (SD) **cambia de signo** lejos del núcleo de la lluvia. En el UMD, que está enterrado, no. Durante unas dos semanas, el tesista y varios agentes buscaron una explicación física: divergencia cinemática, geometría del tanque, atenuación, dispersión coulombiana.
- **La respuesta.** Era un **sesgo de selección**. El observable del SD sólo incluía estaciones presentes en el evento *reconstruido*. Incluyendo todas las estaciones simuladas, la inversión desaparece ($A_1 = +0.069$ en lugar de $-0.124$ a 1200–1350 m).
- **El casi-hallazgo.** El **7/09**, un subagente de Claude señaló la línea exacta del código (`HasStation` en `Procesamiento_ADST_v8-2.py:182`) y describió el mecanismo. Esa misma sesión lo descartó con un test que *no podía* detectar ese tipo de sesgo. El prompt que Claude escribió después para Codex dio ese descarte por «establecido».
- **El rescate.** El **10/09**, a los 12 minutos de su primera sesión, **Codex (modelo `gpt-6-astra`, «Astra»)** leyó el código, rechazó la conclusión heredada y corrió el contrafactual correcto sobre los archivos crudos de simulación: $+0.068 \to -0.095$.
- **Revisión cruzada.** Después, Claude revisó a Astra con un subagente adversarial. Claude corrigió un error de Astra que eliminaba filas, y que el tesista había detectado por el conteo de filas. Astra auditó el reprocesamiento final de Claude.

**Qué funcionó:** una lectura independiente por un segundo modelo, reproducir los resultados antes de extenderlos, un archivo de memoria persistente del proyecto (`CLAUDE.md`) y el control humano de los *commits*, las fusiones y el cómputo pesado.
**Qué falló:** un test que no podía fallar, resúmenes que perdieron el detalle clave, una afirmación de «verificado» que no lo era, código entregado sin ejecutar y una operación de git destructiva.

## Estructura del repositorio (en orden cronológico)

| Carpeta | Contenido | Producido por | Fechas (2026) |
|---|---|---|---|
| [`informe/`](informe/) | **Informes finales (PDF):** versión breve, 4 pp. (`informe_breve.pdf`), y versión extendida, 16 pp. (`informe.pdf`) | — | sep. |
| [`00_punto_de_partida_notas_GAP/`](00_punto_de_partida_notas_GAP/) | Punto de partida: el borrador anterior de la nota interna (con el argumento de divergencia cinemática), la nota publicada GAP-2026-041 y una nota inconclusa sobre el sesgo de reconstrucción del núcleo | tesista | antes de ago. |
| [`01_contexto_y_prompts/`](01_contexto_y_prompts/) | «Memoria del proyecto»: `CLAUDE.md` (reglas y mapa del repositorio que leen los agentes), `AGENTS.md` (hace que Codex lea el mismo archivo), los prompts de revisión y la memoria persistente de Claude (lecciones de las correcciones del tesista) | tesista + Claude | 29/08 → |
| [`02_revisiones_claude_notas_GAP/`](02_revisiones_claude_notas_GAP/) | Primeras revisiones de las notas GAP por Claude, cuatro versiones sucesivas (v1–v4) | Claude (Sonnet 5 / Opus 5) | 29/08–02/09 |
| [`03_divergencia_cinematica_claude/`](03_divergencia_cinematica_claude/) | Cuaderno explicativo de la divergencia cinemática, el cálculo ponderado por espectro corregido y borradores de capítulos de la tesis | Claude | 03–07/09 |
| [`04_modelo_unificado_claude/`](04_modelo_unificado_claude/) | Modelo unificado de la asimetría, con una retractación documentada. **Contiene el casi-hallazgo descartado** (§5 de `report.md`) | Claude | 07–10/09 |
| [`05_revision_astra_codex_sesgo_seleccion/`](05_revision_astra_codex_sesgo_seleccion/) | **El hallazgo del sesgo de selección.** Empezar por `README.md` o `RESUMEN_PARA_DIRECCION.pdf` | Codex («Astra») | 10–17/09 |
| [`06_revision_cruzada_claude_sobre_astra/`](06_revision_cruzada_claude_sobre_astra/) | Revisión escéptica de Claude sobre el trabajo de Astra (6 subagentes de revisión + 1 adversarial). Veredicto: «parcialmente de acuerdo» | Claude | 11/09 |
| [`07_reprocesamiento_claude/`](07_reprocesamiento_claude/) | Nuevo lector que conserva todas las estaciones simuladas; confirmación sobre el pipeline del propio tesista | Claude (Opus 5) | 17–24/09 |
| [`08_charla_RAFA_2026/`](08_charla_RAFA_2026/) | Charla en el congreso RAFA 2026, que presenta el resultado como preliminar | tesista + Claude | 10–17/09 |
| [`09_borradores_capitulos_astra/`](09_borradores_capitulos_astra/) | Borradores de los capítulos 3, 5 y 6 de la tesis, escritos por tres subagentes de Codex (uno por capítulo) más un integrador | Codex | 24/09 |
| [`10_estudio_de_caso/`](10_estudio_de_caso/) | **Cómo se hizo este estudio de caso:** notas de evidencia por fuente, cronología verificada, análisis, verificación cruzada de 21 afirmaciones clave, revisión adversarial del informe (61 observaciones), fuentes LaTeX y figuras | Claude (Opus 5.5) + 10 subagentes | 24–28/09 |

### Dentro de `10_estudio_de_caso/`
- `timeline.md`: la cronología verificada; cada evento cita su evidencia (commit, archivo o registro de sesión).
- `notes/`: una nota de evidencia por familia de fuentes (registros de sesiones de Claude y de Codex, historial de git, material producido por los agentes y el trabajo previo a la IA), más `crosscheck_phase1.md` y `analysis.md`.
- `report/`: las fuentes LaTeX de ambos informes y `REVISION_ADVERSARIAL_v1.md`, con las 61 observaciones del revisor adversarial, todas aplicadas.
- `PROGRESS.md`: registro paso a paso del trabajo, incluidas las fallas de nuestro propio proceso.
- `questions/`: las preguntas que se le hicieron al tesista y sus respuestas.

## Notas
- **Todos los resultados físicos son simulaciones Monte Carlo:** 20 archivos, primarios protón, SIBYLL 2.3e, ángulo cenital de 30° a 40°. El mecanismo físico detrás de la selección sigue siendo una hipótesis.
- **No se incluyen los registros crudos de las sesiones con los agentes,** porque contienen rutas de servidores internos de la colaboración. El script que los convierte a texto legible está en `10_estudio_de_caso/notes/tools/`.
- **Idioma:** el material de trabajo de los agentes está mayormente en inglés; los informes y los borradores de la tesis, en castellano.
- **Documentos internos:** las notas GAP son documentos internos de la Colaboración Pierre Auger.
