#!/bin/bash
set -u

SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"
source $SCRIPT_DIR/_common.sh

AGENT=$1
MODEL_LABEL=$2
PROMPT=$3

MODEL=$(expandModel $MODEL_LABEL)

if [ -f "plan.md" ]; then
  printf 'Warning: plan.md already exists and will be overwritten.\n'
  printf 'Continue? [y/N] '
  read -r reply
  case "$reply" in
    y|Y|yes|YES)
      ;;
    *)
      printf 'Aborted.\n'
      exit 1
      ;;
  esac
fi

sbx run opencode -- \
  run --agent $AGENT --model $MODEL \"$PROMPT\"
