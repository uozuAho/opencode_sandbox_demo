# $input/output, coding index from openrouter benchmark
# in rough order of value - strength per cost
function expandModel {
  case "$1" in
    # 3/15, 50.9
    sonnet) echo "openrouter/anthropic/claude-sonnet-4.6" ;;
    # .4/1.7, 39.5
    kimi) echo "openrouter/moonshotai/kimi-k2.5" ;;
    *) echo "Invalid model name $1" >&2; return 1 ;;
  esac
}
