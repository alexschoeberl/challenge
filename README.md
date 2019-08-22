# Vocabulary Catalogue Web Service

This repository contains a Python WSGI web service application.
It is intended to be run with the Gunicorn HTTP server behind a NGINX reverse proxy.
The web application requires Python 3.6+ (`f`-Strings are used).
The application connects to a PostgreSQL database on port `5432`.
The environment variables `DBUSER` and `DBPSSWD` have to be set.

## API Documentation

The application makes 3 resources available.
It expects an `application/json` content type for requests.
The response will also be of this content type.

- `/api/book`
  - `GET`: Returns an array of all books
  - `POST`: Stores a new book
- `/api/book/<id>`
  - `GET`: Returns the specified book
  -	`DELETE`: Deletes the specified book
- `/api/book/<id>/preference`
  - `GET`: Returns preferences associated with the specified book
  - `PUT`: Updates preferences associated with the specified book
- `/api/book/<id>/vocabulary`
  - `GET`: Returns an array of all words in the specified books vocabulary
  - `POST`:
    - Stores words from the submitted text in the specified books vocabulary
    - Preferences associated with the specified book will be considered
    - Returns an array of the most and least common words in the text
- `/api/book/<id>/vocabulary/<word>`
  - `GET`: Returns information on the specified word
  - `DELETE`: Deletes the specified word from the catalogue

## Assumptions

- Only one user
- No login required
- No management of different languages needed
- Every word is unique in the vocabulary and the whole catalogue
- Frequencies are calculated at text upload (since vocabularies are unique)

## TODOs

- Testing
- Management of time zones
- Uppercase/lowercase processing for words
- Add WSGI entry point
- Type hints (optional)
