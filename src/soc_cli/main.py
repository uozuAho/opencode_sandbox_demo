import typer

from soc_cli.commands.quick import quick
from soc_cli.commands.plan import plan
from soc_cli.commands.approve import approve
from soc_cli.commands.task import task

app = typer.Typer()

app.command()(quick)
app.command()(plan)
app.command()(approve)
app.command()(task)


if __name__ == "__main__":
    app()
