# API de Escola

Este repositório contém uma API para gerenciamento de uma escola. A API é desenvolvida usando Django e Docker. 

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Make](https://www.gnu.org/software/make/)

## Configuração Inicial

Para configurar o ambiente e iniciar a aplicação, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/JoseGuiFerreira17/api_school.git
   cd api_school

2. **Crie os arquivos de configuração necessários:**
   ```bash
   make prebuild

3. **Crie a rede Docker necessária:**

   ```bash
   make create_network

4. **Construa e inicie os containers Docker:**

   ```bash
   make build

5. **Aplique as migrações do banco de dados:**

   ```bash
   make migrate

## Comandos Makefile

Aqui estão os comandos definidos no `Makefile` e suas funções:

- **`prebuild`**: Cria os arquivos de configuração `.env` e `.db.env` a partir dos arquivos de exemplo fornecidos.

  ```bash
  cp example.env .env
  cp example.db.env .db.env

- **`create_network`**: Cria uma rede Docker personalizada para a aplicação.

  ```bash
   docker network create --gateway 10.7.0.1 --subnet 10.7.0.0/16 schoolnetwork

- **`build`**: Constrói e inicia os containers Docker definidos no `docker-compose.yml`.
  ```bash
   docker compose up --build

- **`migrate`**: Aplica as migrações do banco de dados usando o Django.
  ```bash
   docker compose exec school_django python manage.py migrate

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

#### Termos Principais:

- **Permissões:** Você pode usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e vender cópias do Software.
- **Isenção de Garantia:** O software é fornecido "como está", sem garantias de qualquer tipo. O autor não será responsável por qualquer dano que possa resultar do uso do software.

Para mais detalhes, consulte o arquivo [LICENSE](LICENSE) no repositório.