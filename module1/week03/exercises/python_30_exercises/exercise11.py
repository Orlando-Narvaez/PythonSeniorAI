""" 
Ejercicio 11 

Enunciado: 
 Crea un programa que lea tres números diferentes y determine si pueden formar los 
lados de un triángulo. Si es posible, indica qué tipo de triángulo es: 
●  Equilátero (tres lados iguales)  
●  Isósceles (dos lados iguales)  
●  Escaleno (todos diferentes)  

Competencia que evalúa: 
 Uso de condicionales anidados, operadores lógicos y validación de relaciones 
numéricas para clasificar casos múltiples.
"""

while True:
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        num3 = float(input("Ingresa el tercer número: "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingresa números válidos.")

if num1 == num2 and num1 == num3:
    print("Los números forman un triángulo equilátero.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Los números forman un triángulo isósceles.")
else:
    print("Los números forman un triángulo escaleno.")