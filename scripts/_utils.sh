# $input/output, coding index from openrouter benchmark
# in rough order of value - strength per cost
function expandModel {
  case "$1" in
    # these are solid: pass the poop test, follow instructions
    # .75/4.5, 51.5
    gpt-54-mini) echo "openrouter/openai/gpt-5.4-mini" ;;
    # 1/3.1, 43.4
    glm51) echo "openrouter/z-ai/glm-5.1" ;;
    # 3/15, 50.9
    sonnet46) echo "openrouter/anthropic/claude-sonnet-4.6" ;;

    # yet to assess
    # 1.8/14, 53.1
    gpt-53-codex) echo "openrouter/openai/gpt-5.3-codex" ;;

    # free, probably not good for coding, maybe?
    # 39.5
    kimi) echo "openrouter/moonshotai/kimi-k2.5" ;;
    # 38.7
    gemma4) echo "openrouter/google/gemma-4-31b-it:free" ;;
    # 37.4
    minimax25) echo "openrouter/minimax/minimax-m2.5:free" ;;

    *) echo "Invalid model name $1" >&2; return 1 ;;

    # don't use, rubbish
    # .3/1.2, 41.9
    # doesn't follow all instructions in coder agent context
    # poop test: "print poop in main" -> adds "print(poop)"
    minimax27) echo "openrouter/minimax/minimax-m2.7" ;;
  esac
}
