from .vehiculo import Vehiculo
from .motor import Motor


class Moto(Vehiculo):

    def __init__(
        self, 
        placa: str, 
        motor: Motor, 
        casco: bool
        ) -> None:
        super().__init__(placa, motor)
        if isinstance(casco, bool):
            self._casco = casco
        else:
            raise ValueError("El valor de casco debe ser un booleano.")

    @property
    def casco(self) -> bool:
        return self._casco
    
    @casco.setter
    def casco(self, value: bool) -> None:
        if isinstance(value, bool):
            self._casco = value
        else:
            raise ValueError("El valor de casco debe ser un booleano.")

    def iniciar_jornada(self) -> None:
        if not self.conductor:
            raise ValueError(
                "No se puede iniciar la jornada sin un conductor asignado."
            )

        if not self.casco:
            raise ValueError("No se puede iniciar la jornada: el casco es obligatorio.")

        print(f"Moto {self.placa}: jornada iniciada con el conductor {self.conductor.nombre}.")
