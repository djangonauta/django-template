#!/usr/bin/env python3
"""
Script para gerenciamento remoto do ambiente de produção.
https://docs.fabfile.org/en/2.6/

As variáveis de ambiente PIPENV e PROJETO são caminhos do executável pipenv e do diretório da aplicação,
respectivamente. Esses caminhos são relacionados aos nós da aplicação (nodes). Essas variáveis podem ser
setadas em um arquivo .env no mesmo diretório onde se encontra este script (fabfile.py).

A variável de ambiente NODES refere-se ao nome dos nós da aplicação atrás do balanceador. A configuração
desses nós deve ser adicionada ao arquivo ~/.ssh/config que é lido pelo fabric. A conexão com o balanceador
(chamada de nginx) também deve ser configurada nesse arquivo.

Arquivo .env (exemplo):

PIPENV='/home/ubuntu/.pyenv/shims/pipenv'
PROJETO='/home/ubuntu/projeto'
NODES='node1,node2,node3'

Arquivo ~/.ssh/config (exemplo):

Host nginx
    HostName 54.232.253.128
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/ec2-2021.pem

Host node1
    HostName 18.228.157.91
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/ec2-2021.pem

Host node2
    HostName 18.230.108.112
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/ec2-2021.pem

Host node3
    HostName 18.230.26.199
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/ec2-2021.pem

"""
import environ
import fabric
import halo
import invoke
import patchwork.transfers

env = environ.Env()
environ.Env.read_env()

pipenv = env('PIPENV')
p_dir = env('PROJETO')


nginx = fabric.Connection('nginx')
nodes = env.list('NODES')


def desligar_nginx():
    with halo.Halo(text='Desligando nginx |', spinner='dots') as spinner:
        nginx.sudo('service nginx stop')

    spinner.succeed('Nginx desligado com sucesso.')


def religar_nginx():
    with halo.Halo(text='Religando nginx |', spinner='dots') as spinner:
        nginx.sudo('service nginx start')

    spinner.succeed('Nginx religado com sucesso')


def atualizar_assets():
    with halo.Halo(text='Reconstruindo e enviando assets |', spinner='dots') as spinner:
        invoke.run('inv collectstatic --clear')
        patchwork.transfers.rsync(nginx, 'public/', '~/public/', delete=True, strict_host_keys=False,
                                  rsync_opts='-quiet')

    spinner.succeed('Assets atualizados com sucesso.')


def desligar_nodes():
    for node in nodes:
        c = fabric.Connection(node)
        with halo.Halo(text=f'Desligando {node} |', spinner='dots') as spinner:
            c.sudo('service gunicorn stop')

        spinner.succeed(f'{node} desligado com sucesso.')


def religar_nodes():
    for node in nodes:
        c = fabric.Connection(node)
        with halo.Halo(text=f'Religando {node} |', spinner='dots') as spinner:
            c.sudo('service gunicorn start')

        spinner.succeed(f'{node} religado com sucesso.')


def git_pull():
    for node in nodes:
        c = fabric.Connection(node)
        with halo.Halo(text=f'Atualizando {node} |', spinner='dots') as spinner:
            c.run(f'cd {p_dir} && git pull origin master')

        spinner.succeed(f'{node} atualizado com sucesso.')


def atualizar_dependencias():
    for node in nodes:
        c = fabric.Connection(node)
        with halo.Halo(text=f'Atualizando dependências ({node}) |', spinner='dots') as spinner:
            c.run(f'cd {p_dir} && {pipenv} install')

        spinner.succeed(f'Dependências ({node}) atualizadas com sucesso.')


def executar_migracoes():
    for node in nodes:
        c = fabric.Connection(node)
        with halo.Halo(text=f'Executando migrações ({node}) |', spinner='dots') as spinner:
            cmd = f'cd {p_dir} && {pipenv} run ./manage.py makemigrations && {pipenv} run ./manage.py migrate'
            c.run(cmd)

        spinner.succeed(f'Migrações ({node}) executadas.')


@fabric.task
def deploy_static(c, start_nginx=True):
    desligar_nginx()
    atualizar_assets()

    if start_nginx:
        religar_nginx()


@fabric.task
def update_project(c, start_nginx=False):
    desligar_nodes()
    git_pull()
    atualizar_dependencias()
    executar_migracoes()
    religar_nodes()

    if start_nginx:
        religar_nginx()


@fabric.task
def deploy_production(c):
    deploy_static(c, start_nginx=False)
    update_project(c, start_nginx=True)
