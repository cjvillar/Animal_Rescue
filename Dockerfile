FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /animal_rescue_app

COPY requirements.txt /animal_rescue_app/

# required system dependencies
RUN apk add --no-cache \
        gcc \
        musl-dev \
        libffi-dev \
        openssl-dev \
        sqlite-dev

# python dependencies
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]