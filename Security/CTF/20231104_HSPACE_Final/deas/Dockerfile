FROM python:3.11.4

RUN apt-get update
RUN apt-get install -y socat

RUN adduser --shell /sbin/nologin kuics2

COPY . /home/kuics2

RUN chown -R root:kuics2 /home/kuics2
RUN chmod -R 750 /home/kuics2

WORKDIR /home/kuics2

ENTRYPOINT ["socat","TCP-LISTEN:1014,reuseaddr,fork,su=kuics2","EXEC:python main.py,stderr"]
