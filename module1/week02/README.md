# 🧠 Clase 2: Variables, Tipos de Datos y Operadores en Python

## 🎯 Objetivos de Aprendizaje

- Comprender la lógica de las variables, su declaración y asignación dinámica.  
- Manipular tipos de datos primitivos en Python.  
- Utilizar operadores correctamente con sentido lógico y seguro.

---

## 🧩 1. Introducción a las Variables y la Inferencia de Tipos

Una **variable** es un espacio en memoria que almacena un valor.  
En Python, no es necesario declarar el tipo de dato de forma explícita porque el lenguaje usa **tipado dinámico**: el tipo se determina automáticamente según el valor asignado.

### 💡 Convenciones Internacionales (PEP 8)
- Los nombres de variables deben escribirse en **snake_case**.  
  Ejemplo: `nombre_usuario`, `numero_total`, `precio_unitario`.  
- Los nombres deben ser **significativos** y describir su propósito.  
- Se deben agregar comentarios cuando el código no sea obvio o requiera contexto.

### 🧠 Mejores prácticas
- Documentar siempre el código para mejorar su comprensión.  
- Utilizar formatos de impresión claros (como las f-strings) en lugar de concatenar textos, para evitar errores y mantener legibilidad.

---

## 🧮 2. Tipos de Datos Primitivos en Python

Python cuenta con varios tipos de datos básicos que se utilizan constantemente en programación:

1. **Enteros (int)**  
   Representan números sin parte decimal.  
   Se utilizan en operaciones aritméticas básicas como sumas, restas o conteos.

2. **Decimales (float)**  
   Permiten trabajar con números que tienen parte fraccionaria.  
   Son útiles en cálculos científicos o financieros donde se requiere precisión.

3. **Cadenas de texto (str)**  
   Almacenan texto y caracteres.  
   Son fundamentales para mostrar información o trabajar con entradas del usuario.

4. **Booleanos (bool)**  
   Representan valores lógicos: `True` o `False`.  
   Son la base para tomar decisiones mediante estructuras condicionales.

---

## 🔄 3. Conversión de Tipos (Casting)

En muchos casos, es necesario **convertir** un tipo de dato en otro, por ejemplo, transformar un número en texto o viceversa.

Sin embargo, estas conversiones deben hacerse con cuidado, ya que un valor no válido puede causar errores.

### ⚠️ Norma de Seguridad (OWASP)
Siempre **valida los datos de entrada** antes de intentar convertirlos.  
Nunca confíes directamente en lo que el usuario introduce, ya que podría generar fallos o vulnerabilidades en tu programa.

---

## ➕ 4. Operadores en Python

Los operadores permiten realizar acciones o comparaciones entre variables y valores.  
Se dividen principalmente en tres categorías:

### 1. Operadores Aritméticos
Permiten realizar operaciones matemáticas básicas: suma, resta, multiplicación, división y módulo.

### 2. Operadores Relacionales
Comparan valores y devuelven un resultado lógico (verdadero o falso).  
Se usan para tomar decisiones en condicionales (`if`, `else`, etc.).

### 3. Operadores Lógicos
Combinan o invierten condiciones utilizando las palabras clave `and`, `or` y `not`.  
Permiten crear expresiones complejas para validar varios criterios a la vez.

---

## 🧠 5. Buenas Prácticas Profesionales

- Utiliza nombres claros y coherentes para las variables.  
- Evita el uso de letras sueltas como `a`, `b` o `x` sin contexto.  
- Comenta las partes importantes del código.  
- Controla los errores al recibir y procesar datos del usuario.  
- Mantén un estilo de escritura uniforme para que el proyecto sea entendible por otros desarrolladores.

---

## 🧾 6. Reflexión Final

Esta clase sienta las bases de la **programación estructurada** en Python.  
Comprender cómo funcionan las variables, los tipos de datos y los operadores es esencial para construir programas confiables y mantener el control sobre la información.

> 💡 Ser un buen programador no consiste solo en saber escribir código, sino en **entender cómo se comporta y cómo hacerlo seguro, limpio y mantenible.**

---

## 🧩 7. Archivos de esta Clase

- Apuntes y explicaciones teóricas sobre variables y tipos de datos.  
- Ejercicios prácticos de operadores y conversiones.  
- Este archivo `README.md` como resumen educativo.

---