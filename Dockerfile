FROM python:alpine3.12

RUN mkdir /app

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD flask run -h 0.0.0.0

