from __future__ import annotations

import subprocess

from soc_cli.common import expand_model
from sbx.sbx import run_sbx_custom


def run_quick(
    agent: str, model_label: str, task: str
) -> subprocess.CompletedProcess[str]:
    model = expand_model(model_label)
    return run_sbx_custom(
        "opencode-openrouter-just", "--agent", agent, "--model", model, task
    )
