check-all:
    uv run ruff format
    uv run ruff check --fix
    uv run ty check

install:
    # reinstall so I don't have to keep bumping the version
    uv tool install --reinstall .
