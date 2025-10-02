"""ejercicio_5.py"""
import re
from datetime import datetime

"""Mapeo de meses en español (para la conversión)"""
MESES = {
    'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'ago': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dic': 12,
    'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
    'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12,
}

def convertir_a_estandar(match: re.Match) -> tuple[str, str]:
    """
    Convierte una fecha encontrada por la regex a formato YYYY-MM-DD.
    La lógica depende de cuál grupo de captura (formato) fue el que coincidió.
    """
    fecha_original = match.group(0)
    
    """Formato DD/MM/YYYY (Grupo 'dmy_slash')"""
    if match.group('dmy_slash'):
        return fecha_original, datetime.strptime(fecha_original, '%d/%m/%Y').strftime('%Y-%m-%d')
    
    # Formato YYYY-MM-DD (Grupo 'ymd_hyphen')
    elif match.group('ymd_hyphen'):
        return fecha_original, fecha_original # Ya está en formato estándar
    
    # Formato DD-MMM-YYYY (Grupo 'dmy_month')
    elif match.group('dmy_month'):
        dia = match.group('dia_dmy')
        mes_str = match.group('mes_dmy').lower()
        anio = match.group('anio_dmy')
        mes_num = MESES.get(mes_str)
        if mes_num:
            fecha_dt = datetime(int(anio), mes_num, int(dia))
            return fecha_original, fecha_dt.strftime('%Y-%m-%d')

    # Formato Mes DD, YYYY (Grupo 'month_d_y')
    elif match.group('month_d_y'):
        mes_str = match.group('mes_mdy').lower()
        dia = match.group('dia_mdy')
        anio = match.group('anio_mdy')
        mes_num = MESES.get(mes_str)
        if mes_num:
            fecha_dt = datetime(int(anio), mes_num, int(dia))
            return fecha_original, fecha_dt.strftime('%Y-%m-%d')
            
    return fecha_original, "Error de conversión"


def analizar_y_formatear_fechas(texto: str) -> list[tuple[str, str]]:
    """
    Busca fechas en múltiples formatos y las convierte a YYYY-MM-DD.
    """
    
    """
    Construccion de la expresion regular combinada:
    - Se definen patrones individuales para cada formato de fecha soportado.
    - Cada patron principal esta envuelto en un grupo nombrado (ej. `?P<dmy_slash>...`)
      para que la funcion de conversion pueda identificar que formato coincidio.
    - Para los formatos con nombres de meses, los patrones se generan dinamicamente
      a partir del diccionario `MESES` para mayor flexibilidad.
    - Todos los patrones se unen con el operador `|` (OR) en una sola `regex_combinada`.
      Esto permite buscar cualquiera de los formatos en una sola pasada.
    - `re.finditer` se usa para encontrar todas las coincidencias en el texto, devolviendo
      un iterador de objetos `match` que contienen la informacion de cada fecha encontrada.
      `re.IGNORECASE` asegura que los meses se detecten sin importar mayusculas o minusculas.
    """
    """1. DD/MM/YYYY"""
    patron_slash = r'(?P<dmy_slash>\d{2}\/\d{2}\/\d{4})'
    
    """2. YYYY-MM-DD"""
    patron_hyphen = r'(?P<ymd_hyphen>\d{4}-\d{2}-\d{2})'
    
    """3. DD-MMM-YYYY (Ej: 01-Dic-2024). Grupos de captura: Dia, Mes, Anio"""
    patron_dmy_month = r'(?P<dmy_month>(?P<dia_dmy>\d{2})-(?P<mes_dmy>[a-zA-Z]{3})-(?P<anio_dmy>\d{4}))'
    
    """4. Mes DD, YYYY (Ej: Diciembre 01, 2024). Grupos de captura: Mes, Dia, Anio"""
    patron_month_d_y = r'(?P<month_d_y>(?P<mes_mdy>[a-zA-Z]+)\s+(?P<dia_mdy>\d{1,2}),\s*(?P<anio_mdy>\d{4}))'
    
    """Combinar todos los patrones con el operador OR (|)"""
    regex_combinada = f"{patron_slash}|{patron_hyphen}|{patron_dmy_month}|{patron_month_d_y}"
    
    fechas_encontradas = re.finditer(regex_combinada, texto, re.IGNORECASE)
    
    resultados_conversion = []
    for match in fechas_encontradas:
        original, estandar = convertir_a_estandar(match)
        resultados_conversion.append((original, estandar))
        
    return resultados_conversion

# Ejemplo de texto 
texto_entrada = "El reporte fue generado el 2023-12-25. La proxima revision es el 10/08/2024. El evento de lanzamiento sera en Febrero 01, 2025. No olvidar la fecha limite: 15-Mar-2025."

resultados = analizar_y_formatear_fechas(texto_entrada)

print("\n--- Ejercicio 5: Analizador de Fechas y Formateador ---")
print("Fechas encontradas y convertidas (formato estándar YYYY-MM-DD):")
for original, estandar in resultados:
    print(f"- Formato original: {original} -> Estándar: {estandar}")

"""
Este script fue desarrollado y modificado con la asistencia de Gemini Code Assist.
"""

# Nota sobre el 01-Jul-2024: Se asume que el mes abreviado es en español (Jul = Julio).
# La implementación usa un diccionario MESES flexible para esto.