"""   
Ejercicio 2 - Verificar acceso (operador in )
Un sistema tiene usuarios autorizados:
usuarios_autorizados = {"ana", "carlos", "maria", "pedro"}
El programa debe pedir nombre y decir si puede entrar o no

Actividad
1 Solicitar nombre con input
2 Indicar si pertenece al conjunto
Que debe aprender el estudiante: Los sets permiten busquedas extremadamente rapidas (mejor que lista)
"""

usuarios_autorizados = {"ana", "carlos", "maria", "pedro"}

# 1 Solicitar nombre con input
nombre = input("Ingrese el nombre: ").strip().lower()

# 2 Indicar si pertenece al conjunto
pertenece = nombre in usuarios_autorizados
print(f"¿El usuario {nombre} tiene acceso? ", end="")
print("Sí" if pertenece else "No")