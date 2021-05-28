# RAILS LINE

A web service that offers data about various London Underground lines and stations.

## Installation

1. Install pipenv - `pip install pipenv`

2. Initial pipenv - `pipenv shell`

3. Install dependencies - `pipenv install` | `pipenv install -r requirements.txt`


## Running the server locally

1. Start up the server - Run `python manage.py runserver`

2. Server should be running on http://localhost:8000/ by default

## Routes

| Routes                                                           | Description                              | Auth roles                            |
| -----------------------------------------------------------------|----------------------------------------- | ------------------------------------- |
| [GET] &nbsp; /api/lines/                                  | Returns a JSON containing information about all the London Underground lines                     | none                                     
| [GET] &nbsp; /api/stations/                                  | Returns a JSON containing information about London Underground stations                             | none                                                               
