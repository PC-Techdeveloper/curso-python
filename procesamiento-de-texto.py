"""
El módulo 're' permite trabajar con expresiones regulares.

¿Qué es una expresión regular?
También conocida como regex o regexp, es una cadena de texto que conforma un patrón de búsqueda. Se utilizan principalmente para la búsqueda de patrones en cadenas de caracteres u operaciones de sustituciones 

Caracteres especiales:

. -> Coincide con cualquier caracter expecto una nueva línea.


^ -> Coincide con el comienzo de una cadena o línea.

$ -> Coincide con el final de una cadena o línea.

* -> Coincide con cero o más veces el caracter anterior.

+ -> Coincide con uno o más veces el caracter anterior.

? -> Coincide con cero o una veces el caracter anterior.

/ -> Permite escapar el caracter que le sigue. Es decir, quitarle el significado especial del caracter.

[] -> Coincide con el conjunto de caracteres entre los corchetes.

| -> Coincide con una expresión regular u otra, separada por el caracter |.

(...) -> Coincide con el grupo de caracteres entre los paréntesis.

(?P<name>...) -> Coincide con cualquier expresión regular que esté dentro de los paréntesis; el contenido del grupo de captura es accesible por name

(?:...) ->Coincide con cualquier expresión regular que esté dentro de los paréntesis pero no crea un grupo de captura

\number -> Coincide con el contenido del grupo del mismo número. Se usa en conjunción con (...)

\b -> Coincide con el comienzo o el final de una palabra

\B -> Coincide con cualquier caracter que no sea comienzo o final de una palabra

\d -> Coincide con cualquier dígito decimal. Equivalente a [0-9]

\D -> Coincide con cualquier carácter que no sea un dígito decimal. Equivalente a [^0-9]

\s -> Coincide con cualquier espacio en blanco. Equivalente a [ \t\n\r\f\v]

\S -> Coincide con cualquier carácter que no sea un espacio en blanco. Equivalente a [^ \t\n\r\f\v]

\w ->Coincide con cualquier carácter alfanumérico. Equivalente a [a-zA-Z0-9_]

\W -> Coincide con cualquier carácter que no sea un carácter alfanumérico. Equivalente a [^a-zA-Z0-9_]
"""

"""
Expresiones en crudo: 
Cuando definimos una expresión regular, es conveniente utilizar el formato raw en las cadenas de texto para que los caracteres especiales no pierdan su semántica.
"""

regex = r"\t[abc]$"
print(regex)

"""
Operacione:
"""

# Buscar:
import re

text = "Estaré disponible en el +573142439919 el lunes por la tarde"

regex = r"\+?\d{2}\d{9}"

# Esta función devuelve un objeto de tipos Match, con el resultado de span
# que indica el alcance de la coincidencia.
print(re.search(regex, text))

# findall(): Buscar todas las coincidencias de una expresión regular en una cadena de texto.

text = "El coste ascendió a 36€ más un 12% de impuestos para un total de 40€ "

print(re.findall(r"\d+€ ", text))

# Utilizando un grupo de captura, podemos extraer el contenido de cada coincidencia. -> (?:...) sin capturar grupos.

print(re.findall(r"(\d+)€", text))

"""
Coincidencia:
El tipo de objeto Match es utilizado en este módulo para representar una coinicidencia de una expresión regular.
"""

text = "Estaré disponible en el +34755142009 el lunes por la noche"

regex = r"\+?\d{2}\d{9}"

m = re.search(regex, text)

print(m)

# Accessing the match object's attributes:
print(m[0])
print(m.group(0))

# Conocer donde empieza y termina la coincidencia:

# Accediengo por separado:
print(m.start())
print(m.end())
print(m.span())  # Equivale a m.span(0)

"""
Grupos de captura:

Los grupos de captura permiten extraer partes de la expresión regular para luego acceder a cada una de forma directa e independiente.
"""

m = re.search((r"\+?(\d{2})(\d{9})"), text)

# Acceder a los grupos capturados:
# Equivale a m.group(1), m.group(2)
print(m[1])
print(m[2])

# Acceder a los índices de comienzo y fin de cada grupo de captura:
print(m.span(1))
print(m.span(2))

# Aproximación más semántica añadiendo nombres a los grupos de captura:
regex = r"\+?(?P<prefix>\d{2})(?P<number>\d{9})"
m = re.search(regex, text)

# Con el cambio podemos acceder a los grupos de captura por su nombre
# Equivale a m.group("prefix"), m.group("number")
print(m["prefix"])
print(m["number"])

# Obtener el diccionario completo de los grupos de captura
print(m.groupdict())

"""
Ignorar mayúsculas y minúsculas: re.IGNORECASE
"""
name = "Alan Turing"
# Encuentra todas las vocales del nombre:
regex = r"[aeiou]"

print(re.findall(regex, name, re.IGNORECASE))

# También se puede abreviar de la siguiente manera:
print(re.findall(r"[aeiou]", name, re.I))

"""
Separar o dividir cadenas de texto: re.split()
"""

regex = r"[.,]"
print(re.split(regex, "3.14"))
print(re.split(regex, "3,14"))

# Es mejor capturar el separador:
# Con los paréntesis se añade el grupo de captura
regex = r"([.,])"
print(re.split(regex, "3.14"))
print(re.split(regex, "3,14"))

"""
Reemplazar: Reemplazar ocurrencias dentro de un texto.
"""

name = "Alan Turing"

regex = r"(\w+) +(\w+)"

replaced = r"\2, \1"
# Formato apellido, nombre
print(re.sub(regex, replaced, name))

# Posibilidad de nombrar los grupos de captura
name = "Alan Turing"

regex = r"(?P<name>\w+), +(?P<surname>\w+)"

repl = r"\g<surname>, \g<name>"
print(re.sub(regex, repl, name))

# Podemos para una función en vez de una cadena de texto
name = "Alan Turing"

regex = r"(\w+) +(\w+)"

# Existe una función re.subn() que devuelve una tupla con los resultados de las sustituciones
repl = re.sub(regex, lambda m: f"{m[2].upper()}, {m[1].title()}", name)
print(repl)

"""
Casar: Si lo que se desea buscar es ver una determinada cadena de texto coincide con un patrón de expresión regular, podemos utilizar la función re.fullmatch().
"""

regex = r"\d{8}[A-Z]"
text = "54632178Y"
# Si el patrón no casa con ninguna coincidencia, devuelve None
print(re.fullmatch(regex, text))


# Dando uso de una sentencia condicional y el operador morsa
def checkIdCard(text: str) -> None:
    REGEX = r"\d{8}[A-Z]"
    if match := re.fullmatch(REGEX, text):
        print(f"{text} es un DNI válido!")
        print(match.span())
    else:
        print(f"{text} no es un DNI válido")


checkIdCard("54632178Y")
checkIdCard("54632178Z$")

"""
Hay una variable más flexible para casar y es re.match() y comprueba si la existencia del patrón sólo desde el comienzo de la cadena. Es decir, que si el final de la cadena no coincide sigue casando.
"""

regex = r"\d{8}[A-Z]"

text = "54632178Y###"

print(re.match(regex, text))

# Sin embargo, no sucede lo mismo si se añade un caracter al principio y al final de la cadena.

regex = r"\d{8}[A-Z]"

text = "&&54632178Y###"

# is None, no casa
print(re.match(regex, text) is None)

# Se puede obligar al indicar el comienzo y el final de la línea.
regex = r"^\d{8}[A-Z]$"

text = "54632178Y"
print(re.match(regex, text))

"""
Compilar una expresión regular: re.compile() para mejorar el rendimiento.
"""

regex = r"\d+"

pat = re.compile(regex)
print(type(pat))
print(pat, "1:abc;10:def;20:ghi")
