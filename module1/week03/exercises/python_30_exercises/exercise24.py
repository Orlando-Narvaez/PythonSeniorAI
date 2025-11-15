""" 
Ejercicio 24 

Enunciado: 
 Elabora un programa que solicite un número entero positivo y determine si es un 
número perfecto, es decir, si la suma de sus divisores propios (excluyendo el 
número mismo) es igual al número. 

Competencia que evalúa: 
 Implementación de ciclos anidados, divisibilidad, acumuladores y validación de 
condiciones lógicas complejas.
"""

while True:
    try:
        n = int(input("Ingresa un número entero positivo: "))
        if n <= 0:
            print("Por favor, ingresa un número entero positivo.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")
        

suma_divisores = 0
for i in range(1, n):
    if n % i == 0:
        suma_divisores += i
if suma_divisores == n:
    print(f"{n} es un número perfecto.")
else:
    print(f"{n} no es un número perfecto.")