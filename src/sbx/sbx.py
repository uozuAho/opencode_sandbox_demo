import subprocess
from pathlib import Path


_CUSTOM_TEMPLATE_IMAGE = "docker.io/library/opencode-openrouter-just:latest"


def sbx_root_dir(cwd: Path | None = None):
    current_dir = cwd or Path.cwd()
    return current_dir / ".sbx"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    _ensure_sandbox_exists(expected_sandbox_name)
    return _sbx("run", expected_sandbox_name, "--", "run", *args)


def run_sbx_custom_branch(
    expected_sandbox_name: str, branch: str, *args: str
) -> subprocess.CompletedProcess[str]:
    _ensure_sandbox_exists(expected_sandbox_name)
    return _sbx("run", expected_sandbox_name, "--branch", branch, "--", "run", *args)


def _sbx(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["sbx", *args], check=check, text=True, capture_output=True)

def _default_sandbox_name(cwd: Path) -> str:
    return f"opencode-{current_dir.name}".replace("_", "-")


def _ensure_sandbox_exists() -> None:
    sandbox_name = _default_sandbox_name(Path.cwd())
    result = _sbx("ls", check=True)
    if expected_sandbox_name not in result.stdout:
        print(f"Expected sandbox {expected_sandbox_name} not found, creating...")
        _sbx("create", "-t", _CUSTOM_TEMPLATE_IMAGE, "opencode", ".")
    print(f"OK: Expected sandbox exists: {expected_sandbox_name}")
