import subprocess
from pathlib import Path

_CUSTOM_TEMPLATE_IMAGE = "docker.io/library/opencode-openrouter-just:latest"


def sbx_root_dir(cwd: Path | None = None):
    current_dir = cwd or Path.cwd()
    return current_dir / ".sbx"


def run(agent: str, model: str, prompt: str, branch: str | None = None) -> subprocess.CompletedProcess[str]:
    sandbox = _default_sandbox_name()
    _ensure_sandbox_exists(sandbox)
    _args = ["run", sandbox]
    if branch:
        _args += ["--branch", branch]
    _args += ["--", "run", "--agent", agent, "--model", model, prompt]
    return _sbx(*_args)


def _sbx(
    *args: str, check: bool = True, capture_output=False
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["sbx", *args], check=check, text=True, capture_output=capture_output
    )


def _default_sandbox_name(cwd: Path | None = None) -> str:
    current_dir = cwd or Path.cwd()
    return f"opencode-{current_dir.name}".replace("_", "-")


def _ensure_sandbox_exists(sandbox_name: str) -> None:
    result = _sbx("ls", check=True, capture_output=True)
    if sandbox_name not in result.stdout:
        print(f"Expected sandbox {sandbox_name} not found, creating...")
        _sbx("create", "-t", _CUSTOM_TEMPLATE_IMAGE, "opencode", ".")
    print(f"OK: Expected sandbox exists: {sandbox_name}")
