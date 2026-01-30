# Una tienda desea guardar la lista de nombres de sus clientes registrados para promociones
# El sistema debe permitir:
# 1. Agregar un nuevos clientes.
# 2. Recorrer la lista y mostrar todos los clientes.
# 3. Modificar un nombre en caso de error
# 4. Eliminar un cliente de la lista

def agregar_cliente(lista_clientes, nombres):
    if isinstance(nombres, list) and 2 <= len(nombres) <= 50:
        lista_clientes.append(nombres.title())
        print(f"Cliente '{nombres.title()}' agregado exitosamente.")
    else:
        print("Nombre invalido")
        
def mostrar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print(cliente)
        
def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    if not (isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50):
        print("Nombre invalido")
        return
    if 0 <= indice < len(lista_clientes):
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"Cliente en el indice {indice} modificado exitosamente.")
        
def eliminar_cliente(lista_clientes, indice):
    if 0 <= indice < len(lista_clientes):
        eliminado = lista_clientes.pop(indice)
        print(f"Cliente '{eliminado}' eliminado exitosamente.")
    else:
        print("Indice invalido")
        
def main():
    clientes = ["Ana", "Luis", "Maria"]
    print("Lista de clientes:")
    mostrar_clientes(clientes)
    
    agregar_cliente(clientes, "Carlos")
    print("\nLista de clientes despues de agregar:")
    mostrar_clientes(clientes)  
    
    modificar_cliente(clientes, 1, "Luis Miguel")
    print("\nLista de clientes despues de modificar:")
    mostrar_clientes(clientes)
    
    eliminar_cliente(clientes, 0)
    print("\nLista de clientes despues de eliminar:")   
    mostrar_clientes(clientes)

if __name__ == "__main__":
    main()