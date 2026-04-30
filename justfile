# run an example
run:
  uv run main.py example.log

# lint + test
check-all:
  uv run ruff format
  uv run ruff check --fix
  uv run ty check

# get the planning agent to write up an implementation plan
plan PROMPT MODEL='gptmini':
  ./scripts/plan.sh planner {{MODEL}} "{{PROMPT}}"

# get coder agent to do TASK in this dir, no branch
quick TASK MODEL='gptmini':
  ./scripts/quick.sh coder {{MODEL}} "{{TASK}}"

# get coder agent to follow instructions in PATH
task PATH MODEL='gptmini':
  ./scripts/task.sh coder {{MODEL}} {{PATH}}

# merge a task branch and remove it
approve PATH MSG:
  ./scripts/approve.sh {{PATH}} "{{MSG}}"

# reject and delete a task branch
reject PATH:
  ./scripts/reject.sh {{PATH}}
