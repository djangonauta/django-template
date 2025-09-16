#!/usr/bin/env python3
from invoke.tasks import task


@task(default=True)
def runserver(
    c, interactive=False, clear=True, verbosity=0, settings="development", port=8000, noreload=False
):
    collectstatic(c, interactive, clear, verbosity, settings)
    noreload = "--noreload" if noreload else ""
    cmd = (
        f"./manage.py runserver 0.0.0.0:{port} "
        f"--settings=projeto.settings.{settings} {noreload}"
    )
    c.run(cmd)


@task
def collectstatic(c, interactive=False, clear=True, verbosity=0, settings="production"):
    args = []
    args.append("" if interactive else "--noinput")
    args.append("--clear" if clear else "")
    args = " ".join(args)

    cmd = (
        f"./manage.py collectstatic "
        f"--verbosity={verbosity} "
        f"--settings=projeto.settings.{settings} "
        f"{args}"
    )
    c.run(cmd)


@task
def makemigrations(c, settings="production", merge=True):
    merge = " --merge" if merge else ""
    cmd = f"./manage.py makemigrations --settings=projeto.settings.{settings}{merge}"
    c.run(cmd)


@task
def migrate(c, settings="production", merge=True):
    makemigrations(c, settings, merge)
    cmd = f"./manage.py migrate --settings=projeto.settings.{settings}"
    c.run(cmd)


@task
def celery(c, settings="production", log_level="INFO", events=True):
    events = "-E" if events else ""
    log_level = "DEBUG" if settings == "development" else log_level
    cmd = (
        f'DJANGO_SETTINGS_MODULE="projeto.settings.{settings}" '
        f"celery -A projeto worker -l {log_level} {events}"
    )
    c.run(cmd)


@task
def runserverplus(c, interactive=False, clear=False, verbosity=0, settings="whitenoise", port=8000):
    collectstatic(c, interactive, clear, verbosity, settings)
    cmd = (
        f"./manage.py runserver_plus "
        f"--cert-file cert.crt "
        f"--settings=projeto.settings.{settings} 0.0.0.0:{port}"
    )
    c.run(cmd)


@task
def tests(c, flags="-Wa", package="", settings="test", parallel=False, keepdb=False):
    args = []
    args.append("--parallel" if parallel else "")
    args.append("--keepdb" if keepdb else "")
    args = " ".join(args)

    cmd = (
        f"python3 {flags} -m coverage run manage.py test {package} "
        f"--settings=projeto.settings.{settings} {args}"
    )
    c.run(cmd)

    cmd = "coverage report"
    c.run(cmd)


@task
def testapps(c, flags="-Wa", package="projeto.apps", settings="test", parallel=False, keepdb=False):
    tests(c, flags, package, settings, parallel, keepdb)


@task
def testfunctional(
    c,
    interactive=False,
    clear=False,
    verbosity=0,
    flags="-Wa",
    package="projeto.functional_tests",
    settings="test",
    parallel=False,
    keepdb=False,
):
    collectstatic(c, interactive, clear, verbosity, settings)
    tests(c, flags, package, settings, parallel, keepdb)


@task
def gunicorn(c):
    cmd = (
        "gunicorn "
        "--pid /run/gunicorn/pid "
        "--access-logfile /var/log/gunicorn/acesso.log "
        "--log-file /var/log/gunicorn/app.log "
        "--capture-output "
        "--enable-stdio-inheritance "
        "--workers 4 "
        "--bind 0.0.0.0:8000 projeto.wsgi"
    )
    c.run(cmd)


@task
def criar_schemas(c, database, container="postgresql-17", usuario="postgres"):
    cmd = (
        f"docker exec -it {container} psql -U postgres -d {database} "
        f'-c "create schema arquitetura authorization {usuario};"'
    )
    c.run(cmd)
    cmd = (
        f"docker exec -it {container} psql -U postgres -d {database} "
        f'-c "create schema administrativo authorization {usuario};"'
    )
    c.run(cmd)


@task
def shell_plus(c, print_sql=True, settings="development"):
    print_sql = " --print-sql" if print_sql else ""
    cmd = f"./manage.py shell_plus{print_sql} --settings=projeto.settings.{settings}"
    c.run(cmd)
