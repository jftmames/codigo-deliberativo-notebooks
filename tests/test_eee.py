# tests/test_eee.py

import pytest
from deliberative_core.eee import profundidad, pluralidad, compute_eee

# Datos de prueba que simulan una trayectoria con 2 niveles de profundidad.
@pytest.fixture
def sample_trajectory():
    """Crea una trayectoria de prueba para usar en los tests."""
    return [
        # Nivel 0
        {"id": "root", "parent_id": None},
        # Nivel 1 (hijos de root)
        {"id": "child1", "parent_id": "root"},
        {"id": "child2", "parent_id": "root"},
        # Nivel 2 (hijo de child1)
        {"id": "grandchild1", "parent_id": "child1"},
    ]

def test_profundidad(sample_trajectory):
    """Verifica que la profundidad máxima se calcule correctamente."""
    # La profundidad máxima en los datos de prueba es 2.
    assert profundidad(sample_trajectory) == 2.0

def test_pluralidad(sample_trajectory):
    """Verifica que la ramificación promedio se calcule correctamente."""
    # Hay 2 nodos padre (root y child1).
    # 'root' tiene 2 hijos. 'child1' tiene 1 hijo.
    # El promedio es (2 + 1) / 2 = 1.5
    assert pluralidad(sample_trajectory) == 1.5

def test_compute_eee(sample_trajectory):
    """Verifica que el cálculo completo del EEE sea correcto."""
    metrics = compute_eee(sample_trajectory)

    assert metrics["profundidad"] == 2.0
    assert metrics["pluralidad"] == 1.5

    # EEE = (2.0 * 0.6) + (1.5 * 0.4) = 1.2 + 0.6 = 1.8
    assert metrics["eee_score_ponderado"] == pytest.approx(1.8)

def test_empty_trajectory():
    """Verifica que las funciones manejan correctamente una trayectoria vacía."""
    assert profundidad([]) == 0.0
    assert pluralidad([]) == 0.0
    metrics = compute_eee([])
    assert metrics["eee_score_ponderado"] == 0.0