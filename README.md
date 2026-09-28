# An inversion that wasn't physics: a case study in AI-assisted research

**Course:** *Investigación asistida por inteligencia artificial: aplicación en ondas gravitacionales* (M. Zaldarriaga), FCEN-UBA, 2026
**Authors:** Lautaro Silva Pizzi and Manuel Racca
*(Versión en castellano: [`LEEME.md`](LEEME.md))*

This repository documents how AI coding agents (**Claude Code** and **OpenAI Codex**) were used in a real, ongoing research problem: L. Silva Pizzi's Licenciatura thesis (FCEN-UBA / ITeDA) on the azimuthal asymmetries of the muon density measured with the Underground Muon Detector (UMD) of the Pierre Auger Observatory. We reconstructed the process from primary evidence (149 git commits, 49 agent session logs and every document the agents produced) and asked one question: **did the agents help or hinder the discovery that an apparently physical effect was a selection artifact?**

➡️ **Start with the short report (4 pages): [`informe/informe_breve.pdf`](informe/informe_breve.pdf)** (in Spanish).
The extended version (16 pages, with the full chronology and methods) is [`informe/informe.pdf`](informe/informe.pdf).

---

## The story in brief

- **The puzzle.** In Monte Carlo simulations, the first-harmonic azimuthal amplitude $A_1$ in $\rho(\varphi)=\rho_0(1+A_1\cos\varphi)$ of the muon count in the surface-detector (SD) water tanks **changes sign** far from the shower core. The buried UMD does not. For about two weeks the thesis author and several agents looked for a physical explanation: kinematic divergence, tank geometry, attenuation, Coulomb scattering.
- **The answer.** It was a **selection bias**. The SD observable only included stations present in the *reconstructed* event. Including every simulated station, the inversion disappears ($A_1 = +0.069$ instead of $-0.124$ at 1200–1350 m).
- **The near-miss.** On **7 Sep**, a Claude subagent pointed to the exact line of code, `HasStation` in `Procesamiento_ADST_v8-2.py:182`, and described the mechanism. The same session then dismissed it with a test that *could not* detect this kind of bias. The prompt Claude later wrote for Codex called that dismissal "established".
- **The rescue.** On **10 Sep**, 12 minutes into its first session, **Codex (model `gpt-6-astra`, "Astra")** read the code, rejected the inherited conclusion, and ran the right counterfactual on the raw simulation files: $+0.068 \to -0.095$.
- **Cross-review.** Claude then reviewed Astra with an adversarial subagent. Claude caught a row-dropping bug in Astra's code, which the author had spotted from the row counts. Astra audited Claude's final reprocessing.

**What worked:** an independent reading by a second model, reproducing results before extending them, a persistent project-memory file (`CLAUDE.md`), and human control over commits, merges and heavy compute.
**What failed:** a test that couldn't fail, summaries that lost the key detail, a "verified" claim that wasn't, code delivered without being run, and a destructive git operation.

## Repository structure (chronological)

| Folder | Contents | Produced by | Dates (2026) |
|---|---|---|---|
| [`informe/`](informe/) | **Final reports (PDF, Spanish):** short version, 4 pp. (`informe_breve.pdf`), and extended version, 16 pp. (`informe.pdf`) | — | Sep |
| [`00_punto_de_partida_notas_GAP/`](00_punto_de_partida_notas_GAP/) | Starting point: the earlier internal note draft (with the kinematic-divergence argument), the published note GAP-2026-041, and an unfinished note on core-reconstruction bias | thesis author | before Aug |
| [`01_contexto_y_prompts/`](01_contexto_y_prompts/) | "Project memory": `CLAUDE.md` (rules and repository map read by the agents), `AGENTS.md` (makes Codex read the same file), the review prompts, and Claude's persistent memory (lessons from the author's corrections) | author + Claude | 29 Aug → |
| [`02_revisiones_claude_notas_GAP/`](02_revisiones_claude_notas_GAP/) | First Claude reviews of the GAP notes, four successive versions (v1–v4) | Claude (Sonnet 5 / Opus 5) | 29 Aug–2 Sep |
| [`03_divergencia_cinematica_claude/`](03_divergencia_cinematica_claude/) | Kinematic-divergence explainer notebook, the corrected spectrum-weighted calculation, draft thesis chapters | Claude | 3–7 Sep |
| [`04_modelo_unificado_claude/`](04_modelo_unificado_claude/) | Unified asymmetry model, with a documented retraction. **Contains the dismissed near-miss** (§5 of `report.md`) | Claude | 7–10 Sep |
| [`05_revision_astra_codex_sesgo_seleccion/`](05_revision_astra_codex_sesgo_seleccion/) | **The selection-bias finding.** Start with `README.md` or `RESUMEN_PARA_DIRECCION.pdf` | Codex ("Astra") | 10–17 Sep |
| [`06_revision_cruzada_claude_sobre_astra/`](06_revision_cruzada_claude_sobre_astra/) | Claude's skeptical review of Astra's work (6 review subagents + 1 adversarial). Verdict: "partially agree" | Claude | 11 Sep |
| [`07_reprocesamiento_claude/`](07_reprocesamiento_claude/) | New reader that keeps every simulated station; confirmation on the author's own pipeline | Claude (Opus 5) | 17–24 Sep |
| [`08_charla_RAFA_2026/`](08_charla_RAFA_2026/) | Conference talk (RAFA 2026) presenting the result as preliminary | author + Claude | 10–17 Sep |
| [`09_borradores_capitulos_astra/`](09_borradores_capitulos_astra/) | Draft thesis chapters 3, 5 and 6, written by three Codex subagents (one per chapter) plus an integrator | Codex | 24 Sep |
| [`10_estudio_de_caso/`](10_estudio_de_caso/) | **How this case study was made:** per-source evidence notes, verified timeline, analysis, cross-check of 21 key claims, adversarial review of the report (61 findings), LaTeX sources and figures | Claude (Opus 5.5) + 10 subagents | 24–28 Sep |

### Inside `10_estudio_de_caso/`
- `timeline.md`: the verified chronology; every event cites its evidence (commit, file or session log).
- `notes/`: one evidence note per source family (Claude and Codex session logs, git history, the agent-produced material, the pre-AI work), plus `crosscheck_phase1.md` and `analysis.md`.
- `report/`: the report's LaTeX source, and `REVISION_ADVERSARIAL_v1.md` with the adversarial reviewer's 61 findings, all applied.
- `PROGRESS.md`: step-by-step log of the work, including the failures of our own process.
- `questions/`: the questions put to the thesis author, with his answers.

## Notes
- **All physics results are Monte Carlo simulations:** 20 files, proton primaries, SIBYLL 2.3e, zenith 30°–40°. The physical mechanism behind the selection is still a hypothesis.
- **The raw agent session logs are not included,** because they contain internal collaboration server paths. The script that converts them to readable text is in `10_estudio_de_caso/notes/tools/`.
- **Language:** the agents' working material is mostly in English; the report and the thesis drafts are in Spanish.
- **Internal documents:** the GAP notes are internal documents of the Pierre Auger Collaboration.
