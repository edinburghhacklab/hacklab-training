FROM python:3.12

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y texlive-latex-base texlive-latex-extra texlive-fonts-extra

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

ADD training_generator /app/training_generator
ADD templates /app/templates
ADD assets /app/assets
ADD pyproject.toml uv.lock /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

RUN git config --global --add safe.directory '*'

ENTRYPOINT ["/app/.venv/bin/python", "./training_generator/main.py"]
