""" 
Ejercicio 18 

Enunciado: 
 Desarrolla un programa que lea un número entero y determine la cantidad de 
dígitos que tiene. 

Competencia que evalúa: 
 Uso de divisiones enteras y ciclos while para análisis numérico y control de 
iteraciones según valor residual.
"""

while True:
    try:
        x = int(input("Ingresa un número entero: "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")
        
digitos = 0

while x != 0:
    x = x//10
    digitos = digitos+1
    
print(f"El numero {x} tiene {digitos} digitos.")