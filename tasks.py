"""Módulo que contém as tarefas locais utilizadas com invoke."""

import invoke


@invoke.task
def makemigrations(ctx, settings='development'):
    """Gera os arquivos de migração."""
    cmd = './manage.py makemigrations --settings={{ project_name }}.settings.{}'.format(settings)
    ctx.run(cmd, echo=True, pty=True)


@invoke.task
def migrate(ctx, settings='development'):
    """Aplica as migrações."""
    cmd = './manage.py migrate --settings={{ project_name }}.settings.{}'.format(settings)
    ctx.run(cmd, echo=True, pty=True)


@invoke.task
def test(ctx, tests='', settings='test'):
    """Testa as aplicações do projeto (com exceção dos testes funcionais)."""
    cmd = 'coverage run ./manage.py test {} --settings={{ project_name }}.settings.{}'.format(tests, settings)
    ctx.run(cmd, echo=True, pty=True)
    cmd = 'coverage report'
    ctx.run(cmd, echo=True, pty=True)


@invoke.task
def functional_tests(ctx, package='functional_tests.histories', settings='test'):
    """Executa os testes funcionais."""
    collectstatic(ctx, settings, True)
    cmd = 'coverage run ./manage.py test {} . --settings={{ project_name }}.settings.{}'
    cmd = cmd.format(package, settings)
    ctx.run(cmd, echo=True, pty=True)
    cmd = 'coverage report'
    ctx.run(cmd, echo=True, pty=True)


@invoke.task(default=True)
def run_server(ctx, addr='0.0.0.0:8000', settings='development'):
    """Executa o servidor web."""
    cmd = './manage.py runserver {} --settings={{ project_name }}.settings.{}'.format(addr, settings)
    if 'prod' in settings:
        cmd = 'gunicorn {{ project_name }}.wsgi --workers=4'

    ctx.run(cmd, echo=True, pty=True)


@invoke.task
def collectstatic(ctx, settings='development', noinput=False, clear=False):
    """Coleta arquivos estáticos."""
    noinput = '--noinput' if noinput else ''
    clear = '--clear' if clear else ''
    cmd = './manage.py collectstatic {} {} --settings={{ project_name }}.settings.{}'
    cmd = cmd.format(noinput, clear, settings)
    ctx.run(cmd, echo=True, pty=True)


@invoke.task
def celery(ctx, settings='development'):
    """Executa celery."""
    cmd = 'DJANGO_SETTINGS_MODULE={{ project_name }}.settings.{} '
    cmd += 'celery -A {{ project_name }} worker -E -l info'
    cmd = cmd.format(settings)
    ctx.run(cmd, echo=True, pty=True)


@invoke.task
def send_queued_mail(ctx, settings='development'):
    """Envia emails enfileirados pela aplicação django_post_office."""
    cmd = './manage.py send_queued_mail --settings={{ project_name }}.settings.{}'.format(settings)
    ctx.run(cmd, echo=True, pty=True)
