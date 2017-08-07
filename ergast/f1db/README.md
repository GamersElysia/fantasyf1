Ergast Database Image
=====================

The Ergast Developer API offers its full data set as a MySQL database dump.

http://ergast.com/mrd/db/

This script quickly sets it up in a Docker container for investigation.

Instructions
------------

1. Run `./f1db.sh` in this directory

2. Run `docker ps` to see which port MariaDB is exposed on

        $ docker ps
        IMAGE           ...    PORTS
        mariadb:10.3    ...    0.0.0.0:32771->3306/tcp

3. Connect to the database with your favourite tool (e.g. MySQL Workbench)
    * Host: `localhost`
    * Port: per `docker ps` (above would be 32771)
    * Username: `root`
    * No password