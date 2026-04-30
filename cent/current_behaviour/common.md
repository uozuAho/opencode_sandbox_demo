- before any command is run, a common script determines the expected sandbox
  name based on the current working directory:
  ```sh
    function expectedSandboxName {
        cwd=$(pwd)
        expected_sandbox=opencode-$(basename $cwd)
        echo $expected_sandbox | tr '_' '-'
    }
    EXPECTED_SANDBOX_NAME=$(expectedSandboxName)
  ```
