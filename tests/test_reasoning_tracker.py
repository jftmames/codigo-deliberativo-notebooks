# tests/test_reasoning_tracker.py

from deliberative_core.reasoning_tracker import ReasoningTracker, ReasoningNode

def test_add_and_get_node():
    """Verifica que se puede añadir y recuperar un nodo correctamente."""
    tracker = ReasoningTracker()
    node = ReasoningNode(contenido="Pregunta de prueba")

    tracker.add_node(node)

    retrieved_node = tracker.get_node(node.id)

    assert retrieved_node is not None
    assert retrieved_node.id == node.id
    assert retrieved_node.contenido == "Pregunta de prueba"

def test_update_node_status():
    """Verifica que el estado de un nodo se puede actualizar."""
    tracker = ReasoningTracker()
    node = ReasoningNode(estado="abierta")
    tracker.add_node(node)

    tracker.update_node_status(node.id, "cerrada")

    updated_node = tracker.get_node(node.id)
    assert updated_node.estado == "cerrada"

def test_export_history():
    """Verifica que el historial se exporta como una lista de diccionarios."""
    tracker = ReasoningTracker()
    tracker.add_node(ReasoningNode(contenido="Nodo 1"))
    tracker.add_node(ReasoningNode(contenido="Nodo 2"))

    history = tracker.export_history_as_list()

    assert isinstance(history, list)
    assert len(history) == 2
    assert isinstance(history[0], dict)
    assert history[0]['contenido'] == "Nodo 1"