"""
schema_agent.py

Purpose:
Discover and return the database schema for downstream AI agents.
"""

from services.database_service import DatabaseService


class SchemaAgent:
    """
    AI Agent responsible for understanding the database schema.
    """

    def __init__(self):

        self.database = DatabaseService()

    def discover_schema(self):

        return self.database.get_schema()