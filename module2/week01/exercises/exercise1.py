class Automovil:
    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio
        
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def precio(self):
        return self.__precio
    
    @marca.setter
    def marca(self, nueva_marca):
        if isinstance(nueva_marca, (str)):
            self.__marca = nueva_marca
        else:
            print("Error, solo se permiten caracteres ")
    
    @modelo.setter
    def modelo(self, nuevo_modelo):
        if isinstance(nuevo_modelo, (int)):
            self.__modelo = nuevo_modelo
        else:
            print("ERROR al ingresar el modelo del automovil")
            
    @precio.setter
    def precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int , float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("ERROR al ingresar el precio del automovil")
    
    def mostrar_informacion(self):
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")
        print(f"Precio: {self.__precio}")
        
def main():
    print("\n*** SISTEMA DE REGISTRO DE AUTOMOVILES ***") 
    
    auto1 = Automovil("Ford", 2010, 50000000)
    auto2 = Automovil("Mazda", 2024, 120000000)
    auto3 = Automovil("Ferrari", 2025, 1250000000)
    
    print("Información de los automoviles")
    auto1.mostrar_informacion()
    auto2.mostrar_informacion()
    auto3.mostrar_informacion()
    
    auto1.marca = "Volkswagen"
    auto2.modelo = 2020
    auto3.precio = 2000000000
    
    print("Información de los automoviles actaulizada")
    auto1.mostrar_informacion()
    auto2.mostrar_informacion()
    auto3.mostrar_informacion()
    
if __name__ == "__main__":
    main()
        