from __future__ import annotations

import subprocess

from soc_cli.common import expand_model
from sbx import sbx


def run_quick(
    task: str, agent: str, model_label: str
) -> subprocess.CompletedProcess[str]:
    model = expand_model(model_label)
    return sbx.run("--agent", agent, "--model", model, task)
