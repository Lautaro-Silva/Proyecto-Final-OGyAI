# Questions for the author: personal experience

These feed the report's first-person and "lessons" sections. Answer inline, however briefly.
Spanish is fine. New questions are appended as the evidence review goes on.

## Before AI
1. When did you start using AI tools for this thesis (any tool: ChatGPT web, Copilot, Claude web…)? Was there any AI use before the Claude Code session of 2026-08-29? For what?
1b. The Nov-2025 reader code has comments like "¡TU IDEA! Creamos el flag en lugar de filtrar" next to the saturation flag, and "Sin sdStation, no hay geometría" at the HasStation skip. These read like a chat assistant's replies (an agent's inference, unverified). Was that code written with a web chatbot (ChatGPT/Claude.ai)? If so, the HasStation cut itself was *AI-assisted*, and that would change the story.
2. When you abandoned the Fast-MC toy model (July 2026, `6d6b97b`), had any AI been involved in designing it?
3. Why did you decide to bring in an AI agent at the end of August, just before the cover date?

## Working style
4. How did you decide which model/tool to use for which task (Claude Code vs Codex/"Astra" vs chat UIs)? Where does the name "Astra" come from?
5. How much of your time went into reading and verifying AI output vs. doing the work yourself? Did that ratio change over the weeks?
6. The prompts in `thesis_review_prompt*.txt` are very structured (role, reading order, bibliography rule). Did you write them yourself, or with AI help? Did you learn that style in the course?
7. Did you ever run Claude and Codex on the *same* question on purpose, to cross-check them? Or did the cross-review arise by accident?

## The phenomenology → selection-bias arc
8. Before the selection bias surfaced, how convinced were you that the SD inversion was physical? What was your supervisor's view (e.g. on the Version_Vieja kinematic-divergence argument)?
9. What exactly prompted the question that led to `HasStation`? Was it your idea, something you asked Codex to check, or something Codex raised unprompted?
10. What was your reaction when the flip +0.068 → −0.095 appeared? Did you trust it immediately? What convinced you?
11. Looking back, were there earlier moments where the AI (or you) could have caught the selection effect but didn't?

## Failures and friction
12. The `.ipynb` untracking deleted your local figures (2026-09-02). How did that affect your trust in the agent?
13. You pushed back on applying the SD-derived Bertou & Billoir result to the UMD (unified-model retraction). Can you describe that moment? Was it easy to spot?
14. Were there AI claims you accepted and later found wrong, that are *not* documented in the repo?
15. Was anything the AI produced useless or counterproductive, e.g. too much volume to read, or too many versions (v1–v4)?

## Added after reading the session logs (Step 2)

19. **The 09-07 near-miss.** On 09-07 a Claude subagent pointed at `v8-2.py:182` as "the single, unlabelled trigger/selection gate of the entire pipeline". The main agent then "ruled it out" with a test that could not detect it. Did you see that part of `unified_asymmetry_model_v1/report.md` at the time? If so, did it seem convincing?
20. The Codex kickoff prompt was written by Claude and pasted verbatim. Did you read it before pasting? Did you notice it told Codex to treat the "no pipeline artifact" result as established?
21. On 09-02 you wrote "the data I've analysed doesn't seem to have any errors or bugs (we could check later), so … the sign inversion is physical". In hindsight, why did the pipeline audit get deferred? Was it trust in your own code, which had been checked for months?
22. When Astra's result came in (+0.068 → −0.095), you first said "I didn't really get wtf you did", and later "could be the answer to all my problems". How did your confidence evolve? What convinced you: the reproduction of your own figure, Claude's review, or the full reprocessing?
23. You caught the two most consequential engineering bugs (the lost rows and the flag design) from **row counts**, not by reading code. Is that a habit, or luck?
24. Several times you corrected the AI's physics (the probability weighting on 09-04; "B&B was done with the SD" on 09-10). Did the AI ever correct *your* physics in a way you found valuable? (Evidence suggests yes: A_geo's sign, Population B's energy range, the tank cancellation.)
25. You switched Codex to the automatic approval reviewer (`auto_review`) on 09-11. It approved all 109 actions, including the one that dropped 63,747 rows. Did handing off approvals change how closely you watched?
26. Running Claude and Codex in parallel on the same checkout: was that deliberate cross-checking, a way around usage limits, or both? How did you decide which to ask?
27. How much money/usage did the whole thing cost you, roughly? Did the course's Pro access cover it?
28. The volume: 4 versioned review folders, a 223-file package, 7-subagent reviews. How much of it did you actually read? What would you have wanted instead?
29. What did your supervisor(s) say when you showed them the advisor summary (`RESUMEN_PARA_DIRECCION`)?

## Outcomes
16. How did your directors react to the AI-assisted findings (RAFA talk, advisor summary)?
17. What would you do differently if you started the thesis again with these tools?
18. Do you feel the AI helped or hindered finding the selection bias? Why?
