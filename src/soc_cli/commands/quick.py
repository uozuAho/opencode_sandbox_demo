from __future__ import annotations

import subprocess

import typer

from sbx import sbx

from soc_cli.common import expand_model

DEFAULT_MODEL = "gptmini"


def run_quick(task: str, agent: str, model_label: str) -> subprocess.CompletedProcess[str]:
    model = expand_model(model_label)
    return sbx.run("--agent", agent, "--model", model, task)


def quick(task: str, agent: str = "coder", model_label: str = DEFAULT_MODEL) -> None:
    result = run_quick(task=task, agent=agent, model_label=model_label)
    raise typer.Exit(result.returncode)
