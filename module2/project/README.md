# 🚚 Proyecto: Sistema de Gestión de Transporte – Python

Un proyecto que modela digitalmente la operación básica de una empresa que maneja vehículos y conductores.
Desarrollado como parte del **Reto Final del Módulo 2 – Curso Dev Senior**.

---

## 🚀 Funcionalidades Principales

✔ Registrar conductores con datos validados
✔ Crear diferentes tipos de vehículos (Moto, Carro y Camión)
✔ Asignar conductores a vehículos (Agregación)
✔ Componer cada vehículo con un Motor
✔ Aplicar reglas de negocio según el tipo de vehículo:
- Moto → casco obligatorio
- Carro → revisión técnico-mecánica vigente
- Camión → planilla de carga + control de peso máximo
✔ Iniciar jornada de trabajo usando polimorfismo
✔ Simular movimiento gracias a la interfaz `Movible`
✔ Listados de vehículos y conductores
✔ Simulación de almacenamiento con servicios

---

## 🧠 ¿Qué Practica Este Proyecto?

- Programación orientada a objetos (POO)
- Encapsulación con `@property`
- Herencia y clases abstractas
- Polimorfismo (mismo método, diferentes resultados)
- Composición (Vehículo contiene Motor)
- Agregación (Conductor asignado opcionalmente)
- Validación de datos
- Servicios como capa de negocio

Este proyecto modela un escenario real del sector transporte aplicando buenas prácticas de diseño.

---

### 🗂 Estructura del Proyecto

```
ProyectoModulo2/
│
├── models/
│   ├── persona.py 
│   ├── conductor.py 
│   ├── motor.py 
│   ├── vehiculo.py 
│   ├── moto.py 
│   ├── carro.py 
│   ├── movible.py 
│   └── camion.py 
│
├── services/
│   ├── conductor_service.py 
│   └── vehiculo_service.py 
│
└── main.py 
```

---

## ▶️ Cómo Ejecutarlo

1. Requiere **Python 3.12 o superior**
2. Abrir la terminal en la carpeta del proyecto
3. Ejecutar:

```
python main.py
```

El programa mostrará:
- Conductores registrados
- Vehículos creados
- Asignaciones
- Reglas aplicadas al iniciar jornada

---

## 🎥 Video explicativo del proyecto

---

[![Ver video](https://img.youtube.com/vi/zO1RTINVpyE/maxresdefault.jpg)](https://youtu.be/zO1RTINVpyE)

---

---

## 🧑‍💻 Autor
**Orlando Narvaez Baracaldo — Ingeniería en Sistemas y Computación**
Proyecto construido para reforzar conceptos fundamentales de POO en Python.

## 📄 Licencia
Proyecto con fines educativos. Puede ser adaptado libremente.