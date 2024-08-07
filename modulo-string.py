"""
El módulo de 'string' proporciona una serie de constantes muy útiles para manejo de strings, a demás de distintas estrategias de formateado de cadenas de texto.
"""

"""
CONSTANTES:
"""
import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.whitespace)
print(string.printable)

"""
PLANTILLAS: El módulo string también proporciona plantillas con interpolación de variables. Algo similar a las f-strings.
"""
from string import Template

template1 = Template("$lang is the best programming language in the $place!")

# Realizando las sustituciones
print(template1.substitute(lang="Python", place="Earth"))
# También se puede pasar con un diccionario
print(template1.substitute({"lang": "Python", "place": "Earth"}))

# Utilizar llaves para evitar la ambiguedad
template2 = Template("You won several ${price}s")
print(template2.substitute(price="phone"))

urlBase = Template("https://python.org/3/library/$module.html")

for module in ("string", "re", "difflib"):
    url = urlBase.substitute(module=module)
    print(url)
