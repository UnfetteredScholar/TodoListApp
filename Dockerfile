# app/Dockerfile

FROM python:3.9-slim AS builder

RUN apt update
RUN apt-get install -y libpq-dev gcc

WORKDIR /Todo-App

RUN mkdir -p /Todo-App
RUN mkdir -p /Todo-App/images
RUN mkdir -p /Todo-App/db_driver


COPY ./images /Todo-App/images

COPY ./db_driver /Todo-App/db_driver

COPY ./requirements.txt /Todo-App

COPY ./main.py /Todo-App


# RUN apt-get install libpq-dev gcc # this is required as psycopg2 uses pg_config

RUN pip3 install -r /Todo-App/requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
