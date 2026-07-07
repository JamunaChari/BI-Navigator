"""
sql_generator_agent.py

Purpose:
Generates SQL queries from the user's intent and database schema.
"""

import re

from services.gemini_service import GeminiService


class SQLGeneratorAgent:

    def __init__(self):

        self.gemini = GeminiService()

    def generate_sql(self, intent: dict, schema: dict) -> str:

        prompt = f"""
You are an expert SQL developer.

Your task is to generate a SQLite SQL query.

Database Schema:
{schema}

User Intent:
{intent}

Rules:

1. Return ONLY SQL.
2. Do NOT include explanations.
3. Do NOT use markdown.
4. Only use tables and columns from the schema.
5. Generate valid SQLite SQL.
"""

        response = self.gemini.generate_response(prompt)

        sql = response.strip()

        # Remove markdown if Gemini returns it
        sql = re.sub(r"^```sql", "", sql, flags=re.IGNORECASE).strip()
        sql = re.sub(r"^```", "", sql).strip()
        sql = re.sub(r"```$", "", sql).strip()

        return sql