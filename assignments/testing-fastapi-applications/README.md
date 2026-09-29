# 📘 Assignment: Testing FastAPI Applications

## 🎯 Objective

Aprenda a testar uma API FastAPI usando pytest e TestClient, verificando respostas de sucesso, validação de entrada e tratamento de erros sem depender de um servidor externo.

## 📝 Tasks

### 🛠️ Test GET Endpoints

#### Descrição

Complete os testes iniciais para verificar a listagem de tarefas e a busca de uma tarefa específica na API fornecida.

#### Requisitos

O programa concluído deve:

- Criar um teste para confirmar que `GET /tasks` retorna status `200`.
- Verificar que a resposta de `GET /tasks` é uma lista com as tarefas esperadas.
- Criar um teste para confirmar que `GET /tasks/{task_id}` retorna a tarefa correta.
- Executar os testes com pytest sem iniciar o servidor Uvicorn manualmente.

### 🛠️ Test Creation and Error Responses

#### Descrição

Adicione testes para a criação de tarefas e para os cenários em que a API recebe dados inválidos ou um ID inexistente.

#### Requisitos

O programa concluído deve:

- Testar `POST /tasks` com dados válidos e verificar o status `201`.
- Confirmar que a tarefa criada aparece na resposta com os dados enviados.
- Testar a busca de uma tarefa inexistente e verificar o status `404`.
- Testar uma requisição `POST` sem um campo obrigatório e verificar o status `422`.
- Verificar o conteúdo básico das mensagens de erro.

### 🛠️ Isolate Tests with Fixtures

#### Descrição

Melhore a organização dos testes usando fixtures do pytest e garantindo que cada teste possa ser executado de forma independente.

#### Requisitos

O programa concluído deve:

- Criar pelo menos uma fixture para compartilhar o `TestClient` entre os testes.
- Evitar que uma tarefa criada em um teste altere o resultado de outro teste.
- Manter todos os testes automatizados em `test_app.py`.
- Fazer todos os testes passarem com o comando `pytest`.
