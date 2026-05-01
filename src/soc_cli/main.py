import subprocess

import typer

from soc_cli.quick import run_quick

app = typer.Typer()


@app.command()
def quick(agent: str, model_label: str, task: str) -> None:
    result = run_quick(agent, model_label, task)
    raise typer.Exit(result.returncode)


if __name__ == "__main__":
    app()
