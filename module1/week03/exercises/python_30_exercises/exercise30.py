""" 
Ejercicio 30 
Enunciado: 
 Crea un programa que permita calcular el total a pagar en un parqueadero.  El usuario ingresa las horas de permanencia y el tipo de vehículo: 
●  Carro: $5 000 por hora  
●  Moto: $2 000 por hora  Si la permanencia supera las 10 horas, se aplica un descuento del 10% 
sobre el total.  
Competencia que evalúa: 
 Uso combinado de condicionales anidados, operadores aritméticos y estructuras de 
decisión para resolver un problema de negocio con múltiples condiciones. 
 
"""

# Solicitar al usuario las horas de permanencia y el tipo de vehículo
horas = int(input("Ingrese las horas de permanencia: "))
tipo_vehiculo = int(input("Ingrese el tipo de vehículo (1 para carro, 2 para moto): "))

# Definir las tarifas por hora
tarifa_carro = 5000
tarifa_moto = 2000
total = 0

# Calcular el total a pagar según el tipo de vehículo
if tipo_vehiculo == 1:  # Carro
    total = horas * tarifa_carro
elif tipo_vehiculo == 2:  # Moto
    total = horas * tarifa_moto
else:
    print("Tipo de vehículo no válido.")
    total = None
    
# Aplicar descuento si la permanencia supera las 10 horas
if total is not None:
    if horas > 10:
        descuento = total * 0.10
        total -= descuento

# Mostrar el total a pagar
print(f"El total a pagar es: ${total:.2f}")
    