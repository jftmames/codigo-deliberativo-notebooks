# tests/test_navigator.py

from deliberative_core.navigator import Navigator
from deliberative_core.reasoning_tracker import ReasoningTracker

def test_navigator_explore_node(mocker):
    """
    Prueba el flujo de exploración del Navigator, usando un 'mock'
    para simular la respuesta del inquiry_engine.
    """
    # 1. Preparación
    tracker = ReasoningTracker()
    navigator = Navigator(tracker)

    # 2. Configuración del Mock
    # Creamos una respuesta falsa que nuestro 'impostor' devolverá.
    fake_subquestions = ["Subpregunta falsa 1", "Subpregunta falsa 2"]

    # Le decimos a pytest que reemplace 'generate_subquestions'
    # con un mock que siempre devuelve nuestra lista falsa.
    mocker.patch(
        'deliberative_core.navigator.generate_subquestions',
        return_value=fake_subquestions
    )

    # 3. Ejecución
    # Iniciamos y exploramos un nodo, como en la simulación real.
    main_node = navigator.start_deliberation("Pregunta inicial")
    navigator.explore_node(main_node.id)

    # 4. Verificación (Asserts)
    # Comprobamos que el resultado es el esperado.
    history = tracker.export_history_as_list()

    # Debe haber 3 nodos en total: 1 principal + 2 subpreguntas falsas.
    assert len(history) == 3

    # El estado del nodo principal debe ser 'respondida'.
    assert history[0]['estado'] == 'respondida'

    # El contenido de la segunda subpregunta debe ser el que definimos.
    # (El historial no garantiza el orden, así que buscamos por contenido)
    subquestion_contents = {node['contenido'] for node in history if node['tipo'] == 'subpregunta'}
    assert "Subpregunta falsa 2" in subquestion_contents