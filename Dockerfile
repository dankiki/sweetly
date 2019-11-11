FROM python:3.8.0-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /sweetly
WORKDIR /sweetly
ADD . /sweetly/
RUN pip install -r requirements.txt