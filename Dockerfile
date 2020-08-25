FROM alpine:3.12.0

RUN apk add python3 py3-pip

ADD / /app/

WORKDIR /app

RUN pip install .

RUN python3 pyepsg_test.py

