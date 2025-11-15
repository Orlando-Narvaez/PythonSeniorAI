"""
Ejercicio 20 

Enunciado: 
 Escribe un programa que solicite una cantidad n y calcule el factorial de ese 
número (n!), es decir, el producto de todos los números enteros desde 1 hasta n. 

Competencia que evalúa: 
 Implementación de ciclos con acumuladores y comprensión de patrones 
matemáticos iterativos."""
 
while True:
    try:
        n = int(input("Ingresa un número para calcular su factorial: "))
        if n < 0:
            print("Por favor, ingresa un número entero no negativo.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"El factorial de {n} es {factorial}.")