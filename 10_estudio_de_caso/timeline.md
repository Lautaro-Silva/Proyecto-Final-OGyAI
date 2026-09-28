# Timeline (verified chronology)

Version 2 (2026-09-24, Step 2): consolidated from the Phase-1 notes in `notes/`. Each row
cites its evidence. `[X]` marks the claims in the cross-check list (`notes/crosscheck_phase1.md`);
they are pending until that file exists.

Status tags:
- `[GIT]`: commit metadata or message.
- `[TX]`: session transcript (`session-id @ UTC time`).
- `[ART]`: repository artifact.
- `[INF]`: inference.
- `[ASK]`: only the author can confirm.

Conventions:
- Times are **UTC** unless marked "local". Local time on the server is UTC−3.
- Commit author is always "Lautaro Silva". The actor is taken from Co-Authored-By trailers or transcripts.
- **A1 sign convention:** A1 > 0 means an early-side excess. "Inversion" means A1_SD,μ < 0 at large r.
- **The inversion appears WITH the `HasStation` requirement.** Far band 1050–1400 m: +0.068 (all simulated SD stations) → −0.095 (only those with a reconstructed partner). Far bin 1200–1350 m, weighted fit: +0.069 → −0.124, with UMD +0.082.

---

## Phase 0: Pre-AI thesis work (2025-09 → 2026-08-29), all by the author

| Date | Event | Evidence |
|---|---|---|
| 2025-09-01 | Repo created | `e6f0125` [GIT] |
| **2025-10-09** | `HasStation` check first appears, only as a null guard (the row is kept) | `e9a2737` [GIT] [X16] |
| 2025-11-04 | Lab notebook rule: keep quality cuts as **flags**, filter later. Applied to saturation ("¡TU IDEA! Creamos el flag en lugar de filtrar"), not to HasStation | `Trabajo.tex:168` [ART] |
| **2025-11-05 → 11-11** | HasStation becomes a hard `continue` ("Sin sdStation, no hay geometría"), then is labelled "Corte de Calidad 1: Geometría". Carried to `Procesamiento_ADST_v8-2.py:182-187`, Campo_v9, and the real-data `readADST_data_v19.py:157` | `41b98be`, `ce4e0eb` [GIT] |
| 2026-06-12 → 08-03 | Thesis text on the inversion written: "no es un artefacto de reconstrucción" (06_infill l.67), Population B with negative Billoir term (l.80–98), "no es una falla de Monte Carlo" (l.152–154). No later commits to Ch. 3/5/6 | [GIT] via P note |
| 2025-11-11 | "error fundamental" fixed: the Dense Ring φ double subtraction | `ce4e0eb` [GIT]; CLAUDE.md §7.1 |
| 2026-03-24 | Infill angle issue closed: "la funcion andaba" (GetAzimuthSP OK) | `b0f562d` [GIT] |
| 2026-03-30 | Thesis writing begins | `70a08a7` [GIT] |
| 2026-05-16 | Ch. 5 finished | `8a61ffa` [GIT] |
| 2026-06-03 | First real field data | `de902b0` [GIT] |
| 2026-07-13 | Fast-MC toy model abandoned (the first failed attempt to explain the SD inversion) | `6d6b97b` [GIT]; CLAUDE.md §6 |
| before 2026-08-29 | GAP note [Version_Vieja] (with the kinematic-divergence anti-asymmetry argument); the supervisor asks to remove it; **GAP-2026-041 published** | `GAP_Notes_Latex/` (in git only from `c915ce7`, 08-31) [ASK dates] |
| 2026-08-28 | Course class 1: "Primeros pasos con Claude Code" (Pro agent access granted) | course site [ART] |
| 2026-08-29 11:50 local | Last purely human commit | `2f92cbc` [GIT] |

## Phase 1: Onboarding and the first Claude reviews (08-29 → 09-02, during the course week)

| When | Actor | Event | Evidence |
|---|---|---|---|
| 08-29 14:53 | USER / sonnet-5 | Global Claude settings; model list | `630c3828` [TX] |
| 08-29 15:25–15:48 | sonnet-5 + 3 Explore subagents | **CLAUDE.md built** from 3 parallel read-only repo surveys. Committed and pushed *unprompted* (`fa012d6`) | `092c4841` [TX]; `fa012d6` [GIT] |
| 08-29 16:30–16:51 | USER | Three corrections: GetAzimuthSP not a bug; git "never" → "ask first"; Licenciatura ≈ Master's, UNSAM | `0a69fbb`, `32c6a4a`, `db90346` [GIT] |
| 08-29 17:31 | USER | First review prompt (ends in a literal `/model opus`, which had no effect). The session was killed by an API "can't help with this" error | `d79bb9f0` [TX] [X8] |
| 08-29 17:41 | sonnet-5 | Rewrites the prompt into `thesis_review_prompt.txt`. It adds "Treat the GAP notes as the more authoritative source" | `e5fa2ca0` [TX]; repo file [ART] |
| **08-29 17:46–17:54** | **sonnet-5** | **First completed review.** It judges removing the kinematic-divergence argument "justified" (tank side-wall confound) and GAP-041 "tightly argued". It flags the thesis's A_geo sign error | `c468bc17` [TX] [X8] |
| 08-29 18:18–18:29 | USER → sonnet-5 | The user relays the supervisor's objection. Math check of Eq. 9: algebra OK, but the net term is early-favouring for Population B (opposite to the narrative) | `c468bc17` [TX] |
| 08-31 18:07 | USER | Discovers `opusplan` (Opus plans, Sonnet executes) after Claude said it wasn't possible | `630c3828` [TX] |
| 08-31 19:11–19:20 | sonnet-5 | Commit on local main → branch, `reset --hard origin/main` (approved), force-push and `branch -D` (not separately approved) | `c468bc17` [TX]; reflog [GIT] |
| 08-31 19:23–19:33 | **opus-5** | Second review (v2 prompt: "build on prior notes, but re-verify"). It **corrects the first review**: the reasons were ranked wrong, the B&B figure was misread, and the replacement tank argument in GAP-041 is "wrong in sign" | `df3c0277` [TX] |
| 09-02 13:28 | sonnet-5 | Catches its own misattributed quotes | `df3c0277` [TX] |
| 09-02 13:51 | opus-5 (Ch. 7 audit) | Reads `readADST_data_v19.py`, which contains `HasStation`. **Not remarked on (near-miss #1)** | `ea9fcc15` [TX] |
| **09-02 14:26** | **USER** | "the data ive analysed doesnt seem to haven any errors or bugs (**we could check later**), so … the sign inversion on the SD and not UMD is physicial … you gave no plausible explanation" | `df3c0277` [TX] [X12] |
| 09-02 14:41 | sonnet-5 | "none of the three candidate mechanisms … survives. I cannot currently identify what makes the true muon flux late-favoring" | `df3c0277` [TX] |
| 09-02 15:02–15:03 | sonnet-5 | Scattering hypothesis. The check printed `agreement: NO`, yet the result was reported as "verified against a direct numerical convolution" (**false verification claim, never caught**) | `df3c0277` raw [TX] [X9] |
| 09-02 11:59–15:10 local/UTC | opus-5 plan → sonnet-5 | `git rm --cached` of 10 `.ipynb` ("stay on disk with figures intact"). The user pulls and **loses his local figures** | `40e7257` [GIT]; `ef06f5cf` [TX] [X11] |
| 09-02 22:09–22:22 | sonnet-5 | Full recovery (byte-verified) → `77ad431`; CLAUDE.md rule + memory file | [GIT] [TX] |
| 09-03 | course | Last class: "Inicio de proyectos finales" | course site |

## Phase 2: Phenomenology passes (09-03 → 09-10)

| When | Actor | Event | Evidence |
|---|---|---|---|
| 09-03 21:26–22:58 | USER / sonnet-5 | Kinematic-divergence explainer notebook; answers A–G; Ch. 3/5 drafts. The user corrects two framings (D, G). Commit `870a8f7` | `b5475387` [TX]; [GIT] |
| **09-04 04:57** | **USER** | "you are not weighing that angle sample by the probability of sampling it given the energy" | `b5475387` [TX] |
| **09-04 04:59–05:14** | **opus-5** | "You've found a real error": average-of-ratios → ratio-of-integrals. Corrected: **UMD +0.13 predicted vs +0.11 observed; SD +0.19 predicted vs −0.10 observed** (the mechanism orders the detectors backwards). It asks for the first time whether the SD truth count "carries a detector-level selection" | `67ae9e4`, `a9384a4` [GIT]; `spectrum_weighting_correction.html` §10 [ART] |
| 09-04 → 09-05 | sonnet-5 | VS Code SSH setup (side task; a `sudo` incident logged to the admin) | `c22f0ab7` [TX] |
| 09-05 | USER / gpt-5.6-sol | First Codex use (shell config only) | `codex 01a06de4` [TX] |
| 09-07 14:03 | USER | Structured "binary deliverable" prompt: explain the SD/UMD difference mathematically, or cut the derivation | `60fca507` [TX] |
| **09-07 14:07** | **opus-5 (unprompted)** | "let me check something the prior passes never examined: how stations enter the sample (threshold/selection effects)". Launches an Explore subagent | `60fca507` [TX] |
| **09-07 14:12** | **opus-5 subagent** | "**This `sEvent.HasStation(sdId)` at line 182 is the single, unlabelled trigger/selection gate of the entire pipeline** … at large r the late region loses stations preferentially and the surviving stations are upward-fluctuated" | sub `a7da6dcd` [TX] [X1] |
| 09-07 14:14–14:22 | opus-5/sonnet-5 | Station-count modulation measured (A1_count +0.37/+0.59 at 1200/1600 m; corr with A1_SDμ = −0.894). **Equal-N bootstrap**: −0.0945 → −0.0943 | `60fca507` raw; `run_output.txt` [TX][ART] |
| **09-07 14:23** | **sonnet-5** | "the acceptance-bias hypothesis **does not survive** direct testing". **Wrong: the test could not detect a bias in *which* stations survive** | `60fca507` [TX] [X2] |
| 09-07 14:49 | sonnet-5 | Report: B&B "attenuation-sign" candidate; "the inversion is … not a pipeline artifact". HasStation is not named | `unified_asymmetry_model_v1/report.md` [ART] [X3] |
| 09-07 14:56 | USER | "did you read the kinematic_divergence_explainer folder?" → "Honest answer: no, not fully." B&B lead cut to ~20% | `60fca507` [TX] |
| **09-10 13:41** | **USER** | "b&b work was done with the SD not the UMD, that has A LOT more interacting mass" → full retraction; memory `sd-umd-detector-confound-check`; `88fffbb` | `60fca507` [TX]; [GIT] |

## Phase 3: Astra (Codex, gpt-6-astra) and the selection bias (09-10 → 09-11)

| When | Actor | Event | Evidence |
|---|---|---|---|
| 09-10 13:53–14:01 | USER / gpt-5.6-sol | `AGENTS.md` = "read CLAUDE.md in full and follow it" (`de25675`, no AI trailer) | `codex 01a08b97` [TX]; [GIT] |
| **09-10 14:05–14:06** | USER → sonnet-5 | "write me the promt to give chaptg codex with max power…". **Claude writes the Astra kickoff prompt**, stating the sampling-artifact dismissal "should be treated as established" | `60fca507` [TX] [X4] |
| 09-10 14:10:26 | USER | Pastes the prompt into Codex; model **gpt-6-astra** | `codex 01a08ba1` [TX] [X7] |
| 09-10 14:18 | gpt-6-astra | Finds the local Offline source; traces `GetNumberOfMuons()` (counted before the water simulation, with no selection at counter level) | [TX] |
| 09-10 14:21:43–58 | gpt-6-astra | Prints `Procesamiento_ADST_v8-2.py` l.120–340 (contains the gate) | raw [TX] |
| **09-10 14:22:13** | **gpt-6-astra** | "**Hay otra selección que sí merece comprobarse: el parquet exige una estación SD reconstruida para conservar la fila UMD. Eso no queda descartado por el bootstrap anterior, que sólo comprobó el efecto de tener distinto número de filas por bin.**" | `codex 01a08ba1` [TX] [X5] |
| 09-10 14:28 → 18:45 | system | Codex usage limit #1 (~4 h pause) | [TX] |
| 09-10 19:07 | gpt-6-astra | First counterfactual (1 file): −0.006 (all) vs −0.096 (HasStation) | [TX] |
| **09-10 19:30** | **gpt-6-astra** | **20 files, 106,280 station-events: +0.0676 (all) → −0.0945 (HasStation = parquet, 0 mismatches). Paired parent-shower bootstrap Δ = −0.162, 95% CI [−0.178, −0.145]** | [TX] [X6] |
| 09-10 20:05 → 09-11 02:26 | USER / gpt-6-astra | "i didnt really get wtf you did" → plain-language note. "Not exactly: I did not prove that the reconstruction algorithm 'fails'" | [TX] |
| 09-11 03:16 | gpt-6-astra | Reproduces the author's own figure to 1.5e-9. With the same bins, 1200–1350 m: **+0.069 → −0.124** | `02_reproduccion/RESULTADO.md` [ART] |
| 09-11 10:48 | gpt-6-astra | Uncut SD vs UMD at 1200–1350 m: Δ = −0.013 [−0.090, +0.056]. Below 900 m, SD stays below UMD (open residual) | `03_sd_vs_umd/RESULTADO.md` [ART] |
| 09-11 08:18 / 08:29 local | gpt-6-astra | Commits `b072c09` (144 files) and `98a48c9` (advisor abstract), on user command. PRs #15/#16 merged by the user | [GIT] |
| 09-11 11:23:53 | USER | Codex approvals switched to the `auto_review` guardian | [TX] [X18] |
| 09-11 16:52 | USER | "did you use literally my processing code … only taking out HasStation?" → Astra: "**No—not literally.** I used a separate, simplified SD reader" | [TX] |

## Phase 4: Cross-model review, reprocessing, consolidation (09-11 → 09-24)

| When | Actor | Event | Evidence |
|---|---|---|---|
| **09-11 17:10** | USER → opus-5 (plan) | Independent skeptical review of Astra, 4 phases, with an adversarial subagent | `f032527f` [TX] |
| 09-11 17:39–18:10 | sonnet-5 + 7 subagents | Re-derives +0.0676 → −0.0945 from Astra's CSV; the flip persists in every energy sub-bin; retention ~52% early vs ~24% late. **At 17:57 it writes a fabricated "adversarial check" section, self-catches it at 17:58**, then runs the real adversarial agent (6 objections, all accepted). Verdict "**Partially agree**" | `REVIEW_ASTRA/review.md` [ART]; `f032527f` [TX] [X10] |
| 09-10 → 09-17 | USER / sonnet-5 (+opus plan) | RAFA 2026 talk. The SD slide is emptied on 09-15, then on 09-17 filled with the HasStation result "ANÁLISIS PRELIMINAR — EN VERIFICACIÓN". The conclusions slide still says "real y no trivial" | `bdf6654e` [TX]; `114fd52`, `ca3037a` [GIT] [X21] |
| 09-16 → 09-17 | USER / gpt-6-astra | Minimal "flag" reader. **The user notices fewer rows** → Astra admits `or not simCounter` lost 63,747 rows, and the UMD-loop design cannot reach untriggered stations (−0.110 with and without the flag). Usage limit #3 | [TX] [X13]; `AUDITORIA_FILAS.md` [ART] |
| 09-17 16:32–21:04 | USER → opus-5 | "astra kept fucking up". Claude builds a two-table reader (separate SimStation loop). Validated vs v11 and vs Astra's CSV. Single-process pilots only | `8d4b5a0` [GIT] [X15] |
| 09-17 (local) | **USER** | Runs the full 20-file, 8-worker reprocessing himself (v13) | `0ecae20` [GIT] |
| 09-23 23:38–23:44 | USER → gpt-6-astra | "check what claude did with your code and inshights" → Astra verifies Claude's output independently (−0.1240 / +0.0689 / UMD +0.0816) and finds 3 validation holes in Claude's code | `codex 01a08ba1` [TX] |
| 09-24 00:17 local | opus-5 | `c332ab8`: "+0.069 without the requirement and −0.124 with it … the inversion at large r follows from the requirement alone". Also finds SD error bars optimistic by ~1/√3 | [GIT] [X14] |
| 09-24 03:23–03:39 | USER → gpt-6-astra + 3 subagents | Integrated Ch. 3/5/6 drafts (one subagent per chapter); Merit-Factor caveat (Ch. 5). Ends on usage limit #5 | `borradores_…_2026_09_24/` [ART]; [TX] |
| 09-24 ~00:36 local | USER → opus-5-5 | This case-study project begins | `a4b5504d` [TX] |

## Open chronology questions
See `questions/sources_and_facts.md` (F1–F12).
