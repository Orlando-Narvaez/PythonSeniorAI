""" 
3. Ejercicio 3: Verificar rango de valores

Enunciado:
Pide un número y muestra un mensaje solo si está entre 10 y 50 (inclusive).
"""

numero = int(input("Ingrese un número: "))
if 10 <= numero <= 50:
    print("El número está en el rango de 10 a 50.")
else:
    print("El número está fuera del rango de 10 a 50.")