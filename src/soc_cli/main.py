
import typer

from soc_cli.quick import run_quick

app = typer.Typer()

DEFAULT_MODEL = "gptmini"


@app.command()
def quick(task: str, agent: str = "coder", model_label: str = DEFAULT_MODEL) -> None:
    result = run_quick(task=task, agent=agent, model_label=model_label)
    raise typer.Exit(result.returncode)


@app.command()
def dummy():
    print("yo")


if __name__ == "__main__":
    app()
