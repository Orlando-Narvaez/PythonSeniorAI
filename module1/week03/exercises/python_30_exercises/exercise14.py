""" 
Ejercicio 14 

Enunciado: 
 Diseña un programa que muestre los primeros n términos de la serie de 
Fibonacci, donde n es un número entero ingresado por el usuario. 

Competencia que evalúa: 
 Aplicación de ciclos con variables acumuladoras y comprensión de relaciones 
recursivas sin uso de funciones.
"""

while True:
    try:
        n = int(input("Ingresa un número entero positivo: "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")
        
a = 0
b = 1
print(f"F(0) = {a}")
print(f"F(1) = {b}")
        
for i in range(2, n+1):
    fibo = a + b
    print(f"F({i}) = {a} + {b} = {fibo}")
    a = b
    b = fibo
