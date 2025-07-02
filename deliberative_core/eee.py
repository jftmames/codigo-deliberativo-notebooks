# deliberative_core/eee.py

from typing import List, Dict, Any

def _get_node_depth(node_id: str, nodes_by_id: Dict[str, Dict], memo: Dict) -> int:
    """Función auxiliar para calcular la profundidad de un nodo con memoización."""
    if node_id in memo:
        return memo[node_id]
    
    node = nodes_by_id.get(node_id)
    if not node or node.get("parent_id") is None:
        memo[node_id] = 0
        return 0
    
    parent_depth = _get_node_depth(node["parent_id"], nodes_by_id, memo)
    memo[node_id] = 1 + parent_depth
    return 1 + parent_depth

def profundidad(trayectoria: List[Dict[str, Any]]) -> float:
    """
    Mide la profundidad máxima del árbol de razonamiento.
    Un valor más alto indica una exploración más profunda de las ideas.
    """
    if not trayectoria:
        return 0.0

    nodes_by_id = {node["id"]: node for node in trayectoria}
    memo = {} # Memoización para evitar recalcular profundidades
    
    max_depth = 0
    for node in trayectoria:
        depth = _get_node_depth(node["id"], nodes_by_id, memo)
        if depth > max_depth:
            max_depth = depth
            
    return float(max_depth)

def pluralidad(trayectoria: List[Dict[str, Any]]) -> float:
    """
    Mide el número promedio de subpreguntas por cada pregunta explorada.
    Un valor más alto indica una mayor ramificación y exploración de alternativas.
    """
    parent_nodes = {} # {parent_id: count_of_children}
    for node in trayectoria:
        parent_id = node.get("parent_id")
        if parent_id:
            parent_nodes[parent_id] = parent_nodes.get(parent_id, 0) + 1
            
    if not parent_nodes:
        return 0.0
        
    avg_branching = sum(parent_nodes.values()) / len(parent_nodes)
    return avg_branching

def compute_eee(trayectoria: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calcula las métricas del Índice de Equilibrio Erotético (EEE).
    """
    p_profundidad = profundidad(trayectoria)
    p_pluralidad = pluralidad(trayectoria)
    
    # El EEE final puede ser un promedio ponderado, por ahora los devolvemos por separado.
    # Se pueden añadir otras métricas como trazabilidad o reversibilidad.
    eee_score = (p_profundidad * 0.6) + (p_pluralidad * 0.4)

    return {
        "profundidad": p_profundidad,
        "pluralidad": p_pluralidad,
        "eee_score_ponderado": eee_score
    }