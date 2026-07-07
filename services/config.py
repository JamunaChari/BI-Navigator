"""
config.py

Purpose:
Loads environment variables for BI Navigator.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please check your .env file."
    )