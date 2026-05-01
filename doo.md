# Create Python package for distributable CLI

Add package metadata and console entry point to pyproject.toml:
  - package name: `sandboxed-opencode`
  - script entry: `soc = soc_cli.main:app`

Users should be able to run `uv tool install .`, then run `soc` anywhere

**Done when:** `uv run soc --help` (or equivalent local invoke) displays Typer
help.
