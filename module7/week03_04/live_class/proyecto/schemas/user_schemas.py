from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Nombre de usuario unico", examples=["usuario123"])
    password: str = Field(..., min_length=6, max_length=255, description="Contraseña del usuario", examples=["contraseñaSegura123"])

class UserLogin(BaseModel):
    username: str = Field(..., description="Nombre de usuario unico", examples=["usuario123"])
    password: str = Field(..., description="Contraseña del usuario", examples=["contraseñaSegura123"])

class UserResponse(BaseModel):
    id: int
    username: str
    created_at: Optional[datetime] = Field(default=None, example="2023-01-01T12:00:00")
    updated_at: Optional[datetime] = Field(default=None, example="2023-01-02T12:00:00")
    model_config = ConfigDict(from_attributes=True)  # Permite la conversión de atributos del modelo a diccionario

class Token(BaseModel):
    access_token: str = Field(..., description="Token de acceso JWT", examples=["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."])
    token_type: str = Field(default="bearer", description="Tipo de token", examples=["bearer"])

class LoginResponse(BaseModel):
    access_token: str = Field(..., description="Token de acceso JWT", examples=["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."])
    token_type: str = Field(default="bearer", description="Tipo de token", examples=["bearer"])
    user: UserResponse = Field(..., description="Información del usuario autenticado")

class Message(BaseModel):
    message: str = Field(..., description="Mensaje de respuesta", examples=["Operación realizada con éxito"])