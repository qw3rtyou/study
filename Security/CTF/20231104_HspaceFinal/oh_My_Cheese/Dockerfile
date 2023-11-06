FROM python:3


WORKDIR /prb
COPY app.py /prb
COPY templates /prb
COPY static /prb

COPY templates/* templates/
COPY static/* static/

RUN pip install flask


EXPOSE 10011

CMD python app.py
