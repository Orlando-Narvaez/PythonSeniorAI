"""  
Slicing: 
    Dada la lista:
    
    empleados = ["Ana", "Luis", "Carlos", "Marta", "Diana"]
    
    Hacer:
    
    1. Extrae los elementos desde “Luis” hasta “Marta” (inclusive).
    2. Extrae los elementos excluyendo el primero y el último.
"""

empleados = ["Ana", "Luis", "Carlos", "Marta", "Diana"]

# 1. Extrae los elementos desde “Luis” hasta “Marta” (inclusive).
sublista1 = empleados[1:4]

# 2. Extrae los elementos excluyendo el primero y el último.
sublista2 = empleados[1:-1]

print("Elementos desde 'Luis' hasta 'Marta':", sublista1)
print("Elementos excluyendo el primero y el último:", sublista2)