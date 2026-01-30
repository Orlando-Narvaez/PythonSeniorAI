from typing import Dict, List, Optional
from models.vehiculo import Vehiculo
from models.conductor import Conductor


class VehiculoServicio:

    def __init__(self) -> None:
        self._vehiculos: Dict[str, Vehiculo] = {}

    # Create
    def registrar_vehiculo(self, vehiculo: Vehiculo) -> None:
        if vehiculo.placa in self._vehiculos:
            raise ValueError("El vehículo ya está registrado.")
        self._vehiculos[vehiculo.placa] = vehiculo

    # Read
    def obtener_vehiculo(self, placa: str) -> Optional[Vehiculo]:
        return self._vehiculos.get(placa)

    def listar_vehiculos(self) -> List[Vehiculo]:
        return list(self._vehiculos.values())

    # Reglas de negocio
    def asignar_conductor(self, placa: str, conductor: Conductor) -> None:
        vehiculo = self.obtener_vehiculo(placa)
        if vehiculo is None:
            raise ValueError("Vehículo no encontrado.")

        vehiculo.asignar_conductor(conductor)

    def iniciar_jornada(self, placa: str) -> None:
        vehiculo = self.obtener_vehiculo(placa)
        if vehiculo is None:
            raise ValueError("Vehículo no encontrado.")

        vehiculo.iniciar_jornada()