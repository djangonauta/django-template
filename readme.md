Instalação
==========

As seguintes váriaveis de ambiente são requeridas (exemplos):

    SECRET_KEY='ztibsdwjar1v1pnp-6osx@r(1@!mfklak0$acg9^l^ut!7!sf1'
    DATABASE_URL='postgres://igor:123@localhost:5432/project'
    ADMINS='igor=igor.dev.py@gmail.com'
    EMAIL_URL='consolemail://:@'
    #EMAIL_URL='postoffice://:@localhost:1025'
    CACHE_URL='pymemcachecache://127.0.0.1:11211'
    DISABLE_ACCOUNT_REGISTRATION=False
    CSRF_TRUSTED_ORIGINS='https://localhost'

Essas variáveis devem ser definidas em {{ project_name }}/settings/.env


Certificado teste
=================

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
```
