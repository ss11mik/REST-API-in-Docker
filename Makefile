# Makefile for Python-based microservice
# author: Ondrej Mikula
# 2023

.ONESHELL:

install:
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	python init_db.py

run:
	source .venv/bin/activate
	python init_db.py
	python microservice.py

docker_image:
	source .venv/bin/activate
	docker image build -t microservice .

run_docker:
	docker run -p 8080:8080 microservice

test:
	sh test.sh

clean:
	rm movies.db
