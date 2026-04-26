from alumnos import crear_alumno, elimnar_alumno
from programas import crear_programa, listar_programas
from notas import actualizar_nota
from consultas import listar_alumnos_con_programa

def menu():
    while True:
        print("\n SISTEMA ACADÉMICO")
        print("1. Crear programa")
        print("2. Ver programa")
        print("3. Crear alumno")
        print("4. Ver alumnos")
        print("5. Actualizar nota")
        print("6. Eliminar estudiante")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del programa: ")
            crear_programa(nombre)

        elif opcion == "2":
            listar_programas()

        elif opcion == "3":
            nombre = input("Nombre: ")
            email = input("Email: ")
            programa_id = int(input("ID programa: "))
            crear_alumno(nombre, email, programa_id)

        elif opcion == "4":
            listar_alumnos_con_programa()

        elif opcion == "5":
            id_alumno = int(input("ID alumno: "))
            nota = float(input("Nota: "))
            actualizar_nota(id_alumno, nota)

        elif opcion == "6":
            try:

                id_alumno = int(input("ID del alumno a eliminar: "))
                elimnar_alumno(id_alumno)
            except ValueError:
                print("Debes ingresar un número válido")
            
        elif opcion == "7":
            break

        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()