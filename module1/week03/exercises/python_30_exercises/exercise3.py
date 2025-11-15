""" 
Ejercicio 3 

Enunciado: 
 Realiza un programa que solicite tres números al usuario y determine cuál es el 
mayor y cuál es el menor. 

Competencia que evalúa: 
 Uso de condicionales compuestos y operadores lógicos para comparar múltiples 
valores.
"""

while True:
    try: 
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        num3 = int(input("Ingrese el tercer numero: "))
        break
    except ValueError:
        print("Tienen que ser numeros")
 
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"El numero mayor es {num1} y el menor es {num3}")
    else:
        print(f"El numero mayor es {num1} y el menor es {num2}")
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"El numero mayor es {num2} y el menor es {num3}")
    else:
        print(f"El numero mayor es {num2} y el menor es {num1}")
else:
    if num1 > num2:
        print(f"El numero mayor es {num3} y el menor es {num2}")
    else:
        print(f"El numero mayor es {num3} y el menor es {num1}")