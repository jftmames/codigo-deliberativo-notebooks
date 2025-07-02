import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno (la API key)
load_dotenv()

# Inicializar el cliente de OpenAI
# Se leerá la variable de entorno OPENAI_API_KEY automáticamente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_subquestions(
    main_question: str,
    concepts: list[str],
    domain: str = "general",
    user_profile: str = "consultor"
) -> list[str]:
    """
    Genera subpreguntas exploratorias a partir de una pregunta principal y conceptos clave,
    utilizando un modelo de lenguaje grande (LLM).

    Args:
        main_question: La pregunta central del proceso deliberativo.
        concepts: Una lista de conceptos extraídos del contexto para guiar la generación.
        domain: El dominio temático (e.g., "econ", "legal") para contextualizar.
        user_profile: El perfil del usuario para ajustar el estilo de las preguntas.

    Returns:
        Una lista de subpreguntas generadas por el LLM.
    """
    prompt_template = f"""
    Eres un asistente experto en deliberación y análisis crítico en el dominio de '{domain}'.
    Tu tarea es descomponer una pregunta principal en subpreguntas más pequeñas y manejables
    para un perfil de '{user_profile}'.

    Pregunta Principal: "{main_question}"

    Conceptos Clave a Considerar: {', '.join(concepts)}

    Basado en la pregunta y los conceptos, genera 5 subpreguntas que ayuden a explorar el problema
    desde diferentes ángulos (causas, consecuencias, soluciones, implicaciones).
    Devuelve las preguntas como una lista de Python, usando comillas dobles para cada string.
    Formato exacto de salida: ["Pregunta 1", "Pregunta 2", "Pregunta 3", "Pregunta 4", "Pregunta 5"]
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un asistente experto en análisis crítico."},
                {"role": "user", "content": prompt_template}
            ],
            temperature=0.7,
            max_tokens=250
        )

        raw_response = response.choices[0].message.content

        # Intenta parsear la respuesta del modelo de forma segura
        subquestions = eval(raw_response.strip())

        if isinstance(subquestions, list):
            return subquestions
        else:
            print(f"ADVERTENCIA: La respuesta del LLM no fue una lista: {raw_response}")
            return []

    except Exception as e:
        print(f"Error al conectar con el API de OpenAI o al procesar la respuesta: {e}")
        return []