mi_set = set()
frutas = {"pera", "manzana", "banano"}

# conversion de lista a set
numeros = [1, 2, 3, 4, 5]
conversion = set(numeros)
print(conversion)

frutas = {"pera", "manzana", "banano"}
frutas.add("uva")
print(frutas)

frutas.update(["kiwi", "mango"])
print(frutas)

frutas.discard("pera")
print(frutas)

#frutas.remove("pera")  # Esto generará un error porque "pera" ya fue eliminada
print(frutas)

frutas.clear()
print(frutas)

# Operaciones con sets
# Unión
# Intersección
# Diferencia
# Diferencia simétrica

a = {1, 2, 3}
b = {3, 4, 5}

print("Unión")
print(a | b)  # Unión

print("Intersección")
print(a & b)  # Intersección

print("Diferencia")
print(a - b)  # Diferencia

print("Diferencia simétrica")
print(a ^ b)  # Diferencia simétrica

# Validacion de elementos con set
usuarios = {"Maryan", "Pablo", "Ignacio"}
print("Maryan" in usuarios)  # True
print("Juan" in usuarios)    # False