
import typer

from soc_cli.quick import run_quick

app = typer.Typer()

DEFAULT_MODEL = "gptmini"


@app.command()
def quick(task: str, agent: str = "coder", model_label: str = DEFAULT_MODEL) -> None:
    result = run_quick(agent, model_label, task)
    raise typer.Exit(result.returncode)


if __name__ == "__main__":
    app()
