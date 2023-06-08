Instalação
==========

As seguintes váriaveis de ambiente são requeridas (exemplos):

    SECRET_KEY='ztibsdwjar1v1pnp-6osx@r(1@!mfklak0$acg9^l^ut!7!sf1'
    DATABASE_URL='postgres://igor:123@localhost:5432/django-template'
    ADMINS='admin=admin@domain.com'
    EMAIL_URL='consolemail://:@'
    #EMAIL_URL='postoffice://:@localhost:1025'
    CACHE_URL='redis://127.0.0.1:6379'
    BROKER_URL='amqp://igor:123@localhost:5672/projeto'
    DISABLE_ACCOUNT_REGISTRATION='False'
    ACCOUNT_EMAIL_VERIFICATION='none' # mandatory, optional
    CSRF_TRUSTED_ORIGINS='https://localhost'

Essas variáveis devem ser definidas em {{ project_name }}/settings/.env


Certificado teste
=================

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
```

Shell Plus
==========

Utilizado em conjunto com whitenoise para servir arquivos estáticos.


```bash
./manage.py runserver_plus --settings projeto.settings.whitenoite
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