Make a custom docker sandbox. Use the docker opencode sandbox base image. On top
of this:

- install [just](https://github.com/casey/just). It should be available as an
apt package.
- export OPENROUTER_API_KEY from the host environment

For information on how to do this, read https://docs.docker.com/ai/sandboxes/agents/custom-environments/#custom-templates

expected output:
- dockerfile
- instructions on how to use the custom sandbox
