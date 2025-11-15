""" 
Ejercicio 5 

Enunciado: 
 Crea un programa que lea la edad de una persona y determine si puede votar 
(mayor o igual a 18 años), si debe presentar tarjeta de identidad (entre 7 y 17 años), 
o si es menor para tener documento. 

Competencia que evalúa: 
 Uso de estructuras if, elif, else para manejar condiciones múltiples con 
intervalos numéricos.
"""

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Por favor ingrese un número válido.")

if edad >= 18:
    print("Puede votar")
elif edad >= 7:
    print("Debe presentar tarjeta de identidad")
else:
    print("Es menor para tener documento")