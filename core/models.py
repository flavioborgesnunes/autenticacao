from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Modelo personalizado de usuário que substitui o padrão do Django.

    Herda de AbstractUser para manter toda a funcionalidade de autenticação,
    mas utiliza email como identificador principal em vez de username.

    Atributos:
        email (EmailField): Campo único para autenticação (substitui username)
        nome (CharField): Nome completo do usuário

    Configurações:
        USERNAME_FIELD: Define qual campo será usado como identificador de 
        login
        REQUIRED_FIELDS: Campos obrigatórios além do USERNAME_FIELD e senha
    """
    username = None  # Remove o campo username padrão do Django
    email = models.EmailField(unique=True)  # Email único para cada usuário
    nome = models.CharField(max_length=255)  # Nome completo do usuário

    # Configurações para autenticação:
    USERNAME_FIELD = 'email'  # Usa email como identificador principal
    REQUIRED_FIELDS = ['nome']  # Campos obrigatórios para criação de usuário

    def __str__(self):
        """
        Representação em string do objeto User.

        Retorna:
            str: O email do usuário (usado para representações amigáveis)
        """
        return self.email
