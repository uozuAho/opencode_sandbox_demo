from typer import Typer

app = Typer()


@app.command()
def main() -> None:
    print("hello from soc")


if __name__ == "__main__":
    app()
