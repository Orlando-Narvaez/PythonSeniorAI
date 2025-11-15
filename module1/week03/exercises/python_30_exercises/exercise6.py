""" 
Ejercicio 6 

Enunciado: 
 Escribe un programa que simule un intento de acceso con contraseña. El usuario 
tendrá tres intentos para escribir la clave correcta. Si la acierta antes de agotar los 
intentos, el programa muestra un mensaje de éxito; si no, muestra “Acceso 
bloqueado”. 

Competencia que evalúa: 
 Control de ciclos con contador y validación de condiciones combinadas.
"""

contrasena = "hola1"
contador = 0

for contador in range(3):
    intento = input("Ingrese la contraseña: ")
    if intento == contrasena:
        print("Acceso concedido")
        break
    else:
        print(f"Contraseña incorrecta le quedan {2 - contador} intentos")
        contador += 1
        if contador == 3:
            print("Acceso bloqueado")
            break