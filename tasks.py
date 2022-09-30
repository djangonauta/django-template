#!/usr/bin/env python3
import invoke


@invoke.task(default=True)
def run_server(c, noinput=True, clear=False, verbosity=0, settings='development', port=8000):
    collectstatic(c, noinput, clear, verbosity, settings)
    cmd = f'./manage.py runserver 0.0.0.0:{port} --settings=projeto.settings.{settings}'
    c.run(cmd, echo=True, pty=True)


@invoke.task
def test(c, flags='-Wa', package='', settings='test', parallel=False, keepdb=False):
    args = []
    args.append('--parallel' if parallel else '')
    args.append('--keepdb' if keepdb else '')
    args = ' '.join(args)

    cmd = f'python3 {flags} -m coverage run manage.py test {package} --settings=projeto.settings.{settings} '
    cmd += f'{args}'
    c.run(cmd, echo=True, pty=True)

    cmd = 'coverage report'
    c.run(cmd, echo=True, pty=True)


@invoke.task
def test_apps(c, flags='-Wa', package='projeto.apps', settings='test', parallel=False, keepdb=False):
    test(c, flags, package, settings, parallel, keepdb)


@invoke.task
def test_functional(c, noinput=True, clear=False, verbosity=0, flags='-Wa',
                    package='projeto.functional_tests', settings='test', parallel=False, keepdb=False):
    collectstatic(c, noinput, clear, verbosity, settings)
    test(c, flags, package, settings, parallel, keepdb)


@invoke.task
def collectstatic(c, noinput=True, clear=False, verbosity=0, settings='development'):
    args = []
    args.append('--noinput' if noinput else '')
    args.append('--clear' if clear else '')
    args = ' '.join(args)

    cmd = f'./manage.py collectstatic --verbosity={verbosity} --settings=projeto.settings.{settings} '
    cmd += f'{args}'
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
