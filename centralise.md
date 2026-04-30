Currently to use this project, you have to copy its scripts and justfile to the
project you're working on. I want to be able to have this project's
functionality available to the user, no matter their working directory, without
having to copy these files. Currently my ideal is having something like a simple
command that the user can run anywhere. I'll call it 'soc' for now, shorthand
for 'sandboxed opencode'. The user could do thinks like:

```sh
soc ask "what's the meaning of life?"  # ask an LLM a question
soc quick "check my readme for inconsistencies"  # get an agent to do a quick task in the current branch
soc task tasks/task2.md  # get an agent to do a task in a worktree
soc task tasks/task2.md --model "codex"  # get an agent to do a task, specifying which LLM to use
# etc.
```

I'm thinking of using python to replace `just`, justfile and the bash scripts.

Help me plan how to do this. Is python a good choice? Is it easy to make the
`soc` executable that I can run from anywhere? What are some alternative
implementation languages to consider?

Write your output to plan.md
