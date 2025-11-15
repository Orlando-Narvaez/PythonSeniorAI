""" 
Ejercicio 16 

Enunciado: 
 Escribe un programa que pida un número entero y calcule la suma de todos los 
números pares desde 1 hasta ese número. 

Competencia que evalúa: 
 Uso de ciclos y operadores lógicos para acumulación condicional dentro de un 
rango numérico. 
"""

while True:
    try:
        n = int(input("Ingresa un número entero positivo: "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

suma = 0
        
for i in range(1,n+1):
    if i%2 == 0:
        print(f"{i} es par por lo tanto {suma} + {i} = {suma+i}")
        suma = suma + i
        
print(f"La suma de todos los pares hasta el numero {n} es: {suma}")
        
    