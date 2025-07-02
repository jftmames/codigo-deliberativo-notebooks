import os
import json # Importamos la librería JSON
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar el cliente de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_subquestions(
    main_question: str,
    concepts: list[str],
    domain: str = "general",
    user_profile: str = "consultor"
) -> list[str]:
    """
    Genera subpreguntas utilizando un LLM y espera una respuesta en formato JSON.
    """
    # 🧠 Prompt mejorado: Pedimos explícitamente un objeto JSON.
    prompt_template = f"""
    Eres un asistente experto en análisis crítico en el dominio '{domain}'.
    Tu tarea es descomponer una pregunta principal en 5 subpreguntas clave para un perfil de '{user_profile}'.

    Pregunta Principal: "{main_question}"
    Conceptos Clave: {', '.join(concepts)}

    Devuelve únicamente un objeto JSON que contenga una única clave "subpreguntas",
    cuyo valor sea un array de 5 strings.
    Ejemplo de formato de salida:
    {{"subpreguntas": ["¿Cuál es el impacto a corto plazo?", "¿Qué riesgos existen?", ...]}}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            # ✨ Forzamos a que la respuesta sea JSON
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "Eres un asistente experto que siempre responde con JSON válido."},
                {"role": "user", "content": prompt_template}
            ],
            temperature=0.7,
            max_tokens=500
        )

        raw_response = response.choices[0].message.content

        # 🔒 Usamos json.loads() en lugar de eval(). Es más seguro y robusto.
        data = json.loads(raw_response)

        subquestions = data.get("subpreguntas", []) # Usamos .get() para evitar errores si la clave no existe

        if isinstance(subquestions, list):
            return subquestions
        else:
            print(f"ADVERTENCIA: La clave 'subpreguntas' no contenía una lista: {subquestions}")
            return []

    except json.JSONDecodeError:
        print(f"ERROR: La respuesta del LLM no era un JSON válido: {raw_response}")
        return []
    except Exception as e:
        print(f"Error al conectar con el API de OpenAI o al procesar la respuesta: {e}")
        return []