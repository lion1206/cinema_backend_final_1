FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Миграции, создание суперпользователя и тестовых данных, сбор статики, запуск Gunicorn
CMD python manage.py migrate --noinput && \
    python manage.py createsu && \
    python manage.py collectstatic --noinput && \
    gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
