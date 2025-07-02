import os
from dotenv import load_dotenv

api_key = os.getenv("OPENAI_API_KEY")
# Ahora puedes usar la variable api_key para configurar el cliente de OpenAI
# client = OpenAI(api_key=api_key)
