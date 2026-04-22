Projeto Raízes do Nordeste - Backend API 


Esse repositório contém o código-fonte da API desenvolvida para o Projeto Multidisciplinar do curso de Análise e Desenvolvimento de Sistemas da Uninter.



Sobre o projeto:

O sistema é o motor de backend de uma rede de lanchonetes nordestinas (Raízes do Nordeste), projetado para gerenciar pedidos de forma multicanal (Aplicativo, Totem e Balcão).
O foco deste ciclo é a autenticação segura, a persistência de pedidos com registro de consentimento LGPD e a simulação de fluxos de pagamento (Mock), garantindo a integridade das regras de negócio em cada transação.



Arquitetura:

O projeto foi construído utilizando os princípios de Arquitetura em Camadas (Clean Architecture), separando claramente as responsabilidades:

API: Rotas e contratos de entrada/saída (Swagger).

Application: Orquestração de serviços e regras de fluxo.

Domain: Entidades centrais do negócio (Pedidos, Usuários, Produtos).

Infrastructure: Persistência em banco de dados SQLite e segurança JWT.



Tecnologias Utilizadas:

Python 3.10+

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


Para cumprir as exigências do roteiro, a coleção collection_postman.json contém 10 cenários de teste organizados para validar a resiliência do sistema (6 Fluxos Positivos e 4 Negativos).


Fluxos Positivos (Sucesso)

T01 - Login com sucesso: Geração de token JWT (admin/admin).

T02 - Criar Pedido: Persistência de novo pedido no banco de dados.

T03 - Listagem de Pedidos: Recuperação de histórico de pedidos.

T04 - Consentimento LGPD: Registro explícito do aceite de termos de privacidade.

T05 - Pagamento Aprovado: Validação de transação via Mock (Status: APROVADO).

T06 - Atualização de Status: Atualização automática de status pós-pagamento.


Fluxos Negativos (Tratamento de Erros)

T07 - Acesso sem Token (401): Bloqueio de acesso sem token válido.

T08 - Campo Obrigatório Ausente (422): Erro ao enviar JSON com campos obrigatórios ausentes.

T09 - Formato de Dado Inválido (422): Erro ao enviar formatos de dados inválidos (ex: texto em campo numérico).

T10 - Pedido Inexistente (404): Busca por recurso (ID de pedido) inexistente no sistema.

Licença e LGPD

Este projeto implementa o registro explícito de consentimento do usuário, armazenando a prova de aceite dos termos de privacidade diretamente no banco de dados, conforme exigido pela Lei Geral de Proteção de Dados.

