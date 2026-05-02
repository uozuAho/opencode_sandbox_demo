# `soc`: Sandboxed opencode runner

Provides a convenient way to run sandboxed [opencode](https://opencode.ai/) locally, using
[openrouter](https://openrouter.ai/). Uses [docker sandboxes](https://docs.docker.com/ai/sandboxes/),
AKA `sbx`.

# quick start
Install:
- [uv](https://docs.astral.sh/uv/)
- [just](https://github.com/casey/just)
- [docker sandboxes](https://docs.docker.com/ai/sandboxes/)
    - I chose restrictive network - nothing allowed. Whitelist as I go.

Get some [openrouter](https://openrouter.ai/) credits + API key, then:


## first run only - install `soc` and create the sandbox template
This creates a template image used as a base for sandboxes. It installs
`just`, and sets up your openrouter API key.

Note: this requires one time manual work and annoying scripts to
ensure the expected sandbox exists. TODO: make this easier, maybe
use kits? See "custom sandboxes" below.

```sh
# install the soc tool globally from this repo - allows you to run soc everywhere
just install

sbx run opencode
# - start opencode tui
# - select /connect
# - search and select openrouter
# - enter your api key
# - exit

# install just in the sandbox. If this breaks, run sbx exec -it opencode-soc bash
# then update & install
sbx policy allow network archive.ubuntu.com
sbx exec -it opencode-soc sudo apt-get update
sbx exec -it opencode-soc sudo apt-get install -y just
sbx policy rm network --resource archive.ubuntu.com

# check just + api key are working - get agent to run a just task
sbx policy allow network "openrouter.ai,files.pythonhosted.org,pypi.org"
sbx run opencode -- run --model openrouter/openai/gpt-5.4-mini "run just check-all"

# save as a template
sbx template save opencode-soc opencode-openrouter-just

# remove the sandbox so that it can be recreated using the template
# (otherwise commands below fail)
sbx rm opencode-soc
```


## subsequent runs
Now you have a sandbox template with `just` installed and OpenRouter
API key configured. Let's do some work!

```sh
# copy agents to your project (quirk, see more about this in quirks below)
cp -r .opencode /path/to/my/project

# ensure just is installed in the sandbox
soc quick "run just check-all"

# check instructions are correct
soc quick "list all your instructions"

# do a longer task in a git worktree
echo "print poop in the main function" > tasks/poop.md
git add . && git commit -m "add poop task"
soc task tasks/poop.md

# once you're happy with the change, commit it, then:
soc approve tasks/poop.md "added poop"

# or if you don't like it, reject and delete it
soc reject tasks/poop.md

# for more, see
soc --help
```


# quirks
`soc` expects there to be an .opencode folder with agents `coder` and `planner`. If it
doesn't find them, it falls back to a default agent built into opencode. I might fix
this at some point.

`sbx` doesn't let you configure where your git worktrees go. They go into .sbx in your
project. To review work done with `soc task`, look under .sbx for the directory named
after the task file.


# More info
## OpenCode basics
- ./AGENTS.md is fed to all agents
- ./opencode/agents contains specific agent prompts. To use
  a specific agent, run `opencode run --agent AGENT "prompt"`.
  `soc` is intended to make this a bit easier.

## custom sandboxes
I went with saving an existing sandbox as a template. It's a bit clunky,
but you only need to do it once.

Alternatives:

- kit? https://docs.docker.com/ai/sandboxes/customize/kits/
    - try again now that you've got latest sbx version
    - how to get API key in safely & without manual intervention?
- custom env? https://docs.docker.com/ai/sandboxes/agents/custom-environments/
    - nah have to push to registry


# todo
- maybe: add ask & quickpath from dwg
    - probably should fix how agents work first
        - read about opencode agents, subagents. just let projects define their
          own, don't use any here?
- change approve/reject to take worktree/branch/task name
    - bonus: autocomplete task names
- speed up startup: don't check for existing sandbox if it's been checked recently
- command to print available model aliases
- rename project here + on github to soc?
- ability to run 'soc quick' tasks within a worktree
    - maybe already fixed? try
- add an automated benchmark to test new LLMs/agents/clis
    - do this in another project
- maybe: better way to create & run custom sandboxes
    - get rid of initial manual steps
- maybe: layered config
    - soc.toml
