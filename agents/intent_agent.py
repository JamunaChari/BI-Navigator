"""
intent_agent.py

Purpose:
Analyze a user's business question and extract structured intent
using the Gemini model.
"""

import json
from pathlib import Path

from services.gemini_service import GeminiService


class IntentAgent:
    """
    AI Agent responsible for understanding user intent.
    """

    def __init__(self):

        self.gemini = GeminiService()

        prompt_path = Path("prompts") / "intent_prompt.txt"

        self.system_prompt = prompt_path.read_text(encoding="utf-8")

    def analyze(self, user_question: str) -> dict:
        """
        Analyze the user's business question and return structured JSON.
        """

        full_prompt = f"""
{self.system_prompt}

User Question:

{user_question}
"""

        response = self.gemini.generate_response(full_prompt)

        try:
            return json.loads(response)

        except json.JSONDecodeError:

            return {
                "error": "Intent Agent returned invalid JSON.",
                "raw_response": response
            }