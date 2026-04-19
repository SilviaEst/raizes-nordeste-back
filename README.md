Projeto Raízes do Nordeste - Backend API 


Esse repositório contém o código-fonte da API desenvolvida para o Projeto Multidisciplinar do curso de Análise e Desenvolvimento de Sistemas da Uninter.



Sobre o projeto:

O sistema simula o backend de uma rede de lanchonetes nordestinas (Raízes do Nordeste), projetado para gerenciar pedidos de forma multicanal (Aplicativo, Totem e Balcão).
O foco do projeto é garantir a centralização das regras de negócio, controle de estoque por unidade e integração com simuladores de pagamento.



Arquitetura:

O projeto foi construído utilizando os princípios de Arquitetura em Camadas (Clean Architecture), separando claramente as responsabilidades:

API: Rotas e contratos de entrada/saída (Swagger).

Application: Orquestração de serviços e regras de fluxo.

Domain: Entidades centrais do negócio (Pedidos, Usuários, Produtos).

Infrastructure: Persistência de dados e integrações externas.



Tecnologias Utilizadas:

Python 3

FastAPI (Roteamento e Documentação Automática com Swagger)

Pydantic (Validação de Dados e Schemas)

SQLAlchemy + SQLite (Mapeamento Objeto-Relacional e Persistência)

PyJWT (Segurança e Autenticação)



Como configurar e rodar o projeto localmente

1. Clonar o repositório

git clone https://github.com/SilviaEst/raizes-nordeste-back
cd raizes-nordeste-back


2. Ambiente Virtual (VENV)

python -m venv venv
# Windows:
.\venv\Scripts\activate


3. Instalar dependências

pip install -r requirements.txt


4. Iniciar a API

uvicorn main:app --reload


Acesse a documentação interativa (Swagger) em: http://127.0.0.1:8000/docs

Plano de Testes e Validação (Postman)

Para cumprir as exigências do roteiro, a coleção collection_postman.json contém 10 cenários de teste organizados por recursos.


- Ordem de Execução Recomendada:

01 - Auth: Execute o T01 - Gerar Token (Credenciais: admin/admin). Copie o token gerado.

- Configuração: Nas demais pastas, insira o token na aba Authorization como Bearer Token.

- Execução dos Fluxos:

02 - Pedidos: Criação (Status 201) e Listagem de pedidos. (T02 e T05)
03 - Pagamento: Validação do fluxo de confirmação via mock. (T03)
04 - Produtos: Consulta ao cardápio completo. (T06)
05 - Estoque: Consulta de saldo por unidade física. (T07)
06 - Erros: Cenários negativos (422 - Falta de dados, 401 - Sem Token, 404 - Unidade Inválida e Pagamento Rejeitado ). (T04, T08, T09 e T10)


Licença e LGPD

Este projeto implementa o registro explícito de consentimento do usuário, armazenando a prova de aceite dos termos de privacidade diretamente no banco de dados, conforme exigido pela Lei Geral de Proteção de Dados.

