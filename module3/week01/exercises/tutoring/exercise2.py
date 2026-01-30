def agregar_notas(asignaturas) -> list:
    for asignatura in asignaturas:
        asignatura["notas"] = float(input(f"Ingrese la nota para {asignatura['nombre']}: "))
    print("Notas agregadas con éxito.")
    return asignaturas

def evaluar_asignaturas(asignaturas) -> list:
    asignaturas_perdidas = []
    for asignatura in asignaturas:
        if asignatura["notas"] < 3:
            asignaturas_perdidas.append(asignatura)
    return asignaturas_perdidas

def mostrar_asignaturas(asignaturas_perdidas) -> None:
    if not asignaturas_perdidas:
        print("¡Felicidades! No hay asignaturas que repetir.")
        return    
    print("Asignaturas que debe repetir: ")
    for i, asignatura in enumerate(asignaturas_perdidas, start=1):
        print(f"{i}. {asignatura['nombre']} con nota de {asignatura['notas']}")
    
def main():
    asignaturas = [{"nombre": "Matematicas"}, 
               {"nombre": "Fisica"}, 
               {"nombre": "Quimica"}, 
               {"nombre": "Historia"}, 
               {"nombre": "Lengua"}
    ]
    
    agregar_notas(asignaturas)
    asignaturas_perdidas = evaluar_asignaturas(asignaturas)
    mostrar_asignaturas(asignaturas_perdidas)
    
if __name__ == "__main__":
    main()