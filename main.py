import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve environment variables
openai_key = os.getenv("OPENAI_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")
database_url = os.getenv("DATABASE_URL")

# Display availability without revealing values
print("OPENAI_API_KEY:", bool(openai_key))
print("GEMINI_API_KEY:", bool(gemini_key))
print("DATABASE_URL:", bool(database_url))