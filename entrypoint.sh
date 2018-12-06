#!/bin/sh

# Before-start hooks
echo "Running database migrations"

#Execute merge scripts. Put in path to each merge script you want to run here.
python3 manage.py migrate

# continue to run default CMD (runserver)
exec "$@"