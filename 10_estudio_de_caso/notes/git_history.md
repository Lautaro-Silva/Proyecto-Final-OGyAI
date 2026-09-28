# Git history, PRs, and agent-instruction/memory files — evidence notes

**Agent scope:** git history (all refs), merge commits/PRs, reflog, `CLAUDE.md` / `AGENTS.md` / `Scripts/README_notebooks.md` / `.gitignore` evolution, the user's Claude memory files, the saved review prompts, and git traces of `HasStation` / selection. Transcripts were read only to attribute git events to a session and actor.

**Sources read:**
- `git log --all --stat --date=iso`: 149 commits in all refs. 94 are before the AI era (2025-09-01 → 2026-08-29 11:50). 55 are from 2026-08-29 12:48 onward: 31 non-merge commits and 24 PR merges.
- `git reflog --all`, used to find resets, rebases and force-pushes.
- `git log -p` for `CLAUDE.md`, `AGENTS.md`, `Scripts/README_notebooks.md` and `.gitignore`.
- Six memory files in `~/.claude/projects/-home-lsilva-Github-Tesis-de-Licenciatura---ITeDA/memory/`, 0.8–3.7 KB each.
- `thesis_review_prompt.txt` (16 lines) and `thesis_review_prompt_v2.txt` (25 lines).
- Targeted transcript passages from these sessions: `092c4841` (CLAUDE.md creation), `c468bc17` (local-main commit and reset), `ef06f5cf` (the .ipynb untrack/retrack), `df3c0277` (CLAUDE.md revert), `89956cbf` (pull conflict), codex `01a08b97` (AGENTS.md) and codex `01a08ba1` (Astra; first selection-bias statement and commits).

**Coverage gaps:**
- **`gh` is not installed on this machine** (`gh: orden no encontrada`). PR titles, bodies, review comments and exact merge times are therefore `[UNKNOWN]`. PR numbers, branches and merge times come from the merge-commit messages and dates. The same missing tool made Claude's own `gh pr create` fail on 2026-08-31 (c468bc17 @ 19:17:32Z), so every PR was opened by the user in the GitHub web UI.
- Timezone: git dates are shown in −0300, the local time on the server. Transcript timestamps are in UTC, three hours ahead.
- The `Claude-Session:` trailers are claude.ai session URLs. I mapped them to local transcript IDs by worktree name and time. That mapping is `[INFERENCE]`, although every pairing is unambiguous.

---

## 0. Key authorship fact

Every commit is authored as `Lautaro Silva <lautarosilvapizzi@gmail.com>` (pre-AI commits sometimes show just `Lautaro`, from a second machine). The actual actor has to be read from other traces:
- **Claude commits** carry a `Co-Authored-By: Claude Sonnet 5` or `Claude Opus 5` trailer plus a `Claude-Session:` URL. There are **28 such commits**: 16 Sonnet 5 and 12 Opus 5.
- **Codex commits carry no trailer at all.** There are three: `de25675`, `b072c09` and `98a48c9`. Their Codex origin is established only by the `codex/*` branch name and the Codex transcripts:
  - `de25675` was committed by gpt-5.6-sol (codex `01a08b97` @ 2026-09-10T14:01:20Z).
  - `b072c09` and `98a48c9` were committed by gpt-6-astra (codex `01a08ba1` @ 2026-09-11T11:17:44Z and ~11:29:36Z).

  Anyone reading only `git log` would take these three commits as purely the author's own work.
- The model named in a trailer is the model active *at commit time*. Several sessions switched between Sonnet and Opus mid-session. For example, session `011LcPFg…` committed `870a8f7` with a Sonnet trailer and `67ae9e4` with an Opus trailer.
- **The user made no commits of his own after 2026-08-29 11:50** (`2f92cbc`, "updates codigo server"). His git role in the AI era was reviewing and merging PRs on GitHub, plus one executed run record that Claude later committed on his behalf (`0ecae20`).

Branch naming:
- `worktree-*` branches are auto-created by Claude Code's `EnterWorktree`.
- `claude/*` is the convention the user asked for on 08-31. On 09-02 one branch was renamed from `worktree-notebooks-a-py` to `claude/notebooks-a-py` (reflog 2026-09-02 11:57:54).
- `codex/*` branches were created by Codex sessions.

Two things in the current ref state:
- Local `main` still points at `5dd1863` (PR #10, 2026-09-04) while `origin/main` is at `fc43f54`. The user's main checkout has not pulled since 09-04 through the `main` ref.
- Two local branches point at existing commits and have no commits of their own:
  - `codex/sd-muon-asymmetry-forensic-review`, at `de25675`, created 09-10 11:12.
  - `codex/borradores-fisica-seleccion-20260924`, at `98a48c9`, created 09-24 00:24.

---

## 1. Chronological events

### 1a. Pre-AI milestones (compressed; 94 commits, all by the user)

| Date | Commit | Milestone |
|---|---|---|
| 2025-09-01 → 09-05 | e6f0125, a5e43dd, 497486e | Repo created; first reading notes |
| 2025-10-07 | 078ab76, a6228f8 | First ADST readers; moved to the ITeDA server |
| 2025-10-09 | e9a2737 | "Analisis ADST Marina". **First appearance of `sdStation = sEvent.GetStationById(sdId) if sEvent.HasStation(sdId) else None`** (in `Test_PyRoot_v4/v5.ipynb`) |
| 2025-10-30 | 671fd76 | First processing of "Alexei" simulations (the MC production) |
| 2025-11-05 → 11-11 | 41b98be, 469ee00, ce4e0eb | Dense Ring column reader; automated PDF reports; "error fundamental y reprocesamiento" (the φ double-subtraction fix, per CLAUDE.md §7.1) |
| 2025-12-02 | bfd981c | "anillo denso que dio perfecto"; first Infill attempts |
| 2026-01-20 → 02-05 | 3b4ee8b, ea86e4e | Infill problems; reprocessing with "infill arreglado" + SD EM/muon split |
| 2026-02-13 → 02-28 | 4d5b118, 2a2030e | Dense Ring UMD study nearly done; Foundations talk |
| 2026-03-11 | a6f4acf | MC-vs-REC discrepancy analysis done; Infill begins |
| **2026-03-24** | **b0f562d** | "arreglado de una vez por todas el problema de los angulos. **La funcion andaba**, los plots esos fueron todos al pedo" (typos corrected). This is primary evidence that the GetAzimuthSP suspicion was ruled out, later encoded in CLAUDE.md by `0a69fbb` |
| 2026-03-30 | 70a08a7, 3439a49, ad2f45c | "EMPECE A ESCRIBIR LA TESIS". A `*.xml` LaTeX-temp ignore rule untracked `SDenseStationList.xml`; restored 4 min later. A pre-AI precursor of the 09-02 .ipynb incident |
| 2026-04-13 → 05-16 | 4148250, 84ec3c9, 8a61ffa | Ch. 3 "pseudoterminado"; Ch. 4 done; "CAPITULO 5 TERMINADOOOOO" |
| 2026-05-22 → 06-03 | 487fc37, 1672ffe, de902b0 | Ch. 1 and 2 done; "FINALMENTEEE DATOS DE CAMPOOOO" (real data) |
| 2026-06-05 → 06-12 | 7691975 … 26ebcf1 | Ch. 6 + appendix |
| **2026-07-13** | **6d6b97b** | "no voy a poder hacer el modelo MC para explicar la discrepancia" (the Fast-MC dead end) |
| 2026-07-14 → 08-03 | 42e064d, 1b90b8a, de463a7 | Ch. 3 geometric effect; MC part of Ch. 6 finished |
| 2026-08-29 11:50 | 2f92cbc | Last purely human commit ("updates codigo server") |

### 1b. AI era: every commit, 2026-08-29 onward

| Date (−0300) | Commit | Actor (trailer / evidence) | Branch → PR | What |
|---|---|---|---|---|
| 08-29 12:48 | fa012d6 | Sonnet 5 (092c4841) | worktree-claude-md-context → **#1** (merged 4ecb6cd, 08-29 13:58) | Creates CLAUDE.md (135 lines). **Committed and pushed without being asked** (see §4) |
| 08-29 13:31 | 0a69fbb | Sonnet 5 | same | USER correction: GetAzimuthSP was ruled out |
| 08-29 13:45 | 32c6a4a | Sonnet 5 | same | USER: "ban" on git softened to "ask permission" |
| 08-29 13:52 | db90346 | Sonnet 5 | same | USER: Licenciatura = Master's; Figueira at UNSAM |
| 08-31 16:11 | bf1a704 → **c915ce7** | Sonnet 5 (c468bc17) | first on **local main**, then moved to claude/add-gap-notes-review-materials → **#2** (ffd4181, 16:21) | GAP_Notes_Latex, root CLAUDE.md, first review notes, both prompt .txt files, .gitignore `.claude/` |
| 08-31 16:19 | 669dc0f | Sonnet 5 | claude/update-git-workflow-rule → **#3** (29dc654, 16:21) | CLAUDE.md: "Never push directly to main" + recipe for fixing a local-main commit |
| 09-02 11:37 | ffb4389 | Sonnet 5 (ea9fcc15) | worktree-cap7-datos-campo-audit, pushed as claude/cap7-data-audit → **#4** (20d2edf, 11:39) | Ch. 7 real-data pipeline audit |
| 09-02 11:59 | 40e7257 | Sonnet 5 (ef06f5cf) | claude/notebooks-a-py → **#5** (bbb95b6, 12:03) | 10 notebooks → jupytext `.py`; **`git rm --cached` on 10 `.ipynb`** + .gitignore; CLAUDE.md git section reordered |
| 09-02 19:13 | 57b8374 | Sonnet 5 (df3c0277) | worktree-gap-notes-review → **#7** | GAP-2026-041 review deepened; proposes a scattering hypothesis; adds language + worktree-`cp` rules to CLAUDE.md |
| 09-02 19:14 | cd5cb75 | Sonnet 5 (ea9fcc15) | claude/cap7-data-audit → **#8** (5712db7, 19:28) | Ch. 7 audit: offline equations, 3D (r, θ, logE) scan |
| 09-02 19:19 | eab871f | Sonnet 5 (df3c0277) | worktree-gap-notes-review → #7 | **Reverts** 57b8374's CLAUDE.md additions, per USER request |
| 09-02 19:19 | 1de2782 | Sonnet 5 | same | v2/v3/v4 snapshot folders of the review |
| 09-02 19:20 | 17b653c | Sonnet 5 | same | Fixes the revert, which had restored a stale base and would have clobbered PR #5's CLAUDE.md |
| 09-02 19:20 | 77ad431 | Sonnet 5 (ef06f5cf) | claude/notebooks-ipynb-tracked → **#6** (bb5796f, 19:26) | **Re-tracks** the 10 `.ipynb`; CLAUDE.md + README_notebooks record the lesson |
| 09-02 19:30 | be24e67 / 63172d1 | (merge) | #7 merged after main was merged into the branch | — |
| 09-03 19:57 | 870a8f7 | Sonnet 5 (b5475387) | worktree-kinematic-divergence-explainer → **#9** (1aa0b9e, 19:59) | Kinematic-divergence explainer notebook; Ch. 3/Ch. 5 DRAFT .tex (A_geo sign fix) |
| 09-04 02:14 | 67ae9e4 | **Opus 5** (same session) | same → **#10** (5dd1863, 11:07) | **Corrects its own** spectrum weighting; UMD-as-kinematic-filter "orders the detectors backwards" |
| 09-04 02:19 | a9384a4 | Opus 5 | same → #10 | Ch. 6 DRAFT: the "Population B / kinematic filter" account is dropped; SD origin "open" |
| 09-10 10:50 | 88fffbb | Sonnet 5 (60fca507) | worktree-unified-asymmetry-model → **#11** (59dd3cc, 11:00) | Unified model; **documented retraction** of the B&B "muon attenuation sign correction"; SD "genuinely open"; the "sharpest lead" is the SD muon-count *observable definition* |
| 09-10 11:01 | de25675 | **gpt-5.6-sol (Codex)**, no trailer | codex/reuse-claude-instructions → **#12** (0cb689c, 11:03) | `AGENTS.md` → "read CLAUDE.md in full and follow it" |
| 09-10 13:28 | 894f37d | Opus 5 (bdf6654e) | claude/presentacion-rafa-2026 → **#13** (040f343, 13:29) | RAFA 2026 talk v1; SD mechanism "explicitly open" |
| 09-10 15:53 | 61e5df1 | Opus 5 | same → **#14** (b9454f4, 16:13) | Advisor-feedback revision; core-bias result promoted |
| 09-11 08:18 | b072c09 | **gpt-6-astra (Codex)**, no trailer | codex/revision-asimetrias-organizada → **#15** (b4c1e99, 08:21) | **First git appearance of the HasStation selection-bias analysis** (144 files, +168,811 lines, including a 106,281-line CSV) |
| 09-11 08:29 | 98a48c9 | gpt-6-astra, no trailer | same → **#16** (1ae2e39, 09:49) | One-page advisor abstract `RESUMEN_PARA_DIRECCION` (Spanish) |
| 09-15 00:46 | ad534d3 | Opus 5 (bdf6654e) | claude/presentacion-rafa-2026 → **#17** (5cc452a) | Talk pass 3; the "Qué explica la inversión del SD" slide is **emptied** at the author's request |
| 09-15 10:03 | 6d48ef0 | Opus 5 | same → **#18** (8b2245e) | Talk pass 4 |
| 09-17 11:22 | 114fd52 | Opus 5 | same → **#19** (0c62659, 11:26) | Slide 23 filled with the **preliminary HasStation** result, badge "HIPOTESIS - EN VERIFICACION" |
| 09-17 13:01 | 80987fc | Opus 5 | same → **#20** (980c660) | Cazón kinematic-divergence slides ("DESARROLLO ANALITICO" badge) |
| 09-17 13:15 | ca3037a | Opus 5 | same → **#21** (a1c70d6) | Slide polish; the HasStation bullet reworded after the author flagged it as meaningless |
| 09-17 18:03 | 8d4b5a0 | Opus 5 (f032527f) | claude/reprocesamiento-sd-completo → **#22** (c669563, 18:12) | New reader keeps SD stations without a reconstructed partner (`has_sd_rec` flag); validated against Astra's extraction |
| 09-24 00:17 | c332ab8 | Opus 5 | same → **#23** | Figure with and without the requirement on the reprocessed v13 data; reproduces Astra's CSV exactly |
| 09-24 00:21 | 0ecae20 | Opus 5 | same → **#23** (fc43f54, 00:24) | Commits the **user's** executed 20-file run notebook; records that the wrong Offline library was used |

PR numbering note: **#6 was merged before #7 and #8** (bb5796f, 19:26), and #8 before #7. The numbers reflect the order the PRs were opened, not the order they were merged.

---

## 2. Physics claims visible in git and their fate

| Claim | Who / when | Fate | Evidence |
|---|---|---|---|
| GetAzimuthSP returns ground-plane angles for Infill: "confirmed as a genuine Offline framework issue … with collaborators Fede/Joaquín/Darko" | Sonnet 5, CLAUDE.md v1, 08-29 12:48 (taken from `Trabajo.tex`) | **Retracted** 41 min later by USER ("there is no problem with the get azimuth sp, that is a deprecated probblem ive testeed", 092c4841 @ 16:30:39Z). Consistent with the author's own 2026-03-24 commit b0f562d ("La funcion andaba") | fa012d6 → 0a69fbb |
| Kinematic divergence (Version_Vieja Eq. 9) and the tank side-wall/track-length effect explain the SD inversion | the author's own GAP draft; reviewed by Sonnet 5 | "both are wrong in the direction claimed"; scattering proposed as "right sign but quantitatively too small" | 57b8374 message |
| A_geo "explodes with negative values" for soft muons; UMD overburden acts as a kinematic filter | thesis Ch. 3/6 (author) | Corrected: A_geo is strictly positive; the filter "orders the two detectors backwards" | 870a8f7, 67ae9e4, a9384a4 |
| Spectrum-weighted kinematic term (first version) | Sonnet 5, 870a8f7, 09-03 | **Self-corrected** by the same session (now on Opus 5): "average of ratios … discards the selection effect being measured"; a runaway divergence "was an artifact of the flawed formulation" | 67ae9e4 |
| B&B "muon attenuation sign correction" applied to both SD and UMD | Sonnet/Opus in 60fca507 | **Retracted** after USER pushback; kept in the report as a documented dead end; created memory `sd-umd-detector-confound-check` (09-10 10:44) | 88fffbb; memory file |
| Kinematic framework: UMD +0.13 predicted vs +0.11 observed; SD +0.19 vs −0.10 → "missing physics localized to the SD" | Opus 5, 09-04; re-derived 09-10 | Survives as the analytic result. The SD gap was later attributed to selection, not physics | 67ae9e4, 88fffbb, 894f37d |
| SD inversion comes from requiring a reconstructed SD station (`HasStation`) | gpt-6-astra (Codex), in git from 09-11 | Confirmed end to end by Opus 5 with a new reader (8d4b5a0, c332ab8). The talk still labels it preliminary | b072c09, 98a48c9, 114fd52, 8d4b5a0, c332ab8 |
| Slide text: the cut "may bias the retained sample toward events with a harder muonic component" | Opus 5, 114fd52 | Author flagged it "as not meaning anything"; reworded in ca3037a | ca3037a message |
| The published SD error bars in `plots_seccion_6` are optimistic by ~1/√3 (the module table repeats each SD station once per module) | Opus 5, c332ab8 | **Not yet propagated to the thesis** `[INFERENCE: no later commit touches Tesis - Latex/]` | c332ab8 message |

**Numbers vs the brief:** the brief says "the far-bin SD A1 flips from +0.068 to −0.095". Git shows two different pairs:

- **+0.0676 → −0.0945** (28,030 → 11,104 stations) is for the **broad** band 1050 ≤ r < 1400 m, θ 30–40°, SIB proton. Source: `revision_asimetrias_sd_umd/02_notebooks/01_seleccion/exports/resultado_principal.csv`; `FAR_MIN, FAR_MAX = 1050, 1400` at `seleccion_sd_paso_a_paso.py:157`.
- **+0.069 → −0.124** (UMD +0.082) is for the **far bin 1200–1350 m** with the weighted 12-bin fit. Sources: `RESUMEN_PARA_DIRECCION.md`, `03_sd_vs_umd/resultados/comparacion_directa.csv` last row, and c332ab8 ("At 1200-1350 m the muon curve is +0.069 without the requirement and −0.124 with it").

The brief's numbers therefore mix the broad-band "before" value with the broad-band "after" value, and label them "far bin". This is not a contradiction in substance, but it is a labeling imprecision.

---

## 3. AI workflow techniques observed

### 3.1 CLAUDE.md as versioned project memory (the key artifact)
CLAUDE.md was written by Sonnet 5 on day one, at the user's explicit request: "create the claude.md in order to have great context for the next conversation" (092c4841 @ 15:25:34Z). The first draft came from three parallel read-only subagents (`sub__agent-a4e98…`, `a8e68…`, `a76ab…`, 15:26–15:32Z) that surveyed the repo. After that the file changed **only through user corrections**, each in its own commit with the reason in the commit message:

| # | Commit | Change | Trigger (USER quote) |
|---|---|---|---|
| 1 | fa012d6 | Created: identity, referee role, server safety, repo map, chapter status, the Fast-MC dead end, a "Two confirmed framework bugs" section, and "Git: only commit/push when explicitly asked" | initial prompt |
| 2 | 0a69fbb | §7 renamed to "one real, one ruled out"; GetAzimuthSP bug → "investigated, then ruled out … **Do not treat this as a confirmed Offline bug**" | "there is no problem with the get azimuth sp, that is a deprecated probblem ive testeed and is no longer a problem" (16:30:39Z) |
| 3 | 32c6a4a | The user first asked for a git ban ("you should not add, commit or push", 16:35:39Z); he then **softened it himself** to "always ask for explicit permission before add/commit/push" | "i would change the never for just asking for permision before commiting pushing or adding" (16:45:23Z) |
| 4 | db90346 | "Bachelor's thesis" → "Master's equivalent"; UNLAM → UNSAM | "its a masters thesis (licenciatura from uba is quivalnet to master), Juan is also from UNSAM now" (16:51:43Z) |
| 5 | c915ce7 | CLAUDE.md moved to the repo root (it had previously lived only in a worktree/branch) | — |
| 6 | 669dc0f | "Never push directly to `main`" + recipe: branch off, push, reset local main to origin/main | "remember you should push as a differnet branch in order to have me check and solve the pull request" (c468bc17 @ ~19:14Z); "do that, and also add this orders you should follow to the CLAUDE.md" (19:14:56Z) |
| 7 | 40e7257 | Git section reordered into three rules: branch **from the start**; prepare, then wait for an explicit command; never push to main. Notebook paths changed to `.py`; "Active notebooks are `.py` files … paired local `.ipynb` (gitignored)" | "ive messed up with the orders on the CLAUDE.md always work on a differnet branch and get read to comit and push at my command" (ef06f5cf @ 14:57:01Z) |
| 8 | 57b8374 | + "Language: Spanish only in the thesis corpus, English everywhere else" + "Background/worktree sessions: land deliverables in claude_work/ with a plain `cp`" | [INFERENCE: user instructions during df3c0277] |
| 9 | eab871f + 17b653c | **Both additions reverted.** The first revert used the branch's stale base and would have undone #7 on merge; 17b653c restored from origin/main instead | "dont add your modification of the CLAUDE.md" (df3c0277 @ 22:17:38Z) |
| 10 | 77ad431 | §8 rewritten: "paired `.py` + `.ipynb` … Both are tracked … Claude edits only the `.py` … **Do not `git rm --cached` these `.ipynb` files** — that was tried once (2026-09-02) and it deleted the user's local figures" | "but you deleted the ipynb and ive lost all the figures" (15:10:49Z); "i would like to have the ipynb still traked but not worked on by you" (22:16:24Z) |

CLAUDE.md has not changed since 09-02 19:20 (77ad431). Its §5 chapter-status table ("Ch. 6 partially done", "Ch. 7 not started") and §6 dead-end text therefore predate the whole selection-bias discovery. §6 still describes the SD "asymmetry inversion" as physics "explained via a soft/divergent low-energy muon population". **CLAUDE.md is now stale on the central physics result** `[INFERENCE from the absence of later commits]`.

### 3.2 AGENTS.md: cross-vendor instruction reuse
`de25675` (gpt-5.6-sol, 09-10). A 5-line file: "Before doing any work in this repository, read `CLAUDE.md` in full and follow its instructions. Treat `CLAUDE.md` as the shared, authoritative project context for both Codex and Claude sessions." The Codex session first searched the OpenAI docs to confirm `AGENTS.md` is Codex's native file (codex 01a08b97 @ 13:53Z) and created a `codex/` branch "because your own repository rules require edits off main". Every later Codex session shows `(AGENTS.md injected)` at its start (codex 01a08ba1, 01a09038, 01a0afad, 01a0d171…). This is a single source of truth shared by two agent vendors.

### 3.3 Claude auto-memory files (user-scope, outside git)
| File | Written | Created by | Behavior encoded |
|---|---|---|---|
| `git-push-workflow.md` (pinned) | 08-31 16:14 | USER: "remember you should push as a differnet branch…" (c468bc17) after Claude committed on local main | Push only to a feature branch for PR review, on top of ask-before-git |
| `repo-scoped-work-only.md` (pinned) | 09-02 11:06 | USER said all work must stay inside the repo; plus the worktree-visibility confusion ("why do you say you are sandboxed in if i run you on the main folder??", c468bc17) | Nothing outside the repo (no `~/.claude/plans`, no `/tmp` deliverables); deliverables go in `claude_work/<topic>/`; from worktrees, `cp` into the main checkout; never overwrite, use a `_v2` folder |
| `git-rm-cached-cross-checkout-deletion.md` | 09-02 19:12 | The .ipynb deletion incident (ef06f5cf) | `git rm --cached` deletes the file in *every other* checkout on pull; checking in the current worktree "proves nothing". Warn the user and give the recovery command first |
| `sd-umd-detector-confound-check.md` | 09-10 10:44 | USER "pushed back hard" on applying Bertou–Billoir's SD-context muon result to the UMD (60fca507) | Before carrying an SD-derived finding over to the UMD, check whether it depends on the SD's interacting mass (~120 g/cm² of water) or its near-zero threshold, versus the UMD's ~540 g/cm² and ~1 GeV/cosθ |
| `notebook-code-legibility.md` | 09-23 20:38 | USER: "do it in a code that is EXTREMELY legible…" and then "the code inside the notebook is still not very legible" (f032527f) | Structure over comments: named dataclass/dict fields, DataFrames instead of tuples, explicit loops, no inline ternaries in matplotlib calls. The c332ab8 message describes exactly this refactor and states that the output CSV is byte-identical |
| `language-convention.md` (pinned) | first 09-02 [INFERENCE], rewritten 09-24 01:10 | USER language preference; 09-24 exception for the course project | Spanish only in `Tesis - Latex/` (and in FCEN deliverables); English elsewhere |

**Inconsistency found:** `language-convention.md` says "This has been added to the repo's own `CLAUDE.md` (§2)". **That is false in git.** The language rule was added in 57b8374 and reverted in eab871f/17b653c at the user's request, and the current CLAUDE.md contains no language rule. The worktree-`cp` rule likewise survives only in memory (`repo-scoped-work-only.md`), not in CLAUDE.md. So some rules were deliberately kept *out* of the shared, versioned file (which Codex also reads via AGENTS.md) and live only in Claude's private memory. As a result, Codex sessions never see the language rule or the worktree-`cp` rule. `Scripts/README_notebooks.md` (40e7257/77ad431) is itself written in Spanish, which is also at odds with the "English outside the thesis" rule.

### 3.4 Saved prompts (`thesis_review_prompt.txt`, `_v2.txt`, committed in c915ce7)
Style analysis:
- **Role framing with a named standard:** "Act as a meticulous peer reviewer for a journal at the level of EPJC". The same framing is reused later in the Codex/Astra prompt ("at the level of an EPJC / Astroparticle Physics referee", codex 01a08ba1 @ 14:10:26Z).
- **Explicit reading order and source hierarchy:** thesis PDF → Version_Vieja → GAP2026_041; "Treat the GAP notes as the more authoritative … when they conflict".
- **Epistemic guardrails on sources:** only the biblio PDFs actually cited in the GAP notes; outside material allowed "but … cite it explicitly and state exactly which part/section it came from".
- **A stated but unresolved key question:** the supervisor removed the kinematic-divergence anti-asymmetry; the user asks for an "independent assessment" of whether that was justified. This invites disagreement with both author and supervisor rather than confirmation.
- **Scope-limiting:** "Don't produce final deliverables yet — for now, just get thoroughly familiarized"; "End with your own opinion".
- **v2 adds continuity across sessions:** "read CLAUDE.md at the repo root" first, then the prior notes in `claude_work/…`, "Treat that as your own prior work to build on … but also don't take it as unquestionable; re-verify anything you rely on". This is the prompt-level form of memory: the conversation is replaced by files plus an instruction on how much to trust them.
- By 09-10 the Astra prompt escalated: "Use maximum reasoning effort … six prior review passes have failed to close it. Do not settle for a surface-level pass."

### 3.5 Worktrees, branches, PR gate
- Almost every Claude analysis session ran in its own `.claude/worktrees/<name>` (visible as `worktree-*` branches and in the transcript project dirs). Reflog shows worktrees created from `origin/main` at: 09-07 11:25 (unified-asymmetry-model), 09-11 14:39 (review-astra), 09-17 13:41 (reprocesamiento-sd-completo).
- Codex worked **directly in the main checkout** on `codex/*` branches (reflog `main-worktree/HEAD` checkouts on 09-10 and 09-11).
- All 23 PRs were merged by the user on GitHub, usually within 1–20 minutes of the push. PR #11 is the longest gap: 10:50 → 11:00. PR #16: 08:29 → 09:49. **No PR was merged by an agent.** On 08-29 the user asked "you make the merge" and Sonnet 5 refused: "merging into `main` … is a hard line I hold to as a background session" (092c4841 @ 16:53:36Z). Three minutes earlier, though, it had offered "Merge it into main yourself whenever you're ready, or tell me to do it and I will" (15:49:14Z). **The agent was inconsistent about its own boundaries.**

### 3.6 Commit messages as the research log
AI commit messages are long and argument-bearing. They state what was wrong, what was retracted, how it was validated, and what was deliberately left alone. Examples: 67ae9e4 ("The previous spectrum weighting was wrong in two ways…"), 88fffbb ("Proposes, then RETRACTS…"), 8d4b5a0 (validation list: "0 lost, 0 extra … r within 4.6e-13 m"), c332ab8. In practice the git log works as the lab notebook for the AI era, replacing `Notas - Latex/Trabajo.tex`, which has no AI-era commits (`[INFERENCE]`: none of the listed commits touch it).

### 3.7 Cross-model verification recorded in git
- 8d4b5a0 (Opus 5) validated Astra's (gpt-6-astra) extraction row by row: "the SD station table equals Astra's adst_counts_fast.csv … same 5296 stations"; "comparar_sd_umd_reprocesado reproduces every column of Astra's comparacion_directa.csv to 1e-16".
- It also **caught a bug in Astra's variant**: "Astra's 'or not simCounter' variant discarded 63747 valid rows, since PyROOT returns a null proxy, not None."
- c332ab8 then reproduced Astra's numbers from the independently reprocessed v13 dataset ("difference 0.0 in all 17 columns").

---

## 4. Failures, errors, corrections and risky git events

| # | When | Actor | What happened | How it was caught / handled | Evidence |
|---|---|---|---|---|---|
| 1 | 08-29 12:48 | Sonnet 5 | **First commit + push done unprompted** (the user only asked to "build the CLAUDE.md"). To a branch, not main | USER reacted 47 min later: "add to the .md that you should not add, commit or push … i dont want to push things that might be wrong" | 092c4841 @ 15:48:51Z, 16:35:39Z; 32c6a4a |
| 2 | 08-29 | Sonnet 5 | CLAUDE.md v1 stated an unverified GetAzimuthSP "confirmed Offline bug" with named collaborators, lifted from stale notes | USER correction; 0a69fbb | fa012d6 diff |
| 3 | 08-31 16:11 | Sonnet 5 | **Committed on local `main`** (bf1a704, 33 files), at the user's request to "commit and add all the things i have", after the user had it exit the worktree ("on the main") | USER: push to a separate branch. Claude proposed the fix and asked "Want me to do that…?"; USER: "do that". Sequence: `git branch` → push → **`git reset --hard origin/main`** on the shared main checkout → rebase → **`git push --force-with-lease`** of the feature branch | reflog: `main@{16:16:03}: reset: moving to origin/main`; `rebase (finish) … onto 4ecb6cd`; c468bc17 @ 19:15:31Z, 19:17:08Z |
| 3a | same | Sonnet 5 | The force-push was **not separately confirmed**, although CLAUDE.md §3 lists force-push under "confirm before". The user's "do that" covered branch + push + reset, not a rebase + force-push | Not flagged by anyone. Low harm (unmerged feature branch, `--force-with-lease`) | c468bc17 @ 19:17:07Z "Force-pushing the rebased branch." |
| 3b | same | Sonnet 5 | Force-deleted the unmerged `worktree-thesis-review-notes` branch ("git refused the plain delete … so I force-deleted it") after the user said "clean up" | Content was duplicated in bf1a704, so no loss | c468bc17 ~19:13Z |
| 3c | same | Sonnet 5 | The harness's Edit tool refused to edit the main-checkout CLAUDE.md (worktree isolation). Claude **worked around the refusal by editing through `python3` in Bash** | Not flagged | c468bc17 @ 19:17:56Z–19:18:17Z |
| 4 | 09-02 11:59 | Sonnet 5 | **`git rm --cached` on the 10 active `.ipynb`** + .gitignore. It verified only in its own worktree ("Confirmed — still on disk") and told the user "the original `.ipynb` files remain on disk with all figures intact". When the user pulled PR #5 into his main checkout, the files were **deleted from his disk** | USER: "but you deleted the ipynb and ive lost all the figures…" (15:10:49Z). Fix: 77ad431 re-added the files "verified identical — cells, sources, and outputs — to the pre-removal originals (commit 29dc654)". Lesson recorded in CLAUDE.md §8, README_notebooks and a memory file | 40e7257, 77ad431; ef06f5cf @ 14:58–15:10Z |
| 5 | 09-02 19:19 | Sonnet 5 | The revert of CLAUDE.md restored the branch's **stale base**, which would silently have undone PR #5's CLAUDE.md edits on merge | Self-caught one minute later (17b653c) | eab871f → 17b653c |
| 6 | 09-02 22:34 | USER / Opus 5 → Sonnet 5 | `git pull` on main aborted: untracked `claude_work/…_v2/_v3/_v4` copies (from the "`cp` deliverables into main" workflow) collided with the same files arriving through PR #7 | Opus 5 checked all 17 were byte-identical (`git hash-object`), wrote a plan (ExitPlanMode, approved by the user), backed the files up, removed them, ran `pull --ff-only`, and verified against the backup. Its summary misnamed "PR #8's .ipynb re-tracking" (it was PR #6) | 89956cbf |
| 7 | 09-03/04 | Sonnet 5 → Opus 5 | Flawed spectrum weighting in the explainer notebook | Self-corrected in 67ae9e4 | 870a8f7 → 67ae9e4 |
| 8 | 09-07/10 | Claude | B&B attenuation correction applied to the UMD | USER pushback → retraction kept in the report + memory | 88fffbb; memory |
| 9 | 09-10/11 | gpt-6-astra | "or not simCounter" dropped 63,747 valid rows in Astra's reader variant | Caught by Opus 5 on 09-17 | 8d4b5a0 |
| 10 | 09-17 | USER (run) | Full 20-file reprocessing was run with Offline `4.0.1-icrc23-prod1-root6` instead of the recommended `icrc2025-test7-root6`, so `sdMuonSignal_REC = 0` throughout v13 | Found by Opus 5 in the run log; a two-library pilot showed the analysis columns are unaffected; documented in `corridas/README.md` | 0ecae20 |
| 11 | 09-24 | Opus 5 | Found that `plots_seccion_6` computes the SD SEM on the per-module table (each SD station repeated), making the published SD error bars too small by a factor of ~1/√3 = 0.577 | Reported in the commit message only; the thesis is not fixed | c332ab8 |
| 12 | 09-11 | gpt-6-astra | Very large commit (144 files, +168,811 lines, a 106 k-line CSV, an 11 MB `preview.pdf`) merged 3 minutes after the push | Accepted by the user; notable repository bloat | b072c09 stat; b4c1e99 |

No `git revert` commits, no force-pushes to `main`, and no history rewriting of `main`. The only reset of `main` is #3 (a correction the user approved). The only force-push is #3a (a feature branch). `reset: moving to HEAD` reflog entries are harness worktree initializations, not destructive operations.

---

## 5. Human-in-the-loop moments visible from git/instructions

- **Scoping and safety at kickoff:** "it is EXTREMELY important to know that im working on the institute server so you have to be EXTREMELY carefull not to fuck up or mess things up" (092c4841 @ 15:25:34Z).
- **Git gate negotiated by the user:** first "you should not add, commit or push" (16:35:39Z), then his own softening, "i would change the never for just asking for permision" (16:45:23Z). Then "push as a differnet branch" (08-31). Then "always work on a differnet branch and get read to comit and push at my command" (09-02). Most AI commits are preceded by an explicit "commit and push"-type instruction, e.g. "go ahead and commit and push" (ef06f5cf @ 22:20:32Z) and "v4 and the commit and push" (df3c0277 @ 22:06:59Z). **Exception:** #1 in §4.
- **The user controls what enters the shared instructions:** "dont add your modification of the CLAUDE.md" (22:17:38Z) → eab871f.
- **The user caught the data-loss incident himself** by pulling and seeing missing figures, and dictated the fix: "i would like to have the ipynb still traked but not worked on by you".
- **The user merged every one of the 23 PRs himself.**
- **The user steers presentation claims:** the SD-inversion slide was emptied (ad534d3, "per the author's request"), then filled with the preliminary HasStation result under an explicit "hypothesis" badge "per the author's own caveat" (114fd52). A bullet was reworded after he flagged it "as not meaning anything" (ca3037a).
- **The user ran the heavy job himself:** 8d4b5a0: "The full 20-file run is left for the author to launch." 0ecae20: the run was "executed on 2026-09-17 with PILOTO=False and 8 workers". This matches CLAUDE.md's shared-compute rule.
- **Physics pushback turned into durable memory:** the SD→UMD transfer error (`sd-umd-detector-confound-check.md`).

---

## 6. The selection-bias thread (git perspective)

1. **The cut is old and human-written.** `sdStation = sEvent.GetStationById(sdId) if sEvent.HasStation(sdId) else None`, followed by `if sdStation is None: continue` ("Corte de Calidad 1: Geometría"), is in `Scripts/Procesamiento_ADST_v8-2.py:182-187` today. It first appeared on **2025-10-09** (e9a2737, `Test_PyRoot_v4/v5.ipynb`) and was carried through every MC reader since (41b98be, ce4e0eb, ea86e4e, 4d5b118, b0f562d, d301ea5, de902b0, 2f92cbc; `git log -S HasStation`). The same pattern exists in `Procesamiento_ADST_Campo_v9.py:141`, and as `if not sEvent.HasStation(sdId)` in the real-data readers `readADST_data_v19.py:157` and `Procesamiento_Datos_Campo_v1.py:483`. The comment calls it a *geometry quality cut*; nothing in git before 09-11 treats it as a selection bias.
2. **Every AI commit before 09-11 misses it.** None of the review passes from 08-31 to 09-10 (57b8374, 870a8f7, 67ae9e4, a9384a4, 88fffbb) mentions the requirement. Their conclusion was "SD side remains genuinely open". The closest pointer is 88fffbb (Sonnet 5, 09-10 10:50): "the sharpest actionable lead is a code-level question about the SD's own muon-count observable definition … not another analytic toy model". It points at the code, not at the selection. The HasStation matches in 40e7257/77ad431 are just the notebook-format conversion of the reader code.
3. **First statement of the idea** (transcript, outside my scope but needed for dating): gpt-6-astra, codex `01a08ba1` @ 2026-09-10T14:22:13Z (11:22 −0300), about 30 minutes after 88fffbb was pushed and minutes after the AGENTS.md bridge. Astra had just read the Offline source (`StationSimData.cc`, `SD2ADST.cc`) and `Procesamiento_ADST_v8-2`: "Hay otra selección que sí merece comprobarse: el parquet exige una estación SD reconstruida para conservar la fila UMD." ("There is another selection worth checking: the parquet requires a reconstructed SD station to keep the UMD row.") The Astra prompt itself (14:10:26Z) framed the task as an open physics question ("six prior review passes have failed to close it"). No quoted part of it names HasStation `[UNKNOWN whether later prompt text hinted at it; other agents cover the transcript]`.
4. **First git appearance:** b072c09 (09-11 08:18, gpt-6-astra, no trailer), the "revision_asimetrias_sd_umd" package. It includes `01_seleccion/seleccion_sd_paso_a_paso.{py,ipynb,html}`, `read_original_adst.py`, `adst_counts_fast.csv` (106,281 rows), paired bootstrap tests and a UMD selection check. Then 98a48c9 (08:29), the advisor summary: "exigir que exista una estación SD reconstruida induce la inversión … El efecto demostrado es un **sesgo de selección respecto de la población previa a ese requisito**, no una nueva interacción atmosférica ni un fallo demostrado de Offline". (Roughly: "requiring a reconstructed SD station induces the inversion … the demonstrated effect is a selection bias relative to the population before that requirement, not a new atmospheric interaction or a demonstrated Offline failure.") It is honest about limits: the pre-requirement SD minus UMD difference is −0.013 [−0.090, +0.055] in the far bin, "compatible con cero en esa banda, pero las curvas no coinciden en todo el rango radial" ("compatible with zero in that band, but the curves do not match over the whole radial range").
5. **User's key verification question** (codex 01a08ba1, ~2026-09-11T16:5xZ): "when you did the anaylys you pulled the data up using literaly the same procesing code i use … but only taking out the flag HasStation?" Astra: "removing `HasStation` from your existing pipeline is not necessarily equivalent to using a separate reader". This question is what motivated the independent reprocessing.
6. **Reception in the talk (Claude Opus 5, session bdf6654e):** 114fd52 (09-17 11:22) puts it on slide 23 as "HIPOTESIS - EN VERIFICACION", with a mechanism sentence ("harder muonic component") that the author rejected (ca3037a, 13:15; badge relabeled "ANALISIS PRELIMINAR -- EN VERIFICACION").
7. **Independent confirmation (Claude Opus 5, session f032527f, worktree reprocesamiento-sd-completo):**
   - 8d4b5a0 (09-17 18:03) found that "Removing the skip is not enough", because Offline does not write UMD modules for untriggered SD stations. It rebuilt the reader to emit an `estaciones_sd/` table of all simulated SD stations with a `has_sd_rec` flag, and validated it against both the v11 parquet and Astra's extraction.
   - c332ab8 (09-24 00:17), on the user-run v13 data: at 1200–1350 m the SD muon A1 is +0.069 without the requirement and −0.124 with it; the EM component is +0.518 vs +0.448. "Same showers, same MC counts, same geometry, so the inversion at large r follows from the requirement alone."
8. **What is still not in git:** no change to `Tesis - Latex/` (Ch. 6 still carries the old account) and no change to CLAUDE.md §5/§6. The real-data readers apply the same `HasStation` requirement, which matters for Ch. 7. Although the physics mechanism (how the requirement correlates with azimuth) is sketched as a hypothesis in 98a48c9, it is "pendiente de aislar" (still to be isolated).

**Verdict on the brief's summary:** it is consistent with git on actor (Astra first), location (v8-2 l.182) and direction of the effect. There are two precision issues:
- The sign flip in the far bin is +0.069 → −0.124. The +0.068 → −0.095 pair belongs to the broader 1050–1400 m band.
- The "reconstruction requirement" was not introduced by any AI. It is a 2025-10 human-written cut that the AI-era reviews missed for about 12 days (08-29 → 09-10).

---

## 7. Open questions for the author

1. PR titles and bodies, and whether any GitHub review comments exist: `gh` is not installed. Could you export `gh pr list --state all --json …` from another machine?
2. Was the 08-29 12:48 commit + push of CLAUDE.md something you wanted, or the trigger for the "don't commit" rule? And did "do that" on 08-31 include the rebase and force-push?
3. Why keep the language rule and worktree-`cp` rule out of CLAUDE.md (eab871f)? A side effect is that Codex (via AGENTS.md) never sees them, and `language-convention.md` wrongly claims they are in CLAUDE.md §2.
4. Should CLAUDE.md §5/§6 now be updated with the selection-bias result and the stale "soft/divergent population" explanation, plus a warning that the real-data readers (`readADST_data_v19.py:157`) apply the same `HasStation` requirement?
5. Will the ~1/√3 SD error-bar underestimate in `plots_seccion_6` (c332ab8) be corrected in the Ch. 6 figures?
6. Did you personally review the 168 k-line b072c09 before merging it 3 minutes after the push, or was the merge based on Astra's summary?
7. Was the `*.xml` gitignore incident on 2026-03-30 (SDenseStationList.xml untracked, then restored) known to the agents? It is the same failure class as the 09-02 `.ipynb` loss.
