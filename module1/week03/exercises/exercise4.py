""" 
4. Verificar hora del día

Descripción: Pedir la hora (0 a 23) e indicar si es mañana, tarde o noche.
"""

hora = int(input("Por favor, ingrese la hora (0-23): "))

if 0 <= hora < 12:
    print("Es de mañana")
elif 12 <= hora < 18:
    print("Es de tarde")
elif 18 <= hora < 24:
    print("Es de noche")
else:
    print("Hora inválida")