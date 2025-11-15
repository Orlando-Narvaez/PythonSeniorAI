""" 
2. Clasificador de notas

Descripción: El usuario ingresa una nota de 0 a 100. Mostrar el nivel académico según el puntaje.

| Rango  | Mensaje   |
| ------ | ----------|
| 90–100 | Excelente |
| 70–89  | Aprobado  |
| 0–69   | Reprobado |
"""

nota = float(input("Ingresa una nota entre 0 a 100: "))

if 0 <= nota <= 69:
    print("Reprobado")
elif 70 <= nota <= 89:
    print("Aprobado")
elif 90 <= nota <= 100:
    print("Excelente")
else:
    print("Nota inválida")