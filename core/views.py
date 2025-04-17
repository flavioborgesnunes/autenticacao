from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MeSerializer, SignupSerializer

# Obtém o modelo de usuário personalizado definido no projeto
User = get_user_model()


class SignupView(generics.CreateAPIView):
    """
    View para cadastro (signup) de novos usuários.

    Herda de CreateAPIView para fornecer um endpoint de criação simples.
    Permite que novos usuários se cadastrem no sistema.

    Atributos:
        queryset: Todos os usuários existentes (para compatibilidade com DRF)
        serializer_class: Serializer responsável pela validação e criação

    Métodos HTTP permitidos:
        POST: Cria um novo usuário com email, nome e senha

    Acesso:
        Público (não requer autenticação)
    """
    queryset = User.objects.all()  # QuerySet padrão para todas as instâncias de User
    serializer_class = SignupSerializer  # Usa o SignupSerializer para validação


class MeView(APIView):
    """
    View para obter informações do usuário atualmente autenticado.

    Fornece um endpoint seguro para o usuário logado visualizar
    suas próprias informações.

    Permissões:
        Requer autenticação (apenas usuários logados podem acessar)

    Métodos HTTP permitidos:
        GET: Retorna os dados do usuário logado (id, email, nome)

    Acesso:
        Privado (requer token de autenticação válido)
    """
    permission_classes = [
        permissions.IsAuthenticated]  # Somente usuários autenticados

    def get(self, request):
        """
        Manipula requisições GET para obter dados do usuário logado.

        Parâmetros:
            request: Objeto HttpRequest com informações do usuário autenticado

        Retorna:
            Response: Objeto contendo os dados serializados do usuário
            (id, email, nome)
        """
        serializer = MeSerializer(
            request.user)  # Serializa o usuário da requisição
        return Response(serializer.data)  # Retorna os dados serializados
