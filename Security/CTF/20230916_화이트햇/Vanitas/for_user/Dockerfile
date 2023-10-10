FROM ubuntu@sha256:b492494d8e0113c4ad3fe4528a4b5ff89faa5331f7d52c5c138196f69ce176a6

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y > /dev/null
RUN apt-get upgrade -y > /dev/null
RUN apt-get install iputils-ping sqlite3 libsqlite3-dev python3 perl -y > /dev/null

RUN useradd -ms /bin/bash user
ADD ./share /home/user
RUN chown -R root:user /home/user
RUN chmod -R 750 /home/user
RUN chmod -R 770 /home/user/cgi-bin

RUN chmod 444 /home/user/flag
RUN mv /home/user/flag /flag_$(md5sum /flag | awk '{print $1}')

WORKDIR /home/user
USER user
ENTRYPOINT ["/home/user/entrypoint.sh"]
