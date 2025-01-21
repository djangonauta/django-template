Instalação
==========

As seguintes váriaveis devem ser definidas no arquivo projeto/settings/.env (exemplos):

    SECRET_KEY='ztibsdwjar1v1pnp-6osx@r(1@!mfklak0$acg9^l^ut!7!sf1'
    DATABASE_URL='postgres://postgres:admin@localhost:5432/django-template'
    ADMINS='admin=admin@domain.com'
    EMAIL_URL='consolemail://:@'
    #EMAIL_URL='postoffice://:@localhost:1025'
    CACHE_URL='redis://127.0.0.1:6379'
    BROKER_URL='amqp://igor:123@localhost:5672/projeto'
    DISABLE_ACCOUNT_REGISTRATION='False'
    ACCOUNT_EMAIL_VERIFICATION='none' # mandatory, optional
    CSRF_TRUSTED_ORIGINS='https://localhost'
    AUTH_LDAP_SERVER_URI='ldap://localhost'
    AUTH_LDAP_USER_DN_TEMPLATE='uid=%(user)s,ou=Usuarios,dc=jus,dc=br'

Essas variáveis devem ser definidas em projeto/settings/.env


Poetry
======

[Poetry](https://python-poetry.org/) é utilizado para gerenciar as dependências do projeto. As instruções de
instalação podem ser obtidas no [site oficial](https://python-poetry.org/docs/#installing-with-pipx), ou
simplesmente utilizando [pip](https://pip.pypa.io/en/stable/):

```bash
pip3 install -U poetry
poetry self add poetry-plugin-shell
```

Os seguintes comandos são utilizados para instalar as dependências do projeto.

```bash
cd django-template  # move para o diretório do projeto
poetry shell  # inicializa o ambiente virtual
```

Alterações no arquivo ``pyproject.toml``
----------------------------------------

Será necessário atualizar o arquivo ``poetry.lock`` caso o arquivo ``pyproject.toml`` tenha sido  alterado. 

```bash
poetry lock --no-update
```

Ambiente de Desenvolvimento
---------------------------

```bash
poetry install --with dev --sync  # instala as dependências do projeto incluindo as de desenvolvimento
```

Ambiente de Produção
--------------------

```bash
poetry install --without dev --sync --compile # instala as dependências do projeto excluindo as de desenvolvimento
```

Certificado teste
=================

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
```

RunServer Plus
==============

Utilizado em conjunto com whitenoise para servir arquivos estáticos.


```bash
./manage.py runserver_plus --cert-file cert.crt --settings projeto.settings.whitenoise 0.0.0.0:8000
```

RabbitMQ
========

Remover usuário guest:

```bash
sudo rabbitmqctl delete_user guest
```

Adicionar VHOST do projeto:

```bash
sudo rabbitmqctl delete_vhost /
sudo rabbitmqctl add_vhost projeto
```

Adicionar usuário:

```bash
sudo rabbitmqctl add_user usuario senha
```

Atribuir permissões:

```bash
sudo rabbitmqctl set_permissions -p projeto usuario ".*" ".*" ".*"
```

Ativar inteface web localhost:15672

```bash
sudo rabbitmq-plugins enable rabbitmq_management # ativar o plugin
sudo rabbitmqctl set_user_tags usuario administrator # adicionar permissão ao usuário
```

Prometheus
==========

``/etc/prometheus/prometheus.yml``

```yml

scrape_configs:
    ...

  - job_name: 'django_app'
    static_configs:
      - targets: ['<IP_DO_SERVIDOR>:<PORTA>']
```