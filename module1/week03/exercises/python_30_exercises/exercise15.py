""" 
Ejercicio 15 

Enunciado: 
 Crea un programa que simule una calculadora con un menú interactivo que 
permita realizar suma, resta, multiplicación y división. El programa debe repetirse 
hasta que el usuario elija la opción “Salir”. 

Competencia que evalúa: 
 Uso de bucles controlados por condición, estructuras de selección múltiple y 
manejo de menús interactivos básicos. 
"""

opcion = None
operaciones = 0

while opcion != 5:
    print("Bienvenido a la calculadora ")
    print("Selecciona la operacion que deseas realizar:")
    print("Opcion 1: suma")
    print("Opcion 2: resta")
    print("Opcion 3: multiplicacion")
    print("Opcion 4: division")
    print("Opcion 5: salir\n\n")
    
    opcion = int(input("Ingrese la opcion: "))
    
    if opcion == 5:
        print(f"Saliendo fue un gusto ayudarte con {operaciones} operaciones aritmeticas")
        break
    if opcion < 1 or opcion > 5:
        print("Opcion incorrecta solo puedes ingresar la opcion 1,2,3,4 y 5")
        continue
    
    num1 = int(input("Ingrese el primero numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    
    if opcion == 1:
        resultado = num1+num2
        print(f"El resultado de la suma es: {resultado}")
        operaciones= operaciones+1
    elif opcion == 2:
        resultado = num1-num2
        print(f"El resultado de la resta es: {resultado}")
        operaciones= operaciones+1
    elif opcion == 3:
        resultado = num1*num2
        print(f"El resultado de la multiplicacion es: {resultado}")
        operaciones= operaciones+1
    else:
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
            continue
        resultado = num1/num2
        print(f"El resultado de la division es: {resultado}")
        operaciones= operaciones+1
    
     