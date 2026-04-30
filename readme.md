# Opencode demo project

A toy coding project to demonstrate sandboxed opencode agents.

# quick start
Install:
- [uv](https://docs.astral.sh/uv/)
- [just](https://github.com/casey/just)
- [docker sandboxes](https://docs.docker.com/ai/sandboxes/)
    - I chose restrictive network - nothing allowed. Whitelist as I go.

Get some [openrouter](https://openrouter.ai/) credits + API key, then:


## first run only - create sandbox template with `just` and API key
Note, there's probably a way to automate this. See more options
discussed below in "custom sandboxes".

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
```


## subsequent runs
Now you have a sandbox template with `just` installed and OpenRouter
API key configured. Let's do some work!

```sh
# check check that your config is correct, and to create a sandbox
# for the step below:
just quick "list all your instructions" kimi

# run "the poop test": check if models can do what they're told:
# quick run in the current working branch
just quick "print poop in the main function"

# do a longer task in a git worktree
echo "print poop in the main function" > tasks/poop.md
git add . && git commit "add poop task"
just task tasks/poop.md

# once you're happy with the change, commit it, then:
just approve tasks/poop.md "added poop"

# or if you don't like it, reject and delete it
just reject tasks/poop.md

# for more, see
just -l
```


# More info

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

## custom sandboxes
I went with saving an existing sandbox as a template. Bit clunky, but only need
to do once.

Alternatives:

- custom env? https://docs.docker.com/ai/sandboxes/agents/custom-environments/
    - nah have to push to registry
- kit? https://docs.docker.com/ai/sandboxes/customize/kits/
    - nah doesn't work (too new?). I didn't spend much time on this, may work

# todo
- WIP clean up docs once you get something working
- fix scripts and justfile to use custom template
    - test
- get rid of openrouter api key env var
- centralise this proj so that you don't have to copy scripts etc to other proj
    - ie. make a bunch of aliases to run the agents etc in this project
- add just ask from dwg
- ability to run 'just quick' tasks within a worktree
    - maybe custom env will solve this
- add an automated benchmark to test new LLMs/agents/clis
