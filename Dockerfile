FROM python:3.10-slim

ARG TARBALL

COPY dist/${TARBALL} .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir $TARBALL

ENTRYPOINT HOST="0.0.0.0" authexchange run --prod