
import re
import matplotlib.pyplot as plt

def validar_correo_simple(correo: str) -> bool:
    """
    Valida si una cadena es un correo electronico simple (usuario@dominio.tld).
    """
    patron = r"[\w\.-]+@[\w\.-]+\.\w{2,}"
    if re.fullmatch(patron, correo):
        return True
    else:
        return False

# Leer el archivo de correos
correos = []
with open("../../../Downloads/Laboratorio Expresiones regulares-20251004/correos.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            # Separar por '. ' para obtener el correo después del número
            parts = line.split('. ', 1)
            if len(parts) == 2:
                email = parts[1]
                correos.append(email)

validos = 0
invalidos = 0
for correo in correos:
    es_valido = validar_correo_simple(correo)
    if es_valido:
        validos += 1
    else:
        invalidos += 1

print(f"Total de correos válidos: {validos}")
print(f"Total de correos inválidos: {invalidos}")

# Generar gráfico de barras
plt.bar(['Válidos', 'Inválidos'], [validos, invalidos], color=['green', 'red'])
plt.title('Validación de Correos Electrónicos')
plt.ylabel('Cantidad')
plt.show()

"""
Este script fue desarrollado y modificado con la asistencia de Gemini Code Assist.
"""
