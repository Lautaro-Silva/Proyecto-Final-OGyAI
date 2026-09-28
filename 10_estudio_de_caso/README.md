# Proyecto Final IA — AI-assisted physics investigation, as a case study

Final project for the FCEN-UBA course **"Inteligencia Artificial Para Investigación en
Astrofísica de Ondas Gravitacionales"** (Zaldarriaga),
https://asignaturas.df.uba.ar/iapiaaeog-zaldarriaga/.

**Subject:** the Licenciatura thesis in this repository (azimuthal asymmetries of the muon
density measured with the AMIGA Underground Muon Detector, Pierre Auger Observatory), and
specifically how the thesis's key open question (the SD muon-asymmetry "sign inversion" at
large core distance) was investigated with AI assistance. The investigation first pursued
phenomenological explanations and ended by identifying an SD station-selection bias.

**Deliverables:**
1. A written report (course final-project format). Language and format are still TBD with the author.
2. A 15–20 min slide deck derived from the report, produced only after the report is approved.

## Ground rules (inherited from the repo `CLAUDE.md`; read it first, in full)

- Work only on branch `claude/proyecto-final-ia`. Never commit, add or push without the
  author's explicit go-ahead. Never push to `main`.
- Never reproduce internal collaboration-server paths or usernames (see CLAUDE.md §3).
- No heavy compute. This project is documentary: it reads evidence and does not rerun pipelines.
- Edit only the `.py` half of jupytext pairs, if a notebook is ever touched (it shouldn't need to be).
- **Evidence standard:** every factual claim in `timeline.md` and in the report must cite
  its evidence (commit hash, `path:line`, transcript session id plus timestamp, or "author
  testimony, date"). Anything unverified is tagged `[UNVERIFIED]` or `[ASK]`. No
  plausible-sounding fill-ins.
- Language: project meta-files (this README, PROGRESS, timeline, notes) are in English, per
  the repo convention. The report/slides language is decided with the author.

## Structure

| Path | Purpose |
|---|---|
| `README.md` | This file: purpose, rules, structure, how to resume |
| `PROGRESS.md` | Living log: steps done, sources used, findings, agent usage, TODO |
| `timeline.md` | Verified chronology; each entry carries its evidence and a verification status |
| `questions/experience.md` | Questions for the author about their personal experience (feeds the report's human side) |
| `questions/sources_and_facts.md` | Missing sources and factual ambiguities that only the author can resolve |
| `notes/` | Extracted evidence notes, one file per source family (git, scripts, lab notes, thesis, claude_work, transcripts, GAP notes) |
| `report/` | Report source and build script (after the format is confirmed) |
| `slides/` | Slide deck source (only after the report is approved) |
| `figures/` | Timeline and workflow diagrams, plus reused thesis figures with their source cited |

## Building

TBD once the format is confirmed. The plan is LaTeX: `report/build.sh` → `report/informe.pdf`,
and Beamer for the slides, reusing `claude_work/presentacion_rafa_2026/iteda_colores.tex`.

## For a future Claude session picking this up

1. Read the repo `CLAUDE.md`, then this README, then `PROGRESS.md` (especially the last
   entry and the TODO list), then `timeline.md`.
2. Check `questions/*.md` for answers the author may have added since the last session.
3. You are in (or should enter) the worktree for branch `claude/proyecto-final-ia`. The main
   checkout contains **untracked** folders that a fresh worktree does not have (e.g.
   `claude_work/REVIEW_ASTRA/`, `claude_work/unified_asymmetry_model_v1/`,
   `claude_work/borradores_capitulos_3_5_6_integrados_2026_09_24/`). Read those via the
   main checkout's absolute path. Don't `cd` there for git commands; git history is shared, so
   run git from the worktree.
4. After finishing a step, update `PROGRESS.md`, then copy this folder to the main checkout's
   `claude_work/Proyecto_Final_IA/` with plain `cp -r` (no git) so the author can see it.
5. Out of scope: `claude_work/auditoria_datos_campo_cap7/` and `claude_work/notebooks_a_py/`.
