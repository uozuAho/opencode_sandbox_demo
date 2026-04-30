# Goal: Centralise Runner as Global `soc` CLI

Convert the current `just` + bash workflow into a Python package
(`sandboxed-opencode`) that exposes a global `soc` command, while preserving
existing behavior.

Preserve these existing workflows and semantics:

1. `plan`: planner prompt in current repo sandbox
2. `quick`: coder task in current branch
3. `task`: coder in task-specific branch/worktree from a committed task file
4. `approve`: merge task branch, remove worktree/branch, delete task file
5. `reject`: discard task branch/worktree, delete task file
6. model alias expansion (`gptmini`, `glm51`, etc.)
7. sandbox auto-ensure logic based on cwd name
