#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    create schema administrativo authorization $POSTGRES_USER;
    create schema arquitetura authorization $POSTGRES_USER;
EOSQL
