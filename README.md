# [TALANTA](https://github.com/koyoo-maxwel/TALANTA.git)

## Authors

[Jeff musa](https://github.com/jeffmusa)

[vonmutinda](https://github.com/vonmutinda)
[koyoo maxwel](https://github.com/koyoo-maxwel)
[Brian juma](https://github.com/alampulo)
[Dancan Arani](https://github.com/DuncanArani)

## Description

Talata is an online platform that gives people  an opportunity to showcase their
talents and meet mentors online to facilitate their ability.
It not only gives mentorship programmes but also help the users reach out to the their financial needs by linking them with different people who are willing and able to offer such support to them.

### 19th/09/2018

## Specifications

Get the specs [here](https://github.com/koyoo-maxwel/TALANTA/blob/master/specs.md)

## Set-up and Installation

### Prerequiites

    - Python 3.`your version`
    - Ubuntu software

`Clone the Repo`

> Run the following command on the terminal:
`git clone https://github.com/vonmutinda/TALANTA.git`

Install [Postgres](https://www.postgresql.org/download/)



### Create a Virtual Environment

Run the following commands in the same terminal:
'''bash

sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
'''

### Install dependancies

Install dependancies that will create an environment for the app to run
`pip install -r requirements`

### Prepare environment variables

```bash
export DATABASE_URL='postgresql+psycopg2://<your-username>:<your-password>@localhost/talanta'
export SECRET_KEY='Your secret key'
export DATABASE_URL_TEST='postgresql+psycopg2://<your-username>:<your-password>@localhost/talanta_test'
export MAIL_SERVER='smtp.googlemail.com'
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-email>
export MAIL_PASSWORD=<your-password>
```

``

### Run Database Migrations

```bash
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development

In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs

Sending batch emails bug
If others are found, E-mail us at[support@talanta.co.ke](talanta)

## Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details

Contact talanta for any burgs to help us improve[support@talanta.co.ke](talanta) and make the app more interactive

### License

Copyright (c) [license](license)
