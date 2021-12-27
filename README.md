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

Testando acesso a API via terminal

curl -H 'Accept: application/json; indent=4' -u admin:admin http://127.0.0.1:8000/users/

[Autorização e Autencicação] (http://localhost:8000/api-auth/login/) 

Para listar todos os Itens:

http://127.0.0.1:8000/itens/


Para consultar a lista de todos usuários do sistemas:

http://localhost:8000/users/

Para consultar um usuário em especifico por (id):

http://localhost:8000/users/2/

Especificando o formato JSON:  

http://localhost:8000/users/2/?format=json

Especificando o formato XML:

http://localhost:8000/users/2/?format=xml




[0]: http://www.django-rest-framework.org/
[1]: http://www.django-rest-framework.org/tutorial/1-serialization/
[2]: https://jpadilla.github.io/django-rest-framework-xml
[3]: http://pythonclub.com.br/django-rest-framework-serialization.html
