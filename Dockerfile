FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Применяем миграции, создаем тестовых пользователей и билеты, собираем статику
CMD python manage.py migrate --noinput && \
    python manage.py createsu && \
    python manage.py collectstatic --noinput && \
    gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
