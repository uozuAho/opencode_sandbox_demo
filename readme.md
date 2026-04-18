# Opencode demo project

A toy coding project to demonstrate opencode config, agents etc.

Install:
- uv
- [just](https://github.com/casey/just)
- [docker sandboxes](https://docs.docker.com/ai/sandboxes/)

Get some openrouter credits, then:

```sh
# check everything's working locally:
just check-all

# install just in the sandbox:
# TODO custom env with just preinstalled: https://docs.docker.com/ai/sandboxes/agents/custom-environments/
sbx policy allow network archive.ubuntu.com
sbx ls   # find your sandbox name
sbx exec -it <sandbox name> bash
apt update
sudo apt install just
exit
sbx policy rm network --resource archive.ubuntu.com

# example task delegation to sandboxed agents:
# quick task, do work in the current branch
just quick "print poop in the main function"

# do a longer task in a git worktree
echo "print poop in the main function" > tasks/poop.md
just task tasks/poop.md

just approve tasks/poop.md "added poop"
```

# todo
- WIP try differnt models
  - working as expected?
    - do agents read context?
    - do coding agents run chekc, write PR.md etc?
      - minimax: nope
- update my opencode notes
- update this readme with basic instructions, notes
- push this repo - gihtub?
- maube: add autocomplete to just
