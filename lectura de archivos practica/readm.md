## lectura de archivo de correo##
## Importación de Módulos
python
import re
import matplotlib.pyplot as plt
import re: Importa el módulo de expresiones regulares de Python. Este módulo es fundamental para definir el patrón de un correo electrónico y comprobar si una cadena de texto coincide con él.
import matplotlib.pyplot as plt: Importa la biblioteca matplotlib, que es una de las más populares en Python para crear gráficos y visualizaciones de datos. Se le asigna el alias plt por convención, para que sea más corto y fácil de usar en el resto del código.
## Definición de la Función de Validación
python
 Show full code block 
def validar_correo_simple(correo: str) -> bool:
    """
    Valida si una cadena es un correo electronico simple (usuario@dominio.tld).
    """
    patron = r"[\w\.-]+@[\w\.-]+\.\w{2,}"
    if re.fullmatch(patron, correo):
        return True
    else:
        return False
Función: Este bloque define una función llamada validar_correo_simple que toma una cadena de texto (correo) y devuelve True si es un correo válido o False si no lo es.
patron: Contiene la expresión regular que define la estructura de un correo electrónico.
re.fullmatch(patron, correo): Esta es la operación clave. Comprueba si la cadena correo coincide completamente con el patron definido. Es estricto, por lo que toda la cadena debe ajustarse al patrón, sin caracteres sobrantes.
return True / False: Devuelve el resultado de la validación.
Nota de mejora: Esta función es una copia de la que se encuentra en ejercicio_1.py. En un proyecto más grande, sería mejor importar la función desde el otro archivo para no duplicar código. Por ejemplo: from ejercicio_1 import validar_correo_simple.

 ## Lectura y Procesamiento del Archivo de Correos
python
 Show full code block 
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
correos = []: Se inicializa una lista vacía que se usará para almacenar las direcciones de correo electrónico extraídas del archivo.
with open(...) as f:: Este es el método recomendado en Python para abrir y leer archivos. Abre el archivo correos.txt en modo lectura ("r") y con la codificación utf-8 (para manejar caracteres especiales). La estructura with asegura que el archivo se cierre automáticamente al finalizar, incluso si ocurren errores.
for line in f:: Se itera sobre cada línea del archivo.
line = line.strip(): Elimina cualquier espacio en blanco o salto de línea al principio y al final de la línea.
if line:: Se asegura de no procesar líneas vacías.
parts = line.split('. ', 1): Esta es la parte clave del procesamiento. Asume que cada línea tiene un formato como "1. correo@ejemplo.com". El método split('. ', 1) divide la línea en dos partes usando ". " como separador, pero lo hace solo una vez (1). El resultado es una lista, por ejemplo: ['1', 'correo@ejemplo.com'].
if len(parts) == 2:: Comprueba que la división haya producido exactamente dos partes (el número y el correo).
email = parts[1]: Extrae la segunda parte de la lista, que es la dirección de correo.
correos.append(email): Añade el correo extraído a la lista correos.
## Conteo de Correos Válidos e Inválidos
python
 Show full code block 
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
validos = 0, invalidos = 0: Se inicializan dos contadores para llevar la cuenta de los correos que pasan la validación y los que no.
for correo in correos:: Se recorre la lista de correos que se extrajo en el paso anterior.
es_valido = validar_correo_simple(correo): Para cada correo en la lista, se llama a la función de validación.
if es_valido:: Si la función devuelve True, se incrementa el contador validos. De lo contrario, se incrementa invalidos.
print(...): Al final del bucle, se imprimen en la consola los totales de correos válidos e inválidos.
## Generación del Gráfico
python
# Generar gráfico de barras
plt.bar(['Válidos', 'Inválidos'], [validos, invalidos], color=['green', 'red'])
plt.title('Validación de Correos Electrónicos')
plt.ylabel('Cantidad')
plt.show()
plt.bar(...): Esta función de matplotlib crea un gráfico de barras.
El primer argumento ['Válidos', 'Inválidos'] son las etiquetas para el eje X (cada barra).
El segundo argumento [validos, invalidos] son los valores (alturas) de cada barra.
color=['green', 'red'] asigna un color a cada barra respectivamente.
plt.title(...): Establece el título principal del gráfico.
plt.ylabel(...): Define la etiqueta para el eje Y (vertical).
plt.show(): Muestra la ventana con el gráfico generado. Sin esta línea, el gráfico se crearía en memoria pero no sería visible.
