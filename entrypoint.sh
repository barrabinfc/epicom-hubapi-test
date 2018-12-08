#!/bin/sh

# Before-start hooks
echo "Running database migrations"

#Execute merge scripts. Put in path to each merge script you want to run here.
python manage.py migrate

# continue to run default CMD (runserver)
echo "Running Django HTTP Server"
exec "$@"