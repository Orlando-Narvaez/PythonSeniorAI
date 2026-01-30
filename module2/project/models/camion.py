from .vehiculo import Vehiculo
from .motor import Motor


class Camion(Vehiculo):

    def __init__(
        self,
        placa: str,
        motor: Motor,
        planilla_carga: bool,
        peso_actual: float,
        peso_maximo: float
    ) -> None:
        super().__init__(placa, motor)

        if isinstance(planilla_carga, bool):
            self._planilla_carga = planilla_carga
        else:
            raise ValueError("La planilla de carga debe ser un valor booleano.")

        if isinstance(peso_maximo, (int, float)) and peso_maximo > 0:
            self._peso_maximo = float(peso_maximo)
        else:
            raise ValueError("El peso máximo debe ser un número positivo.")

        if isinstance(peso_actual, (int, float)) and peso_actual >= 0:
            self._peso_actual = float(peso_actual)
        else:
            raise ValueError("El peso actual debe ser un número válido.")

    @property
    def planilla_carga(self) -> bool:
        return self._planilla_carga

    @planilla_carga.setter
    def planilla_carga(self, value: bool) -> None:
        if isinstance(value, bool):
            self._planilla_carga = value
        else:
            raise ValueError("La planilla de carga debe ser un valor booleano.")

    @property
    def peso_maximo(self) -> float:
        return self._peso_maximo

    @peso_maximo.setter
    def peso_maximo(self, value: float) -> None:
        if isinstance(value, (int, float)) and value > 0:
            self._peso_maximo = float(value)
        else:
            raise ValueError("El peso máximo debe ser un número positivo.")

    @property
    def peso_actual(self) -> float:
        return self._peso_actual

    @peso_actual.setter
    def peso_actual(self, value: float) -> None:
        if isinstance(value, (int, float)) and value >= 0:
            self._peso_actual = float(value)
        else:
            raise ValueError("El peso actual debe ser un número válido.")

    # ---------- Polimorfismo ----------

    def iniciar_jornada(self) -> None:
        if not self.conductor:
            raise ValueError("No se puede iniciar la jornada sin un conductor asignado.")

        if not self.planilla_carga:
            raise ValueError("No se puede iniciar la jornada: la planilla de carga es obligatoria.")

        if self.peso_actual > self.peso_maximo:
            raise ValueError("No se puede iniciar la jornada: el peso excede el máximo permitido.")

        print(
            f"Camión {self.placa}: jornada iniciada con el conductor "
            f"{self.conductor.nombre}. Peso: {self.peso_actual}/{self.peso_maximo}."
        )
