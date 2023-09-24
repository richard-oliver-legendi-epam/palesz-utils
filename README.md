# Palesz Utils

Sample app based on https://flask.palletsprojects.com/en/2.3.x/tutorial/

## Running the app

    flask --app palesz_utils run --debug

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

    pip install palesz_utils-1.0.0-py3-none-any.whl

## Secret key update

    python -c 'import secrets; print(secrets.token_hex())'

## Run with prod server

    waitress-serve --call 'palesz_utils:create_app'

## TODO
* Linting in the tutorial???
* Dockerize
* Host somewhere
* Add unit tests, trivial only
* Add coverage reporting
* Add license
