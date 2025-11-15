"""
Ejercicio 29 

Enunciado: 
 Escribe un programa que pida un número entero y determine si es un número 
Armstrong. Un número es Armstrong si la suma de sus dígitos elevados al número 
de dígitos es igual al mismo número (por ejemplo, 153 → 1³ + 5³ + 3³ = 153). 

Competencia que evalúa: 
 Razonamiento aritmético avanzado, control de bucles, uso del operador potencia y 
validación de igualdad compleja. 
"""
def es_numero_armstrong(numero):
    num_str = str(numero)
    num_digitos = len(num_str)
    suma = 0

    for digito in num_str:
        suma += int(digito) ** num_digitos

    return suma == numero

try:
    numero = int(input("Ingresa un número entero: "))
    if numero < 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        if es_numero_armstrong(numero):
            print(f"{numero} es un número Armstrong.")
        else:
            print(f"{numero} no es un número Armstrong.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")

