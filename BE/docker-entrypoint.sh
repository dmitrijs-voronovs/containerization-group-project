#!/bin/bash

echo "Wait 10 sec until DB is ready"

sleep 10

echo "Flush the manage.py command it any"

while ! python manage.py flush --no-input 2>&1; do
  echo "Flusing django manage command"
  sleep 3
done

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   python manage.py migrate
   echo "Migration is in progress status"
   sleep 3
done

echo "Django docker is fully configured successfully."

exec "$@"

