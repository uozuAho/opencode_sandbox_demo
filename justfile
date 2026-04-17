# run an example
run:
  uv run main.py example.log

# lint + test
check-all:
  uv run ruff format
  uv run ruff check --fix
  uv run ty check

quick TASK:
  sbx run opencode -- run --agent coder "{{TASK}}"

task PATH:
  ./scripts/sbx-do.sh {{PATH}}

approve PATH MSG:
  ./scripts/sbx-approve.sh {{PATH}} "{{MSG}}"
