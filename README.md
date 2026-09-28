# Proyecto Final — Investigación asistida por IA

**Curso:** *Investigación asistida por inteligencia artificial: aplicación en ondas gravitacionales* (Zaldarriaga), FCEN-UBA, 2026.
**Autores:** Lautaro Silva Pizzi y Manuel Racca.
*(English version: [`README.en.md`](README.en.md))*

Este repositorio documenta un **estudio de caso**: cómo se usaron agentes de IA (Claude Code y Codex) en una investigación real, la tesis de licenciatura de L. Silva Pizzi sobre las asimetrías azimutales de la densidad de muones medidas con el Detector Subterráneo de Muones (UMD) del Observatorio Pierre Auger.

➡️ **Empezar por el informe breve (4 páginas): [`informe/informe_breve.pdf`](informe/informe_breve.pdf)**
La versión extendida (16 páginas, con la cronología completa y la metodología) es [`informe/informe.pdf`](informe/informe.pdf).

---

## La historia en un párrafo

En simulaciones Monte Carlo, la amplitud de la asimetría azimutal ($A_1$) del número de muones que atraviesan los tanques del detector de superficie (SD) **cambiaba de signo** a grandes distancias del núcleo de la lluvia. En el UMD, en cambio, no cambiaba. Durante casi dos semanas, el tesista y varios agentes buscaron una explicación física: divergencia cinemática, geometría del tanque, atenuación, dispersión. La respuesta resultó ser un **sesgo de selección**: el observable del SD sólo incluía estaciones presentes en el evento reconstruido. Incluyendo todas las estaciones simuladas, la inversión desaparece.

Lo más interesante para el curso es que **un subagente de Claude propuso esa hipótesis el 7/09, pero se descartó con un test que no podía detectarla**. Tres días después, **Codex (modelo «Astra») rechazó esa conclusión heredada** y demostró el efecto. Después, ambos modelos se revisaron mutuamente.

## Estructura del repositorio (en orden cronológico)

| Carpeta | Qué contiene | Quién | Fecha |
|---|---|---|---|
| [`informe/`](informe/) | **Informes finales (PDF):** breve, 4 pp. (`informe_breve.pdf`), y extendido, 16 pp. (`informe.pdf`) | — | sep. 2026 |
| [`00_punto_de_partida_notas_GAP/`](00_punto_de_partida_notas_GAP/) | Punto de partida: la nota interna previa (versión vieja, con el argumento de divergencia cinemática), la nota publicada GAP-2026-041 y una nota inconclusa sobre el sesgo de reconstrucción del núcleo | tesista | antes de ago. 2026 |
| [`01_contexto_y_prompts/`](01_contexto_y_prompts/) | La «memoria de proyecto»: `CLAUDE.md` (reglas y mapa del repositorio que leen los agentes), `AGENTS.md` (hace que Codex lea lo mismo), los prompts de revisión y la memoria persistente de Claude (lecciones aprendidas de correcciones del tesista) | tesista + Claude | 29/08 → |
| [`02_revisiones_claude_notas_GAP/`](02_revisiones_claude_notas_GAP/) | Primeras revisiones de las notas GAP por Claude, en cuatro versiones sucesivas (v1–v4) | Claude (Sonnet 5 / Opus 5) | 29/08–02/09 |
| [`03_divergencia_cinematica_claude/`](03_divergencia_cinematica_claude/) | Cuaderno explicativo de la divergencia cinemática, corrección del cálculo ponderado por espectro y borradores de capítulos | Claude | 03/09–07/09 |
| [`04_modelo_unificado_claude/`](04_modelo_unificado_claude/) | Modelo unificado, con una retractación documentada. **Aquí está el casi-hallazgo descartado** (§5 de `report.md`) | Claude | 07/09–10/09 |
| [`05_revision_astra_codex_sesgo_seleccion/`](05_revision_astra_codex_sesgo_seleccion/) | **El hallazgo del sesgo de selección.** Empezar por `README.md` o `RESUMEN_PARA_DIRECCION.pdf` | Codex («Astra», gpt-6-astra) | 10/09–17/09 |
| [`06_revision_cruzada_claude_sobre_astra/`](06_revision_cruzada_claude_sobre_astra/) | Revisión escéptica de Claude sobre el trabajo de Astra, con un subagente adversarial. Veredicto: «parcialmente de acuerdo» | Claude + 6 subagentes + 1 adversarial | 11/09 |
| [`07_reprocesamiento_claude/`](07_reprocesamiento_claude/) | Nuevo lector que conserva todas las estaciones simuladas; confirmación sobre el pipeline del tesista | Claude (Opus 5) | 17/09–24/09 |
| [`08_charla_RAFA_2026/`](08_charla_RAFA_2026/) | Charla en la reunión RAFA 2026, con el resultado presentado como «análisis preliminar» | tesista + Claude | 10/09–17/09 |
| [`09_borradores_capitulos_astra/`](09_borradores_capitulos_astra/) | Borradores de los capítulos 3, 5 y 6 de la tesis, escritos por tres subagentes de Codex (uno por capítulo) con un integrador | Codex | 24/09 |
| [`10_estudio_de_caso/`](10_estudio_de_caso/) | **Cómo se hizo este estudio:** notas de evidencia por fuente, cronología verificada, análisis, verificación cruzada, revisión adversarial del informe, fuentes LaTeX y figuras | Claude (Opus 5.5) + 10 agentes | 24/09– |

### Dentro de `10_estudio_de_caso/`
- `timeline.md`: la cronología verificada; cada evento cita su evidencia (commit, archivo o transcripción).
- `notes/`: una nota por fuente (transcripciones de Claude y de Codex, historial de git, artefactos, trabajo previo). También `crosscheck_phase1.md` (21 afirmaciones verificadas contra las fuentes primarias) y `analysis.md`.
- `report/`: fuente LaTeX del informe y `REVISION_ADVERSARIAL_v1.md` (las 61 observaciones del revisor adversarial, aplicadas en la versión actual).
- `PROGRESS.md`: registro paso a paso del trabajo, incluidas las fallas del propio proceso.
- `questions/`: preguntas al tesista y sus respuestas (`answers_2026-09-28.md`).

## Notas
- Todos los resultados físicos son **simulaciones Monte Carlo**: 20 archivos, protones, SIBYLL 2.3e, 30°–40° de ángulo cenital.
- Las transcripciones completas de las sesiones con los agentes **no se incluyen**, porque contienen rutas de servidores internos de la colaboración. El script que las convierte a texto está en `10_estudio_de_caso/notes/tools/`.
- Casi todo el material de trabajo de los agentes (notas, código, comentarios) está en inglés; el informe y los borradores de la tesis están en castellano.
- Las notas GAP son documentos internos de la Colaboración Pierre Auger.
