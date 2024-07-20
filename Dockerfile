FROM python:slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

COPY reqs.txt .
RUN pip3 install mysql-connector-python
RUN pip install --no-cache-dir --upgrade -r reqs.txt

CMD "uvicorn main:app --reload"