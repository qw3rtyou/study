FROM python:3.11.4

RUN apt-get update
RUN apt-get install -y socat

RUN adduser --shell /sbin/nologin jail

COPY . /home/jail

RUN chown -R root:jail /home/jail
RUN chmod -R 750 /home/jail
RUN chmod 444 /home/jail/flag.txt

WORKDIR /home/jail

ENTRYPOINT ["socat","TCP-LISTEN:8000,reuseaddr,fork,su=jail","EXEC:python jail.py,stderr"]
