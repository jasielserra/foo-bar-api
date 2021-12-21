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

