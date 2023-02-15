FROM python:3.10-slim-buster

ENV HOME=/app
ENV APP_HOME=/app/backend


RUN mkdir -p /app && \
   groupadd -r appuser && useradd --no-log-init -r -g appuser appuser && \
    python -m pip install --upgrade pip

WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

RUN python -m pip install -r requirements.txt && pip install ipython==8.2.0
