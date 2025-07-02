# main_simulation.py

from deliberative_core.reasoning_tracker import ReasoningTracker
from deliberative_core.navigator import Navigator
from deliberative_core.eee import compute_eee
import json

# --- CONFIGURACIÓN ---
tracker = ReasoningTracker()
navigator = Navigator(tracker)

# --- EJECUCIÓN DEL FLUJO ---
main_node = navigator.start_deliberation(
    "¿Cuáles son las implicaciones de la nueva ley de inteligencia artificial?"
)

# 1. Exploración con perfil de "consultor" en el dominio "legal"
print("\n" + "="*20 + " PRUEBA 1: CONSULTOR LEGAL " + "="*20)
navigator.explore_node(
    main_node.id,
    domain="legal",
    user_profile="consultor"
)

# 2. Exploración con perfil de "docente" en el dominio "educativo"
# Nota: exploramos el mismo nodo principal, pero el resultado será diferente.
# Para una simulación real, deberíamos reiniciar el tracker.
print("\n" + "="*20 + " PRUEBA 2: DOCENTE EDUCATIVO " + "="*20)
# Creamos un nuevo tracker y navigator para una simulación limpia
tracker_docente = ReasoningTracker()
navigator_docente = Navigator(tracker_docente)
main_node_docente = navigator_docente.start_deliberation(
    "¿Cuáles son las implicaciones de la nueva ley de inteligencia artificial?"
)
navigator_docente.explore_node(
    main_node_docente.id,
    domain="educativo",
    user_profile="docente"
)


# --- EVALUACIÓN Y RESULTADOS ---
print("\n--- Resultados para la simulación del CONSULTOR ---")
historial_consultor = tracker.export_history_as_list()
metricas_consultor = compute_eee(historial_consultor)
print(f"Profundidad: {metricas_consultor['profundidad']}, Pluralidad: {metricas_consultor['pluralidad']:.2f}")
print(json.dumps(historial_consultor, indent=2, ensure_ascii=False))


print("\n--- Resultados para la simulación del DOCENTE ---")
historial_docente = tracker_docente.export_history_as_list()
metricas_docente = compute_eee(historial_docente)
print(f"Profundidad: {metricas_docente['profundidad']}, Pluralidad: {metricas_docente['pluralidad']:.2f}")
print(json.dumps(historial_docente, indent=2, ensure_ascii=False))