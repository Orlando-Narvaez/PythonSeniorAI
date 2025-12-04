"""
Desarrolle una app que cree una clase abstracta "Estudiante" y al menos 3 subclases y como minmimo 2 comportamientos/funciones/métodos/definiciones.
"""

# Clase abstracta
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def estudiar(self):
        raise NotImplementedError("Este método debe implementarse en la subclase")

    def presentar_examen(self):
        raise NotImplementedError("Este método debe implementarse en la subclase")


# Subclase 1
class EstudiantePrimaria(Estudiante):
    def estudiar(self):
        return f"{self.nombre} está coloreando y haciendo tareas básicas."

    def presentar_examen(self):
        return f"{self.nombre} presentó un examen sencillo de matemáticas."


# Subclase 2
class EstudianteSecundaria(Estudiante):
    def estudiar(self):
        return f"{self.nombre} está estudiando álgebra y ciencias."

    def presentar_examen(self):
        return f"{self.nombre} presentó un examen de química."


# Subclase 3
class EstudianteUniversitario(Estudiante):
    def estudiar(self):
        return f"{self.nombre} está estudiando para parciales y proyectos."

    def presentar_examen(self):
        return f"{self.nombre} presentó un examen final muy difícil."


# Crear objetos de cada tipo
e1 = EstudiantePrimaria("Laura")
e2 = EstudianteSecundaria("Carlos")
e3 = EstudianteUniversitario("Orlando")

# Probar comportamientos
print(e1.estudiar())
print(e1.presentar_examen())

print(e2.estudiar())
print(e2.presentar_examen())

print(e3.estudiar())
print(e3.presentar_examen())

