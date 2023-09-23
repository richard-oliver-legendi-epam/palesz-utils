# Palesz Utils

Sample app based on https://flask.palletsprojects.com/en/2.3.x/tutorial/

## Running the app

    flask --app flaskr run --debug

## Initializing the DB

    flask --app flaskr init-db

## Installing pkg

    pip install -e .

## Listing dependencies

    pip list

## Running tests

    pytest

or

    pytest -v

## Coverage

    coverage run -m pytest
    coverage report
    coverage html

## Build

    python -m build --wheel

## Install in a new env

    pip install flaskr-1.0.0-py3-none-any.whl
    flask --app flaskr init-db

## Secret key update

    python -c 'import secrets; print(secrets.token_hex())'

## Run with prod server

    waitress-serve --call 'flaskr:create_app'
