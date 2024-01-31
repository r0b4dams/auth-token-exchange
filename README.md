# token-exchange-server

A server to perform the OAuth token exchange FusionAuth.

## Installation

Run `make` to set up a virtual environment and install dependencies

## Usage

After installation run `make dev` to spin up the development server

| command        | description                                              |
| -------------- | -------------------------------------------------------- |
| `make`         | create virtual environment and install requirements      |
| `make dev`     | run the app in development using the Flask dev server    |
| `make preview` | run the app via the gunicorn WSGI server                 |
| `make add`     | install a pip package to the virtual environment         |
| `make save`    | update requirements.txt with current venv packages       |
| `make clean`   | remove the virtual environment and delete all .pyc files |
