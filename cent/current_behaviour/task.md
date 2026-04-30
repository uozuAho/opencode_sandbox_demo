Currently, running `just task PATH MODEL='gptmini'` does:

- expands MODEL into the full name, defined by ./cent/current_behaviour/model_mapping.sh

- ensures the specified PATH is committed to git and has no uncommitted changes:
```sh
if ! git ls-files --error-unmatch "$TASK_PATH" &>/dev/null; then
    echo "Error: $TASK_PATH has not been committed to the current working tree"
    exit 1
fi

if ! git diff --quiet HEAD -- "$TASK_PATH"; then
    echo "Error: $TASK_PATH has uncommitted changes"
    exit 1
fi
```

- ensures the expected sandbox exists, creating it if needed:
```sh
if ! sbx ls | grep -q "$EXPECTED_SANDBOX_NAME"; then
    echo "Expected sandbox $EXPECTED_SANDBOX_NAME not found, creating..."
    sbx create -t $CUSTOM_TEMPLATE opencode .
fi
echo "Expected sandbox exists: $EXPECTED_SANDBOX_NAME"
```

- determines the name of the task from the given PATH:

TASK_PATH=PATH
TASK_FILENAME=$(basename $TASK_PATH)
TASK_NAME=${TASK_FILENAME%.md}

- runs `sbx run "$EXPECTED_SANDBOX_NAME" --branch "$TASK_NAME" -- run --agent coder --model $MODEL "follow the instructions in $TASK_PATH"`
