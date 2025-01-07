FROM python:3.11.4-slim-buster
WORKDIR /src/app
RUN apt-get update && apt-get install -y build-essential libpq-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .