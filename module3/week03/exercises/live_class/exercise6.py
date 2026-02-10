"""
Enunciado

Desarrolle un programa en Python que permita comparar los productos disponibles en dos tiendas.

El sistema debe solicitar por teclado los nombres de los productos de la "Tienda A" y la "Tienda B", almacenándolos en estructuras de tipo set[str].

Implemente "todas las funciones necesarias con tipado fuerte (type hints)", incluyendo:

* Una función para leer los productos por teclado
* Una función que reciba ambos conjuntos y retorne:

  * La "unión"
  * La "intersección"
  * La "diferencia" (productos exclusivos de la Tienda A)

Finalmente, el programa principal debe invocar las funciones y mostrar los resultados obtenidos.

"""
from typing import Set, Tuple

def agregar_productos(nombre_tienda: str)-> Set[str]:
  while True:
    productos = input(f"Ingrese los productos de {nombre_tienda} separados por coma: ")
    if not productos.strip():
      print("Error: el espacio no debe estar vacio. ")
      continue
    print(f"\nLos siguientes productos fueron agregados con exito: {productos}\n")
    return {p.strip().lower().title() for p in productos.split(",") if p.strip()}

def conjuntos(tienda_1: Set[str], tienda_2: Set[str]) -> Tuple[Set[str], Set[str], Set[str]]:
  union = tienda_1 | tienda_2
  interseccion = tienda_1 & tienda_2
  diferencia = tienda_1 - tienda_2
  return union, interseccion, diferencia

def main():
  tienda_1 = agregar_productos("Tienda A")
  tienda_2 = agregar_productos("Tienda B")
  u, i, d = conjuntos(tienda_1, tienda_2)
  print(f"\nUnion: {u}")
  print(f"Interseccion: {i}")
  print(f"Diferencia: {d}")

if __name__ == "__main__":
  main()