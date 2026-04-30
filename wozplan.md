### Task 0.1 — Freeze current command behavior in a reference doc
- Read and summarize exact behavior from:
  - `justfile`
  - `scripts/_common.sh`
  - `scripts/plan.sh`
  - `scripts/quick.sh`
  - `scripts/task.sh`
  - `scripts/approve.sh`
  - `scripts/reject.sh`
- Record:
  - exact input args
  - prechecks
  - shell commands invoked
  - error messages and exit behavior
  - side-effects (git/worktree/file deletion)
- Output to a new internal doc (e.g. `docs/parity-reference.md`).

**Done when:** a new contributor can reproduce current behavior without opening
shell scripts.
