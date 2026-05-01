from __future__ import annotations

import subprocess
from pathlib import Path

import typer

from sbx import sbx

from soc_cli.common import expand_model, DEFAULT_MODEL


def _task_name(task_path: Path) -> str:
    return task_path.stem


def _ensure_committed(task_path: Path) -> None:
    committed = subprocess.run(
        ["git", "ls-files", "--error-unmatch", str(task_path)],
        check=False,
        capture_output=True,
        text=True,
    )
    if committed.returncode != 0:
        typer.echo(
            f"Error: {task_path} has not been committed to the current working tree"
        )
        raise typer.Exit(1)

    clean = subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", str(task_path)],
        check=False,
        capture_output=True,
        text=True,
    )
    if clean.returncode != 0:
        typer.echo(f"Error: {task_path} has uncommitted changes")
        raise typer.Exit(1)


def task(
    task_path: Path, agent: str = "coder", model_label: str = DEFAULT_MODEL
) -> None:
    model = expand_model(model_label)
    _ensure_committed(task_path)
    result = sbx.run(
        agent=agent,
        model_label=model,
        prompt=f"follow the instructions in {task_path}",
        branch=_task_name(task_path),
    )
    raise typer.Exit(result.returncode)
