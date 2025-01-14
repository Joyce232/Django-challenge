FROM python:3.8

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY ./ /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
