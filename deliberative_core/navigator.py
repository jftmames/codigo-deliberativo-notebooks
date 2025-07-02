# deliberative_core/navigator.py

from .inquiry_engine import generate_subquestions
from .reasoning_tracker import ReasoningTracker, ReasoningNode
from .external_context import get_concepts

class Navigator:
    """
    Orquesta el flujo del proceso deliberativo. Utiliza los otros módulos
    para gestionar el estado, generar preguntas y registrar la historia.
    """
    def __init__(self, tracker: ReasoningTracker):
        self.tracker = tracker

    def start_deliberation(self, main_question_text: str) -> ReasoningNode:
        """
        Inicia un nuevo proceso deliberativo con una pregunta principal.
        """
        print(f"\n🚀 Iniciando deliberación para: '{main_question_text}'")
        node = ReasoningNode(
            tipo="pregunta_principal",
            origen="humano",
            contenido=main_question_text,
            estado="abierta"
        )
        return self.tracker.add_node(node)

    def explore_node(self, node_id: str):
        """
        Explora un nodo de pregunta, generando y registrando sus subpreguntas.
        """
        node_to_explore = self.tracker.get_node(node_id)
        if not node_to_explore or node_to_explore.tipo not in ["pregunta_principal", "subpregunta"]:
            print(f"ERROR: No se puede explorar el nodo {node_id}. No es una pregunta válida.")
            return

        if node_to_explore.estado != "abierta":
            print(f"INFO: El nodo {node_id} ya fue explorado o está cerrado. Estado: {node_to_explore.estado}")
            return
            
        print(f"\n🧠 Explorando nodo {node_id}: '{node_to_explore.contenido}'")
        self.tracker.update_node_status(node_id, "en_proceso")

        # 1. Obtener conceptos (mock por ahora)
        concepts = get_concepts(node_to_explore.contenido)
        print(f"   Concepts identificados: {concepts}")

        # 2. Generar subpreguntas con la IA
        subquestion_texts = generate_subquestions(node_to_explore.contenido, concepts)
        print(f"   Subpreguntas generadas por la IA: {len(subquestion_texts)}")

        # 3. Registrar las nuevas subpreguntas
        for sq_text in subquestion_texts:
            new_node = ReasoningNode(
                tipo="subpregunta",
                origen="ia_generativa",
                contenido=sq_text,
                parent_id=node_id
            )
            self.tracker.