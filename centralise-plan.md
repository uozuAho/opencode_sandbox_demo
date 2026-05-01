# Plan: Centralise Sandbox Runner as a Global `soc` CLI

## Current behavior to preserve

From existing `justfile` + bash scripts, preserve these workflows:

1. `plan`: run planner agent prompt in current repo sandbox
2. `quick`: run coder agent task in current branch
3. `task`: run coder agent in task-specific branch/worktree from a committed
   task file
4. `approve`: merge task branch, remove worktree/branch, delete task file
5. `reject`: discard task branch/worktree, delete task file
6. model label expansion (`gptmini`, `glm51`, etc.)
7. sandbox auto-ensure logic based on current working directory name

## CLI UX

Similar to how `just` works now in this project. Changes: exe is now
called `soc`, and you can run it from anywhere. Examples that do the
same as their `just` counterparts:

```sh
soc quick "check my readme for inconsistencies"
soc task tasks/task2.md
soc task tasks/task2.md --model codex
soc approve tasks/task2.md "added changes"
soc reject tasks/task2.md
```


## Design choices
### 1) Build a Python package with console entry point

Create a distributable package called `sandboxed-opencode` exposing entry point:

- `soc = soc_cli.main:app`

Install options for “run anywhere”:

`uv tool install <package>`

This gives a global `soc` in PATH without copying scripts into target repos.

Only support linux and uv for now.

### 2) Use modern CLI stack

- Use Typer for subcommands/options/help
- `subprocess.run(..., check=True)` for `sbx` / `git` / `opencode run`
- `pathlib.Path` for path correctness
- structured error handling with user-friendly messages and non-zero exit codes

### 3) Configuration model

Support layered config for portability:

1. CLI flags (highest priority)
2. local repo config (optional, e.g. `.soc.toml`)
3. user config (`~/.config/soc/config.toml`)
4. defaults baked into package

Include:

- model alias map (current aliases from `_common.sh`)
- default agent per command
- sbx template image

### 4) Keep shelling out; don’t reimplement git/sbx internals

Continue using `git` and `sbx` commands rather than trying to reimplement
behavior in Python libraries. This keeps semantics close to existing scripts and
reduces migration risk.


## Phase 1 — parity implementation

- Implement `soc quick/task/approve/reject/ask` with behavior matching scripts
- Keep `just` commands as wrappers temporarily (optional compatibility period)
- Add `--verbose` for emitted shell commands

## Phase 2 — packaging + install docs

- Add install docs for `uv tool`
- Add “no-copy” usage examples from arbitrary repos
- Add troubleshooting section for missing `sbx`, missing template, missing auth

## Phase 3 - QoL improvements

- environment assumptions (sbx/opencode/git availability)
  - add startup dependency checks with actionable install hints

- accidental destructive git operations
  - add explicit prechecks, confirmation prompts where appropriate
