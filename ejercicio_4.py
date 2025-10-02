"""ejercicio_4.py"""
import re

def extraer_urls_y_componentes(texto: str):
    """
    Extrae URLs y separa protocolo, dominio y ruta usando grupos de captura.
    
    Patron:
    (https?:\/\/)?  -> Grupo 1 (Protocolo): 'http://' o 'https://' (opcional)
    (www\.)?        -> Grupo 2 (Subdominio www): 'www.' (opcional)
    ([\w\.-]+)      -> Grupo 3 (Dominio principal): El nombre del dominio
    (\.\w{2,})      -> Grupo 4 (TLD): El TLD (.com, .org, etc.)
    (\/.*)?         -> Grupo 5 (Ruta): '/ruta/...' (opcional)
    
    Al agrupar Grupos 2, 3 y 4 se obtiene el dominio completo.
    """
    
    """
    Version simplificada y mejorada del patron para URLs comunes:
    Captura 1: Protocolo (http:// o https:// o nada)
    Captura 2: Dominio completo (incluyendo www y TLD)
    Captura 3: Ruta (opcional)
    """
    patron = r'(https?:\/\/)?(www\.|[\w\.-]+)\.([\w]{2,})(\/.*)?'
    
    """Una version mas robusta y legible para este objetivo especifico:"""
    patron_robusto = r'(?P<protocolo>https?:\/\/)?(?P<dominio_completo>(?:www\.|[\w\.-]+)\.[\w]{2,})(?P<ruta>\/.*)?'
    
    urls_encontradas = re.finditer(patron_robusto, texto)
    
    resultados = []
    
    for i, match in enumerate(urls_encontradas, 1):
        """Obtenemos los grupos nombrados"""
        protocolo = match.group('protocolo') if match.group('protocolo') else ''
        dominio_completo = match.group('dominio_completo')
        ruta = match.group('ruta') if match.group('ruta') else ''
        
        """Grupo 0 es la coincidencia completa"""
        url_completa = match.group(0)
        
        """Limpieza de protocolo para la salida"""
        protocolo_limpio = protocolo.replace('://', '') if protocolo else 'Ninguno'
        
        """Extraccion del dominio simple (sin www., para el ejemplo)"""
        dominio_simple = dominio_completo
        if dominio_simple.startswith('www.'):
            dominio_simple = dominio_simple[4:]
        
        resultados.append({
            "url_completa": url_completa,
            "protocolo": protocolo_limpio,
            "dominio": dominio_completo,
            "ruta": ruta,
        })
        
    return resultados

"""Ejemplos de texto y dominios, url"""
textos_de_prueba = [
    "Revisa mi portafolio en mi-sitio.dev/proyectos/regex. Tambien puedes encontrarme en https://linkedin.com/in/mi-usuario. Para documentacion, consulta developer.mozilla.org.",
    " Busca en example.com/search?query=regex. Para la seccion de instalacion, ve a my-page.com/docs#installation."
]

print("\n--- Ejercicio 4: Extractor de URLs y Dominios ---")

"""
Bucle principal para procesar y mostrar los resultados:
- El primer bucle 'for' itera sobre la lista 'textos_de_prueba'. Se usa 'enumerate(..., 1)'
  para obtener un indice que empieza en 1 (Ejemplo 1, Ejemplo 2, ...).
- Para cada texto, se llama a la funcion 'extraer_urls_y_componentes' y se guardan
  los resultados.
- Se comprueba si la lista de 'resultados' esta vacia. Si es asi, se informa al usuario
  y se salta a la siguiente iteracion con 'continue'.
- El segundo bucle 'for' itera sobre cada diccionario de resultado encontrado para
  imprimir sus componentes (URL completa, protocolo, dominio y ruta) de forma
  estructurada y legible. La ruta solo se imprime si existe.
"""
for i, texto in enumerate(textos_de_prueba, 1):
    print(f"\n--- Analizando Ejemplo {i} ---")
    
    resultados = extraer_urls_y_componentes(texto)
    
    if not resultados:
        print("  No se encontraron URLs.")
        continue

    for j, res in enumerate(resultados, 1):
        print(f"  URL {j}: {res['url_completa']}")
        print(f"    Protocolo: {res['protocolo']}")
        print(f"    Dominio: {res['dominio']}")
        if res['ruta']:
            print(f"    Ruta: {res['ruta']}")

"""
Este script fue desarrollado y modificado con la asistencia de Gemini Code Assist.
"""