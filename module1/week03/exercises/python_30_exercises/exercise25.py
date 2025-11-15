""" 
Ejercicio 25 

Enunciado: 
 Desarrolla un programa que calcule la media aritmética de una cantidad 
desconocida de números ingresados por el usuario. El proceso termina cuando el 
usuario ingrese el número 0, el cual no debe incluirse en el cálculo. 

Competencia que evalúa: 
 Control de flujo con condición de salida, manejo de acumuladores y contadores, y 
validación de entrada dinámica.
"""

def calcular_media():
    suma = 0
    contador = 0

    while True:
        try:
            numero = float(input("Ingrese un número (0 para terminar): "))
            if numero == 0:
                break
            suma += numero
            contador += 1
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    if contador == 0:
        print("No se ingresaron números para calcular la media.")
    else:
        media = suma / contador
        print(f"La media aritmética es: {media}")

calcular_media()