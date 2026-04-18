# run an example
run:
  uv run main.py example.log

# lint + test
check-all:
  uv run ruff format
  uv run ruff check --fix
  uv run ty check

# get coder agent to do TASK in this dir, no branch
quick TASK MODEL='gpt-54-mini':
  ./scripts/sbx-quick.sh coder {{MODEL}} "{{TASK}}"

# get coder agent to follow instructions in PATH
task PATH MODEL='gpt-54-mini':
  ./scripts/sbx-do.sh coder {{MODEL}} {{PATH}}

# merge a task branch and remove it
approve PATH MSG:
  ./scripts/sbx-approve.sh {{PATH}} "{{MSG}}"
