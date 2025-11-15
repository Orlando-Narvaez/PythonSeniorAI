""" 
Ejercicio 13 

Enunciado: 
 Elabora un programa que solicite un número entero positivo y determine si es 
número primo (solo divisible por 1 y por sí mismo). 

Competencia que evalúa: 
 Uso de ciclos con control lógico y operadores módulo para validar divisibilidad y 
optimizar procesos de decisión.
"""

while True:
    try:
        num = int(input("Ingresa un número entero positivo: "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")
    
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"El número {num} no es primo.")
            break
    else:
        print(f"El número {num} es primo.")