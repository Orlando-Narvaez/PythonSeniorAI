""" 
Ejercicio 10 

Enunciado: 
 Realiza un programa que muestre todos los números del 1 al 100 y al final indique 
cuántos de ellos son múltiplos de 3. 

Competencia que evalúa: 
 Uso de ciclos con contador, operaciones aritméticas y condicionales para 
acumulación de resultados.
"""
contador = 0
for i in range(1,101):
    print(i)
    if i%3 == 0:
        contador=contador+1
    
print(f"Hay {contador} números múltiplos de 3 entre 1 y 100.")