""" 
Ejercicio 28 

Enunciado: 
 Desarrolla un programa que genere un patrón numérico en forma de triángulo 
rectángulo. El usuario ingresa un número n y el programa imprime líneas del 1 hasta 
n, repitiendo el número según la línea.  Ejemplo para n = 4: 
1   
22   
333   
4444
"""
def generar_triangulo(n):
    for i in range(1, n + 1):
        print(str(i) * i)
        
n = int(input("Ingrese un número: "))
generar_triangulo(n)