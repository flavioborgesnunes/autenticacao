# API de Autenticação - Django + JWT

Esta é uma API de autenticação simples construída com Django e Django Rest Framework, utilizando autenticação via JWT. A API permite o cadastro, login e recuperação dos dados do usuário autenticado.

## 🚀 Tecnologias Utilizadas

- **Django 4+**: Framework backend para desenvolvimento rápido de aplicações web.
- **Django Rest Framework (DRF)**: Ferramenta para construir APIs robustas e seguras.
- **SimpleJWT**: Para geração e verificação de tokens JWT.
- **SQLite**: Banco de dados utilizado localmente.
- **Fly.io**: Serviço de deploy da aplicação.
- **Docker**: Para containerização da aplicação.

## 💻 Como Rodar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/flavioborgesnunes/autenticacao.git
   cd autenticacao
   
2 - Crie um ambiente virtual:
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
  
3 - Instale as dependências:
    pip install -r requirements.txt

4 - Realize as migrações do banco de dados:
    python manage.py migrate

5 - Crie um superusuário (opcional, para acessar o admin do Django):
    python manage.py createsuperuser

6 - Inicie o servidor local:
    python manage.py runserver

Agora você pode acessar a API no endereço http://127.0.0.1:8000/.

🔑 Como Testar o Login

1 - Realize o cadastro de um usuário através da rota POST /api/signup/ com um corpo de requisição semelhante a:
    {
      "email": "teste@example.com",
      "nome": "Usuário Teste",
      "senha": "minhasenhaforte"
    }

2 - Faça o login na rota POST /api/login/ passando o email e senha:
    {
      "email": "teste@example.com",
      "senha": "minhasenhaforte"
    }

3 - A resposta será algo como:
    {
      "access": "seu_token_jwt",
      "refresh": "seu_token_refresh"
    }

4 - Após receber o token JWT (access), você pode usá-lo para acessar as rotas protegidas da API, como a rota GET /api/me/ para obter os dados do usuário autenticado.

🌐 Link da API Online
A API está disponível online no Fly.io em:
https://teste-tecnico.fly.dev/

🔧 Como Testar a API
    Para testar as rotas protegidas (como GET /api/me/), basta incluir o token JWT recebido no login no cabeçalho da requisição:
    Authorization: Bearer seu_token_jwt

📂 Link do Repositório GitHub
    O código-fonte do projeto pode ser acessado em:
    https://github.com/flavioborgesnunes/autenticacao.git






