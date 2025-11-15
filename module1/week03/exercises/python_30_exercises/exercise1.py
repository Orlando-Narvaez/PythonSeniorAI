""" 
Ejercicio 1 

Enunciado: 
 Diseña un programa que reciba una cantidad de dinero e indique cuántos billetes 
de 50 000, 20 000, 10 000, 5 000, 2 000 y 1 000 se necesitan para completar esa 
suma, utilizando la menor cantidad posible de billetes. 

Competencia que evalúa: 
 Uso de operadores aritméticos (división y módulo) y aplicación de condicionales 
para resolver problemas de descomposición numérica. 
"""

while True:
    entrada = input("Ingrese la cantidad de dinero en pesos colombianos (sin puntos ni comas): ")
    try:
        monto = int(entrada)
        if monto < 0:
            print("La entrada no puede ser menor a 0, intentelo de nuevo por favor\n")
            continue
        if monto > 0 and monto < 1000:
            print(" Solo se admiten billetes, no te podemos dar monedas ingrese una cantidad correcta\n")
            continue
        break
    except ValueError:
        print("\n\nEntrada no válida. Intente de nuevo. \n\n")

billete50 = 50000
cantidad50 = monto//billete50
monto = monto%billete50

billete20 = 20000
cantidad20 = monto//billete20
monto = monto%billete20

billete10 = 10000
cantidad10 = monto//billete10
monto = monto%billete10

billete5 = 5000
cantidad5 = monto//billete5
monto = monto%billete5

billete2 = 2000
cantidad2 = monto//billete2
monto = monto%billete2

billete1 = 1000
cantidad1 = monto//billete1

print(f"Para entregar la cantidad de {entrada} se encesitan {cantidad50} billetes de 50000, {cantidad20} billetes de 20000, {cantidad10} billetes de 10000, {cantidad5} billetes de 5000, {cantidad2} billetes de 2000 y {cantidad1} billetes de 1000.")