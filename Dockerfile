FROM python:3.11.4

COPY microservice.py init_db.py requirements.txt /microservice/

WORKDIR /microservice/

RUN pip install -r requirements.txt


EXPOSE 8080

CMD python init_db.py && python microservice.py
