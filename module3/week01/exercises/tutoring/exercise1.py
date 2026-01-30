precios = [50, 75, 46, 25, 80, 65, 8]
precios.sort()

def precio_mayor(precios):
    max = precios[0]
    for precio in precios:
        if precio > max:
            max = precio
    print(f"El precio mayor es: {max}")
    
def precio_menor(precios):
    min = precios[0]
    for precio in precios:
        if precio < min:
            min = precio
    print(f"El precio menor es: {min}")
    
def main():
    precio_mayor(precios)
    precio_menor(precios)
    
if __name__ == "__main__":
    main()