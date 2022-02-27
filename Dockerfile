FROM python:3.10

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY . /app

RUN python manage.py migrate
