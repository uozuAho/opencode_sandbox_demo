from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


SBX_ROOT = Path(".sbx/opencode-opencode-demo-worktrees")
CUSTOM_TEMPLATE = "docker.io/library/opencode-openrouter-just:latest"


def expand_model(model: str) -> str:
    models = {
        "gptmini": "openrouter/openai/gpt-5.4-mini",
        "glm51": "openrouter/z-ai/glm-5.1",
        "gpt-53-codex": "openrouter/openai/gpt-5.3-codex",
        "sonnet46": "openrouter/anthropic/claude-sonnet-4.6",
        "kimi": "openrouter/moonshotai/kimi-k2.5",
        "gemma4": "openrouter/google/gemma-4-31b-it:free",
        "minimax25": "openrouter/minimax/minimax-m2.5:free",
    }
    try:
        return models[model]
    except KeyError as exc:
        raise ValueError(f"Invalid model name {model}") from exc


def run_sbx(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["sbx", *args], check=check, text=True, capture_output=True)


def expected_sandbox_name(cwd: Path | None = None) -> str:
    current_dir = cwd or Path.cwd()
    return f"opencode-{current_dir.name}".replace("_", "-")


def ensure_sandbox_exists(expected_sandbox_name: str) -> None:
    result = run_sbx("ls", check=True)
    if expected_sandbox_name not in result.stdout:
        print(f"Expected sandbox {expected_sandbox_name} not found, creating...")
        run_sbx("create", "-t", CUSTOM_TEMPLATE, "opencode", ".")
    print(f"Expected sandbox exists: {expected_sandbox_name}")


def run_sbx_custom(expected_sandbox_name: str, *args: str) -> subprocess.CompletedProcess[str]:
    ensure_sandbox_exists(expected_sandbox_name)
    return run_sbx("run", expected_sandbox_name, "--", "run", *args)


def run_sbx_custom_branch(
    expected_sandbox_name: str, branch: str, *args: str
) -> subprocess.CompletedProcess[str]:
    ensure_sandbox_exists(expected_sandbox_name)
    return run_sbx("run", expected_sandbox_name, "--branch", branch, "--", "run", *args)
