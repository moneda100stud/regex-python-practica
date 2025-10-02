"""ejercicio_2.py"""
import re

def extraer_telefonos(texto: str) -> list[str]:
    """
    Busca y extrae numeros de telefono de 10 digitos en varios formatos.
    
    El patron considera:
    1. (DDD) o DDD o D{3} (captura del codigo de area, opcional con parentesis).
    2. Espacios, guiones o nada como separadores.
    3. Los siguientes 7 dígitos restantes.
    
    Patron: r'(\(\d{3}\)\s*|\d{3}[-\s]*)?\d{3}[-\s]?\d{4}'
    """
    
    """Desglose de la expresion regular: r'\(\d{3}\)\s*\d{3}-\d{4}|\d{3}[-\s]?\d{3}[-\s]?\d{4}'
    
    Esta expresion se compone de dos patrones principales unidos por el operador '|' (OR),
    lo que significa que buscara una coincidencia con el primer patron o con el segundo.

    Patron 1: \(\d{3}\)\s*\d{3}-\d{4}
    - \(\d{3}\) : Busca exactamente tres digitos encerrados en parentesis. Ej: (646)
    - \s*       : Busca cero o mas espacios en blanco.
    - \d{3}     : Busca exactamente tres digitos.
    - -         : Busca un guion literal.
    - \d{4}     : Busca exactamente cuatro digitos.
    -> Este patron captura formatos como '(664) 987-6543'.

    Patron 2: \d{3}[-\s]?\d{3}[-\s]?\d{4}
    - \d{3}     : Busca exactamente tres digitos.
    - [-\s]?    : Busca un separador opcional, que puede ser un guion o un espacio.
    - \d{3}     : Busca los siguientes tres digitos.
    - [-\s]?    : Otro separador opcional.
    - \d{4}     : Busca los ultimos cuatro digitos.
    -> Este patron captura formatos como '646-123-4567', '333 444 5555' y '5551234567'.
    """
    patron = r'\(\d{3}\)\s*\d{3}-\d{4}|\d{3}[-\s]?\d{3}[-\s]?\d{4}'
    
    """
    Uso de re.findall para la extraccion:
    - re.findall(patron, texto): Esta funcion del modulo 're' escanea la cadena 'texto'
      y encuentra todas las subcadenas que no se solapan y que coinciden con el 'patron' definido.
    - El resultado es una lista que contiene todas las coincidencias encontradas en formato de cadena.
      Por ejemplo: ['800-555-1212', '(911) 555-0100', ...].
    - Esta lista se asigna a la variable 'telefonos' y luego se devuelve como el
      resultado final de la funcion 'extraer_telefonos'.
    """
    telefonos = re.findall(patron, texto)
    return telefonos

"""Ejemplo de texto de entrada"""
texto_entrada = "El numero de la oficina es 800-555-1212. Para emergencias, use (911) 555-0100. El fax es 202 555 0177 y el movil 3101234567. Ignore el codigo 12345."

telefonos_encontrados = extraer_telefonos(texto_entrada)

print("\n--- Ejercicio 2: Extractor de Numeros de Telefono ---")
print(f"Texto de entrada:\n'{texto_entrada}'")
print(f"Telefonos encontrados: {telefonos_encontrados}")

"""
Este script fue desarrollado y modificado con la asistencia de Gemini Code Assist.
"""