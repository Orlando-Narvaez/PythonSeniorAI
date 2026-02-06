# Acceso y actualización de diccionarios
usuarios = {
    "u001": {"nombre": "Ana", "correo": "ana@mail.com", "roles": ["admin"]},
    "u002": {"nombre": "Pedro", "correo": "pedro@mail.com", "roles": ["cliente"]}
}

# Acceder al nombre de usuario u001
print("Nombre del usuario u001: ", usuarios["u001"]["nombre"])

# Agregar un nuevo rol al usuario u002
usuarios["u002"]["roles"].append("ventas")
print(f"Roles actualizados para u002: {usuarios['u002']['roles']}")

# Agregar un nuevo usuario
usuarios['u003'] = {"nombre": "Carlos", "correo": "carlos@mail.com", "roles": ["comprador"]}
usuarios['u004'] = {"nombre": "Jose", "correo": "jose@mail.com", "roles": ["secretario"]}

# Imprimir los usuarios registrados
print("\nListado de usuarios registrados:")
for id_usuario, valores_usuario in usuarios.items():
    print(f"ID: {id_usuario} - Nombre: {valores_usuario['nombre']} - Correo: {valores_usuario['correo']} - Roles: {', '.join(valores_usuario['roles'])}")
    
    
# Buscar un usuario de acuerdo a su rol
rol = "comprador"
print(f"\nBuscar el rol {rol}")
for id_usuario, valores_usuario in usuarios.items():
    if rol in valores_usuario.get("roles", []):
        print(f"Usuario: {id_usuario} - Nombre: {valores_usuario['nombre']}")