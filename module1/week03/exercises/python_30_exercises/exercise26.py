""" 
Ejercicio 26 

Enunciado: 
 Diseña un programa que permita calcular el mínimo común múltiplo (MCM) de 
dos números enteros positivos mediante sumas sucesivas. 

Competencia que evalúa: 
 Comprensión de operaciones matemáticas iterativas, control de bucles y 
razonamiento lógico para alcanzar una condición de coincidencia. 
"""
def calcular_mcm(num1, num2):
    multiplo1 = num1
    multiplo2 = num2

    while multiplo1 != multiplo2:
        if multiplo1 < multiplo2:
            multiplo1 += num1
        else:
            multiplo2 += num2

    return multiplo1

print("El MCM es:", calcular_mcm(4, 2))