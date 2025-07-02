# deliberative_core/inquiry_engine.py

import json
from openai import OpenAI
from .utils import load_api_key

api_key = load_api_key()
client = OpenAI(api_key=api_key)

def generate_subquestions(
    main_question: str,
    concepts: list[str],
    domain: str = "general",
    user_profile: str = "consultor"
) -> list[str]:
    """
    Genera subpreguntas utilizando un LLM, adaptando el prompt al dominio
    y perfil de usuario especificados.
    """
    # --- Lógica de Expansión ---
    # Personalizamos el rol del asistente de IA y la tarea según los parámetros.
    system_prompt = f"Eres un asistente experto en análisis crítico en el dominio de '{domain}'."
    
    if user_profile == "docente":
        task_description = f"Tu tarea es descomponer una pregunta principal en 5 subpreguntas que fomenten el pensamiento crítico y el aprendizaje profundo, adecuadas para un perfil de '{user_profile}'."
    elif user_profile == "politica_publica":
        task_description = f"Tu tarea es descomponer una pregunta principal en 5 subpreguntas que evalúen el impacto, la viabilidad y las consecuencias no deseadas, para un perfil de '{user_profile}'."
    else: # Perfil "consultor" o por defecto
        task_description = f"Tu tarea es descomponer una pregunta principal en 5 subpreguntas orientadas a la acción, la estrategia y la toma de decisiones, para un perfil de '{user_profile}'."
    # --- Fin de la lógica de expansión ---

    prompt_template = f"""
    {task_description}

    Pregunta Principal: "{main_question}"
    Conceptos Clave a Considerar: {', '.join(concepts)}

    Devuelve únicamente un objeto JSON que contenga una única clave "subpreguntas",
    cuyo valor sea un array de 5 strings.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_template}
            ],
            temperature=0.7,
            max_tokens=500
        )
        raw_response = response.choices[0].message.content
        data = json.loads(raw_response)
        return data.get("subpreguntas", [])

    except Exception as e:
        print(f"Error al conectar con el API de OpenAI o al procesar la respuesta: {e}")
        return []