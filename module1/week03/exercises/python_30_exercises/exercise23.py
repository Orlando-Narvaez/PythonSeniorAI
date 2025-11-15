""" 
Ejercicio 23 

Enunciado: 
 Crea un programa que calcule la suma de los dígitos de un número entero 
positivo (por ejemplo, 1234 → 10). No se permite convertir el número a texto.
 
Competencia que evalúa: 
 Manipulación numérica con divisiones enteras y módulo, y uso de bucles 
controlados por condición para descomposición aritmética."""

while True:
    try:
        n = int(input("Ingresa un número entero positivo: "))
        if n <= 0:
            print("Por favor, ingresa un número entero positivo.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

suma_digitos = 0
while n > 0:
    suma_digitos += n % 10
    n //= 10

print(f"La suma de los dígitos es: {suma_digitos}")