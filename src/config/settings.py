import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve values
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")
ADZUNA_COUNTRY = os.getenv("ADZUNA_COUNTRY", "gb")

# Verify that the required Gemini key is present
if not GEMINI_API_KEY:
    raise EnvironmentError("Missing required environment variable: GEMINI_API_KEY")
