#!/bin/bash
set -eu

SBX_ROOT=.sbx/opencode-opencode-demo-worktrees
TASK_PATH=$1
COMMIT_MSG=$2
TASK_FILENAME=$(basename $TASK_PATH)
TASK_NAME=${TASK_FILENAME%.md}
WORKTREE_PATH=$SBX_ROOT/$TASK_NAME

# git merge --no-ff $TASK_NAME -m "$COMMIT_MSG"
git worktree remove $WORKTREE_PATH
git branch -d $TASK_NAME
rm -rf $WORKTREE_PATH
rm $TASK_PATH
