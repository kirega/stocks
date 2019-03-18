[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.com/kirega/stocks.svg?branch=develop)](https://travis-ci.com/kirega/stocks)
[![Coverage Status](https://coveralls.io/repos/github/kirega/stocks/badge.svg?branch=ch-setup-seed-%23164593429)](https://coveralls.io/github/kirega/stocks?branch=ch-setup-seed-%23164593429)

Stocks Management
=================
This application aims at creating a simplistic CRUD application for managing stocks.
Technologies used:
- django
- djangorestframework
- djangorestauth
- markdown
- django-filters
To run this application:
    `git clone https://github.com/kirega/stocks.git`
then:
    `virtualenv env`
    `source env/bin/activate`
    `pip install -r requirements.txt`
finally:
    `python manage.py runserver`
You can access the browsable api by going to:
    `localhost:8000`
