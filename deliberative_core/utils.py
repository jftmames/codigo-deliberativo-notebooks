# deliberative_core/utils.py

import os
from dotenv import load_dotenv

def load_api_key():
    """
    Carga la clave de API de OpenAI desde un archivo .env.
    Es una buena práctica centralizar la gestión de configuración.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ADVERTENCIA: La variable de entorno OPENAI_API_KEY no fue encontrada.")
        print("Asegúrate de tener un archivo .env con 'OPENAI_API_KEY=tu_clave'")
    return api_key