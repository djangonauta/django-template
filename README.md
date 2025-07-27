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
    ACCOUNT_EMAIL_VERIFICATION='none'
    CSRF_TRUSTED_ORIGINS='https://localhost'
    AUTH_LDAP_SERVER_URI='ldap://localhost'
    AUTH_LDAP_USER_DN_TEMPLATE='uid=%(user)s,ou=Usuarios,dc=jus,dc=br'

Essas variáveis devem ser definidas em projeto/settings/.env

POSTGRES
========

Criação dos schemas no docker.

``bash
docker exec -it postgresql-17 psql -U postgres -d database -c "create schema arquitetura authorization postgres;"
docker exec -it postgresql-17 psql -U postgres -d database -c "create schema administrativo authorization postgres;"
```

LOGS
====

O diretório de logs de desenvolvimento deve ser criado na raiz do projeto.

```bash
mkdir logs
sudo mkdir -p /var/log/celery/
sudo chown igor:www-data -R /var/log/celery/
sudo mkdir -p /var/log/gunicorn/
sudo chown igor:www-data -R /var/log/gunicorn/
```

Poetry
======

[Poetry](https://python-poetry.org/) é utilizado para gerenciar as dependências do projeto. As instruções de
instalação podem ser obtidas no [site oficial](https://python-poetry.org/docs/#installing-with-pipx), ou
simplesmente utilizando [pip](https://pip.pypa.io/en/stable/):

```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry self add poetry-plugin-shell
```

Os seguintes comandos são utilizados para instalar as dependências do projeto.

```bash
cd projeto  # move para o diretório do projeto
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
sudo rabbitmqctl add_vhost orcamentos
```

Adicionar usuário:

```bash
sudo rabbitmqctl add_user igor senha
```

Atribuir permissões:

```bash
sudo rabbitmqctl set_permissions -p orcamentos igor ".*" ".*" ".*"
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

Invoke
======

O arquivo de configuração ``invoke.yaml`` pode ser colocado na raiz do projeto (ao lado de ``tasks.py``):

```yml
sudo:
  password: ""
run:
  echo: true
  pty: true
```

Paginação
=========

1. Herdar de ``ElidedListView``
2. Definir paginate_by
3. Criar e adicionar um ``DjangoFilter``
4. Incluir o template do paginador

Exemplo:

```python
from projeto.apps.arquitetura.filters import QueryParamFilterSet

class ArtigoFilter(QueryParamFilterSet):
    titulo = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Artigo
        fields = ['id', 'titulo']


class ArtigoView(ElidedListView):
    template_name = 'artigos.html'
    queryset = Artigo.objects.all()
    context_object_name = 'artigos'
    paginate_by = 3
    filter_class = ArtigoFilter


artigo_view = ArtigoView.as_view()
```

```html
// tabela ou form
// ...

{% include "_includes/paginador.html" %}
```

Guardian
========

```python
class ArtigoListView(PermissionListMixin, ElidedListView):
    template_name = 'artigos.html'
    queryset = Artigo.objects.all()
    context_object_name = 'artigos'
    permission_required = 'artigos.view_artigo'
    get_objects_for_user_extra_kwargs = dict(
        # leva em consideração apenas as permissões de objeto, não as globais (lista filtrada).
        accept_global_perms=False
    )
    paginate_by = 3
    filter_class = ArtigoFilter


artigo_view = ArtigoListView.as_view()


class ArtigoDetailView(PermissionRequiredMixin, generic.DetailView):
    template_name = 'artigo.html'
    model = Artigo
    context_object_name = 'artigo'
    permission_required = 'artigos.view_artigo'
    # ao acessar o recurso, 403 é retornado e processado por exception.
    return_403 = True
    raise_exception = True


artigo_detalhe = ArtigoDetailView.as_view()
```

DRF
---

```python
class ArtigoSerializer(ObjectPermissionsAssignmentMixin, ModelSerializer):
    class Meta:
        model = models.Artigo
        fields = '__all__'

    def get_permissions_map(self, created):
        current_user = self.context['request'].user
        # group = Group.objects.get()
        return {
            'artigos.view_artigo': [current_user], # 'artigos.view_artigo': [current_user, group],
        }


class ArtigoViewSet(ModelViewSet):
    serializer_class = ArtigoSerializer
    queryset = models.Artigo.objects.all()
    permission_classes = [CoreObjectPermissions]
    filter_backends = [ObjectPermissionsFilter]
```
