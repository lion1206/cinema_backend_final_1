#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python create_superuser.py
gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
