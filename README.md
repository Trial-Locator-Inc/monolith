# triallocator.org monolith

This repository contains the code for triallocator.org.

It is a Django app deployed to GCP.

## Environments

In all environments the relevant environment variables are set by
`load_dotenv()`, which reads `.env` and sets the environment variables
appropriately.

### Local Development

The following environment variables are set in a local file called `.env`. Place
this file alongside `src/manage.py`.

    DJANGO_SECRET_KEY='<long, randomly generated value>'
    DJANGO_PG_NAME='<your system username>'
    DJANGO_PG_USER='<your system username'
    DJANGO_PG_PASSWORD=''
    DJANGO_PG_HOST='localhost'
    DJANGO_PG_PORT='5432'

### Staging and Production

These require the same environment variables to be set as local development, but
the values are constructed during the deployment process by Github Actions.

## Useful Django Commands

    python manage.py runserver
    python manage.py --check deploy
    python manage.py showmigrations
    python manage.py makemigrations
    python manage.py migrate
    python manage.py test
    python manage.py tailwind start
    python manage.py tailwind build

## Running in Production

    python manage.py collectstatic
    gunicorn triallocator.wsgi
