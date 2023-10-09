FROM python:3.10-slim-buster

ENV USER curlove
ENV PORT 80

RUN apt-get update -y && apt-get install -y python3-pip build-essential curl
RUN apt-get install -y mariadb-common mariadb-server mariadb-client

RUN pip install --upgrade pip
RUN adduser --disabled-password $USER

WORKDIR /app

COPY ./app /app
RUN pip install -r requirements.txt

RUN /bin/bash -c "/usr/bin/mysqld_safe &" && \
  sleep 5 && \
  mysql -uroot < /app/init.sql && \
  rm /app/init.sql

RUN chmod +x run.sh

EXPOSE $PORT

CMD ["./run.sh"]
