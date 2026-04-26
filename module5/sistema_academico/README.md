# 🎓 Sistema Académico

Proyecto desarrollado en Python con PostgreSQL que permite la gestión de alumnos y programas académicos.

## 📌 Descripción

Este sistema permite realizar operaciones básicas de gestión académica, incluyendo:

- Registro de programas
- Registro de alumnos
- Consulta de alumnos y programas
- Actualización de notas
- Eliminación de alumnos

El objetivo del proyecto es simular un sistema real de backend conectado a base de datos.

## 🛠️ Tecnologías utilizadas

- Python 🐍
- PostgreSQL 🐘
- psycopg2
- dotenv (.env)

## 🧱 Estructura del proyecto

## ⚙️ Configuración

1. Crear base de datos en PostgreSQL:

CREATE DATABASE academico;

CREATE TABLE programas (
id SERIAL PRIMARY KEY,
nombre VARCHAR(100) NOT NULL
);

CREATE TABLE alumnos (
id SERIAL PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
programa_id INT,
nota DECIMAL(3,2),
FOREIGN KEY (programa_id) REFERENCES programas(id)
)

# CREACION DEL DOCUMENTO .env

DB_HOST=localhost
DB_PORT=5432
DB_NAME=academico
DB_USER=postgres
DB_PASSWORD=tu_password

#Instalacion de la biblioteca a usar

pip install psycopg2 python-dotenv

# Ejecucio del programa:

python main.py
