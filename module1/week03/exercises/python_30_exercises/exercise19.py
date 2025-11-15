""" 
Ejercicio 19 

Enunciado: 
 Crea un programa que simule un contador regresivo desde un número n hasta 0, 
mostrando un mensaje al final que diga “¡Despegue!”. 

Competencia que evalúa: 
 Aplicación de ciclos while con decremento controlado y manejo de condiciones de 
salida.
"""
import time

while True:
    try:
        x = int(input("Ingresa la cantidad de segundos que se tardara en despegar: "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")
        
while x != 0: 
    print(x)
    time.sleep(2)
    x = x-1

print("¡Despegue!")