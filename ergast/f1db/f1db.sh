#!/bin/sh
set -eu

if [ -z "f1db.sql.gz" ]; then
    curl -LO http://ergast.com/downloads/f1db.sql.gz
fi

docker run -d \
    -p 3306 \
    -e "MYSQL_ALLOW_EMPTY_PASSWORD=1" \
    -e "MYSQL_DATABASE=f1db" \
    -v "$(pwd)/f1db.sql.gz:/docker-entrypoint-initdb.d/f1db.sql.gz" \
    mariadb:10.3
