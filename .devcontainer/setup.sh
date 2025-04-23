#!/bin/bash
set -e

# Set permissions for uv cache
sudo chown -R nonroot:nonroot /home/nonroot/.cache/uv

# Set permissions for pre-commit cache
sudo chown -R nonroot:nonroot /home/nonroot/.cache/pre-commit

# Setup virtual environment if it doesn't exist
if [ ! -f .venv/pyvenv.cfg ]; then
    sudo chown nonroot:nonroot .venv
    uv venv
fi

# Install dependencies and setup pre-commit
uv pip install -e .[all]
uv run pre-commit install
