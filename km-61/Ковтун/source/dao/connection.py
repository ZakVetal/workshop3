import cx_Oracle
from .credentials import *


class OracleConnection:

    def __init__(self):
        self._connection_string = f"{username}/{password}@{host}:{port}/{database}"

    def __enter__(self):
        self._connection = cx_Oracle.connect(self._connection_string)
        self._cursor = self._connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()
        self._connection.close()

    def execute(self, query):
        return self._cursor.execute(query).fetchall()
