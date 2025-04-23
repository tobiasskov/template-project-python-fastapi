ARG BASE_IMAGE=python:3.13-slim

##### Development environmennt
FROM $BASE_IMAGE AS dev
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# The astral base image does not have a non-root user by default, so we create one.
ENV USERNAME=nonroot
ENV USER_UID=1000
ENV USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo git \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

#####################################################################################################
##### Build stage (virtualenv)
# Documentation:
# UV -> https://docs.astral.sh/uv/guides/integration/docker/#non-editable-installs
# Non-root user -> https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user
FROM $BASE_IMAGE AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /workspace

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable

ADD . /workspace

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable

#####################################################################################################
##### Production environment
FROM $BASE_IMAGE AS production

ENV USERNAME=nonroot
ENV USER_UID=1000
ENV USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME


COPY --from=builder --chown=nonroot:nonroot /workspace/.venv /workspace/.venv


USER $USERNAME
