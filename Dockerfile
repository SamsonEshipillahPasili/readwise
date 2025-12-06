FROM python:3.14-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ADD . .

RUN uv sync --locked

CMD ["sh", "run.sh"]

