FROM python:3.10-slim-buster


RUN apt-get update && apt-get install -y \
  build-essential\
  libffi-dev\
  libssl-dev\
  libcurl4-openssl-dev\
  make\
  libc-dev\
  g++\
  gcc\
  libgl1-mesa-dev

WORKDIR /app

ENV PYCURL_SSL_LIBRARY=openssl

RUN pip install --upgrade pip poetry

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install -r requirements.txt

