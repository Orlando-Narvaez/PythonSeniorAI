from abc import ABC, abstractmethod
from typing import Optional # Tipado fuerte => typing: List, Tuple, Dict

# Interfaz

class Movible(ABC):
    @abstractmethod
    def mover(self) -> None:
        pass
    
# Superclase Abstracta 

class Animal(ABC):
    def __init__(self, nombre:str) -> None:
        self._nombre: str = " "
        self.nombre = nombre
        
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor:str) -> None:
            if isinstance(valor, str) and valor.strip():
                self._nombre = valor.strip().title()
            else:
                raise ValueError("El nombre debe ser una cadena de texto valida")
            
    @abstractmethod
    def sonido(self) -> None:
        pass
    
# Subclases 

class Perro(Animal):
    def sonido(self) -> None:
        print(f"El perrito {self.nombre} -> dice: guau guau")

class Gato(Animal):
    def sonido(self) -> None:
        print(f"El gato {self.nombre} -> dice. miau miau")
        
class Vaca(Animal):
    def sonido(self) -> None:
        print(f"La vaca {self.nombre} -> dice: muuuuu")
        
class Leon(Animal, Movible):
    def sonido(self) -> None:
        print(f"El leon {self.nombre} -> dice: grrrrr")
        
    def mover(self) -> None:
        print(f"El leon {self.nombre} camina sigilosamente por la sabana...")
        
def hacer_sonido(animal: Animal) -> None:
    animal.sonido()
    
def main() -> None:
    try:
        animales = [
            Perro("Firulais"),
            Gato("Tom"),
            Vaca("Lola")
        ]
                
        print("Polimorfismo")
        for animal in animales:
            hacer_sonido(animal)
            
        print("Polimorfismo e implementacion de interfaz")
        animal2 = Leon("Simba")
        animal2.sonido()
        animal2.mover()
    except ValueError as e:
        print(f"ERROR de validacion")
        
if __name__ == "__main__":
    main()
        