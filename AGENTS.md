This project aims to:

- provide easy ways to run opencode in a sandbox, in any local project
- provide convenient commands to do common workflow tasks such as:
    - ask an agent a quick question
    - get an agent to perform a quick task
    - get an agent to follow instructions in a file, working in its own worktree
    - approve or reject completed worktrees

It currently uses `just` and bash scripts to provide this functionality.

We are currently transitioning to a python cli app to replace `just` and bash. `uv` is
used for python runtime and package management. The cli app is in ./src/soc_cli and
uses Typer as the app framework.

For more info, read ./readme.md
