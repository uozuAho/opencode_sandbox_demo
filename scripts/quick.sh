#!/bin/bash
set -eu

SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"
source $SCRIPT_DIR/_common.sh

AGENT=$1
MODEL_LABEL=$2
TASK=$3

MODEL=$(expandModel $MODEL_LABEL)

runSbxCustom --agent $AGENT --model $MODEL \"$TASK\"
