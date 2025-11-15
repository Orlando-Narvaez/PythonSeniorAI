""" 
1. Número positivo, negativo o cero

Descripción: Solicitar un número e indicar si es positivo, negativo o cero.
"""

numero = int(input("Ingrese un numero por favor: "))

if numero < 0:
    print(f"El numero {numero} es negativo.")
elif numero == 0:
    print(f"El numero {numero} es un cero.")
else:
    print(f"El numero {numero} es positivo.")