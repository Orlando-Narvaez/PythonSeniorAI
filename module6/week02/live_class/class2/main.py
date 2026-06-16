from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
from models import TareaCreate, TareaUpdate, TareaResponse
from database import tareas

app = FastAPI()

#CREAR TEREA

@app.post("/tareas", response_model=TareaResponse)

def crear_tarea(tarea: TareaCreate):
    nueva_tarea = {
        "id": len(tareas) + 1,
        "titulo": tarea.titulo,
        "descripcion": tarea.descripcion,
        "prioridad": tarea.prioridad,
        "completada": tarea.completada
    }

    tareas.append(nueva_tarea)
    return JSONResponse(status_code=201, content=nueva_tarea)

#LISTAR TAREAS
@app.get("/tareas", response_model= List[TareaResponse])
def listar_tareas():
    return tareas

#OBTENER TAREA POR ID
@app.get("/tareas/{tarea_id}")
def obtener_tarea(tarea_id: int):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            return tarea
        
    return JSONResponse(
        status_code=404, 
        content={"message": "Tarea no encontrada"}
        )

#ACTUALIZAR TAREA
@app.patch("/tareas/{tarea_id}")
def actualizar_tarea(tarea_id: int, datos: TareaUpdate):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            if datos.titulo is not None:
                tarea["titulo"] = datos.titulo

            if datos.descripcion is not None:
                tarea["descripcion"] = datos.descripcion

            if datos.prioridad is not None:
                tarea["prioridad"] = datos.prioridad

            if datos.completada is not None:
                tarea["completada"] = datos.completada
            
            return tarea
    
    return JSONResponse(
        status_code=404, 
        content={"message": "Tarea no encontrada"}
        )

#ELIMINAR TAREA
@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tareas.remove(tarea)
            return {"message": "Tarea eliminada"}
    
    return JSONResponse(
        status_code=404, 
        content={"message": "Tarea no encontrada"}
        )