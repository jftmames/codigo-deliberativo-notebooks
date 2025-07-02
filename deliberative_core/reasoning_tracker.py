# deliberative_core/reasoning_tracker.py

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal, List, Dict, Any

# Tipos para un control más estricto
NodeType = Literal["pregunta_principal", "subpregunta", "respuesta_contextual"]
NodeStatus = Literal["abierta", "en_proceso", "respondida", "cerrada"]
NodeOrigin = Literal["humano", "ia_generativa", "ia_analitica"]

@dataclass
class ReasoningNode:
    """
    Representa un único nodo en el árbol de razonamiento.
    Cumple con el Requisito Epistémico 2.1 de trazabilidad.
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    tipo: NodeType = "subpregunta"
    origen: NodeOrigin = "ia_generativa"
    contenido: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    estado: NodeStatus = "abierta"
    parent_id: str | None = None  # ID del nodo que generó este
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte el nodo a un diccionario para exportación."""
        return {
            "id": self.id,
            "tipo": self.tipo,
            "origen": self.origen,
            "contenido": self.contenido,
            "timestamp": self.timestamp,
            "estado": self.estado,
            "parent_id": self.parent_id,
        }

# (continuación en deliberative_core/reasoning_tracker.py)

class ReasoningTracker:
    """
    Gestiona la colección completa de nodos de razonamiento (la trayectoria).
    Permite registrar y reconstruir el proceso deliberativo.
    """
    def __init__(self):
        self.nodes: Dict[str, ReasoningNode] = {}

    def add_node(self, node: ReasoningNode) -> ReasoningNode:
        """Añade un nuevo nodo al registro."""
        self.nodes[node.id] = node
        print(f"INFO: Nodo {node.id} ({node.tipo}) añadido al tracker.")
        return node

    def get_node(self, node_id: str) -> ReasoningNode | None:
        """Recupera un nodo por su ID."""
        return self.nodes.get(node_id)

    def update_node_status(self, node_id: str, new_status: NodeStatus):
        """Actualiza el estado de un nodo existente."""
        if node := self.get_node(node_id):
            node.estado = new_status
            print(f"INFO: Estado del nodo {node_id} actualizado a '{new_status}'.")
        else:
            print(f"ERROR: No se encontró el nodo con ID {node_id}.")

    def export_history_as_list(self) -> List[Dict[str, Any]]:
        """Exporta la trayectoria completa como una lista de diccionarios."""
        return [node.to_dict() for node in self.nodes.values()]

    def __repr__(self) -> str:
        return f"ReasoningTracker con {len(self.nodes)} nodos."
