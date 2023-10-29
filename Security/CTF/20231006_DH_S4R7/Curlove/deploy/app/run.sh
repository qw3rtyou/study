#!/bin/sh

export MYSQL_USER=curlove_user
export MYSQL_PASSWORD=curlove_password

/usr/bin/mysqld_safe &
sleep 5
python3 app.py
