#!/usr/bin/env bash
set -e

# Run collectstatic (ignores errors if not configured)
python manage.py collectstatic --noinput || true

# Apply migrations
python manage.py migrate --noinput

# Start the app with Gunicorn
exec gunicorn backend.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3
