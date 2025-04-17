from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import MeView, SignupView

urlpatterns = [
    # Endpoint de cadastro de novos usuários
    path(
        'signup/',
        SignupView.as_view(),
        name='signup'
    ),

    # Endpoint de autenticação JWT (obtenção de token)
    path(
        'login/',
        TokenObtainPairView.as_view(),
        name='login'
    ),

    # Endpoint de informações do usuário autenticado
    path(
        'me/',
        MeView.as_view(),
        name='me'
    ),
]

"""
DOCUMENTAÇÃO DA API DE AUTENTICAÇÃO

BASE PATH: /api/auth/

Endpoints disponíveis:

1. Cadastro de Usuário
   - URL: /api/auth/signup/
   - Método: POST
   - Autenticação: Não requer
   - Body (exemplo):
     {
       "email": "usuario@exemplo.com",
       "nome": "Fulano da Silva",
       "senha": "SenhaSegura123"
     }
   - Respostas:
     * 201 Created - Retorna os dados do usuário criado (sem senha)
     * 400 Bad Request - Erros de validação (email já existe, senha fraca, etc)

2. Login (Obtenção de Token JWT)
   - URL: /api/auth/login/
   - Método: POST
   - Autenticação: Não requer (é o endpoint de autenticação)
   - Body (exemplo):
     {
       "email": "usuario@exemplo.com",
       "password": "SenhaSegura123"
     }
   - Respostas:
     * 200 OK - Retorna tokens de acesso e refresh
       {
         "access": "token.jwt.acesso",
         "refresh": "token.jwt.refresh"
       }
     * 401 Unauthorized - Credenciais inválidas

3. Perfil do Usuário
   - URL: /api/auth/me/
   - Método: GET
   - Autenticação: Requer token JWT válido no header
     Authorization: Bearer <token>
   - Respostas:
     * 200 OK - Retorna dados do usuário autenticado
       {
         "id": 1,
         "email": "usuario@exemplo.com",
         "nome": "Fulano da Silva"
       }
     * 401 Unauthorized - Token inválido/expirado
"""
