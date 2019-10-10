#!/usr/bin/env python3
"""Fabric."""

import fabric


@fabric.task
def pull(c, project='project', branch='master'):
    """Git pull."""
    c.run(f'cd ~/{project} && git pull origin {branch}')


@fabric.task
def install(c, project='project'):
    """Pipenv install."""
    c.run(f'cd ~/{project} && pipenv install')


@fabric.task
def collecstatic(c, project='project'):
    """Collectstatic."""
    c.run(f'cd ~/{project} && pipenv run invoke collectstatic --clear')


@fabric.task
def make_migrations(c, project='project'):
    """Gera as migrações."""
    c.run(f'cd ~/{project} && pipenv run invoke make-migrations')


@fabric.task
def migrate(c, project='project'):
    """Executa as migrações."""
    c.run(f'cd ~/{project} && pipenv run invoke migrate')


@fabric.task
def deploy(c, project='project', branch='master'):
    """Deploy."""
    pull(c, project, branch)
    install(c, project)
    collecstatic(c, project)
    make_migrations(c, project)
    migrate(c, project)
