class Motor:
    def __init__(self, tipo: str, potencia: int) -> None:
        if isinstance(tipo, str) and tipo.strip():
            self._tipo = tipo.strip().lower()
        else:
            raise ValueError("El tipo de motor debe ser un texto no vacío.")

        if isinstance(potencia, int) and potencia > 0:
            self._potencia = potencia
        else:
            raise ValueError("La potencia debe ser un número entero positivo.")

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def potencia(self) -> int:
        return self._potencia

    def obtener_detalles(self) -> str:
        return (f"Motor: {self.tipo}, Potencia: {self.potencia} HP")