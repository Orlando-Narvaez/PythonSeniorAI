from typing import Dict, List, Optional
from models.conductor import Conductor


class ConductorServicio:

    def __init__(self) -> None:
        self._conductores: Dict[str, Conductor] = {}

    # Create
    def registrar_conductor(self, conductor: Conductor) -> None:
        if conductor.documento in self._conductores:
            raise ValueError("El conductor ya está registrado.")
        self._conductores[conductor.documento] = conductor

    # Read
    def obtener_conductor(self, documento: str) -> Optional[Conductor]:
        return self._conductores.get(documento)

    def listar_conductores(self) -> List[Conductor]:
        return list(self._conductores.values())