# main_simulation.py

from deliberative_core.inquiry_engine import generate_subquestions
from deliberative_core.external_context import get_concepts
from deliberative_core.reasoning_tracker import ReasoningTracker, ReasoningNode

# 1. Inicia el tracker
tracker = ReasoningTracker()

# 2. El usuario plantea una pregunta principal
main_question_text = "¿Cómo podemos usar la IA para fomentar la innovación educativa?"
main_question_node = tracker.add_node(
    ReasoningNode(
        tipo="pregunta_principal",
        origen="humano",
        contenido=main_question_text,
        estado="en_proceso"
    )
)

# 3. El sistema busca conceptos clave
concepts = get_concepts(main_question_text)

# 4. El sistema genera subpreguntas usando la IA
subquestion_texts = generate_subquestions(main_question_text, concepts)

# 5. El sistema registra cada subpregunta en el tracker
for sq_text in subquestion_texts:
    tracker.add_node(
        ReasoningNode(
            tipo="subpregunta",
            origen="ia_generativa",
            contenido=sq_text,
            parent_id=main_question_node.id  # Vinculamos a la pregunta principal
        )
    )

# 6. Revisa el estado final de la memoria
print("\n--- Estado Final de la Memoria ---")
print(tracker)

print("\n--- Historial Completo Exportado ---")
import json
print(json.dumps(tracker.export_history_as_list(), indent=2))