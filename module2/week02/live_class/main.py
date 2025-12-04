"""class Vehivulo:
    def mover(self):
        print("El vehiculo se está moviendo")
        
class Carro(Vehivulo):
    pass

def main():
    vehivulo1 = Vehivulo()
    carro1 = Carro()
    
    print("Vehiculo")
    vehivulo1.mover()
    
    print("Carro que hereda de la superclase de Vehiculo")
    carro1.mover()
    
if __name__ == "__main__":
    main()
""" 

# SOBRE ESCRITURA
"""
class Vehiculo:
    def mover(self):
        print("El vehiculo se está moviendo")
        
class Carro(Vehiculo):
    def mover(self):
        print("El carro rueda por la calle")
        
def main():
    vehiculo2 = Vehiculo()
    carro2 = Carro()
    
    print("Vehiculo")
    vehiculo2.mover()
    
    print("El carro sobre escribio el metodo (def) mover ya que su movimiento es a traves de ruedas")
    carro2.mover()
    
if __name__ == "__main__":
    main()
    """
    
# Polimorfismo

"""
class Vehiculo():
    def mover(self):
        print("El vehiculo se está moviendo")
        
class Carro(Vehiculo):
    def mover(self):
        print("El carro rueda por la calle")
        
class Avion(Vehiculo):
    def mover(self):
        print("El avion esta volando sobre la ciudad")
        
def main():
    vehiculo3 = Vehiculo()
    carro3 = Carro()
    avion = Avion()
    
    print("Vehiculo")
    vehiculo3.mover()
    
    print("Carro")
    carro3.mover()
    
    print("Avion")
    avion.mover()
    
if __name__ == "__main__":
    main()
    """
    
# 

class Padre():
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
        
class Hijo(Padre):
    def __init__(self, mensaje, nombre) -> None:
        super().__init__(mensaje)
        self.nombre = nombre