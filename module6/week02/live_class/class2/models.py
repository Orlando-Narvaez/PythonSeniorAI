from pydantic import BaseModel, Field

class TareaCreate(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=50)
    descripcion: str = Field(..., min_length=10, max_length=200)
    prioridad: int = Field(..., ge=1, le=5)
    completada: bool = Field(default=False)

class TareaUpdate(BaseModel):
    titulo: str | None = Field(None, min_length=3, max_length=50)
    descripcion: str | None = Field(None, min_length=10, max_length=200)
    prioridad: int | None = Field(None, ge=1, le=5)
    completada: bool | None = Field(default=None)

class TareaResponse(BaseModel):
    id: int
    titulo: str
    descripcion: str
    prioridad: int
    completada: bool
