# Eliminar duplicados de una lista

from typing import List

def eliminar_duplicados(numeros: List[int]) -> List[int]:
    if not isinstance(numeros, list):
        TypeError("Se esperaba una LISTA de numeros")
        
    if not all(isinstance(n,int) for n in numeros):
        raise ValueError("Todos los elementos dentro de lista deben ser numeros enteros")
    
    return sorted(set(numeros))

def main() -> None:
    numeros = [1, 2, 5, 8, 7, 6, 4, 5 , 1, 9, 7]
    print(f"Lista original: {numeros}")
    
    try: 
        resultado = eliminar_duplicados(numeros)
        print(f"Sin duplicados: {resultado}")
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        
if __name__ == "__main__":
    main()
    