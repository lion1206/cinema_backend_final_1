# Deploy notes for Render

This project has been patched to run database migrations automatically on Render.

## Changes
- Added `entrypoint.sh` (runs collectstatic + migrate before starting Gunicorn)
- Updated `render.yaml` (adds `postDeployCommand: python manage.py migrate --noinput`)
- Added this README_DEPLOY.md

## Usage
1. Ensure `DATABASE_URL` is set in Render (use Render Postgres or external DB).
2. Deploy normally; migrations will be applied automatically.
3. If the Django project module differs from `backend`, edit both `entrypoint.sh` and `render.yaml`.
