"""ejercicio_1.py"""
import re

def validar_correo_simple(correo: str) -> bool:
    """
    Valida si una cadena es un correo electronico simple (usuario@dominio.tld).
    
    El patron busca:
    1. Una o mas letras/numeros/puntos/guiones/subrayados (\w\. -) para el usuario.
    2. El simbolo @.
    3. Una o mas letras/numeros/guiones (\w -) para el dominio.
    4. Un punto (escapado como \.).
    5. Dos o mas letras/numeros para el dominio  (ej. com, mx, org).
    """
    """
    Desglose de la expresion regular: r"[\w\.-]+@[\w\.-]+\.\w{2,}"
    r"..."       -> Define una "raw string" en Python. Evita que los '\' se interpreten como secuencias de escape.
    [\w\.-]+    -> Es la parte del 'usuario' antes del @.
      [ ]       -> Define un conjunto de caracteres permitidos.
      \w        -> Cualquier caracter de palabra (letras a-z, A-Z, numeros 0-9 y el guion bajo _).
      \.        -> El punto literal (se escapa con '\' porque '.' tiene un significado especial).
      -         -> El guion literal.
      +         -> Cuantificador que significa "uno o mas" de los caracteres del conjunto anterior.
    @           -> El simbolo literal '@', que separa usuario y dominio.
    [\w\.-]+    -> Es la parte del 'dominio' (y subdominios) después del @. Sigue la misma lógica que la parte del usuario.
    \.          -> El punto literal que separa el dominio del TLD (Top-Level Domain).
    \w{2,}      -> Es la parte del TLD (como 'com', 'org', 'es').
      \w        -> Cualquier caracter de palabra.
      {2,}      -> Cuantificador que significa "dos o mas" del caracter anterior.
    """
    patron = r"[\w\.-]+@[\w\.-]+\.\w{2,}"
    
    """re.fullmatch() asegura que el patron coincida con toda la cadena."""
    if re.fullmatch(patron, correo):
        return True
    else:
        return False

"""Casos de prueba se manejar ejemplos para validar o invalidar los patrones """
casos_prueba = [
    ("usuario@ejemplo.com", "Valido"),
    ("nombre.apellido@dominio.mx", "Válido"),
    ("usuarioejemplo.com", "Invalido"),
    ("@ejemplo.com", "Invalido"),
    ("otro-usuario_123@sub.dominio.org", "Valido"),
    ("sin@tld", "Invalido"),
]

print("--- Ejercicio 1: Validador de Correos Electrónicos Simple ---")
for correo, resultado_esperado in casos_prueba:
    es_valido = validar_correo_simple(correo)
    estado = "Valido" if es_valido else "Invalido"
    """Se cambia el emoji para reflejar directamente la validez, no el exito de la prueba."""
    emoji_resultado = "✅" if es_valido else "❌"
    print(f"{emoji_resultado} '{correo}' -> {estado} ")

"""
Este script fue desarrollado y modificado con la asistencia de Gemini Code Assist.
"""