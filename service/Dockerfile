FROM python:3.10.6-alpine AS builder

WORKDIR /service

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /service/requirements.txt
RUN pip install -r requirements.txt

COPY . /service