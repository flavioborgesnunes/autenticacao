# Use uma imagem oficial do Python
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Cria diretório da app
WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o código da aplicação
COPY . .

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe a porta usada pelo app
EXPOSE 8000

# Inicia o servidor
CMD ["gunicorn", "auth_api.wsgi:application", "--bind", "0.0.0.0:8000"]
