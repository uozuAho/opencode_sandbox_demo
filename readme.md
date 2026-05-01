# Sandboxed opencode runner

Provides a convenient way to run sandboxed opencode locally, using
[openrouter](https://openrouter.ai/). Uses
[docker sandboxes](https://docs.docker.com/ai/sandboxes/).

# quick start
Install:
- [uv](https://docs.astral.sh/uv/)
- [just](https://github.com/casey/just)
- [docker sandboxes](https://docs.docker.com/ai/sandboxes/)
    - I chose restrictive network - nothing allowed. Whitelist as I go.

Get some [openrouter](https://openrouter.ai/) credits + API key, then:


## first run only - create sandbox template with `just` and API key
Note: this requires one time manual work and annoying scripts to
ensure the expected sandbox exists. TODO: make this easier, maybe
use kits? See "custom sandboxes" below.

```sh
sbx run opencode
# - start opencode tui
# - select /connect
# - search and select openrouter
# - enter your api key
# - exit

# install just in the sandbox
sbx policy allow network archive.ubuntu.com
sbx exec -it opencode-opencode-demo sudo apt-get update
sbx exec -it opencode-opencode-demo sudo apt-get install -y just
sbx policy rm network --resource archive.ubuntu.com

# check just + api key are working - get agent to run a just task
sbx run opencode -- \
  run --model openrouter/openai/gpt-5.4-mini "run just check-all"

# save as a template
sbx template save opencode-opencode-demo opencode-openrouter-just

# remove the sandbox so that it can be recreated using the template
# (otherwise commands below fail)
sbx rm opencode-opencode-demo
```


## subsequent runs
Now you have a sandbox template with `just` installed and OpenRouter
API key configured. Let's do some work!

```sh
# ensure just is installed in the sandbox
just quick "run just check-all"

# check instructions are correct
just quick "list all your instructions"

# run "the poop test": check if models can do what they're told:
# quick run in the current working branch
just quick "print poop in the main function"

# do a longer task in a git worktree
echo "print poop in the main function" > tasks/poop.md
git add . && git commit -m "add poop task"
just task tasks/poop.md

# once you're happy with the change, commit it, then:
just approve tasks/poop.md "added poop"

# or if you don't like it, reject and delete it
just reject tasks/poop.md

# for more, see
just -l
```


# WIP New quick start
I'm transitioning this project from `just` + bash to python.

```sh
git clone <this repo>
cd <this repo>
uv tool install .
soc --help  # soc should be available everywhere
```


# More info
## OpenCode basics
- ./AGENTS.md is fed to all agents
- ./opencode/agents contains specific agent prompts. To use
  a specific agent, run `opencode run --agent AGENT "prompt"`.
  Note that the justfile + scripts in this project make this
  a little easier.

## custom sandboxes
I went with saving an existing sandbox as a template. Bit clunky, but only need
to do once.

Alternatives:

- kit? https://docs.docker.com/ai/sandboxes/customize/kits/
    - try again now that you've got latest sbx version
    - how to get API key in safely & without manual intervention?
- custom env? https://docs.docker.com/ai/sandboxes/agents/custom-environments/
    - nah have to push to registry

# todo
- WIP centralise this proj so that you don't have to copy scripts etc to other
  proj
    - WIP extract sbx module
    - add ruff, ty, add just check-all
    - add tests for common?
    - change common.SBX_ROOT to a func
    - WIP port all commands using python
    - codex plan in plan.md
    - when done, rm plan.md
- add ask & quickpath from dwg
- rename project here + on github to soc?
- ability to run 'just quick' tasks within a worktree
    - maybe custom env will solve this
- add an automated benchmark to test new LLMs/agents/clis
    - do this in another project
- maybe: better way to create & run custom sandboxes
    - get rid of initial manual steps
