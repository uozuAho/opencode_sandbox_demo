# Custom opencode sandbox template

This template extends Docker's `opencode` sandbox base image and preinstalls
`just`.

## 1) Build and publish the template

From the repository root:

```sh
docker build -t docker.io/<your-dockerhub-user>/opencode-just:v1 --push .
```

> `sbx` pulls templates from a registry, so the image must be pushed.

## 2) Export `OPENROUTER_API_KEY` on the host

In the same host shell where you will run `sbx`:

```sh
export OPENROUTER_API_KEY=<your-openrouter-api-key>
```

The project already reads this from environment in `.opencode/config.jsonc` via:

```json
"apiKey": "{env:OPENROUTER_API_KEY}"
```

## 3) Run opencode with the custom template

```sh
sbx run --template docker.io/<your-dockerhub-user>/opencode-just:v1 opencode
```

## 4) Verify `just` is available

```sh
sbx ls
sbx exec -it <sandbox-name> bash -lc 'just --version'
```
