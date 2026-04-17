# run an example
run:
  uv run main.py example.log

# lint + test
check-all:
  uv run ruff format
  uv run ruff check --fix
  uv run ty check
