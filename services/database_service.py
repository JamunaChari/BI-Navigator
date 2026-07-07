"""
database_service.py

Purpose:
Provides a reusable interface for interacting with the BI Navigator database.
"""

import sqlite3
from pathlib import Path


class DatabaseService:

    def __init__(self):

        self.database_path = Path("database") / "retail.db"

    def get_connection(self):

        return sqlite3.connect(self.database_path)

    def execute_script(self, script_path: str):

        connection = self.get_connection()

        with open(script_path, "r", encoding="utf-8") as file:
            sql_script = file.read()

        connection.executescript(sql_script)

        connection.commit()

        connection.close()

    def get_schema(self):

        connection = self.get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            ORDER BY name;
        """)

        tables = cursor.fetchall()

        schema = {}

        for table in tables:

            table_name = table[0]

            cursor.execute(f"PRAGMA table_info({table_name});")

            columns = cursor.fetchall()

            schema[table_name] = [
                column[1]
                for column in columns
            ]

        connection.close()

        return schema