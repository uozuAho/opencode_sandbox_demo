# Opencode demo project

A toy coding project to demonstrate opencode config, agents etc.

Install
- [just](https://github.com/casey/just)
- [docker sandboxes](https://docs.docker.com/ai/sandboxes/)

then:

```sh
just -l
just run
just check-all
```

# todo
- WIP minimax fails the poop test?
  - try adding a bit more system context
- try some just tasks with minimax
  - WIP quikc
  - task - echo first to ensure it looks correct
  - approve - echo first to ensure it looks correct
- write some context docs for agents
  - https://opencode.ai/docs/rules/
- working as expected?
  - do agents read context?
  - do coding agents run chekc, write PR.md etc?
- try differnt models
- update my opencode notes
- push this repo - gihtub?
- maube: add autocomplete to just
