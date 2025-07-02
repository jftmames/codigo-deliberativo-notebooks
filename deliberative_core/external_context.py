# deliberative_core/external_context.py

def get_concepts(text: str, domain: str = "general") -> list[str]:
    """
    Extrae conceptos clave de un texto.

    NOTA: Esta es una implementación MOCK (simulada). Devuelve valores fijos
    para facilitar el desarrollo sin dependencias externas.
    A futuro, se conectará a un servicio RAG.
    """
    print("ADVERTENCIA: Usando la función mock de get_concepts.")

    text_lower = text.lower()

    if "innovación educativa" in text_lower or "ia" in text_lower:
        return ["tecnología educativa", "pedagogías activas", "evaluación formativa", "brecha digital"]
    elif "economía" in text_lower:
        return ["inflación", "crecimiento económico", "política fiscal", "mercado laboral"]
    else:
        return ["análisis de datos", "marco regulatorio", "stakeholders", "impacto social"]