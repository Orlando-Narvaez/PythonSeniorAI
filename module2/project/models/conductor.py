from .persona import Persona

class Conductor(Persona):
    def __init__(
        self, 
        nombre: str, 
        documento: str, 
        licencia: str
        ) -> None:
        super().__init__(nombre, documento)
        if isinstance(licencia, str) and licencia.strip():
            self._licencia = licencia.strip()
        else:
            raise ValueError("La licencia debe ser un texto no vacío.")
    
    @property
    def licencia(self) -> str:
        return self._licencia
    
    @licencia.setter
    def licencia(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._licencia = valor.strip().upper()
        else:
            raise ValueError("La licencia debe ser un texto no vacío.")
    
    def obtener_detalles(self) -> str:
        return (
            f"Conductor: {self.nombre}, "
            f"Documento: {self.documento}, "
            f"Licencia: {self.licencia}"
        )
    