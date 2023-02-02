FROM python:3.9
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# FROM ubuntu:16.04

# RUN apt-get update
# RUN apt-get -y install python-pip
# RUN apt-get update
# RUN pip install --upgrade pip
# RUN pip install psycopg2-binary

# COPY base.py base.py

# CMD ["python", "base.py"]