# Summary

- Ported the quick runner from `scripts/quick.sh` to Python.
- Added a `soc quick` command that expands model labels and invokes `sbx` via `subprocess.run`.
- Kept sandbox creation/execution behavior in the shared `sbx` helper.
