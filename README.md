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

Pydantic (Validação de Dados)

SQLAlchemy + SQLite (Mapeamento Objeto-Relacional e Persistência)




Como configurar e rodar o projeto localmente

1. Clonar o repositório

git clone https://github.com/SilviaEst/raizes-nordeste-back
cd raizes-nordeste-api


2. Ambiente Virtual (VENV)

python -m venv venv
# Windows:
.\venv\Scripts\activate


3. Instalar dependências

pip install -r requirements.txt


4. Iniciar a API

uvicorn main:app --reload


Acesse a documentação interativa (Swagger) em: http://127.0.0.1:8000/docs


Testes (Postman)

O arquivo collection_postman.json está na raiz do projeto. Importe-o no Postman para testar o fluxo de criação de pedidos e as validações de erro (como o status 422 para canais de venda inválidos).


Licença e LGPD

Este projeto implementa o registro explícito de consentimento do usuário, armazenando a prova de aceite dos termos de privacidade diretamente no banco de dados, conforme exigido pela Lei Geral de Proteção de Dados.
