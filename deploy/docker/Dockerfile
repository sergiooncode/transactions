FROM python:3.10-slim

ENV PYTHONPATH "${PYTHONPATH}:/srv:/srv/src:/srv/venv"

COPY . /srv/
COPY ./deploy/docker/entrypoint.sh /tmp/entrypoint.sh
WORKDIR /srv

RUN apt-get update && \
    apt-get install -y \
    gcc

RUN pip install --upgrade pip \
    && pip install poetry

RUN adduser -u 1000 --gecos "" --disabled-password belvo \
    && mkdir /venv \
    && chown -R belvo:belvo /venv \
    && chown -R belvo:belvo /srv

USER belvo

RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-ansi

EXPOSE 8000