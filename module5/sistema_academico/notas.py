from conexion import conectar

def actualizar_nota(id_alumno, nota):
    if nota < 0 or nota > 5:
        print("Nota invalida: (0 a 5)")
        return
    
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE alumnos SET nota = %s WHERE id = %s",
            (nota, id_alumno)
        )
        conn.commit()
        print("Nota actualizada")
    except Exception as e:
        print("Error: ", e)

    finally:
        cursor.close()
        conn.close()
