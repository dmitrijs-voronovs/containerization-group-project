FROM python:3.9-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "sh", "./docker-entrypoint.sh" ]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
