# Projeto de Web Scraping com API REST

## Nome do Aluno
**Nome:** David Matheus Seixas Conselvan

---

## Explicação do Projeto

Este projeto consiste em uma aplicação de scraping para extrair dados de fontes específicas da web e disponibilizá-los por meio de uma API RESTful, sem interface gráfica, construída a utilizando FastAPI e PostgreSQL. Possui uma arquitetura baseada em contêineres para garantir a portabilidade e a facilidade de execução, com as imagens hospedadas no Docker Hub.

A API oferece três endpoints, um para registro do usuário que devolve um token de autenticação jwt, um para login que devolve o mesmo token e um de consulta a uma api externa que devolve dados diários do mercado financeiro e que demanda que o usuário esteja autenticado.

---

## Repositórios  
- [Github](https://github.com/DavidConselvan/projeto-cloud)  
- [Docker Hub](https://hub.docker.com/repository/docker/davidconselvan/projeto-cloud/general)
---

## Como Executar a Aplicação

1. **Pré-requisitos**:
   - Docker e Docker Compose instalados

2. **Passos para execução**:
   - Baixe o arquivo **compose.yaml**:  
      - [compose.yaml](https://raw.githubusercontent.com/DavidConselvan/projeto-cloud/refs/heads/main/compose.yaml)  

   - Rodar o container:  
    Com o Docker ativo, execute o docker compose  dentro da pasta onde o arquivo compose.yaml foi baixado:

     ```bash
     docker compose up
     ```
   - Acesse o Swagger (FastAPI) para testar os endpoints da API, em:
     ```bash
     http://localhost:8000/docs#
     ```

    - Parar o container:  
    Quando terminar, pare o container usando:
      ```bash
      docker compose down
      ```
---

## Documentação dos Endpoints da API

### POST /registrar
- **Descrição**: Registra um novo usuário e retorna seu token de autenticação

- **Exemplo de Body da Requisição**:  
    - Insira os dados necessários no seguinte formato:
  ```json
  {
    "email": "joaosilva@gmail.com",
    "name": "João da Silva",
    "password": "12345678"
  }
  
- **Exemplo de Resposta**:
  ```json
  {
    "jwt": "token_autenticacao"
  }

- **Copie e guarde o token gerado!**

- **Teste Registrar**
  
  ![Teste Registrar](/documentation/docs/assets/registrar.png)




### POST /login
- **Descrição**: Verifica credenciais de usuário e retorna seu token de autenticação

- **Exemplo de Body da Requisição**:  
    - Insira seus dados no seguinte formato:
  ```json
  {
    "email": "joaosilva@gmail.com",
    "password": "12345678"
  }
  
- **Exemplo de Resposta**:
  ```json
  {
    "jwt": "token_autenticacao"
  }
  
- **Copie e guarde o token gerado!**

- **Teste Login**
  
  ![Teste Login](/documentation/docs/assets/login.png)  


> 💡 **Atenção!**
> 
> O token JWT gerado é válido por apenas 30 minutos. Após esse período será necessário logar novamente e gerar outro token.

### GET /consultar
- **Descrição**: Verifica se o usuário está autenticado e então consulta e devolve dados externos que contém as principais informações diárias de mercado 

- **Autenticação**:  Faça a autenticação clicando no cadeado no canto direito do endpoint, depois insira seu token JWT obtido anteriormente e clique em **"Authorize"**

- Uma vez autenticado, execute a requisição

- **Exemplo de Resposta**:
  ```json
  {
    "data": {
      "id": "0",
      "type": "day_watch",
      "attributes": {
        "top_gainers": [
          {
            "id": 606232,
            "slug": "ROOT",
            "name": "Root, Inc."
          },
          {
            "id": 3251,
            "slug": "ATEC",
            "name": "Alphatec Holdings, Inc."
          },
          ...
        ]
      }     
      ...
    }
    ...
  }

- **Teste Consulta**  
  - Autenticação:

    ![Teste Login](/documentation/docs/assets/autenticacao.png)  

  - Resposta:

    ![Teste Login](/documentation/docs/assets/api_externa.png)  

- **Video de execução da API**   

    [![Execução](https://img.youtube.com/vi/BZPGxcwkEGI/0.jpg)](https://www.youtube.com/watch?v=BZPGxcwkEGI)