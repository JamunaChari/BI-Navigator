import json

from services.gemini_service import GeminiService


class InsightAgent:

    def __init__(self):

        self.gemini = GeminiService()

    def generate_insights(self, question, sql, results):

        prompt = f"""
            You are a Senior Business Intelligence Analyst.

            A user asked the following business question:

            {question}

            The following SQL was executed:

            {sql}

            The query returned the following results:

            {results}

            Analyze these results and respond ONLY in valid JSON.

            Use the following format:

            {{
                "summary": "...",
                "key_findings": [
                    "...",
                    "...",
                    "..."
                ],
                "recommendations": [
                    "...",
                    "..."
                ]
            }}

            Do not include markdown.

            Do not include explanations.

            Return only JSON.
            """

        try:
            response = self.gemini.generate_response(prompt)

            return json.loads(response)

        except Exception as e:

            print(f"Insight Agent Error: {e}")

            return {
                "summary": "Business insights are temporarily unavailable.",
                "key_findings": [
                    "The AI service could not generate insights."
                ],
                "recommendations": [
                    "Retry in a few moments."
                ]
            }
                