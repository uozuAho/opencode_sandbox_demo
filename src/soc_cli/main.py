import typer

from soc_cli.commands.quick import quick
from soc_cli.commands.task import task

app = typer.Typer()

app.command()(quick)
app.command()(task)


if __name__ == "__main__":
    app()
