from conexion import conectar

#Este metodo funciona como un INSERT dentro de la base de datos para crear un NUEVO alumno
def crear_alumno(nombre, email, programa_id):

    if not nombre.strip() or not email.strip():
        print("Nombre o Email no pueden tener espacios o estar vacíos")

    if not nombre or not email:
        print("Nombre y Email son ablogatorios")
        return
    
    if "@" not in email or "." not in email:
        print("Email Inválido")
        return
    
    conn = conectar()

    if conn is None:
        print("No hay conexion a la base de datos")
        return

    cursor = conn.cursor()

    try: 

        cursor.execute("SELECT id FROM programas WHERE id = %s", (programa_id,))
        programa = cursor.fetchone

        if programa is None:
            print("El programa no existe")
            return

        cursor.execute(
            "INSERT INTO alumnos (nombre, email, programa_id) VALUES (%s, %s, %s)",
            (nombre, email, programa_id)
        )
        conn.commit()
        print("Alumno registrado")

    except Exception as e:
        if "duplicate key" in str(e):
            print("Ya existe un alumno con ese email: ", e)
        else:
            print("Error al crear alumno: ", e)

    finally:
        cursor.close()
        conn.close()
    
#Este metodo funciona para ELIMINAR estudiantes validando su ID dentro de la base de datos
def elimnar_alumno(id_alumno):
    conn = conectar()

    if conn is None:
        print("No hay conexion")
        return
    cursor = conn.cursor()

    try: 

        if not isinstance(id_alumno, int):
            print("El ID debe ser un número")
            return
        
        cursor.execute("SELECT id FROM alumnos WHERE id = %s", (id_alumno,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("No existe un alumno con ese ID")
            return
        
        confirmar = input("Seguro quieres eliminar este usuario? (s/n): ")
        if confirmar.lower() != "s":
            print("Operación cancelada")
            return
        

        cursor.execute(
            "DELETE FROM alumnos WHERE id = %s",
            (id_alumno,)
        )

       
        conn.commit()
        print("Alumno eliminado correctamente")

    except Exception as e:
        print("Error al eliminar alumno: ", e)

    finally:
        cursor.close()
        conn.close()

