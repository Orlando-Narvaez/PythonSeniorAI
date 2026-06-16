from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"message": "API funcionando correctamente"}  

@app.get("/saludo")
def saludo():
    return {"message": f"Hola, bienvenido a FastAPI"}

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"message": f"Hola {nombre}, bienvenido a FastAPI"}

@app.get("/suma/{a}/{b}")
def suma(a: int, b: int):
    return {"message": f"La suma de {a} y {b} es {a + b}"}

@app.get("/edad/{edad}")
def verificar_edad(edad: int):
    if edad >= 18:
        return {"message": "Eres mayor de edad"}
    else:
        return {"message": "Eres menor de edad"}


# LISTA DE TAREAS

tareas = []

@app.get("/tareas")
def obtener_tareas():
    return tareas

@app.post("/tareas")
def crear_tarea(nombre: str):
    tareas.append({"nombre": nombre, "completada": False})
    return {"message": f"Tarea '{nombre}' creada"}

@app.put("/tareas/{inidice}")
def actualizar_tarea(indice: int, nuevo_nombre: str):
    if indice >= len(tareas):
        return {"message": "Índice fuera de rango"}
    tareas[indice]["nombre"] = nuevo_nombre
    return {"message": "tarea actualizada"}

@app.delete("/tareas/{indice}")
def eliminar_tarea(indice: int):
    if indice >= len(tareas):
        return {"message": "Índice fuera de rango"}
    tareas.pop(indice)
    return {"message": "tarea eliminada"}

@app.put("/tareas/completar/{indice}")
def completar_tarea(indice: int):
    if indice >= len(tareas):
        return {"message": "Índice fuera de rango"}
    tareas[indice]["completada"] = True
    return {"message": "tarea completada"}

@app.get("/tareas/pendientes")
def tareas_pendientes():
    return [tarea for tarea in tareas if not tarea["completada"]]

@app.get("/tareas/cantidad")
def cantidad_tareas():
    return {"cantidad": len(tareas)}

@app.get("/tareas/buscar")
def buscar_tarea(nombre: str):
    return [tarea for tarea in tareas if nombre.lower() in tarea["nombre"].lower()]
