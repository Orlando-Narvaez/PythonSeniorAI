""" 
Ejercicio 8 

Enunciado: 
 Diseña un programa que solicite al usuario un número entero y muestre su tabla de 
multiplicar del 1 al 10. 

Competencia que evalúa: 
 Uso de ciclos for o while para generar secuencias controladas
"""

while True:
    try:
        num = int(input("Ingresa un número entero: "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
    