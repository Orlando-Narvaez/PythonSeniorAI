"""
Ejercicio 21 

Enunciado: 
 Crea un programa que solicite dos números enteros y determine si el segundo es 
múltiplo exacto del primero. Si no lo es, el programa debe indicar cuántas unidades 
faltan para que lo sea. 

Competencia que evalúa: 
 Uso combinado de operadores módulo, condicionales y aritmética para verificar y 
calcular relaciones numéricas. """

while True:
    try:
        num1 = int(input("Ingresa el primer número entero: "))
        num2 = int(input("Ingresa el segundo número entero: "))
        break
    except ValueError:
        print("Por favor, ingresa números enteros válidos.")    

if num2 % num1 == 0:
    print(f"{num2} es múltiplo exacto de {num1}.")
else:
    faltan = num1 - (num2 % num1)
    print(f"{num2} no es múltiplo exacto de {num1}. Faltan {faltan} unidades para que lo sea.")