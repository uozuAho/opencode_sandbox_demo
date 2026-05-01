import typer

from soc_cli.commands.quick import quick
from soc_cli.commands.task import task

app = typer.Typer()

app.command()(quick)
app.command()(task)


@app.command()
def dummy():
    print("yo")


if __name__ == "__main__":
    app()
