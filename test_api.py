import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing! Check your .env file.")

print(f"✅ OpenAI API Key Loaded: {OPENAI_API_KEY[:5]}... (Masked)")

