"""
gemini_service.py

Purpose:
Provides a single interface for communicating with the Gemini API.
All AI interactions in BI Navigator should go through this module.
"""

from google import genai
from services.config import GOOGLE_API_KEY


class GeminiService:
    """
    Service class for interacting with the Gemini API.
    """

    def __init__(self):
        self.client = genai.Client(api_key=GOOGLE_API_KEY)

    def generate_response(self, prompt: str) -> str:
        """
        Sends a prompt to Gemini and returns the generated response.
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text