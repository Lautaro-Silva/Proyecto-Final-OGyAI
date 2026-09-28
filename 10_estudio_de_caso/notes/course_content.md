# Course content — for the "links to the course" section

Fetched 2026-09-24 from https://asignaturas.df.uba.ar/iapiaaeog-zaldarriaga/ (pages `programa/`,
`cronograma/`, `referencia/`, `bienvenidos-a-la-materia/`). The summaries were produced by a
fetch tool, so re-check exact wording against the pages before quoting them in the report.

## Facts about the course
- "Investigación asistida por inteligencia artificial: aplicación en ondas gravitacionales" (Zaldarriaga). 5 classes × 4 h, **Fri 28/08 → Thu 03/09/2026**. Final presentations are virtual.
- Objective: "usar agentes de inteligencia artificial como asistentes para la investigación científica"; skills: exploring problems, learning tools, programming, analyzing results, communicating conclusions.
- Each student got **Pro access to an AI agent (Claude Code, Codex or similar)**.
- Final project: team-based, either one of the proposals (reproducing results, catalog exploration, background modelling, ML classification) or **self-designed**. Present and answer questions "como en un ámbito de investigación científica".
- Schedule: 28/08 "Primeros pasos con Claude Code"; 31/08 LVK; 01/09 PTAs ("Simulación de datos PTA con IA"); 02/09 astrophysical modelling; 03/09 "Futuro de OG e IA en ciencia" + start of final projects.

**Timeline link (verified from the transcript index):** the first Claude Code session in this repo is 2026-08-29, the day after the "Primeros pasos con Claude Code" class. The CLAUDE.md creation, the first thesis review and the GAP-notes review (08-29 → 09-02) all ran **during the course week**. `[ASK author]` whether the course's Pro access is what enabled this.

## Course AI readings (bibliography "AI-Assisted Research in Physics")
1. **M. Schwartz, "Vibe physics: The AI grad student"**, Anthropic Science Blog (Mar 2026). Supervised Claude Opus 4.5 through a QFT project ("G2 level").
   - Failure modes: "It says 'verified' when it hasn't actually checked"; "adjusting parameters to make plots match rather than finding actual errors"; the keystone formula was initially wrong; "Claude loves to please".
   - Practices: hierarchical task files ("things it can retrieve rather than things it has to hold in context"); **cross-verification: "I had GPT check Claude's work and vice versa."** (verbatim; re-verified 2026-09-24. CORRECTION: the sentence "They caught each other's errors" that an earlier fetch summary attached to it does NOT appear in the article. It was invented by the fetch tool's summarizer. Other verified verbatim quotes: "It says 'verified' when it hasn't actually checked."; "I think we can distill what is missing in current LLMs to a single word: _Taste_."; "If all three agreed, it was a good indication it was correct." Mishra-Sharma, verbatim: "The failed approaches are important—without them, successive sessions will re-attempt the same dead ends."; "long-running autonomous scientific work today crucially depends on the agent having a way to know whether it's making progress."); CLAUDE.md rules against skipping steps; ask repeatedly "until it finds no others"; domain expertise essential for verification.
   - Remaining bottleneck: **"taste"**, i.e. judgment about which directions are fruitful. Advice to experimentalists: "no amount of compute can tell Claude what is actually in a human cell."
2. **S. Mishra-Sharma, "Long-running Claude for scientific computing"**, Anthropic Science Blog (Mar 2026).
   - CHANGELOG/progress file as "portable long-term memory… lab notes", including **"failed approaches and why they didn't work"** so sessions don't retread dead ends.
   - CLAUDE.md as the plan, which Claude may update.
   - **Test oracles**: "the agent having a way to know whether it's making progress".
   - Commit/push checkpoints; detach-and-check-in autonomy.
3. **OpenAI Academy, "How Physicists Are Using AI to Chase New Physics"** (Mar 2026). The FERMIACC agent pipeline (hypothesis → simulation → comparison with data → scored verification). A cautionary tale about the LHC 750 GeV false excess (~500 papers). "In ChatGPT a model can be a clever collaborator… through the API it begins to serve as scientific infrastructure."
4. **S. Dodelson, "Evolving Dark Energy and AI"**, Substack (Feb 2026). Codex reproduced a model fit on DESI data in minutes. Turning it into a quality paper still "requires more than just polishing text": expert validation.

## Candidate mappings to this case (to be confirmed by Phase-1 evidence)

| Course idea | Our case |
|---|---|
| Cross-verification GPT ↔ Claude (Schwartz) | Claude reviews Astra (`REVIEW_ASTRA`); does Astra review Claude's phenomenology? |
| "Says verified when it hasn't" | Check: the unexecuted `dos_rutas` script; claims of replication resting on one CSV |
| Tuning to match rather than finding errors | Phenomenological passes: were models tuned to fit the SD inversion rather than questioning the data? `[to evaluate]` |
| Progress file with failed approaches (Mishra-Sharma) | CLAUDE.md §6 (Fast-MC dead end), the unified-model "retracted dead-end lead", this project's PROGRESS.md |
| Test oracle | UMD as a quasi-oracle (the predicted +0.13 vs observed +0.11 matched; the SD didn't) → pointed to an SD-specific issue |
| "Taste" remains human | Who chose to question the pipeline rather than the physics? `[key question]` |
| False-alarm cost (LHC 750 GeV) | Months of phenomenology aimed at a selection artifact |
