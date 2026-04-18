# Opencode demo project

A toy coding project to demonstrate sandboxed opencode agents.

# quick start
Install:
- [uv](https://docs.astral.sh/uv/)
- [just](https://github.com/casey/just)
- [docker sandboxes](https://docs.docker.com/ai/sandboxes/)

Get some openrouter credits, then:

```sh
# check everything's working locally:
just check-all

# check check that your config is correct, and to create a sandbox
# for the step below:
just quick "list all your instructions" kimi

# install just in the sandbox:
sbx policy allow network archive.ubuntu.com
sbx ls   # find your sandbox name
sbx exec -it <sandbox name> bash
apt update
sudo apt install just
exit
sbx policy rm network --resource archive.ubuntu.com
# TODO later: custom env with just preinstalled: https://docs.docker.com/ai/sandboxes/agents/custom-environments/

# run "the poop test": check if models can do what they're told:
# quick run in the current working branch
just quick "print poop in the main function"

# do a longer task in a git worktree
echo "print poop in the main function" > tasks/poop.md
git add . && git commit "add poop task"
just task tasks/poop.md

# once you're happy with the change, commit it, then:
just approve tasks/poop.md "added poop"
```

# A bit more info
## The poop test
A very basic agent test:
- prompt it to "print poop in the main function"
- success = print("poop") added somewhere to main
- follows other instructions in .opencode/agents/coder.md
## OpenCode basics
- ./AGENTS.md is fed to all agents
- ./opencode/agents contains specific agent prompts. To use
  a specific agent, run `opencode run --agent AGENT "prompt"`.
  Note that the justfile + scripts in this project make this
  a little easier.
