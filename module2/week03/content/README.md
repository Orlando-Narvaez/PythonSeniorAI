# 📘 Notas Educativas — Módulo 2, Semana 3

### Programación con Python — Manejo de Archivos y Modularidad

Este README educativo resume de manera clara y organizada los conceptos trabajados durante la **Semana 3 del Módulo 2**, enfocado en consolidar el manejo de archivos, la organización del código y la construcción de programas más completos.

---

## 🎯 Objetivos de la Semana

* Comprender el ciclo completo de lectura y escritura de archivos.
* Procesar información proveniente de archivos externos.
* Utilizar modularidad para dividir programas en funciones y secciones.
* Construir estructuras lógicas más robustas utilizando condicionales y bucles.
* Preparar la base para proyectos más grandes con datos persistentes.

---

## 🧠 1. Reforzando el Manejo de Archivos

Esta semana se profundizó en las distintas formas de manejar archivos en Python.

### Conceptos clave:

* Tipos de apertura de archivos.
* Lectura completa vs lectura línea por línea.
* Escritura sobre archivos existentes.
* Creación de nuevos archivos para almacenar información.

El objetivo principal es trabajar con datos que se mantienen incluso cuando se detiene el programa.

---

## 📄 2. Lectura y Procesamiento de Datos

Se practicaron técnicas para recorrer líneas y extraer información útil.

### Habilidades desarrolladas:

* Separar datos por delimitadores.
* Limpiar texto eliminando saltos de línea.
* Convertir texto a valores numéricos.
* Construir listas y diccionarios a partir de archivos.

Este tipo de procesamiento es fundamental para organizar información de usuarios, productos, notas, transacciones, etc.

---

## ✍️ 3. Escritura y Actualización de Archivos

La semana también incluyó la creación y modificación de archivos.

### Se trabajó en:

* Guardar información procesada.
* Generar reportes basados en datos leídos.
* Crear archivos nuevos para almacenar resultados.
* Registrar actualizaciones sin borrar completamente el archivo original.

---

## 🧩 4. Modularidad y Funciones Aplicadas

Para mantener programas más limpios se integraron funciones en cada paso del proceso.

### Beneficios reforzados:

* Reutilización del código.
* Separación lógica entre tareas.
* Claridad al momento de leer o mantener el programa.
* Facilitar pruebas y depuración.

La combinación de funciones y manejo de archivos permite construir programas más profesionales.

---

## 📦 5. Integración de Listas, Diccionarios y Archivos

Se realizaron ejercicios donde se combinan:

* Listas obtenidas desde archivos.
* Diccionarios creados para organizar datos.
* Procesamiento mediante bucles.
* Validaciones con condicionales.

Este enfoque imita situaciones reales como sistemas de inventario, agendas, registros, etc.

---

## 📝 6. Ejercicios y Actividades Realizadas

Durante la semana se desarrollaron prácticas como:

* Leer y analizar datos estructurados.
* Crear programas que transforman y exportan información.
* Construir reportes automatizados.
* Dividir procesos en funciones dedicadas.
* Crear flujos de trabajo completos que integran lectura → procesamiento → escritura.

---

## 🧩 7. Conclusiones Educativas

* El manejo de archivos es esencial para crear software real.
* Leer, procesar y escribir datos requiere combinar varias herramientas del lenguaje.
* Las funciones permiten trabajar de forma organizada y profesional.
* Las estructuras de datos ayudan a representar información compleja.
* La práctica con datos reales fortalece la lógica y el pensamiento algorítmico.

---

## 📚 8. Recomendaciones de Estudio

* Practicar con diferentes tipos de archivos.
* Intentar recrear un pequeño sistema que use archivos como base de datos.
* Crear funciones reutilizables para lectura y escritura.
* Probar separar módulos en diferentes archivos .py.
* Documentar cada paso para reforzar la comprensión.

---

## 📎 Archivos Relacionados

* **01_Modulo_2_Semana_3.ipynb** — Notebook con actividades y ejemplos.
* **README.md** — Documento educativo generado para estudio y repaso.

# 📘 Módulo 2 — Semana 3

## **Estructuras de Datos en Python: Listas, Tuplas y Diccionarios**

Este README educativo resume de manera clara y práctica los temas estudiados en la Semana 3 del Módulo 2. Aquí encontrarás explicaciones simples, ejemplos conceptuales (sin código) y las ideas clave de cada estructura de datos.

---

# 🧠 Introducción

En Python existen estructuras que permiten almacenar y organizar múltiples datos dentro de una sola variable. Cada una tiene características propias que las hacen útiles en distintas situaciones.

En esta semana aprendiste:

* Qué son las **listas**, **tuplas** y **diccionarios**.
* Cómo funcionan sus elementos.
* Cuándo se recomienda usar cada una.
* Qué operaciones conceptuales se pueden realizar con ellas.

---

# 📌 1. Listas en Python

### ✔️ ¿Qué son?

Son colecciones ordenadas y modificables. Permiten almacenar varios valores en una sola variable.

### ✔️ Características principales

* Son **ordenadas** (cada elemento tiene una posición).
* Son **mutables** (sus elementos se pueden cambiar).
* Permiten elementos duplicados.

### ✔️ Ejemplos conceptuales de uso

* Lista de tareas.
* Lista de productos.
* Lista de estudiantes.

### ✔️ Operaciones comunes (explicación en palabras)

* **Agregar elementos**: añadir al final o en posiciones específicas.
* **Eliminar elementos**: quitar por nombre o posición.
* **Buscar elementos**: verificar si algo está dentro de la lista.
* **Ordenar o invertir**: organizar la lista según una regla.

---

# 📌 2. Tuplas en Python

### ✔️ ¿Qué son?

Son colecciones ordenadas pero **inmutables**. Esto significa que, una vez creadas, no se pueden modificar.

### ✔️ Características principales

* Son **más rápidas** que las listas.
* Son **seguras**, ya que su contenido no cambia accidentalmente.
* También permiten elementos duplicados.

### ✔️ Ejemplos conceptuales de uso

* Coordenadas (x, y).
* Información que no debe cambiar, como fechas.
* Configuraciones fijas.

### ✔️ Operaciones comunes (en palabras)

* Consultar el valor en una posición.
* Contar cuántas veces aparece un elemento.
* Obtener su longitud.

---

# 📌 3. Diccionarios en Python

### ✔️ ¿Qué son?

Son colecciones no ordenadas que almacenan datos en forma de **clave : valor**. Son muy útiles para representar información estructurada.

### ✔️ Características principales

* Son **mutables**.
* No permiten claves duplicadas.
* Los valores pueden ser cualquier tipo de dato.

### ✔️ Ejemplos conceptuales de uso

* Perfil de usuario (nombre, edad, correo).
* Producto con propiedades (precio, cantidad, categoría).
* Configuraciones de un sistema.

### ✔️ Operaciones comunes

* **Agregar o modificar valores** mediante una clave.
* **Eliminar entradas**.
* **Obtener valores específicos** usando la clave.
* **Recorrer** todas las claves o valores.

---

# 🧩 Comparación General

| Estructura      | Ordenada | Mutable | Duplicados     | Uso recomendado                        |
| --------------- | -------- | ------- | -------------- | -------------------------------------- |
| **Lista**       | Sí       | Sí      | Sí             | Datos que cambian constantemente       |
| **Tupla**       | Sí       | No      | Sí             | Datos fijos y seguros                  |
| **Diccionario** | No       | Sí      | No (en claves) | Datos estructurados con nombre y valor |

---

# 📚 Conclusión

Esta semana fortaleciste tu manejo de las estructuras de datos más usadas en Python. Aprendiste cuándo usarlas, cómo funcionan y qué ventajas ofrecen según el caso.

Con esto ya puedes almacenar información más compleja y trabajar programas más avanzados.