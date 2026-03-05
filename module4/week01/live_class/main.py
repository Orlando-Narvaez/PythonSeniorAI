"""
f = open("datos.txt", "r")
file1 = open("datos.txt", "w")
file2 = open("datos.txt", "a")
file3 = open("datos.txt", "r+")

with open("datos.txt", "r", encoding= "utf-8") as f:
    contenido = f.read()
"""

# Metodo de lectura
with open("letras.txt", "w", encoding="utf-8") as f:
    f.write("A\n")
    f.write("B\n")
    f.write("C\n")
    f.write("D\n")
    
with open("letras.txt", "r", encoding="utf-8") as f:
    print(f.read())
    
# Metodo .readline() para leer una linea a la vez
with open("letras.txt", "r", encoding="utf-8") as f:
    print(f.readline())
    
# Metodo .readline() imprime una lista de elementos contenidos en el archivo
with open("letras.txt", "r", encoding="utf-8") as f:
    print(f.readlines())
    
# Convencion 
# Nombre|Apellido|Edad
# Orlando|Narvaez|26

# Arquitectura minima para manejo de archivos
# Presentacion -> Interaccion con el usuario
# Servicio -> Modelo/reglas de negocio
# Repositorio -> Acceso a los datos
# Infraestructura -> Archivos fisicos
# Modelo/esquema -> Datos


# Super software

"""
1. FileManager (infraestructura segura)
2. Modelo Task (serialización)
3. Repository (persistencia desacoplada)
4. Service (reglas de negocio + validación)
5. main (interfaz consola)
"""

# ToDo List

"""
    ## Estándares de calidad

| Norma                 | Aplicación                      |
| --------------------- | ------------------------------- |
| PEP8                  | nombres, longitud, imports      |
| DRY                   | no repetir lógica de archivo    |
| KISS                  | funciones pequeñas              |
| SRP                   | cada función hace una sola cosa |
| Fail Fast             | validar antes de guardar        |
| Defensive Programming | proteger el archivo             |
| Idempotencia          | leer no modifica estado         |
| Encapsulación         | no acceder directo al archivo   |
| Tipado fuerte         | typing obligatorio              |

"""