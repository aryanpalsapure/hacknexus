import os
from google import genai
from dotenv import load_dotenv
from pathlib import Path

# Load .env using absolute path (Windows + Streamlit safe)
BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)

# ✅ THIS IS THE KEY LINE (READ CAREFULLY)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not loaded from .env")

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME = "models/gemini-2.5-flash"

def explain_city(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text.strip()
