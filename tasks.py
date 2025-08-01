#!/usr/bin/env python3
import invoke


@invoke.task(default=True)
def runserver(c, interactive=False, clear=True, verbosity=0, settings='development', port=8000,
              noreload=False):
    collectstatic(c, interactive, clear, verbosity, settings)
    noreload = '--noreload' if noreload else ''
    cmd = f'./manage.py runserver 0.0.0.0:{port} --settings=projeto.settings.{settings} {noreload}'
    c.run(cmd)


@invoke.task
def collectstatic(c, interactive=False, clear=True, verbosity=0, settings='production'):
    args = []
    args.append('' if interactive else '--noinput')
    args.append('--clear' if clear else '')
    args = ' '.join(args)

    cmd = (f'./manage.py collectstatic --verbosity={verbosity} --settings=projeto.settings.{settings} '
           f'{args}')
    c.run(cmd)


@invoke.task
def makemigrations(c, settings='production', merge=True):
    merge = ' --merge' if merge else ''
    cmd = f'./manage.py makemigrations --settings=projeto.settings.{settings}{merge}'
    c.run(cmd)


@invoke.task
def migrate(c, settings='production', merge=True):
    makemigrations(c, settings, merge)
    cmd = f'./manage.py migrate --settings=projeto.settings.{settings}'
    c.run(cmd)


@invoke.task
def celery(c, settings='production', log_level='INFO', events=True):
    events = "-E" if events else ""
    log_level = 'DEBUG' if settings == 'development' else log_level
    cmd = (f'DJANGO_SETTINGS_MODULE="projeto.settings.{settings}" celery -A projeto worker -l {log_level} '
           f'{events}')
    c.run(cmd)


@invoke.task
def runserverplus(c, interactive=False, clear=False, verbosity=0, settings='whitenoise', port=8000):
    collectstatic(c, interactive, clear, verbosity, settings)
    cmd = (f'./manage.py runserver_plus --cert-file cert.crt --settings=projeto.settings.{settings} '
           f'0.0.0.0:{port}')
    c.run(cmd)


@invoke.task
def tests(c, flags='-Wa', package='', settings='test', parallel=False, keepdb=False):
    args = []
    args.append('--parallel' if parallel else '')
    args.append('--keepdb' if keepdb else '')
    args = ' '.join(args)

    cmd = (f'python3 {flags} -m coverage run manage.py test {package} --settings=projeto.settings.{settings} '
           f'{args}')
    c.run(cmd)

    cmd = 'coverage report'
    c.run(cmd)


@invoke.task
def testapps(c, flags='-Wa', package='projeto.apps', settings='test', parallel=False, keepdb=False):
    tests(c, flags, package, settings, parallel, keepdb)


@invoke.task
def testfunctional(c, interactive=False, clear=False, verbosity=0, flags='-Wa',
                   package='projeto.functional_tests', settings='test', parallel=False, keepdb=False):
    collectstatic(c, interactive, clear, verbosity, settings)
    tests(c, flags, package, settings, parallel, keepdb)


@invoke.task
def gunicorn(c):
    cmd = ('gunicorn --pid /run/gunicorn/pid --access-logfile /var/log/gunicorn/acesso.log --log-file '
           '/var/log/gunicorn/app.log --capture-output --enable-stdio-inheritance --workers 4 '
           '--bind 0.0.0.0:8000 projeto.wsgi')
    c.run(cmd)


@invoke.task
def criar_schemas(c, database, container='postgresql-17', usuario='postgres'):
    cmd = (f'docker exec -it {container} psql -U postgres -d {database} -c "create schema arquitetura '
           f'authorization {usuario};"')
    c.run(cmd)
    cmd = (f'docker exec -it {container} psql -U postgres -d {database} -c "create schema administrativo '
           f'authorization {usuario};"')
    c.run(cmd)
