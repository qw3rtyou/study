FROM python:3.11.4

RUN apt-get update -y
RUN apt-get install netcat-traditional -y
RUN pip install discord

RUN adduser --shell /sbin/nologin kctf

COPY app/app.py /home/kctf/app.py
COPY flag /home/kctf/flag

RUN chown -R root:kctf /home/kctf
RUN chmod -R 750 /home/kctf
RUN chmod 444 /home/kctf/flag

WORKDIR /home/kctf

USER kctf

CMD [ "python3", "app.py" ]