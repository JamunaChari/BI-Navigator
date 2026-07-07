import json

from services.gemini_service import GeminiService


class SQLValidatorAgent:

    def __init__(self):

        self.gemini = GeminiService()

    def extract_json(self, response: str):

        response = response.strip()

        if response.startswith("```json"):
            response = response[len("```json"):]

        elif response.startswith("```"):
            response = response[len("```"):]

        if response.endswith("```"):
            response = response[:-3]

        return response.strip()


    def validate_sql(self, sql: str):

        prompt = f"""
You are an expert SQL validator.

Review the SQL query below.

Return ONLY valid JSON.

SQL:
{sql}

Response Format:

{{
    "valid": true,
    "reason": "short explanation"
}}
"""

        response = self.gemini.generate_response(prompt)

        print("\n========== RAW GEMINI RESPONSE ==========")
        print(response)
        print("=========================================\n")

        cleaned_response = self.extract_json(response)

        return json.loads(cleaned_response)