""" 
Ejercicio 1 

Enunciado: 
 Crea un programa que solicite el peso (kg) y la altura (m) de una persona, calcule el 
Índice de Masa Corporal (IMC) y muestre un mensaje según el resultado: 
●  Menor a 18.5: Bajo peso  
●  Entre 18.5 y 24.9: Normal  
●  Entre 25 y 29.9: Sobrepeso  
●  30 o más: Obesidad  

Competencia que evalúa: 
 Aplicación de condicionales anidados y operadores relacionales para clasificar 
datos numéricos.
"""

while True:
    try:
        entrada_peso = input("Ingrese su peso en kilogramos (kg): ")
        peso = float(entrada_peso)
        
        if peso < 0:
            print("El peso no puede ser menor a 0, intentelo de nuevo por favor\n")
            continue
        break
    except ValueError:
        print("Entrada no válida. Intente de nuevo. \n")
        
while True:
    try:
        entrada_altura = input("Ingrese su altura en metros (m): ")
        altura = float(entrada_altura)
        
        if altura < 0:
            print("La altura no puede ser menor a 0, intentelo de nuevo por favor\n")
            continue
        break
    except ValueError:
        print("Entrada no válida. Intente de nuevo. \n")
        
imc = peso / (altura**2)

if imc < 18.5:
    print("bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("normal")
elif imc >= 25 and imc <= 29.9:
    print("sobrepeso")
else:
    print("obesidad")