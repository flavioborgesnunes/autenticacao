# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["gunicorn", "auth_api.wsgi:application", "--bind", "0.0.0.0:8000"]
