#!/usr/bin/env python3
import invoke


@invoke.task(default=True)
def runserver(c, interactive=False, clear=True, verbosity=0, settings='development', port=8000):
    collectstatic(c, interactive, clear, verbosity, settings)
    cmd = f'./manage.py runserver 0.0.0.0:{port} --settings=projeto.settings.{settings}'
    c.run(cmd, echo=True, pty=True)


@invoke.task
def collectstatic(c, interactive=False, clear=True, verbosity=0, settings='development'):
    args = []
    args.append('' if interactive else '--noinput')
    args.append('--clear' if clear else '')
    args = ' '.join(args)

    cmd = (f'./manage.py collectstatic --verbosity={verbosity} --settings=projeto.settings.{settings} '
           f'{args}')
    c.run(cmd, echo=True, pty=True)


@invoke.task
def migrate(c, settings='development'):
    cmd = f'./manage.py makemigrations --settings=projeto.settings.{settings}'
    c.run(cmd, echo=True, pty=True)

    cmd = f'./manage.py migrate --settings=projeto.settings.{settings}'
    c.run(cmd, echo=True, pty=True)


@invoke.task
def celery(c, settings='development', log_level='INFO', events=True):
    events = "-E" if events else ""
    cmd = (f'DJANGO_SETTINGS_MODULE="projeto.settings.{settings}" celery -A projeto worker -l {log_level} '
           f'{events}')
    c.run(cmd, echo=True, pty=True)


@invoke.task
def docker(c):
    cmd = 'docker compose -f docker-compose-dev.yml up --build'
    c.run(cmd, echo=True, pty=True)


@invoke.task
def runserverplus(c, interactive=False, clear=False, verbosity=0, settings='whitenoise', port=8000):
    collectstatic(c, interactive, clear, verbosity, settings)
    cmd = (f'./manage.py runserver_plus --cert-file cert.crt --settings=projeto.settings.{settings} '
           f'0.0.0.0:{port}')
    c.run(cmd, echo=True, pty=True)


@invoke.task
def tests(c, flags='-Wa', package='', settings='test', parallel=False, keepdb=False):
    args = []
    args.append('--parallel' if parallel else '')
    args.append('--keepdb' if keepdb else '')
    args = ' '.join(args)

    cmd = (f'python {flags} -m coverage run manage.py test {package} --settings=projeto.settings.{settings} '
           f'{args}')
    c.run(cmd, echo=True, pty=True)

    cmd = 'coverage report'
    c.run(cmd, echo=True, pty=True)


@invoke.task
def testapps(c, flags='-Wa', package='projeto.apps', settings='test', parallel=False, keepdb=False):
    tests(c, flags, package, settings, parallel, keepdb)


@invoke.task
def testfunctional(c, interactive=False, clear=False, verbosity=0, flags='-Wa',
                   package='projeto.functional_tests', settings='test', parallel=False, keepdb=False):
    collectstatic(c, interactive, clear, verbosity, settings)
    tests(c, flags, package, settings, parallel, keepdb)
