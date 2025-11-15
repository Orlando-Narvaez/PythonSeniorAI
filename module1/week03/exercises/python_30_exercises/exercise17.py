""" 
Ejercicio 17 

Enunciado: 
 Crea un programa que calcule la potencia de un número base elevado a un 
exponente n sin usar el operador **. Debes usar un ciclo para realizar el cálculo 
multiplicativo. 

Competencia que evalúa: 
 Construcción de algoritmos iterativos con acumuladores y comprensión de 
multiplicación sucesiva controlada.
"""

while True:
    try:
        x = int(input("Ingresa un número base: "))
        y = int(input("Ingresa un número exponente: "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

acomulador = x

for i in range(1,y):
    acomulador = acomulador*x
    
print(f"El resultado de {x}^{y} es: {acomulador}")