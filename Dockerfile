FROM python:3.10-slim

ARG NAME
ARG VERSION
ARG TARBALL=${NAME}-${VERSION}.tar.gz

COPY dist/${TARBALL} .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir $TARBALL

ENTRYPOINT authexchange run -p