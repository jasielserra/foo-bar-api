# foo-bar-api
Implementando uma API de dados que simula os principais métodos do HTTP

Para executar utilizando o Docker:
  - docker compose up -d 

Sem utilização do docker:

```bash
$ git clone https://github.com/jasielserra/foo-bar-api.git
$ cd foo-bar-api
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

Para consultar a lista de todos usuários do sistemas:

http://localhost:8000/users/

Para consultar um usuário em especifico por (id):

http://localhost:8000/users/2/

Especificando o formato JSON:  

http://localhost:8000/users/2/?format=json

Especificando o formato XML:

http://localhost:8000/users/2/?format=xml