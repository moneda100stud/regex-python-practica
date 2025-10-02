# regex-python-practica
# Practica de Expresiones Regulares en Python

**Nombre:** Luis Alfonso Santacruz Moneda
**Grupo:** 5SS
**materia** LENGUAJES Y AUTÓMATAS 
**actividad** Laboratorio de Expresiones Regulares
Este repositorio contiene una serie de ejercicios practicos para demostrar el uso de expresiones regulares (regex) en Python para diversas tareas de validacion y extraccion de datos.

---

## Ejercicios

### 1. Validador de Correos Electronicos (`ejercicio_1.py`)

Este script utiliza una expresion regular simple para verificar si una cadena de texto tiene el formato de una direccion de correo electronico valida (`usuario@dominio.tld`). Utiliza `re.fullmatch()` para asegurar que toda la cadena coincida con el patron.

### 2. Extractor de Numeros de Telefono (`ejercicio_2.py`)

El script busca y extrae numeros de telefono de 10 digitos de un texto. La expresion regular esta diseñada para reconocer multiples formatos, incluyendo aquellos con parentesis, guiones o espacios como separadores (ej. `(123) 456-7890`, `123-456-7890`, `1234567890`).

### 3. Validador de Contraseñas Seguras (`ejercicio_3.py`)

Este script valida si una contraseña cumple con varios criterios de seguridad: longitud minima, y la inclusion de letras mayusculas, minusculas, numeros y caracteres especiales. Utiliza "lookaheads" en la expresion regular para verificar todas las condiciones de forma eficiente.

### 4. Extractor de URLs y Dominios (`ejercicio_4.py`)

El script encuentra URLs en un texto y las descompone en sus componentes principales: protocolo, dominio y ruta. Hace uso de grupos de captura nombrados (`?P<nombre>...`) para que el codigo sea mas claro y facil de mantener.

### 5. Analizador y Formateador de Fechas (`ejercicio_5.py`)

Este script identifica fechas escritas en diversos formatos (como `DD/MM/YYYY`, `YYYY-MM-DD`, `DD-MMM-YYYY` y `Mes DD, YYYY`) dentro de un texto. Luego, las convierte a un formato estandar `YYYY-MM-DD` para su facil procesamiento.
