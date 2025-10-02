"""ejercicio_3.py"""
import re

def validar_contrasena_segura(contrasena: str) -> tuple[bool, list[str]]:
    """
    Verifica si una contrasena cumple con los criterios de seguridad usando lookaheads.
    """
    """
    Explicacion sobre Lookaheads (?=...):

    Un "lookahead" es un tipo de 'asercion de ancho cero' (zero-width assertion).
    Esto significa que comprueba si un patron existe mas adelante en la cadena,
    pero no consume ningun caracter. Es como 'mirar hacia adelante' sin moverse.

    - Sintaxis: (?=PATRON)
    - Como funciona: En la posicion actual, el motor de regex intenta hacer match con PATRON.
      - Si lo logra, la asercion es exitosa y el motor vuelve a la posicion original para continuar.
      - Si no lo logra, la asercion falla, y por lo tanto, toda la coincidencia falla.

    ¿Por que es util para las contrasenas?
    Permite verificar multiples condiciones independientes desde el mismo punto.
    Por ejemplo, la expresion r"^(?=.*[A-Z])(?=.*\d).{8,}$" verifica que la cadena:
    1. Desde el inicio (^), tenga una mayuscula en algun lugar (?=.*[A-Z]).
    2. Desde el inicio (^), tambien tenga un digito en algun lugar (?=.*\d).
    3. Tenga al menos 8 caracteres en total (.{8,}).
    """
    """Lista de criterios y sus patrones (lookaheads)"""
    criterios = [
        ("Minimo 8 caracteres", r".{8,}"),
        ("Al menos una letra mayuscula", r"(?=.*[A-Z])"),
        ("Al menos una letra minuscula", r"(?=.*[a-z])"),
        ("Al menos un numero", r"(?=.*\d)"),
        ("Al menos un caracter especial (@$!%*?&#)", r"(?=.*[@$!%*?&#])"),
    ]
    
    fallos = []
    """1. Verificar la longitud por separado para mayor claridad"""
    if len(contrasena) < 8:
        fallos.append("Minimo 8 caracteres de longitud")

    """
    2. Construir la regex con lookaheads para los demas criterios.
    La estructura es: ^ + todos los lookaheads + .*$
    El .*$ asegura que la regex intente coincidir con toda la cadena.
    """
    regex_base = r"^" + "".join([patron for _, patron in criterios[1:]]) + r".*$"
    
    """3. Verificar los criterios restantes"""
    if not re.search(regex_base, contrasena):
        """
        Si la regex falla, debemos identificar *cual* de los lookaheads fallo.
        Esto se hace probando cada lookahead individualmente.
        """
        for descripcion, patron in criterios[1:]:
            """Notar que re.search es suficiente para lookaheads"""
            if not re.search(patron, contrasena):
                fallos.append(descripcion)
                
    return (len(fallos) == 0), fallos

"""Casos de prueba"""
casos_prueba = [
    "Segura123!",
    "contrasena",
    "MAYUSCULA123!",
    "P@ssw0rd",
    "Corta1!",
    "L@rgaSinNum",
]

print("\n--- Ejercicio 3: Validador de Contrasenas Seguras ---")
for pswd in casos_prueba:
    es_valida, fallos = validar_contrasena_segura(pswd)
    estado = "VALIDA ✅" if es_valida else "INVALIDA ❌"
    print(f"\nContrasena: '{pswd}' -> {estado}")
    if fallos:
        print("  Criterios NO cumplidos:")
        for fallo in fallos:
            print(f"  - {fallo}")

"""
Este script fue desarrollado y modificado con la asistencia de Gemini Code Assist.
"""