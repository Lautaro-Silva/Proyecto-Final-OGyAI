# Project memory

## Confirmed context — 2026-10-01

- User: Manuel. Communicate in plain Spanish; he wants a short accessible explanation,
  persistent project context, and a first talk draft that can later be edited.
- He confirmed the course talk is 15–20 minutes, not the RAFA physics talk.
- Remote: https://github.com/Lautaro-Silva/Proyecto-Final-OGyAI.git
- Active local checkout: `Proyecto-Final-OGyAI/` under the workspace. Initial HEAD:
  `2b56e30`. Task branch: `codex/memoria-charla-curso`.
- Adjacent `Proyecto-Final-OGyAI-main/` was extracted from the supplied ZIP before
  cloning. It is a snapshot, not the active checkout.

## Reading and source hierarchy

- Reviewed the root README, full archived CLAUDE.md, case-study README/PROGRESS,
  short report, substantial extended-report content, analysis notes, author answers,
  director summary, and reprocessing README. Not every file was read; no raw session
  logs or physics pipelines were executed in this session.
- Prefer the final extended report and author answers over preliminary analysis notes.
  The latter still contain superseded interpretations and a course quote that the
  progress log explicitly records as fabricated and corrected later.
- The historical thesis instructions have stale paths and pre-discovery conclusions.
  Preserve them as evidence; root AGENTS.md provides current course-repo instructions.

## Scientific guardrails

- Selection induces the SD muon sign inversion in the studied Monte Carlo sample.
  This is not a demonstrated Offline bug or a conclusion about all real data.
- Correcting the `HasStation` line alone cannot restore the population: the UMD
  iteration was already conditional. A separate simulated SD station table matters.
- Final highlighted band 1200–1350 m: SD +0.069 before vs −0.124 after selection;
  UMD +0.082. First control +0.068 vs −0.095 uses a different band/estimator.
- UMD remains selected; residual SD–UMD differences below 900 m remain unexplained.
- One case cannot isolate model/vendor effects from fresh context and prompting.

## Deliverables

- `EXPLICACION_CORTA.md`: accessible project summary in Spanish.
- `CHARLA_CURSO_BORRADOR.md`: 12-slide content outline with oral script, source
  pointers, existing figure links, a labeled illustrative selection example, and Q&A.
  Proposed timing sums to 18 minutes; rehearsal still needed. This is editable
  content, not a rendered slide deck.
- `AGENTS.md`: current instructions to read and maintain this memory.

## Pending

Validation performed: all local Markdown links in the two new Spanish deliverables
resolve; the talk has 12 numbered slides and its proposed timings total 18 minutes.
The illustrative table's means are 5, 4, 5, and 6. Scientific numbers were checked
against the director summary and final report, not recomputed from raw simulation.

- User supplied the Git author email on 2026-10-01; use Manuel Racca as the name.
  Configure identity only for this checkout.
- Deliverables were committed as `e50ae2d` on `codex/memoria-charla-curso`,
  authored by Manuel Racca with the email the user provided.
- Push to `origin` failed with HTTP 403: GitHub denied write permission to the
  authenticated account `manuelracca` on `Lautaro-Silva/Proyecto-Final-OGyAI`.
  Network escalation was approved and authentication completed; repository write
  access is the remaining issue. Nothing has been published.
- Asked the user to either obtain collaborator access from Lautaro or supply the
  URL of a writable copy in their own account. Once access is available, push the
  current task branch (including this publication-status update), then verify the
  remote commit. Do not retry the same denied push before access changes.
- Speaker allocation, rehearsal, and visual slide layout remain for the next iteration.
- No full independent re-audit of the historical scientific evidence was performed.
