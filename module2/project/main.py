from models.conductor import Conductor
from models.motor import Motor
from models.moto import Moto
from models.carro import Carro
from models.camion import Camion
from services.conductor_service import ConductorServicio
from services.vehiculo_service import VehiculoServicio


def poblar_datos_iniciales(
    conductor_service: ConductorServicio,
    vehiculo_service: VehiculoServicio
) -> None:

    # ===== CONDUCTORES =====
    c1 = Conductor("Juan Pérez", "123456", "A1")
    c2 = Conductor("María Gómez", "654321", "B1")
    c3 = Conductor("Carlos Ruiz", "987654", "C2")

    conductor_service.registrar_conductor(c1)
    conductor_service.registrar_conductor(c2)
    conductor_service.registrar_conductor(c3)

    # ===== MOTO =====
    motor_moto = Motor("Gasolina",150)
    moto = Moto("MOT123", motor_moto, casco=True)

    # ===== CARRO =====
    motor_carro = Motor("Electrico",1800)
    carro = Carro("CAR456", motor_carro, revision_tecnico_mecanica_vigente=True)

    # ===== CAMIÓN =====
    motor_camion = Motor("Diesel",5000)
    camion = Camion(
        "CAM789",
        motor_camion,
        planilla_carga=True,
        peso_actual=8000,
        peso_maximo=12000
    )

    vehiculo_service.registrar_vehiculo(moto)
    vehiculo_service.registrar_vehiculo(carro)
    vehiculo_service.registrar_vehiculo(camion)

    # ===== ASIGNACIONES =====
    vehiculo_service.asignar_conductor("MOT123", c1)
    vehiculo_service.asignar_conductor("CAR456", c2)
    vehiculo_service.asignar_conductor("CAM789", c3)


def main() -> None:
    conductor_service = ConductorServicio()
    vehiculo_service = VehiculoServicio()

    poblar_datos_iniciales(conductor_service, vehiculo_service)

    print("=== LISTA DE CONDUCTORES ===")
    for conductor in conductor_service.listar_conductores():
        print(conductor.obtener_detalles())

    print("\n=== LISTA DE VEHÍCULOS ===")
    for vehiculo in vehiculo_service.listar_vehiculos():
        print(f"- {vehiculo.__class__.__name__} | Placa: {vehiculo.placa}")

    print("\n=== INICIO DE JORNADAS (POLIMORFISMO) ===")
    for vehiculo in vehiculo_service.listar_vehiculos():
        vehiculo.iniciar_jornada()
    
    for vehiculo in vehiculo_service.listar_vehiculos():
        vehiculo.mover()

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()