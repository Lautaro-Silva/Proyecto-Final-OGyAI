---
name: git-push-workflow
description: In the Tesis-de-Licenciatura---ITeDA repo, push to a separate branch for PR review, never directly to main
metadata:
  pinned: true
---

In this repository (the user's Licenciatura thesis project at ITeDA), when work is ready to be pushed to the remote (`origin`, a GitHub repo), it must go to a separate branch rather than directly to `main`. The user wants to review the change and go through a pull request and merge themselves, rather than having commits land on `main` directly from a push. This is on top of — not a replacement for — the existing rule (from this repo's own `CLAUDE.md`) that `git add`/`commit`/`push` always require the user's explicit permission first; even once permission for a push is given, the push itself should target a feature branch, not `main`.
