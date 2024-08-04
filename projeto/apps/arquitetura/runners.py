from types import MethodType

from django.db import connections
from django.test.runner import DiscoverRunner

SCHEMAS = ['administrativo', 'arquitetura']


def prepare_database(self):
    comandos = map(lambda s: f'create schema {s}', SCHEMAS)
    self.connect()
    self.connection.cursor().execute(';'.join(comandos))


class PostgresSchemaTestRunner(DiscoverRunner):

    def setup_databases(self, **kwargs):
        for connection_name in connections:
            connection = connections[connection_name]
            connection.prepare_database = MethodType(prepare_database, connection)

        return super().setup_databases(**kwargs)
