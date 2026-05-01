import subprocess


def expected_sandbox_name(cwd: Path | None = None) -> str:
    current_dir = cwd or Path.cwd()
    return f"opencode-{current_dir.name}".replace("_", "-")


def ensure_sandbox_exists(expected_sandbox_name: str) -> None:
    result = _sbx("ls", check=True)
    if expected_sandbox_name not in result.stdout:
        print(f"Expected sandbox {expected_sandbox_name} not found, creating...")
        _sbx("create", "-t", CUSTOM_TEMPLATE, "opencode", ".")
    print(f"Expected sandbox exists: {expected_sandbox_name}")


def run_sbx_custom(expected_sandbox_name: str, *args: str) -> subprocess.CompletedProcess[str]:
    ensure_sandbox_exists(expected_sandbox_name)
    return _sbx("run", expected_sandbox_name, "--", "run", *args)


def run_sbx_custom_branch(
    expected_sandbox_name: str, branch: str, *args: str
) -> subprocess.CompletedProcess[str]:
    ensure_sandbox_exists(expected_sandbox_name)
    return _sbx("run", expected_sandbox_name, "--branch", branch, "--", "run", *args)


def _sbx(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["sbx", *args], check=check, text=True, capture_output=True)
