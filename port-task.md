Port the functionality in ./scripts/task.sh to python.
Functionality in _common.sh has already been ported to ./src/soc_cli/common.py and ./src/sbx

Use subprocess.run to wrap calls to `git`

Use ./src/sbx for any interactions with sbx
