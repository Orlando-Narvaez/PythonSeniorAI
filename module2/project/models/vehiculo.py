from abc import ABC, abstractmethod
from .movible import Movible
from .motor import Motor
from .conductor import Conductor


class Vehiculo(Movible, ABC):

    def __init__(self, placa: str, motor: Motor) -> None:
        if isinstance(placa, str) and placa.strip():
            self._placa = placa.strip().upper()
        else:
            raise ValueError("La placa debe ser un texto no vacío.")

        if isinstance(motor, Motor):
            self._motor = motor
        else:
            raise ValueError("El vehículo debe tener un motor válido.")

        # el vehículo puede existir sin conductor
        self._conductor: Conductor | None = None

    @property
    def placa(self) -> str:
        return self._placa

    @property
    def motor(self) -> Motor:
        return self._motor

    @property
    def conductor(self) -> Conductor | None:
        return self._conductor

    # ---------- Agregación ----------
    def asignar_conductor(self, conductor: Conductor) -> None:
        if isinstance(conductor, Conductor):
            self._conductor = conductor
        else:
            raise ValueError("Debe asignarse un conductor válido.")

    def quitar_conductor(self) -> None:
        self._conductor = None

    # ---------- Polimorfismo ----------
    @abstractmethod
    def iniciar_jornada(self) -> None:
        pass

    # ---------- Interfaz Movible ----------
    def mover(self) -> None:
        print(f"El vehículo con placa {self.placa} está en movimiento.")
