from dataclasses import dataclass

@dataclass
class Libro:
    _titulo: str
    _autor: str
    _isbn: str
    _precio: float
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._titulo = valor
        else:
            raise ValueError("Error: El título debe ser una cadena no vacía.")
            
    @property
    def autor(self) -> str:
        return self._autor  
    
    @autor.setter
    def autor(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._autor = valor
        else:
            raise ValueError("Error: El autor debe ser una cadena no vacía.")
    
    @property
    def isbn(self) -> str:
        return self._isbn
    
    @isbn.setter
    def isbn(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._isbn = valor
        else:
            raise ValueError("Error: El ISBN debe ser una cadena no vacía.")
    
    @property
    def precio(self) -> float:
        return self._precio
    
    
    @precio.setter
    def precio(self, valor: float) -> None:
        if isinstance(valor, float) and valor >= 0:
            self._precio = float(valor)
        else:
            raise ValueError("Error: El precio debe ser un número no negativo.")
        
    def __repr__(self) -> str:
        return (f"Libro(titulo='{self._titulo}', autor='{self._autor}', "
                f"ISBN='{self._isbn}', precio={self._precio})"
                )
        
def main():
    print("\n*** SISTEMA DE REGISTRO DE LIBROS ***") 
    
    book1 = Libro("Cien años de soledad", "Gabriel García Márquez", "123-456-789", 1000.0)
    
    print("Información del libro")
    
    # Mostrar información actual del objeto/instancia/ejemplar
    print(book1)
    
    # mostrar el precio actual
    print("Precio actual:", book1.precio)
    
    # Cambiar el precio actual del libro
    book1.precio = 2000.0
    
    print("Nuevo precio: ", book1.precio)
    
    print("\n Software IA finalizado")

if __name__ == "__main__":
    main()