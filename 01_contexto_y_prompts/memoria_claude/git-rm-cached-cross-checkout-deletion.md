---
name: git-rm-cached-cross-checkout-deletion
description: In the Tesis-de-Licenciatura---ITeDA repo, git rm --cached only spares the working tree where you ran it — it deletes the file from disk in every other checkout (including the user's own main checkout) on their next pull
metadata:
  pinned: false
---

In this repository (the user's Licenciatura thesis project at ITeDA), the user works from
their own main checkout in parallel with Claude Code sessions that operate inside separate
git worktrees. This matters for any future task that involves converting an already-tracked
file to untracked (e.g. `git rm --cached` plus a `.gitignore` entry, done to stop a large or
frequently-changing file — like a Jupyter notebook with embedded outputs — from bloating git).

The mistake made once: after running `git rm --cached` on ten `.ipynb` files inside a Claude
worktree and confirming with `ls` that they were still present on disk *in that worktree*,
the session told the user the files "stay on disk with all figures" as if that were true
everywhere. It is not. `git rm --cached` only skips touching the working tree in the exact
repository copy where the command runs (that is what `--cached` means). The resulting commit
still records the file as deleted from the tracked tree. Any *other* checkout — including the
user's own main checkout, which is where they actually do their interactive work — deletes the
corresponding file from its working directory as soon as it pulls or merges that commit, even
though `.gitignore` now covers the path. `.gitignore` only governs untracked-file handling; it
has no effect on how a checkout applies a tracked-file removal during a pull or merge. The user
pulled the change into their main checkout and lost the on-disk `.ipynb` files (including their
baked-in output figures) as a direct result, even though the content remained fully recoverable
from the pre-removal commit in git history.

The lesson for future sessions in this repo: before pushing a change that removes a
previously-tracked file from git (via `git rm --cached`) in order to stop tracking it going
forward, remember that this deletes the file from every other checkout's disk on their next
pull or merge — verifying persistence in the current worktree proves nothing about what happens
elsewhere. Either avoid this pattern for files whose local, uncommitted-going-forward content
the user actually relies on (e.g. notebook outputs), or explicitly warn the user before they
pull that their main checkout's copy will be deleted and give them the exact `git checkout
<pre-removal-commit> -- <path>` recovery command up front, rather than asserting the file is
safe without checking what happens outside the worktree the command was run in.
