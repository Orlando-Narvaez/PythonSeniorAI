""" 
Ejercicio 4 

Enunciado: 
 Desarrolla un programa que solicite al usuario el valor de una compra y calcule el 
total a pagar aplicando un descuento del 10% si el valor supera los $100 000. 

Competencia que evalúa: 
 Comprensión de operadores aritméticos y condicionales simples para aplicar reglas 
de negocio.
"""

while True:
    try:
        valor_compra = float(input("Ingrese el valor de la compra: "))
        break
    except ValueError:
        print("Por favor ingrese un valor numérico válido.\n")
    
if valor_compra >= 100000:
    valor_pagar = valor_compra - (valor_compra * 0.1)
    print(f"Se ha aplicado un descuento del 10%. El valor total a pagar es: ${valor_pagar:,.2f}")
else:
    valor_pagar = valor_compra
    print(f"No se ha aplicado ningún descuento. El valor total a pagar es: ${valor_pagar:,.2f}")