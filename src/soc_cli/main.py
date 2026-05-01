import typer

from soc_cli.commands.quick import quick

app = typer.Typer()

app.command()(quick)


@app.command()
def dummy():
    print("yo")


if __name__ == "__main__":
    app()
