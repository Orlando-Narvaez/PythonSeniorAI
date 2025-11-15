""" 
Ejercicio 22 

Enunciado: 
 Desarrolla un programa que pida al usuario un número entero positivo n y muestre 
todos los números del 1 al n, indicando junto a cada uno si es par o impar. 

Competencia que evalúa: 
 Uso de ciclos con validación condicional y salida controlada para análisis 
secuencial de valores numéricos."""

while True:
    try:
        n = int(input("Ingresa un número entero positivo: "))
        if n <= 0:
            print("Por favor, ingresa un número entero positivo.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} es par.")
    else:
        print(f"{i} es impar.")
