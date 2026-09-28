# Missing sources and factual ambiguities

## Sources needed from the author

| # | Source | Why it's needed | Priority |
|---|---|---|---|
| S1 | **Consent to read** the local Claude Code transcripts (`~/.claude/projects/*ITeDA*`, 16 sessions) and Codex transcripts (`~/.codex/sessions`) | They are the primary record of what each agent proposed, and when. Without them, attribution rests on commit messages. Read-only use; quotes get sanitized (no server paths or usernames) | **High** |
| S2 | ChatGPT web conversations (if "Astra" was, or also used, the ChatGPT web UI rather than only Codex CLI), exported | The selection-bias discovery moment may live there | **High** if they exist |
| S3 | Any claude.ai web chats about the thesis (before or during) | Pre-Aug-29 AI use; the "first Claude review" might be a web chat | Medium |
| S4 | Supervisor feedback (emails/messages) on Version_Vieja and on the selection result, a paraphrase is fine | The "supervisor's call" to remove the kinematic-divergence argument is a key human-in-the-loop moment | Medium |
| S5 | Course materials/slides you want explicitly linked (topics, readings) | For the "links to course content" section | Medium |

## Factual ambiguities

| # | Question | Current evidence |
|---|---|---|
| F1 | Date of the Version_Vieja GAP note, and publication date of GAP-2026-041 | Only enter git on 2026-08-31 (`c915ce7`) |
| F2 | Was Version_Vieja/GAP-041 written with any AI help? | none |
| F3 | *Mostly resolved:* Astra = OpenAI model `gpt-6-astra`, run through the Codex CLI (thread `01a08ba1…`). Still open: is the shared link `cx_6ab4a22f…` the same thread? Did you also use ChatGPT web for this? | Codex session logs |
| F4 | The brief mentions "the Opus 5.5 work", but the transcripts show earlier Claude sessions used only `claude-sonnet-5` and `claude-opus-5`. `claude-opus-5-5` appears only in the 2026-09-24 case-study session. Did you mean Opus 5? Or was Opus 5.5 used somewhere not logged here (e.g. claude.ai web)? | `notes/_transcripts/index.csv` |
| F5 | The brief's ordering is "Claude review → Astra review → later Claude review/re-reasoning/Opus 5.5". Git suggests Claude review (09-02) → Claude explainer/unified model (09-03 → 09-10) → Codex package (09-10/11) → Claude review of Astra (09-11) → reprocessing (09-17/24). Does that match your memory? What was the "re-reasoning pass"? | See `timeline.md` |
| F6 | `[UNFINISHED]GAP_Core_REC` (core reconstruction bias attenuating the early-late asymmetry): should it be part of the story? | Folder exists; "promote core-bias result" in `61e5df1` |
| F7 | *Resolved:* `c332ab8` and `0ecae20` were made by Claude Opus 5 (session f032527f). The integrated drafts are by Astra plus 3 Codex subagents (09-24 03:24–03:39 UTC), and are uncommitted | notes |
| F8 | Is the shared link `chatgpt.com/s/cx_6ab4a22f…` the Codex thread `01a08ba1` (Sep 10 → 24)? Any other ChatGPT/Codex conversations not stored in `~/.codex/sessions` (e.g. the ChatGPT web app)? | link 403 |
| F9 | Does GAP-2026-041's Table 1 SD-Muon(MC) −0.10 come from the `HasStation`-gated parquet? It matters for the report: it would mean the *published* number already contains the selection effect | REVIEW_ASTRA §7.0 open |
| F10 | When exactly did you give the RAFA talk (09-17?), and which version of the SD slide was shown? Any reactions from the audience or your advisors to the HasStation slide? | `bdf6654e` |
| F11 | Why did the reprocessing move from Astra to Claude on 09-17: the Codex usage limit, or a deliberate choice? | Codex usage limit at 14:26 UTC; you asked Claude at 16:32 UTC ("astra kept fucking up") |
| F12 | Who removed the untracked `claude_work/reprocesamiento_sd_completo/` from the main checkout on 09-24? Claude deleted it at your "delete what needs to be deleted", after preserving your run notebook in `0ecae20`. Please confirm that is what you intended | `f032527f` @03:19–03:22 |
