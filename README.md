# REST-API-in-Docker

This project implements a Python-based microservice REST API using Flask and SQLite.

Main code is in the file `microservice.py`, the  `init_db.py` is an auxiliary script  initialize the database. Both scripts work with database in current directory.

Data are stored in database file `movies.db`.

Shell script `test.sh` contains series of commented sample commands to interact with the API using curl.

The API uses TCP port 8080 by default.

## Running outside Docker

Simply use prepared Makefile rules:
```
make install
make run
```

and then either connect to the API by web browser on port 8080 or use prepared script `test.sh`.

## Running inside Docker

Makefile rules for building the Docker image and running it:
```
make install
sudo make docker_image
sudo make run_docker
```

## Dependencies

The project is built upon Python 3.11.4, Flask and SQLite. For SQLite, Python library [pysqlite](https://github.com/coleifer/pysqlite3) is used, as version in Docker image for Python 3.11.4 does not support the `STRICT` table option, used in this project.

## Test script

The test script uses address specified in variable `host` on the first line. It fills the database with sample data and tests edge cases.
