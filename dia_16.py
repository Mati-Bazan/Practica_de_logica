# Expresiones regulares
# Analizan cadenas de texto | buscar | validar 

import re # Importa Expresiones regulares

regex = r"\d+" #  Tiene que empezar con r | "\d" detecta todos los numeros
# r"[0-9]+" = "[0-9]" detecta numeros del 0 al 9 | "+" los nuemeros pueden aparecer mas de una vez

text = "Este es el ejercicio 16 publicado el 15/04/2024"
text_two = "Hola me llamo Matias"

# Funcion que recibe cadena de texto y retorna una lista 
def find_num(text: str) -> list:
    return re.findall(regex, text) # "re.findall" busca todas las coincidencias

print(find_num(text)) # ['16', '15', '04', '2024']
print(find_num(text_two)) # []

"""
Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
"""
# Validar un email
def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))

print(validate_email("mati.bazan97@gmail.com")) # True
print(validate_email("mati.bazan97gmail.com")) # False

# Validar un número de teléfono
def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))

print(validate_phone("911")) # True
print(validate_phone("+54 12357787")) # True

# Validar una url
def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))

print(validate_url("https://moure.dev")) # True