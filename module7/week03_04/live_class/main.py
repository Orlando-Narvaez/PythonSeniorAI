from fastapi import FastAPI, HTTPException, Header
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel, Field
import secrets

HASH_SCHEME = "argon2"
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# modelos pydantic
class LoginData(BaseModel):
    username: str = Field(examples=["usuario123"])
    password: str = Field(examples=["contraseña123"])

class RegisterData(BaseModel):
    username: str = Field(examples=["usuario123"])
    password: str = Field(examples=["contraseña123"])

app = FastAPI()

pwd_context = CryptContext(schemes=[HASH_SCHEME], deprecated="auto")
usuarios_db = {}

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def crear_token(data: dict, expiracion: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiracion)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

# Creacion de endpoints (API Rest)
@app.get("/")
async def inicio():
    return {"mensaje": "API de autentificacion JWT+Passlib"}

@app.post("/registro")
async def registrar_usuario(datos: RegisterData):
    if datos.username in usuarios_db:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    usuarios_db[datos.username] = hash_password(datos.password)

    return{
        "succes": True,
        "mensaje": "Usuario registrado exitosamente",
        "usuario": {
            "username": datos.username,
            "registrado_en": datetime.now(timezone.utc).isoformat()
        }
    }

@app.post("/login")
async def login(datos: LoginData):
    user_pass = usuarios_db.get(datos.username)
    if not user_pass or not verify_password(datos.password, user_pass):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    token = crear_token({"sub": datos.username})

    return {
        "success": True,
        "mensaje": "Login exitoso",
        "access_token": token, # esto no se muestra solo con fines del ejercicio
        "token_access": "bearer ",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        "usuario": {
            "username": datos.username,
        }
    }

def main():
    import uvicorn
    import webbrowser
    import threading

    def abrir_navegador():
        import time
        time.sleep(1.5) 
        webbrowser.open("http://127.0.0.1:8000/docs")

    threading.Thread(target=abrir_navegador, daemon=True).start()

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()