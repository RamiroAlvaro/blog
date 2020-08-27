[![Build Status](https://travis-ci.org/RamiroAlvaro/blog.svg?branch=master)](https://travis-ci.org/RamiroAlvaro/blog)
[![codecov](https://codecov.io/gh/RamiroAlvaro/blog/branch/master/graph/badge.svg)](https://codecov.io/gh/RamiroAlvaro/blog)


## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.8
3. Ative o virtualenv
4. Instale as dependências.
5. Configure a instância com o .env
6. Desativar ou virtualenv
7. Ative o virtualenv
8. Execute os testes

```console
git clone https://github.com/RamiroAlvaro/blog.git blog
cd blog
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
deactivate
source .venv/bin/activate
pytest mysite --cov=mysite
```

1. Faça as migrações
2. Crie um usuário
3. Rode o servidor local

```console
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```