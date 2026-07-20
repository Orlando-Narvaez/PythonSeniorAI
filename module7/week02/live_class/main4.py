from fastapi import FastAPI, HTTPException, Header
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel, Field
import secrets

HASH_SCHEME = "argon2"
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"

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