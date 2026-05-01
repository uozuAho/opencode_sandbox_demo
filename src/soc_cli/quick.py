from __future__ import annotations

import subprocess
from pathlib import Path

from soc_cli.common import expand_model
from sbx import sbx


def run_quick(
    task: str, agent: str, model_label: str
) -> subprocess.CompletedProcess[str]:
    model = expand_model(model_label)

    # todo move this to sbx
    sandbox_name = sbx.expected_sandbox_name(Path.cwd())
    sbx.ensure_sandbox_exists(sandbox_name)

    return sbx.run_sbx_custom(
        sandbox_name, "--agent", agent, "--model", model, task
    )
