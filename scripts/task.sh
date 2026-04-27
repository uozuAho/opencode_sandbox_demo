#!/bin/bash
set -eu

SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"
source $SCRIPT_DIR/_common.sh

AGENT=$1
MODEL_LABEL=$2
TASK_PATH=$3
TASK_FILENAME=$(basename $TASK_PATH)
TASK_NAME=${TASK_FILENAME%.md}

MODEL=$(expandModel $MODEL_LABEL)

if ! git ls-files --error-unmatch "$TASK_PATH" &>/dev/null; then
    echo "Error: $TASK_PATH has not been committed to the current working tree"
    exit 1
fi

if ! git diff --quiet HEAD -- "$TASK_PATH"; then
    echo "Error: $TASK_PATH has uncommitted changes"
    exit 1
fi

sbx run opencode --branch $TASK_NAME -- \
  run --agent $AGENT --model $MODEL \
  "follow the instructions in $TASK_PATH"
