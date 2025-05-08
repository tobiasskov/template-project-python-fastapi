#!/bin/bash
set -e

# Set permissions for uv cache
sudo chown -R nonroot:nonroot /home/nonroot/.cache/uv

# Set permissions for pre-commit cache
sudo chown -R nonroot:nonroot /home/nonroot/.cache/pre-commit

# With ubuntu as baseimage, the remote user setting in devcontainer.json is not able to change ownership of files.
# For other images this line might not be needed, e.g. python:3.13-slim
#sudo chown -R nonroot:nonroot /workspace/

# Setup virtual environment if it doesn't exist
# .venv will always be there (as an empty folder) since it is a named volume
if [ ! -f .venv/pyvenv.cfg ]; then
    sudo chown nonroot:nonroot .venv
    uv venv
fi

# Install dependencies and setup pre-commit
uv pip install -e .[all]
uv run pre-commit install
