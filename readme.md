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
- model aliases?
  - try some free models. providers: opencode, openrouter, more?
- write some context docs for agents
- working as expected?
  - do agents read context?
  - do coding agents run chekc, write PR.md etc?
- try differnt models
- update my opencode notes
- push this repo - gihtub?
- maube: add autocomplete to just

# notes
- model, $/M input, $/M output, weighted coding score from https://benchlm.ai/coding
- opus 4.6, 5/25, 91
- sonnet 4.6, 3/15, 83
- kimi 2.5 (reasoning) .4(?)/1.7(?), 82 (87)
- minimax 2.7, .3/1.2, ?
- glm 5.1, 1/3, 83
- deepseek 3.2, .3/.4, 58
