FROM python:3.7-alpine

RUN apk update \
  && apk add \
    build-base \
    sqlite-dev 

RUN mkdir /app
WORKDIR /app

ADD requirements.pip /app
RUN pip install -r requirements.pip

ENV PYTHONUNBUFFERED 1

ADD . /app
