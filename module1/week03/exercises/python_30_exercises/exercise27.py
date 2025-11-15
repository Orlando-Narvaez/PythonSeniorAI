""" 
Ejercicio 27 

Enunciado: 
 Crea un programa que lea dos números enteros positivos a y b y calcule su 
máximo común divisor (MCD) utilizando el algoritmo de Euclides (mediante restas 
sucesivas). 

Competencia que evalúa: 
 Aplicación de algoritmos clásicos, ciclos con condiciones dependientes y 
optimización de iteraciones lógicas.
"""
def calcular_mcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print("El MCD es:", calcular_mcd(10, 2))