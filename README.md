Epicom teste
============

A REST API for SKU<->products mapping.
It's packaged as a docker container, while the database is under db/

# Start
    $ docker-compose up

[localhost:8000](Index)
[localhost:8000](Admin Interface)

# First run
    $ docker-compose run web python3 manage.py migrate

# Run Tests
    $ docker-compose run web python3 manage.py tests