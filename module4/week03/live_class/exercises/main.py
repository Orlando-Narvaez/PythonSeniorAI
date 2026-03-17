"""
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Dede ingresar un numero")
except TypeError:
    print("Tipo de dato invalido")
except Exception as e:
    print(f" Ocurrio un error inesperado: {e}")
   """ 
    
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Dede ingresar un numero")
else:
    print("La ejecucion dio un resultado positivo (Else)")
finally:
    print("La ejecucion finalizo")