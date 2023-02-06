FROM python:3.9-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT [ "sh", "./docker-entrypoint.sh" ]
# ENTRYPOINT ["python", "manage.py", "migrate", "sleep 5", "exec \"$@\""]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
