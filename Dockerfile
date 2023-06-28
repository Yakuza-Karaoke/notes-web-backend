FROM python:3.10-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8080

