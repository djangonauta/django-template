#!/usr/bin/env python3
import invoke


@invoke.task(default=True)
def run_server(c, noinput=True, clear=False, verbosity=0, settings='development', port=8000):
    collectstatic(c, noinput, clear, verbosity, settings)
    cmd = f'./manage.py runserver 0.0.0.0:{port} --settings=projeto.settings.{settings}'
    c.run(cmd, echo=True, pty=True)


@invoke.task
def test(c, flags='-Wa', package='', settings='test'):
    cmd = f'python3 {flags} -m coverage run manage.py test {package} --settings=projeto.settings.{settings}'
    c.run(cmd, echo=True, pty=True)
    cmd = 'coverage report'
    c.run(cmd, echo=True, pty=True)


@invoke.task
def functional_tests(c, package='functional_tests.histories', settings='test'):
    collectstatic(c, settings, True)
    cmd = f'coverage run ./manage.py test {package} . --settings=projeto.settings.{settings}'
    c.run(cmd, echo=True, pty=True)
    cmd = 'coverage report'
    c.run(cmd, echo=True, pty=True)


@invoke.task
def collectstatic(c, noinput=True, clear=False, verbosity=0, settings='development'):
    noinput = '--noinput' if noinput else ''
    clear = '--clear' if clear else ''
    cmd = f'./manage.py collectstatic {noinput} {clear} --verbosity={verbosity} '
    cmd += f'--settings=projeto.settings.{settings}'
    c.run(cmd, echo=True, pty=True)


@invoke.task
def make_migrations(c):
    c.run('./manage.py makemigrations')


@invoke.task
def migrate(c):
    c.run('./manage.py migrate')


@invoke.task
def update_development(c):
    collectstatic(c, clear=True)
    make_migrations(c)
    migrate(c)
