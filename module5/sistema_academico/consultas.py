
#importo de archivo conexion el metodo conectar
from conexion import conectar

#Metodo para listar los alumnos con sus programas utilizando el INNER JOIN
def listar_alumnos_con_programa():

    #Realizar la conexion
    conn= conectar()
    #Asignar la conexion al cursor para la implementacion de los QUERY
    cursor = conn.cursor()

    #Excepcion de captura donde se aplica el query de INNER JOIN para unir datos de los alumnos, programa y notas
    try:
        cursor.execute("""
            SELECT alumnos.id, alumnos.nombre, alumnos.email, programas.nombre, alumnos.nota
            FROM alumnos
            INNER JOIN programas
            ON alumnos.programa_id = programas.id
            ORDER BY alumnos.nombre

        """)

        #Metodo para traer todos los datos encontrados en un solo variable
        resultados = cursor.fetchall()

        print("\n LISTADO DE ALUMNOS:\n")

        for fila in resultados:
            print(f"ID: {fila[0]} | Nombre: {fila[1]} | Email: {fila[2]} | Programa: {fila[3]} | Nota: {fila[4]}")

    except Exception as e:
        print("Error: " , e)

    finally:
        cursor.close()
        conn.close()