FROM python:3.6.5

ENV PYTHONUNBUFFERED 1

WORKDIR /logisticsnetwork

COPY . /logisticsnetwork/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
