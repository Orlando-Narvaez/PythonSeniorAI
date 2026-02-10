"""  
Ejercicio 1 - Eliminiar datos duplicados
una tienda registro varias veces el mismo producto en el sistema:
productos = ["pan", "leche", "huevos", "pan", "leche", "pan"]

Actividad
1. Convierte la lista en un set
2. Muetsra los productos unicos
3. Indica cuantos productos diferentes existen
"""

productos = ["pan", "leche", "huevos", "pan", "leche", "pan"]

# 1. Convierte la lista en un set
productos_unicos = set(productos)

# 2. Muetsra los productos unicos
print(f"Productos únicos: {productos_unicos}")

# 3. Indica cuantos productos diferentes existen
cantidad_productos_diferentes = len(productos_unicos)
print(f"Cantidad de productos diferentes: {cantidad_productos_diferentes}")