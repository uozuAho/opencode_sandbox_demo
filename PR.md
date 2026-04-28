## Summary

- Added a custom sandbox `Dockerfile` based on
  `docker/sandbox-templates:opencode` that installs `just` via `apt`.
- Added `docs/custom-sandbox.md` with step-by-step usage instructions:
  build/push template, export `OPENROUTER_API_KEY` on host, run `sbx` with
  `--template`, and verify `just` is installed.

## Validation

- `just check-all`
