""" 
Ejercicio 7 

Enunciado: 
 Crea un programa que pida al usuario un número y muestre si es positivo, 
negativo o igual a cero. 

Competencia que evalúa: 
 Aplicación de operadores relacionales y condicionales para clasificación numérica.
"""

while True:
    try:
        num = float(input("Ingresa un numero: "))
        break
    except ValueError:
        print("Por favor ingresa un número válido.")
        
if num == 0:
    print("El número es igual a cero.")
elif num > 0:
    print("El número es positivo.")
else:
    print("El número es negativo.")