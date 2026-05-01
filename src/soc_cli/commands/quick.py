from __future__ import annotations

import typer

from sbx import sbx

from soc_cli.common import expand_model, DEFAULT_MODEL


def quick(task: str, agent: str = "coder", model_label: str = DEFAULT_MODEL) -> None:
    """
    Use the coder agent to do a quick task in the current branch
    """
    model = expand_model(model_label)
    result = sbx.run(agent=agent, model=model, prompt=task)
    raise typer.Exit(result.returncode)
