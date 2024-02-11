FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

## Install essentials
RUN apt update -y && apt upgrade -y && \
    apt install apache2 gcc php git php-curl php-zip php-dom php-gd php-mbstring -y

## Remove index.html
RUN rm -rf /var/www/html

## Install grav
RUN git clone https://github.com/getgrav/grav.git /var/www/html
WORKDIR /var/www/html
RUN bin/grav install && \
    bin/gpm install admin -y

## Add account
COPY deploy/users/hspace.yaml /var/www/html/user/accounts/

## for hide navigation bar
COPY deploy/templates/base.html.twig /var/www/html/user/themes/quark/templates/partials/base.html.twig

## Permission modification && Essential setup
RUN chown -R www-data:www-data /var/www/html/
RUN a2enmod rewrite
RUN sed -i '172s/None/All/' /etc/apache2/apache2.conf

## Add FLAG
COPY /deploy/flag.txt /flag.txt
COPY /deploy/readflag.c /tmp/readflag.c
RUN chmod 440 /flag.txt
RUN gcc /tmp/readflag.c -o /readflag
RUN rm /tmp/readflag.c
RUN chmod 2555 /readflag

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]