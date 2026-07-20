from passlib.context import CryptContext

HASH_SCHEME = "argon2"

pwd_context = CryptContext(schemes=[HASH_SCHEME], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    if not pwd_context.verify(plain_password, hashed_password):
        raise ValueError("Contraseña incorrecta")
    
def main():
    print("Registro de usuario")
    password_registrado = input("Ingrese su contraseña: ")
    hashed = hash_password(password_registrado)
    print(f"Hash generado: {hashed}")

    print("\nPrueba de contraseña")
    try:
        verify_password(password_registrado, hashed)
        print("Contraseña verificada correctamente")
    except ValueError as e: 
        print(f"Error: {e}")

if __name__ == "__main__":
    main()