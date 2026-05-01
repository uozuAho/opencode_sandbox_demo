from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import typer

from sbx import sbx


def _task_name(task_path: Path) -> str:
    return task_path.stem


def reject(task_path: Path) -> None:
    """
    Delete the worktree corresponding to the given task file.
    """
    if not task_path.exists():
        typer.echo(f"Error: {task_path} does not exist")
        raise typer.Exit(1)

    task_name = _task_name(task_path)
    worktree_path = sbx.worktrees_dir(Path.cwd()) / task_name

    assert worktree_path.exists()

    subprocess.run(
        ["git", "worktree", "remove", "--force", str(worktree_path)], check=True
    )
    subprocess.run(["git", "branch", "-d", task_name], check=True)
    shutil.rmtree(worktree_path, ignore_errors=True)
    task_path.unlink()
    raise typer.Exit(0)
