from .vehiculo import Vehiculo
from .motor import Motor


class Carro(Vehiculo):

    def __init__(
        self,
        placa: str,
        motor: Motor,
        revision_tecnico_mecanica_vigente: bool
        ) -> None:
        super().__init__(placa, motor)
        if isinstance(revision_tecnico_mecanica_vigente, bool):
            self.revision_tecnico_mecanica_vigente = revision_tecnico_mecanica_vigente
        else:
            raise ValueError("La revisión técnico-mecánica debe ser un valor booleano.")

    @property
    def revision_tecnico_mecanica_vigente(self) -> bool:
        return self._revision_tecnico_mecanica_vigente

    @revision_tecnico_mecanica_vigente.setter
    def revision_tecnico_mecanica_vigente(self, value: bool) -> None:
        if isinstance(value, bool):
            self._revision_tecnico_mecanica_vigente = value
        else:
            raise ValueError("La revisión técnico-mecánica debe ser un valor booleano.")

    def iniciar_jornada(self) -> None:
        if not self.conductor:
            raise ValueError(
                "No se puede iniciar la jornada sin un conductor asignado."
            )

        if not self.revision_tecnico_mecanica_vigente:
            raise ValueError("No se puede iniciar la jornada: la revisión técnico-mecánica no está vigente.")

        print(f"Carro {self.placa}: jornada iniciada con el conductor {self.conductor.nombre}.")