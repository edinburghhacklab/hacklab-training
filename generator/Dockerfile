FROM python:3.12

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# LaTeX
RUN apt update && apt install -y perl wget
RUN wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh
ENV PATH="$PATH:/root/.TinyTeX/bin/x86_64-linux"
RUN tlmgr install enumitem lastpage ltablex colortbl fancyhdr titlesec inter fontaxes ly1 textgreek cbfonts-fd

# Python dependencies
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# Our app
ADD training_generator /app/training_generator
ADD templates /app/templates
ADD assets /app/assets
ADD pyproject.toml uv.lock /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

RUN git config --global --add safe.directory '*'

ENTRYPOINT ["/app/.venv/bin/python", "./training_generator/main.py"]
