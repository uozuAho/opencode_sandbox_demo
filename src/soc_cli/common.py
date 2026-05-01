from pathlib import Path


SBX_ROOT = Path(".sbx/opencode-opencode-demo-worktrees")


def expand_model(model: str) -> str:
    models = {
        "gptmini": "openrouter/openai/gpt-5.4-mini",
        "glm51": "openrouter/z-ai/glm-5.1",
        "gpt-53-codex": "openrouter/openai/gpt-5.3-codex",
        "sonnet46": "openrouter/anthropic/claude-sonnet-4.6",
        "kimi": "openrouter/moonshotai/kimi-k2.5",
        "gemma4": "openrouter/google/gemma-4-31b-it:free",
        "minimax25": "openrouter/minimax/minimax-m2.5:free",
    }
    try:
        return models[model]
    except KeyError as exc:
        raise ValueError(f"Invalid model name {model}") from exc
