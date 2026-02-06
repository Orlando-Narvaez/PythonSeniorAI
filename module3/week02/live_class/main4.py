import os
import sys


class Cliente:
    def _init_(self, cedula, nombre, telefono, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        
    def obtener_resumen(self):
        return f"Cédula: {self.cedula :<10}, Nombre: {self.nombre:<20}, Teléfono: {self.telefono :<12}, Dirección: {self.direccion :<20}"

clientes_db={
    "000":Cliente("000","Cliente Genérico","000-000-0000","N/A"),
    "001":Cliente("001","Juan Pérez","123-456-7890","Calle Falsa 123"),
}

def mostrar_clientes():
    print("\n--- LISTA DE CLIENTES ---")
    print(f"{'CÉDULA':<10} {'NOMBRE':<20} {'TELÉFONO':<12} {'DIRECCIÓN':<20}")
    print("-" * 62)
    for cliente in clientes_db.values():
        print(cliente.obtener_resumen())
    
def registrar_cliente():
    print("\n--- REGISTRAR NUEVO CLIENTE ---")
    ced= input("Cédula: ").strip()
    if ced in clientes_db:
        print("Error: Cédula ya registrada.")
        return
    
    nom=input("Nombre: ").strip()
    tel=input("Teléfono: ").strip()
    dir=input("Dirección: ").strip()
    
    nuevo_cliente=Cliente(ced,nom,tel,dir)
    clientes_db[ced]=nuevo_cliente
    print(f" Cliente '{nom}' registrado exitosamente.")



inventario = {
    "001": {"nombre": "Martillo", "precio": 15.50, "stock": 10},
    "002": {"nombre": "Destornillador", "precio": 5.00, "stock": 20},
    "003": {"nombre": "Taladro", "precio": 85.00, "stock": 4},
    "004": {"nombre": "Llave Inglesa", "precio": 12.00, "stock": 15}
}


factura_actual = []


def limpiar_pantalla():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado_tabla():
    print(f"{'ID':<6} {'NOMBRE':<20} {'PRECIO':<10} {'STOCK':<8}")
    print("-" * 48)



def mostrar_inventario():
    print("\n--- INVENTARIO COMPLETO ---")
    if not inventario:
        print("El inventario está vacío.")
    else:
        mostrar_encabezado_tabla()
        for id_prod, datos in inventario.items():
            print(f"{id_prod:<6} {datos['nombre']:<20} ${datos['precio']:<9.2f} {datos['stock']:<8}")
    print("-" * 48)

def buscar_producto_nombre():
    print("\n--- BUSCAR POR NOMBRE ---")
    termino = input("Ingrese el nombre o parte del nombre a buscar: ").strip().lower()
    
    encontrados = False
    print("\nResultados de búsqueda:")
    mostrar_encabezado_tabla()
    
    
    for id_prod, datos in inventario.items():
        if termino in datos['nombre'].lower():
            print(f"{id_prod:<6} {datos['nombre']:<20} ${datos['precio']:<9.2f} {datos['stock']:<8}")
            encontrados = True
            
    if not encontrados:
        print("No se encontraron productos con ese nombre.")
    print("-" * 48)

def agregar_nuevo_producto():
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    id_prod = input("Ingrese un ID único: ").strip()
    
    if id_prod in inventario:
        print("Error: Ese ID ya existe (use Modificar para cambiar stock).")
    else:
        nombre = input("Nombre del producto: ").strip()
        try:
            precio = float(input("Precio unitario: "))
            stock = int(input("Stock inicial: "))
            
            inventario[id_prod] = {
                "nombre": nombre,
                "precio": precio,
                "stock": stock
            }
            print(f" Producto '{nombre}' creado exitosamente.")
        except ValueError:
            print("Error: Precio y Stock deben ser números.")

def modificar_producto():
    print("\n--- MODIFICAR PRODUCTO ---")

    mostrar_inventario()
    
    id_prod = input("Ingrese el ID del producto a modificar: ").strip()
    
    if id_prod in inventario:
        prod = inventario[id_prod]
        print(f"\nProducto seleccionado: {prod['nombre']} (Stock: {prod['stock']} | Precio: ${prod['precio']})")
        print("1. Agregar Unidades (Aumentar Stock)")
        print("2. Cambiar Precio")
        print("3. Cancelar")
        
        op_mod = input("Seleccione una opción: ")
        
        try:
            match op_mod:
                case "1":
                    cantidad = int(input("¿Cuántas unidades desea agregar?: "))
                    if cantidad > 0:
                        prod['stock'] += cantidad
                        print(f"Stock actualizado. Nuevo total: {prod['stock']} unidades.")
                    else:
                        print("La cantidad debe ser positiva.")
                case "2":
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    if nuevo_precio >= 0:
                        prod['precio'] = nuevo_precio
                        print(f"Precio actualizado a ${prod['precio']:.2f}")
                    else:
                        print(" El precio no puede ser negativo.")
                case "3":
                    print("Operación cancelada.")
                case _:
                    print("Opción no válida.")
        except ValueError:
            print("Error: Ingrese datos numéricos válidos.")
    else:
        print("Producto no encontrado.")

def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")
    id_prod = input("Ingrese el ID del producto a eliminar: ").strip()
    
    if id_prod in inventario:
        print(f"Va a eliminar: {inventario[id_prod]['nombre']}")
        confirmacion = input("¿Está seguro? Esta acción no se puede deshacer (s/n): ").lower()
        
        if confirmacion == 's':
            eliminado = inventario.pop(id_prod)
            print(f"Producto '{eliminado['nombre']}' eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("ID no encontrado.")

def vender_producto():
    print("\n--- VENTA DE PRODUCTOS ---")
    
    buscar = input("¿Desea buscar el ID por nombre antes? (s/n): ").lower()
    if buscar == 's':
        buscar_producto_nombre()
    
    id_prod = input("Ingrese el ID del producto a vender: ").strip()
    
    if id_prod in inventario:
        prod = inventario[id_prod]
        try:
            print(f"Producto: {prod['nombre']} | Disponible: {prod['stock']}")
            cantidad = int(input("Cantidad a vender: "))
            
            if 0 < cantidad <= prod['stock']:
                subtotal = cantidad * prod['precio']
                prod['stock'] -= cantidad
                
                
                factura_actual.append({
                    "nombre": prod['nombre'],
                    "cantidad": cantidad,
                    "precio": prod['precio'],
                    "subtotal": subtotal
                })
                print(f"Agregado al carrito: ${subtotal:.2f}")
            else:
                print("Cantidad inválida o stock insuficiente.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    else:
        print("Producto no encontrado.")

def generar_factura():
    print("\n" + "="*40)
    print("      FERRETERÍA 'EL TORNILLO FELIZ'")
    print("          FACTURA DE VENTA")
    print("="*40)
    
    if not factura_actual:
        print("No hay items en la factura actual.")
    else:
        total = 0
        print(f"{'CANT':<5} {'ARTICULO':<20} {'UNIT':<8} {'SUBTOTAL':<10}")
        print("-" * 45)
        for item in factura_actual:
            print(f"{item['cantidad']:<5} {item['nombre']:<20} ${item['precio']:<7.2f} ${item['subtotal']:<9.2f}")
            total += item['subtotal']
        print("-" * 45)
        print(f"TOTAL A PAGAR: ${total:.2f}")
        print("="*40)
        
        if input("\n¿Confirmar pago y cerrar venta? (s/n): ").lower() == 's':
            factura_actual.clear()
            print("Venta finalizada. Gracias por su compra.")


def main():
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE FERRETERÍA ===")
        print("1. Mostrar Inventario Completo")
        print("2. Buscar Producto por Nombre")
        print("3. Vender (Agregar a Factura)")
        print("4. Generar Factura / Cerrar Venta")
        print("-" * 30)
        print("5. Agregar NUEVO Producto")
        print("6. Modificar Producto (Stock/Precio)")
        print("7. Eliminar Producto")
        print("8. Salir")
        
        opcion = input("\n>> Seleccione una opción: ")
        
        match opcion:
            case "1": mostrar_inventario()
            case "2": buscar_producto_nombre()
            case "3": vender_producto()
            case "4": generar_factura()
            case "5": agregar_nuevo_producto()
            case "6": modificar_producto()
            case "7": eliminar_producto()
            case "8": 
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida.")
        
        input("\n[Presione ENTER para continuar...]")
        limpiar_pantalla()

if _name_ == "_main_":
    if sys.version_info < (3, 10):
        print("Error: Se requiere Python 3.10 o superior para ejecutar este programa.")
    else:
        main()