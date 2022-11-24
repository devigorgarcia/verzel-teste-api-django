
# Verzel API

Uma api desenvolvida para o desafio Verzel, onde tem como objetivo fazer o cadastro, listagem, atualização e deleção de carros dispostos na vitrine e tambem o cadastro de novos usuarios

Onde apenas o usuario admin logado pode cadastrar, atualizar e deletar e o usuario normal apenas a listagem do catalogo.



## Requisitos

- Python 3.0+

## Funcionalidades

- Cadastro E Login de Usuarios Normais e Administrador
- CRUD de Veiculos
- Verificação de login (se é admin ou não)




## Stack utilizada

**Back-end:** Python, Django, Django Rest Framework, PostgreSQL


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`DB`

`DB_USER`

`DB_PASSWORD`

`DB_HOST`

`DB_PORT`

`SECRET_KEY`


## Rodando localmente

#### Abra o terminal e clone o projeto

```bash
  git clone git@github.com:devigorgarcia/verzel-teste-api-django.git
```

##### Entre no diretório do projeto

```bash
  cd verzel-teste-api-django
```

#### Instale o ambiente virtual

```bash
  python -m venv venv
```

#### Iniciando o ambiente virtual

- Powershell
```bash
  venv/Scripts/activate
```

- bash
```bash
  source venv/Scripts/activate
```

- Linux
```bash
  source venv/bin/activate
```

#### Instale as dependencias pip
```bash
  pip install -r requirements.txt
```

#### Rodando localmente
```bash
  python manage.py runserver
```




## Documentação da API

```htttp
   http://127.0.0.1:8000/api/doc/
```

#### Cadastrar Admin
Para cadastrar um usuário admin, abra o terminal e digite esse comando

```bash
    python manage.py createsuperuser
```

Entre com o seu username, email e password

## Rota Pública Usuario
### Cadastrar Usuario

```http
POST /api/users/
```

#### Corpo da Requisição

```json
{
  "username": "string",
  "password": "string",
  "email": "string"
}
```

#### Response Esperada

```response
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "username": "string",
  "email": "string"
}
```

### Logar Usuario

#### Corpo da Requisição

```json
{
  "username": "string",
  "password": "string"
}
```
Response esperado

```response
{
	"refresh": "string",
	"access": "string"

}
```

## Rota Pública Veículos

### Todos os veículos

```http
  GET /api/vehicles/
```

#### Retorna todos os veículos

```response

[
  {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "brand": "string",
    "model": "string",
    "image": "string",
    "price": 2147483647,
    "user": "76f62a58-5404-486d-9afc-07bded328704"
  }
]
```

### Um unico veículo

```http
  GET /api/vehicles/{vehicle_id}/
```
| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `vehicle_id`      | `string` |



#### Retorna um veículo

```response

{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "user": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "username": "string",
    "email": "string"
  },
  "name": "string",
  "brand": "string",
  "model": "string",
  "image": "string",
  "price": 2147483647
}
```

## Rota Privada

Todas as rotas listadas é necessario o token de admin
### Listar Usuarios

```http
  GET /api/users/
```

Exemplo de Response:
```json
[
  {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "username": "string",
    "email": "string"
  }
]
```

### Adicionar Veiculo
```http
  POST /api/vehicles/
```
#### Retorna todos os veículos
Exemplo de Request


```json
{
  "name": "string",
  "brand": "string",
  "model": "string",
  "image": "string",
  "price": 2147483647
}
```

Exemplo de Response
```response
{
  "name": "string",
  "brand": "string",
  "model": "string",
  "image": "string",
  "price": 2147483647
}
```

### Atualizar Veiculo
```http
  PATCH  /api/vehicles/{vehicle_id}/
```
| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `vehicle_id`      | `string` |


Exemplo de Request

```json
{
  "name": "string",
  "brand": "string",
  "model": "string",
  "image": "string",
  "price": 2147483647
}
```

Exemplo de Response
```response
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "user": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "username": "string",
    "email": "string"
  },
  "name": "string",
  "brand": "string",
  "model": "string",
  "image": "string",
  "price": 2147483647
}
```

### Deletar Veiculo
```http
  DELETE  /api/vehicles/{vehicle_id}/
```
| Parâmetro   | Tipo       |
| :---------- | :--------- |
| `vehicle_id`      | `string` |


Exemplo de Response
```response
- 204 No response body
```
