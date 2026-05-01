from __future__ import annotations

import typer

from sbx import sbx

from soc_cli.common import expand_model, DEFAULT_MODEL


def plan(prompt: str, agent: str = "coder", model_label: str = DEFAULT_MODEL) -> None:
    model = expand_model(model_label)
    result = sbx.run("--agent", agent, "--model", model, prompt)
    raise typer.Exit(result.returncode)
