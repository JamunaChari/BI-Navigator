import json

from services.gemini_service import GeminiService


class VisualizationAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def recommend_visualization(self, question, sql, columns):

        prompt = f"""
You are a Senior Business Intelligence Visualization Expert.

Business Question:
{question}

Generated SQL:
{sql}

Returned Columns:
{columns}

Recommend the best visualization.

Rules:

1. Use categorical columns for the x_axis.

2. Use numeric columns for the y_axis.

3. Prefer bar charts for comparisons.

4. Prefer line charts for trends over time.

5. Prefer pie charts only for percentage distributions.

6. Return ONLY valid JSON.

Return ONLY JSON.

{{
    "chart_type":"",
    "x_axis":"",
    "y_axis":"",
    "title":"",
    "reason":""
}}
"""

        response = self.gemini.generate_response(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return json.loads(response)