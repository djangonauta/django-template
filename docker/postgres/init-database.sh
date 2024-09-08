#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$PGUSER" --dbname "$PGDATABASE" <<-EOSQL
    create schema administrativo authorization $PGUSER;
    create schema arquitetura authorization $PGUSER;
EOSQL
