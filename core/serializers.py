from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

# Obtém o modelo de usuário personalizado definido no projeto
User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    """
    Serializer para cadastro (signup) de novos usuários.

    Valida e cria novos usuários no sistema, incluindo:
    - Validação de senha conforme as políticas do Django
    - Criptografia segura da senha antes de armazenar

    Campos:
        email: Email único do usuário (obrigatório)
        nome: Nome completo do usuário (obrigatório)
        senha: Senha do usuário (obrigatória, validada conforme políticas)
    """
    senha = serializers.CharField(
        write_only=True,  # A senha nunca será retornada nas respostas
        validators=[validate_password]  # Valida a força da senha
    )
    nome = serializers.CharField()  # Campo nome obrigatório

    class Meta:
        model = User
        fields = ['email', 'nome', 'senha']  # Campos incluídos no serializer

    def create(self, validated_data):
        """
        Cria um novo usuário com os dados validados.

        Parâmetros:
            validated_data: Dicionário com os dados já validados 
            (email, nome, senha)

        Processo:
            1. Extrai a senha dos dados validados
            2. Cria o usuário com os demais campos
            3. Criptografa e armazena a senha corretamente
            4. Salva o usuário no banco de dados

        Retorna:
            User: A instância do usuário criado
        """
        senha = validated_data.pop('senha')  # Remove a senha do dicionário
        user = User(**validated_data)  # Cria usuário com email e nome
        user.set_password(senha)  # Criptografa a senha
        user.save()  # Salva no banco de dados
        return user


class MeSerializer(serializers.ModelSerializer):
    """
    Serializer para exibir informações do usuário logado.

    Fornece uma representação segura dos dados do usuário,
    expondo apenas informações não sensíveis.

    Campos incluídos:
        id: ID único do usuário no sistema
        email: Endereço de email do usuário
        nome: Nome completo do usuário
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'nome']  # Campos públicos do usuário
