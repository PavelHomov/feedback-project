FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update

RUN apt-get install libpq-dev -y gcc

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY . /app

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
