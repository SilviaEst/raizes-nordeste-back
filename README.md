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
