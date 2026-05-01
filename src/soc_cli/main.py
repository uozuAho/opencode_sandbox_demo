from typer import Typer

app = Typer()


@app.command()
def main() -> None:
    pass


if __name__ == "__main__":
    app()
