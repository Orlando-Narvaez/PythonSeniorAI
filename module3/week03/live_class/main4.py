from typing import Tuple, Set

def _normailizar_producto(nombre: str) -> str:
    return nombre.strip().capitalize()

def _es_producto_valido(nombre: str) -> bool:
    return nombre != ""

# Entrada de datos
def _leer_entero(mensaje: str) -> int:
    while True:
        valor: str = input(mensaje)
        if valor.isdigit():
            return int(valor)
        print("Error: por favor ingrese un número entero válido.")
        
def _leer_texto(mensaje: str) -> str:
    return input(mensaje)

def _leer_producto(indice: int) -> str:
    while True:
        texto: str = _leer_texto(f"Ingrese el nombre del producto {indice}: ")
        producto: str = _normailizar_producto(texto)
        
        if _es_producto_valido(producto):
            return producto
        
        print("Error: el nombre del producto no puede estar vacío.")
        
def _contruir_conjunto_productos(cantidad: int) -> Set[str]:
    productos: Set[str] = set()
    cantidad: int = _leer_entero(f"Ingrese la cantidad de productos para la tienda: ")
    
    for i in range(1, cantidad + 1):
        producto: str = _leer_producto(i)
        productos.add(producto)
        
    return productos

# Logica el software o el servicio (service)

def operaciones_productos(
    productos_tienda_a: Set[str],
    productos_tienda_b: Set[str]
) -> Tuple[Set[str], Set[str], Set[str]]:
    
    union: Set[str] = productos_tienda_a | productos_tienda_b
    interseccion: Set[str] = productos_tienda_a & productos_tienda_b
    diferencia: Set[str] = productos_tienda_a - productos_tienda_b
    
    return union, interseccion, diferencia

# Presentacion (Capa de presentación)

def _mostrar_conjunto(nombre: str, conjunto: Set[str]) -> None:
    print(f"{nombre}: {conjunto}")
    
def _mostrar_resultados(
    union: Set[str],
    interseccion: Set[str],
    diferencia: Set[str]
) -> None:
    print("\nResultados:")
    _mostrar_conjunto("Unión", union)
    _mostrar_conjunto("Intersección", interseccion)
    _mostrar_conjunto("Diferencia (Tienda A - Tienda B)", diferencia)