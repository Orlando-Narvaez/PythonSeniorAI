"""    
Slicing con pasos (step)
    Dada la lista:

    datos = [1, 2, 3, 4, 5, 6, 7, 8]
    
    Hacer:
    
    1. Obtén los elementos en posiciones pares.
    2. Obtén los elementos en posiciones impares.
"""
datos = [1, 2, 3, 4, 5, 6, 7, 8]

# 1. Obtén los elementos en posiciones pares.
elementos_pares = datos[::2]

# 2. Obtén los elementos en posiciones impares.
elementos_impares = datos[1::2]

print("Elementos en posiciones pares:", elementos_pares)
print("Elementos en posiciones impares:", elementos_impares)