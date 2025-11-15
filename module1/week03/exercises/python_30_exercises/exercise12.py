""" 
Ejercicio 12 

Enunciado: 
 Desarrolla un programa que calcule el salario final de un trabajador.  El usuario ingresa: 
●  Horas trabajadas  
●  Valor por hora  Si trabaja más de 40 horas, las horas extras se pagan al 150% del valor 
normal.  

Competencia que evalúa: 
 Aplicación de estructuras condicionales y operadores aritméticos para resolver un 
problema real con condiciones de cálculo variables.
"""

valor_hora = 6770

while True:
    try:    
        horas = float(input("Ingresa las horas trabajadas: "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

if horas > 40:
    extras = horas-40
    pago = (40*valor_hora) + (extras*(valor_hora*1.5))
    print(f"El pago por horas extras es de: {extras*(valor_hora*1.5)} y el pago total es de: {pago}")
else:
    pago = horas*valor_hora
    print(f"El pago total es de: {pago}")
