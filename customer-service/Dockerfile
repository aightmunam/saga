FROM python:3.11.1-slim

WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt

# install dependencies
RUN pip3 install --no-cache -r /app/requirements.txt

# copy project
COPY . /app/