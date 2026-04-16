run:
	uv run main.py example.log

check-all:
	uv run ruff format
	uv run ruff check --fix
	uv run ty check
