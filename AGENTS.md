This project provides a convenient cli for running opencode in docker sandboxes.

The cli app uses Typer as the app framework. `uv` is used
for management of the python runtime and packages.

Project structure:
./.opencode/   : agent configuration for use in this project
./src          : all python source code
./src/sbx      : wrapper around sbx
./src/soc_cli  : cli implementation

For more info, read ./readme.md
