from conexion import conectar

def crear_programa(nombre):
    print("DEBUG nombre: ", nombre)

    if not nombre:
        print("Nombre vacío")
        return 
    
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO programas (nombre) VALUES (%s)",
            (nombre,)
        )
        conn.commit()
        print("Programa creado")

    except Exception as e:
        print("ERROR REAL: ", e)

    finally:
        cursor.close()
        conn.close()

def listar_programas():

    conn = conectar()

    if conn is None:

        print("No hay conexión")
        return

    cursor = conn.cursor()

    try:

        cursor.execute("SELECT id, nombre FROM programas ORDER BY id")
        resultados = cursor.fetchall()

        if not resultados:
            print("No hay programas registrados")
            return

        print("\nLISTADO DE PROGRAMAS:\n")

        for programa in resultados:
            print(f"ID: {programa[0]} | Nombre: {programa[1]}")

    except Exception as e:
        print(" Error:", e)

    finally:
        cursor.close()
        conn.close()