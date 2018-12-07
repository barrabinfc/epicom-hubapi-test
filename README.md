Epicom teste
============

A REST API for SKU<->products mapping.

It's packaged as a docker container, while the database is single sqlite3 stored under db/

- [Quickstart](#quickstart)
    - [Start Daemon](#start-daemon)
    - [Create admin account](#create-admin-account)
    - [Demo:](#demo)
        - [Default login:](#default-login)
- [Run Tests](#run-tests)

# Quickstart
## Start Daemon
    $ docker-compose up --build

## Create admin account
    $ docker-compose exec web python3 manage.py createsuperuser
    ...

## Demo:
  - [Index](http://localhost:8000)
  - [Admin](http://localhost:8000/admin)

### Default login:

|username |password  |
|:------- |:-------  |
|epicom   |qwertyuiop|

# Run Tests

    $ docker-compose run web python3 manage.py tests


# Contributing

To contribute to code, a basic code review is used as a pre-commit hook. We use pre-commit. Lets install:

    $ pip install -g pre-commit

And code away, most format and linting errors will be detected and fixed correctly.
