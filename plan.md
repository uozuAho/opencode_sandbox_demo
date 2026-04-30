## Phase 0 — Discovery and precise behavior capture

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

### Task 0.2 — Decide and document command mapping
- Define final `soc` command surface (subcommands/options/aliases).
- Map old -> new, e.g.:
  - `just plan <prompt> [model]` -> `soc ask|plan ...` (needs decision)
  - `just quick ...` -> `soc quick ...`
  - etc.
- Explicitly document whether `soc plan` and `soc ask` are both supported, or
  only one.

**Done when:** there is a single authoritative CLI contract with examples.

---

## Phase 1 — Package scaffold and CLI skeleton

### Task 1.1 — Create Python package layout for distributable CLI
- Add standard `src/` layout:
  - `src/soc_cli/__init__.py`
  - `src/soc_cli/main.py` (Typer app entry)
  - `src/soc_cli/commands/` (one module per command)
  - `src/soc_cli/services/` (subprocess/git/sbx/opencode wrappers)
  - `src/soc_cli/config/` (config loading + models)
  - `src/soc_cli/errors.py`
- Add package metadata and console entry point:
  - package name: `sandboxed-opencode`
  - script entry: `soc = soc_cli.main:app`

**Done when:** `uv run soc --help` (or equivalent local invoke) displays Typer
help.

### Task 1.2 — Establish coding conventions and error model
- Define a small exception hierarchy (user errors vs command failures).
- Ensure all user-facing failures are friendly and return non-zero code.
- Define a common command runner API built on `subprocess.run(..., check=True)`.
- Add `--verbose` global option to print emitted shell commands.

**Done when:** all command modules can call a shared runner and produce
consistent errors.

---

## Phase 2 — Core shared logic parity

### Task 2.1 — Implement model alias expansion service
- Port aliases from `_common.sh` to Python defaults.
- Keep invalid model behavior explicit (`Invalid model name ...`).
- Support fully-qualified model IDs directly without alias expansion failure.

**Done when:** aliases resolve exactly to current IDs and invalid alias handling
is deterministic.

### Task 2.2 — Implement sandbox naming + ensure logic
- Port `expectedSandboxName` logic:
  - expected name = `opencode-<cwd basename>`
  - replace `_` with `-`
- Port ensure behavior:
  - if sandbox missing from `sbx ls`, create with template image and current dir
- Keep template configurable (default from current script value).

**Done when:** in a repo with no expected sandbox, running a soc command creates
it once then reuses.

### Task 2.3 — Implement shared sbx invocation helpers
- Add helper for current branch context (`sbx run <sandbox> -- run ...`).
- Add helper for named branch context (`sbx run <sandbox> --branch <name> -- run
  ...`).
- Ensure args with spaces/quotes are passed safely (no shell string
  concatenation).

**Done when:** helper APIs cover all current command use-cases.

---

## Phase 3 — Implement user commands (parity first)

### Task 3.1 — Implement `soc quick`
- Inputs: task text + optional model + optional agent override.
- Defaults: model alias default equivalent to current (`gptmini`), default agent
  = coder.
- Behavior: run opencode in expected sandbox/current branch with quoted task.

**Done when:** `soc quick "..."` behaves like `just quick "..."`.

### Task 3.2 — Implement `soc task`
- Inputs: task file path + optional model/agent.
- Prechecks parity:
  - task path exists
  - task file is tracked (`git ls-files --error-unmatch` equivalent)
  - task file has no uncommitted changes vs `HEAD`
- Branch/worktree name: task filename minus `.md`.
- Behavior: run opencode in sandbox branch with prompt `follow the instructions
  in <path>`.

**Done when:** failure modes and success path match current script expectations.

### Task 3.3 — Implement `soc approve`
- Inputs: task path + merge message.
- Behavior parity:
  - derive task branch name from file stem
  - `git merge --no-ff <task_branch> -m <msg>`
  - remove worktree
  - delete branch
  - delete task file
- Add prechecks for safety:
  - ensure target branch/worktree exists before destructive actions
  - validate current branch is safe for merge (not task branch itself)

**Done when:** approved task is merged and fully cleaned up with clear errors on
invalid state.

### Task 3.4 — Implement `soc reject`
- Inputs: task path.
- Behavior parity:
  - force remove worktree
  - delete task branch
  - delete task file
- Add prechecks for safety and clear confirmations when destructive.

**Done when:** rejected task branch/worktree/task file are removed predictably.

### Task 3.5 — Implement `soc ask` (new)
- Define purpose clearly (ambiguity currently):
  - likely “ask agent a quick question in current repo sandbox”.
- Implement consistent flags/options with `quick`.
- Ensure docs/examples show when to use `ask` vs `quick`.

**Done when:** `soc ask` has clear semantics and works end-to-end.

### Task 3.6 — Optional compatibility wrappers via `just`
- Keep existing `just` recipes temporarily, delegating to `soc` commands.
- Mark as deprecated in help/readme with migration examples.

**Done when:** existing local workflows still work while users migrate.

---

## Phase 4 — Layered config system

### Task 4.1 — Define config schema and defaults
- Schema sections:
  - `models.aliases`
  - `defaults.agent_per_command`
  - `sandbox.template_image`
  - optional `safety` flags (confirmations, strict prechecks)
- Decide parser (TOML) and validation approach (typed dataclasses /
  pydantic-style equivalent).

**Done when:** schema is documented with example config file.

### Task 4.2 — Implement config load/merge precedence
- Merge order (highest -> lowest):
  1. CLI flags
  2. local repo config (e.g. `.soc.toml`)
  3. user config (`~/.config/soc/config.toml`)
  4. package defaults
- Add `soc config show --effective` (or equivalent debug output).

**Done when:** precedence is test-covered and easy to inspect.

### Task 4.3 — Wire config into every command
- Ensure each command resolves effective values via common config service.
- Avoid ad-hoc defaults in command modules.

**Done when:** changing config affects commands predictably without code
changes.

---

## Phase 5 — Safety and dependency checks (QoL)

### Task 5.1 — Startup dependency checks with actionable hints
- Check availability of required binaries:
  - `git`
  - `sbx`
  - `opencode`
- On missing dependency, provide install hint and fail fast.
- Validate sandbox template assumptions before create.

**Done when:** first failure message tells user exactly how to unblock.

### Task 5.2 — Add confirmations for destructive operations
- For `approve`/`reject`, add confirmation prompts by default.
- Add `--yes`/`--force` to bypass prompts for automation.
- Print exact resources to be deleted before confirmation.

**Done when:** accidental destructive actions are harder while CI remains
scriptable.

### Task 5.3 — Improve git state prechecks
- Ensure commands fail clearly when:
  - not inside a git repo
  - merge conflicts/unmerged state exists
  - target task branch/worktree missing or mismatched
- Keep behavior explicit and deterministic.

**Done when:** edge-case failures are caught before side-effects.

---

## Phase 6 — Testing strategy (required for weaker agent reliability)

### Task 6.1 — Unit tests for pure logic
- Test model alias expansion.
- Test sandbox name derivation.
- Test config merge precedence.
- Test command argument normalization.

### Task 6.2 — Integration tests with subprocess mocking
- Assert exact subprocess command arrays for each subcommand.
- Assert error mapping and exit codes.
- Assert `--verbose` output includes emitted commands.

### Task 6.3 — End-to-end smoke checklist (manual)
- In a temporary git repo, verify:
  - `soc quick`
  - `soc task` with committed clean task file
  - `soc approve`
  - `soc reject`
  - sandbox auto-create path
- Record expected output and recovery steps in docs.

**Done when:** test suite and manual smoke steps catch parity regressions.

---

## Phase 7 — Documentation and migration

### Task 7.1 — Installation docs for global CLI
- Add `uv tool install sandboxed-opencode` instructions.
- Document upgrade/uninstall commands.
- State supported platform explicitly (Linux-only for now).

### Task 7.2 — Usage docs from arbitrary repos
- Add examples equivalent to old just flows:
  - `soc quick ...`
  - `soc task ...`
  - `soc approve ...`
  - `soc reject ...`
  - `soc ask ...`
- Include model alias override examples.

### Task 7.3 — Troubleshooting section
- Missing `sbx`.
- Missing template image.
- Missing OpenRouter auth.
- Sandbox name mismatch surprises.

### Task 7.4 — Deprecation/migration note for `just`
- Explain compatibility window.
- Give old->new command mapping table.

**Done when:** new users can install and run without reading shell scripts.

---

## Phase 8 — Release readiness

### Task 8.1 — Final parity verification
- Compare each old command behavior against new `soc` equivalent.
- Verify no required workflow was dropped.

### Task 8.2 — Version and release checklist
- Set initial package version.
- Add changelog entry for migration.
- Tag release once smoke tests pass.

### Task 8.3 — Post-release follow-up tasks
- Collect early user feedback on `ask` semantics and safety prompts.
- Remove `just` wrappers after agreed deprecation period.

---

## Explicit ambiguities to resolve before implementation starts

1. **`ask` command semantics:** should `ask` use planner agent by default, or
   coder, or a distinct “question-only” behavior?
2. **`plan` vs `ask`:** should both commands exist, or should one alias the
   other?
3. **Compatibility period:** do you want to keep `just` wrappers, and for how
   long?
4. **Confirmation defaults:** should `approve/reject` always prompt unless
   `--yes` is provided?
5. **Model handling:** should unknown model strings be rejected, or treated as
   full model IDs by default?

If these five points are confirmed up front, implementation can proceed with
minimal rework.
