"""
Tipos de datos:
- bool -> True, False
- int -> 1, 2, 3...
- float -> 1.0, 2.0, 3.0...
- str -> 'hola', 'mundo'
- list -> [1, 2, 3]
- tuple -> (1, 2, 3)
- set -> set([1, 2, 3])
- dict -> dict({'a': 1, 'b': 2})

"""

# DATOS:

"""
Variables: Las variables permiten definir nombres para los valores que tenemos en memoria y que van a ser usados en nuestro programa. (nombre = valor)

-- Reglas para nombrar variables:
- Letras minúsculas
- No empezar con número
- Letras mayúsculas
- Dígitos
- Guiones bajos (_) -> snake_case
"""

"""
Asignación: En python se usa el símbolo = para asignar un valor a una variable.
"""
print("*** DATOS ***")

# Asignación de variables:
total_population = 157_503
avg_temperature = 10.0
city_name = "San Cristóbal de la Laguna"
# Asignación de constantes:
SOUND_SPEED = 343.2
WATER_DENSITY = 1000
EARTH_NAME = "Earth"
# Asignación múltiple:
tres = three = drei = "La tierra es " + EARTH_NAME
print(drei)

# Asignar una variable a otra variable:
people = 1321
total_population = people

# Conocer el valor de una variable:
print(total_population)

# Conocer el tipo de dato de una variable:
print(type(0))
print(type(1.2))

height = 13242
print(type(height))

name = "Juan"
print(type(name))

# Tipos de objetos según su naturaleza:
"""
Inmutable: bool, int, float, str, tuple, list, dict, set. (No se puede modificar)
Mutable: list, set, dict. (Se puede modificar)
"""

# NÚMEROS
print("*** NÚMEROS ***")
"""
True -> 1
False -> 0
"""
is_opened = True
print(is_opened)
is_closed = False
print(is_closed)

# Enteros
print(8)
print(-99)

"""
Operaciones con enteros:
+ - * / // % **

Prioridad de los operadores:
(), **, -a +a, * / // %, + -
"""

print(2 + 4 + 8)
print(2 - 4 - 8**2)
print(7 / 6)
print(7 // 6)

# Prioridad de los operadores:
print(2**4 / 2)
print(2 ** (2 + 4) / 2)
print(2 ** (2 + 4 / 2))

# Asignación aumentada: +=, -=, *=, /=, //=, %=
totalCars = 100
soldCars = 20
totalCars -= soldCars
print(totalCars)

# Módulo
dividendo = 17
divisor = 2
cociente = dividendo // divisor
resto = dividendo % divisor
print(cociente)
print(resto)

# Exponenciación:
print(f"{2**8.44:.2f}")

# valor absoluto:
print(abs(-10))
print(abs(3.14))

# Flotantes:
print(5.14)
print(7.1415)

"""
Conversión implícita: Cuando mezclamos enteros, booleanos y flotantes. Python realiza una conversión implícita de los valores al tipo de MAYOR RANGO.
"""
print(True + 25)
print(7 * False)
print(True + False)
print(21.8 + True)
print(10 + 11.3)

"""
Conversión explícita: Python ofrece funciones para convertir de un tipo a otro.
"""
print(bool(1))
print(bool(0))
print(int(True))
print(int(False))
print(float(1))
print(float(0))
print(float(True))
print(float(False))

# Con la función int() sobre un flotante retorna la parte más baja:
print(int(7.1415))
print(int(3.15))
print(int(3.9))

print("*** BASES BINARIAS ***")

# 2 símbolos para 0 y 1, prefijo: 0b
print(0b0010)
# Función bin() para convertir a binario
print(bin(9))
print(bin(15))

print("*** BASES OCTALES ***")

# 8 símbolos para 0 hasta 7, prefijo: 0o
print(0o6243)
# Función oct() para convertir a octal
print(oct(3225))
print(oct(687))

print("*** BASES HEXADECIMALES ***")

# 16 símbolos para 0 hasta F, prefijo: 0x
print(0x7F2A)
# Función hex() para convertir a hexadecimal
print(hex(18687))

# CADENAS DE TEXTO:

print("*** CADENAS DE TEXTO***")

poem = """Hay una forma "alternativa" de crear cadenas de texto y es utilizar comillas triples. Su uso está pensado principalmente para cadenas multilínea"""

secondPoem = "Hay una forma alternativa de crear 'cadenas de texto' y es utilizar comillas triples. Su uso está pensado principalmente para cadenas multilínea"

thirdPoem = "Hay una '¡forma!' alternativa de crear cadenas de texto y es utilizar comillas triples. Su uso está pensado principalmente para cadenas multilínea"

print(poem)
print(secondPoem)
print(thirdPoem)

# Cadena vacía -> ""

# CONVERSIÓN:
# Podemos crear strings a partir de otros tipos de datos usando la función str()
print(str(True))
print(str(10))
print(str(21.7))

# De string a número:
print(int("10"))
print(float("21.7"))

# Secuencias de escape:
"""
Salto de línea: \n.
Caracter de tabulación: \t.
Comillas simples: '
Comillas dobles: """
# Barra invertida: \\;
""""""
message = "Primera línea\nSegunda línea\nTercera línea"
print(message)
message = "valor = \t40"
print(message)
message = "Necesitas 'escapar' las comillas simples"
print(message)
message = 'Necesitas "escapar" las comillas dobles'
print(message)
message = "Necesitas \\ escapar las barras invertidas"
print(message)

# Expresiones literales: El modificador r"" es utilizado para las expresiones regulares.
text = "abc\ndef"
print(text)
text = r"abc\ndef"
print(text)
text = "a\tb\tc"
print(text)
text = r"a\tb\tc"
print(text)

"""
Leer datos desde el teclado: Leer información del teclado por parte del usuario se usa la función input()
"""
# name = input("Introduzca su nombre: ")
# age = input("Introduzca su edad: ")
# print(f"Hola {name}, tienes {age} años")

print("Operaciones con strings!")

# Combinar cadenas
proverb1 = "Cuando el rio suena"
proverb2 = "Agua lleva!"

print(proverb1 + ", " + proverb2)

# Repetir cadenas
reaction = "Hola "
print(reaction * 5)

# Obtener un carácter de una cadena
print(proverb1[3])
print(proverb1[-4])

# Trocear una cadena
proverb3 = "El gato de piedra"
print(proverb3[:-1])
print(proverb3[1:])
print(proverb3[1:3])
print(proverb3[-3:])

# Longitud de una cadena
length = len(proverb1)
print(length)

# Pertenencia de una cadena
proverb4 = "El gato de piedra"
print("Cuando" in proverb1)

# Limpiar una cadena -> Método strip() -> Elimina caracteres del principio y del final de una cadena
proverb5 = "Dios es mi pastor y nada me faltará"
cleaned = proverb5.strip()
print(cleaned)

# Realizar búsquedas -> startWith, endWith
print(proverb5.startswith("Dios"))
print(proverb5.endswith("pastor"))

# Encontrar la primera ocurrencia de una subcadena -> find(), index()
lyrics = "¡Ay, qué bonito es el agua!"
print(lyrics.find("bonito"))
index = lyrics.index("agua")
print(index)

# Contabilizar el número de veces que aparece una subcadena -> count()
phrase = "Estoy aprendiendo Python y también aprendiendo JavaScript"
print(phrase.count("aprendiendo"))

# Reemplazar una subcadena -> replace()
phrase2 = "Estoy aprendiendo React"
print(phrase2.replace("aprendiendo", "estudiando"))

# Mayúsculas y minúsculas -> upper(), lower(), title(), capitalize(), swapcase()
phrase3 = "Estoy aprendiendo React"
print(phrase3.upper())
print(phrase3.lower())
print(phrase3.title())
print(phrase3.capitalize())
print(phrase3.swapcase())

"""
Identificando caracteres: isalnum(), isalpha(), isdigit(), isnumeric(), islower(), isupper(), isspace(), istitle(), isprintable(), isascii(), isdecimal().
"""

# Detecta si todos los caracteres son letras y números
print("123abc".isalnum())
# Detecta si todos los caracteres son números
print("123abc".isdigit())
# Detecta si todos los caracteres son letras
print("abc".isalpha())
# Detecta mayúsculas y minúsculas
print("ABC".isupper())
print("abc".islower())

"""
Interpolación de cadenas: Las cadenas de texto pueden ser interpoladas en otras cadenas de texto usando el operador de interpolación de cadenas.

%, {}, .format(), %s, f""
"""

# f-strings
name = "José"
age = 35
print(f"Hola {name}, tienes {age} años")

# %s
print("Hola %s, tienes %s años" % (name, age))

# {} y .format()
print("Hola {}, tienes {} años".format(name, age))

# Comparar cadenas de texto
print("Hola" == "Hola")
print("Hola" != "Hola")
print("Hola" < "Hola")
print("Hola" > "Hola")
print("Hola" <= "Hola")
print("Hola" >= "Hola")

# Biblioteca random -> Genera números aleatorios
import random

aleatorio = random.randrange(1, 10)  # El número de stop no es incluyente.
aleatorio_par = random.randrange(2, 11, 2)  # Número par del 2 al 10 (incluído).
aleatorio_impar = random.randrange(1, 10, 2)  # Número impar del 1 al 9 (incluído).

print(aleatorio)
print(aleatorio_par)
print(aleatorio_impar)

aleatorio_prueba = random.randint(1, 10)
print(aleatorio_prueba)
