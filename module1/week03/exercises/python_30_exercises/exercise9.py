""" 
Ejercicio 9 

Enunciado: 
 Elabora un programa que pida al usuario un número y determine si es par o impar. 
 
Competencia que evalúa: 
 Uso del operador módulo (%) y condicionales simples para validación aritmética.
"""
while True:
    try:
        num = int(input("Ingresa un número entero: "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
        
resultado = num%2

if resultado == 0:
    print("El número es par.")
else: 
    print("El número es impar.")