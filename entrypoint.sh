#!/bin/sh

echo ">> Coletando arquivos estáticos"
python manage.py collectstatic --noinput

echo ">> Aplicando migrações"
python manage.py migrate --noinput

echo ">> Iniciando servidor Gunicorn"
gunicorn auth_api.wsgi:application --bind 0.0.0.0:8000
