from jose import jwt
from datetime import datetime, timedelta, timezone
import secrets

SECRET_KET = secrets.token_urlsafe(32)
ALGORTHM = "HS256"

def crear_token(datos: dict, expiracion: int= 30):
    to_econde = datos.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiracion)
    to_econde.update({"exp": expire})
    print("Datetime:", to_econde.values())
    return jwt.encode(to_econde, SECRET_KET, algorithm=ALGORTHM)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KET, algorithms=[ALGORTHM])
        return payload
    except jwt.ExpiredSignatureError:
        print("Error: el token ha expirado")
        return None
    except jwt.JWTError:
        print("Error: Token invalido")
        return None
    
def main():
    datos_usuario = {
        "sub": "usuario123",
        "rol": "admin"
    }

    token_generado = crear_token(datos_usuario)

    print("Token JWT generado ", token_generado)

    print("\n--- Verificacion de Token ---")
    datos_decodificados = verificar_token(token_generado)
    if datos_decodificados:
        print("Token valido. Datos: ", datos_decodificados)

if __name__ == "__main__":
    main()