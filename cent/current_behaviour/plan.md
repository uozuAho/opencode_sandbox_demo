Currently, running `just plan PROMPT MODEL='gptmini'` does:

- expands MODEL into the full name, defined by ./cent/current_behaviour/model_mapping.sh

- prompts the user if ./plan.md already exists. Asks user if they are
    ok with plan.md being overwritten.

- ensures the expected sandbox exists, creating it if needed:
```sh
if ! sbx ls | grep -q "$EXPECTED_SANDBOX_NAME"; then
    echo "Expected sandbox $EXPECTED_SANDBOX_NAME not found, creating..."
    sbx create -t $CUSTOM_TEMPLATE opencode .
fi
echo "Expected sandbox exists: $EXPECTED_SANDBOX_NAME"
```

- runs `sbx run "$EXPECTED_SANDBOX_NAME" -- run --agent planner --model $MODEL \"$PROMPT\"`
