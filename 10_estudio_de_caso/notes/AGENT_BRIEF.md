# Brief for evidence-extraction agents (Phase 1)

You are one of several parallel agents reconstructing, **from primary evidence only**, how an
AI-assisted physics investigation unfolded in this repository. The output feeds a course
report on AI agents in research, so what matters is both the **physics story** and the
**AI workflow story**.

## The project in two paragraphs
The repo is Lautaro Silva Pizzi's Licenciatura thesis (FCEN-UBA / ITeDA) on the
first-harmonic azimuthal asymmetry A1 of the muon density (ρ(φ)=ρ0(1+A1 cos φ)) measured
by the AMIGA Underground Muon Detector (UMD) of the Pierre Auger Observatory, compared to
the Surface Detector (SD, water-Cherenkov tanks). A puzzling result: the SD muon A1
**inverts sign** (late-side excess) at large core distance, while the UMD does not. The
author first published GAP-2026-041 (an earlier draft, "[Version_Vieja]", had a
kinematic-divergence anti-asymmetry argument that the supervisor had removed).

From 2026-08-29 onward the author used AI agents: Claude Code (models claude-sonnet-5 /
claude-opus-5) and OpenAI Codex CLI (models gpt-5.6-sol, **gpt-6-astra** = "Astra",
codex-auto-review). Over several sessions they tried phenomenological explanations
(attenuation, geometry/divergence, geomagnetic, kinematic divergence, Bertou–Billoir…),
with corrections and retractions. Eventually the inversion was attributed to a
**selection bias**: the MC pipeline (`Scripts/Procesamiento_ADST_v8-2.py` ~l.182) requires
`sEvent.HasStation(sdId)` (a reconstructed SD partner station). That requirement removes
stations non-uniformly in azimuth. The far-bin SD A1 is +0.068 without the requirement
and −0.095 with it, so the inversion is produced BY the requirement. (An earlier version of
this brief stated the direction backwards; corrected after agent T2 flagged it.) Your job is to establish **what actually happened**, not to confirm this summary.
If the evidence contradicts it, say so loudly.

## Paths
- Worktree (git works here; your note goes here):
  `/home/lsilva/Github/Tesis-de-Licenciatura---ITeDA/.claude/worktrees/claude+proyecto-final-ia`
- Main checkout (has **untracked** folders not in the worktree; read-only for you):
  `/home/lsilva/Github/Tesis-de-Licenciatura---ITeDA`
- Extracted transcripts (one .md per session; `index.csv` lists model, start and end):
  `<worktree>/claude_work/Proyecto_Final_IA/notes/_transcripts/`
  Format: `### [timestamp] ROLE (model)` blocks with full text. Tool calls and results are one-liners.
  Raw originals: `~/.claude/projects/*ITeDA*/` and `~/.codex/sessions/`, if you need more detail on a tool result.

## Hard rules
1. **Read-only**, except for writing your single assigned note file. No git writes (no
   add/commit/checkout/stash/reset). No edits anywhere else. No heavy compute: don't run
   the analysis pipelines or anything touching ROOT/ADST.
2. For shell commands, don't `cd` into the main checkout. Use absolute paths or the Read/Grep
   tools. Run git read commands (`git log`, `git show`) from the worktree.
3. **Never copy internal collaboration-server paths or collaborator usernames** into your
   note (e.g. the data-server path in `ADST2ASCII/run.sh`). Write "[internal server path]".
   Don't copy `~/.codex/auth.json` or any credentials.
4. **Evidence for every claim:** commit hash, `path:line`, or `session-id @ timestamp`.
   Quote short passages verbatim (≤3 lines) when they matter, especially user messages
   that steer, correct or push back, and AI statements later shown wrong. Mark inferences
   as `[INFERENCE]` and unknowns as `[UNKNOWN]`. Never fill gaps with plausible fiction.
5. Attribute actors precisely: USER (the author), which model (e.g. claude-opus-5, gpt-6-astra),
   or a named subagent. Note when git shows "Lautaro Silva" as author but the transcript shows
   an agent did the work.
6. Write your note in **English**.

## Note template (write to `<worktree>/claude_work/Proyecto_Final_IA/notes/<your_file>.md`)
```
# <Source family> — evidence notes
Agent scope: ...   Sources read: (list, with sizes/sessions)   Coverage gaps: ...

## 1. Chronological events
| Timestamp (UTC or as given) | Actor | Event | Evidence |

## 2. Physics claims made and their fate
(claim → who made it → when → later confirmed / corrected / retracted, by whom, evidence)

## 3. AI workflow techniques observed
(prompting style and quoted prompts, CLAUDE.md/AGENTS.md use, memory, subagents/parallel agents,
worktrees, cross-model review, self-review, human approval gates, jupytext pairing, etc.;
each with evidence)

## 4. Failures, errors, corrections
(hallucinations, wrong physics accepted, bugs introduced or caught, destructive actions,
over-volume, retractions; who caught each one, and how)

## 5. Human-in-the-loop moments
(user steering, pushback, decisions; quote the user)

## 6. The selection-bias thread
(every mention of HasStation / selection / "sesgo de selección" / reconstruction requirement:
first appearance, who raised it, the trigger, how it was tested, and how it was received)

## 7. Open questions for the author
```
Aim for a thorough but readable note (typically 300–900 lines). Precision beats volume.
When you finish, reply with a ≤250-word summary of your most important findings,
including any contradiction with the summary above.
