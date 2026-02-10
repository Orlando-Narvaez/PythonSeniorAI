"""" 
Ejercicio 5 - Base de datos consolidada ( unión + eliminacion de repetidos)
Dos sucursales registraron clientes:
sucursal1 = {"Carlos", "Maria", "Andres"}
sucursal2 = {"Maria", "Luisa", "Carlos", "Elena"}

Actividad
Crear una base unica de clientes sin duplicados
"""

sucursal1 = {"Carlos", "Maria", "Andres"}
sucursal2 = {"Maria", "Luisa", "Carlos", "Elena"}

base_datos = sucursal1 | sucursal2
print(base_datos)