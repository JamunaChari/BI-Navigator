"""
query_service.py

Purpose:
Executes SQL queries against the BI Navigator database.
"""

import sqlite3
from pathlib import Path


class QueryService:

    def __init__(self):

        self.database_path = Path("database") / "retail.db"

    def execute_query(self, sql: str):

        connection = sqlite3.connect(self.database_path)

        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        cursor.execute(sql)

        rows = cursor.fetchall()

        columns = []

        if cursor.description:

            columns = [
                column[0]
                for column in cursor.description
            ]

        connection.close()

        return columns, rows