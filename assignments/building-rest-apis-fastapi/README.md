# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a construir uma REST API usando o framework FastAPI, praticando rotas HTTP, validação de dados com modelos Pydantic e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Implement GET Endpoints

#### Descrição

Complete os endpoints de leitura no código inicial para que clientes possam listar todos os livros e buscar um livro específico pelo seu identificador.

#### Requisitos

O programa concluído deve:

- Criar um endpoint `GET /books` que retorne todos os livros.
- Criar um endpoint `GET /books/{book_id}` que retorne um livro pelo ID.
- Retornar uma resposta `404 Not Found` quando o ID solicitado não existir.
- Definir tipos de retorno para que a documentação automática da API descreva as respostas.

### 🛠️ Implement POST, PATCH e DELETE Endpoints

#### Descrição

Adicione as operações necessárias para criar, atualizar e remover livros da coleção mantida em memória.

#### Requisitos

O programa concluído deve:

- Criar um modelo Pydantic para validar os dados de um livro.
- Criar um endpoint `POST /books` que adicione um livro e retorne `201 Created`.
- Criar um endpoint `PATCH /books/{book_id}` que atualize os campos enviados de um livro existente.
- Criar um endpoint `DELETE /books/{book_id}` que remova um livro e retorne uma confirmação apropriada.
- Retornar `404 Not Found` ao tentar atualizar ou remover um livro inexistente.

### 🛠️ Documentar e Testar a API

#### Descrição

Use a documentação interativa do FastAPI para testar o fluxo completo da API e confirme que as entradas inválidas recebem respostas claras.

#### Requisitos

O programa concluído deve:

- Iniciar a aplicação com Uvicorn sem erros.
- Disponibilizar a documentação Swagger em `/docs`.
- Validar campos obrigatórios e tipos de dados dos livros.
- Retornar `422 Unprocessable Entity` para requisições que não atendam ao modelo de entrada.
- Demonstrar, na documentação ou em um arquivo de texto, pelo menos uma requisição bem-sucedida e uma requisição com erro.
