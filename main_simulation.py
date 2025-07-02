# main_simulation.py

from deliberative_core.reasoning_tracker import ReasoningTracker
from deliberative_core.navigator import Navigator
import json

# --- CONFIGURACIÓN ---
# 1. Crear las instancias de nuestros módulos.
tracker = ReasoningTracker()
navigator = Navigator(tracker) # El navigator usa el tracker.

# --- EJECUCIÓN DEL FLUJO ---
# 2. Iniciar la deliberación con una pregunta.
main_node = navigator.start_deliberation(
    "¿Cómo podemos usar la IA para fomentar la innovación educativa?"
)

# 3. Explorar la pregunta principal para generar la primera capa de subpreguntas.
navigator.explore_node(main_node.id)

# 4. Ver qué preguntas quedan abiertas.
open_questions = navigator.get_open_questions()
print(f"\n🔍 Hay {len(open_questions)} preguntas abiertas listas para ser exploradas.")
for i, question in enumerate(open_questions, 1):
    print(f"   {i}. [{question.id[:6]}...] {question.contenido}")

# (Opcional) Explorar una de las subpreguntas para crear una segunda capa de profundidad.
if open_questions:
    node_to_explore_next = open_questions[0]
    navigator.explore_node(node_to_explore_next.id)


# --- RESULTADO FINAL ---
print("\n--- Historial Completo Final ---")
print(json.dumps(tracker.export_history_as_list(), indent=2, ensure_ascii=False))