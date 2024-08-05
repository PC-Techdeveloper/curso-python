"""
LISTAS: Una lista está compuesta por cero o más elementos, separados por comas y dentro de corchetes. y Son mutables.
"""

empty_list = []

languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "PHP", "Go"]
fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
data = ["Tenerife", {"cielo": "limpio", "temperatura": 25.0}, 1212, (234.34, 16.234324)]

# Conversión: Para convertir otros tipos de datos en una lista, usamos la función list()

print(list("Java"))

# Lista explícita con la función range()
print(list(range(10)))

# Lista vacía -> list() -> []

print("Operaciones con listas:")

# Obtener un elemento
shopping = ["agua", "huevos", "aceite", "queso", "pan", "mortadela", "arroz"]

print(shopping[-2])

# Trocear una lista
shopping = ["agua", "huevos", "aceite", "queso", "pan", "mortadela", "arroz"]
print(shopping[0:3])
print(shopping[3:])
print(shopping[:3])
print(shopping[-1:-4:-1])

# Invertir una lista: Mediante el troceado
print(shopping[::-1])
# Mediante la función reverse()
lista_reversa = list(reversed(shopping))
print(lista_reversa)


"""
Modificando la lista original:
"""
shopping2 = ["agua", "huevos", "aceite", "sal", "limón"]
shopping2.reverse()
print(shopping2)

"""
Añadir un elemento al final de la lista:
"""
shopping2.append("lechuga")
print(shopping2)

"""
Crear una lista iniciando como vacía:
"""
even_numbers = []

for i in range(20):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

"""
Añadir elementos en cualquier posición de la lista:
"""

shopping2.insert(2, "Jamón")
print(shopping2)

"""
Repetir elementos: *
"""
shopping3 = ["galletas", "sandia", "pera", "manzana", "papaya"]
print(shopping3 * 3)

"""
Combinar litas:
"""

# Mediante el operador + o +=
shopping4 = ["GALLETAS", "SANDIA", "PAPAYA"]
fruit_shop = ["NARANJA", "MANZANA", "PIÑA"]
# shopping4 += fruit_shop
# print(shopping4)

# # Mediante la función extend()
shopping4.extend(fruit_shop)
# extend() itera sobre los elementos de la lista pasada como argumento
shopping4.extend("LIMÓN")
print(shopping4)

"""
Modificar un elemento de la lista:
"""
shopping4[0] = "CRISPETAS"
print(shopping4)

# Modificar con troceado:
shopping4[1:4] = ["ATÚN", "PIZZA"]
print(shopping4)

"""
Borrar elementos de la lista:
"""
# Por su índice:
shopping5 = ["costilla", "carne", "pollo", "tocineta", "hamburguesa"]

del shopping5[0]  # costilla
print(shopping5)

# Por su valor: remove() -> Si existen valores duplicados, solo elimina la primer ocurrencia.
shopping5.remove("carne")
print(shopping5)

# Por su índice con extracción: pop() -> Elimina el último elemento y devuelve el valor.
last_item = shopping5.pop()
print(shopping5)

# Por su rango: Mediante el troceado
shopping6 = ["celular", "teléfono", "computadora", "tableta", "laptop"]
shopping6[0:2] = []
print(shopping6)

# Borrado completo: clear() -> Elimina todos los elementos de la lista.
# shopping6.clear()

# Reinicializar la lista a vacía: []
# shopping6[] = []

"""
Encontrar elementos en una lista:
"""

# Por su índice:
shopping7 = ["doctor", "profesor", "doctora", "profesora", "veterinaria"]

print(shopping7.index("profesora"))

"""
Pertenencia a una lista: Devuelve un valor booleano.
"""
print("doctor" in shopping7)

"""
Número de veces que se repite un elemento en una lista: count() -> Devuelve el número de veces que aparece un elemento en una lista.
"""
# Count()
sheldon_greeting = ["Penny", "Penny", "Amy", "Amy", "Amy", "Penny", "Penny"]
print(sheldon_greeting.count("Penny"))

"""
Dividir una cadena de texto en una lista: split(), devuelve una lista donde cada elemento es una parte de la cadena dividida por el delimitador.
"""

proverb = "No hay mal que por bien no venga"
words = proverb.split()
print(words)

tools = "destornillador,sierra,martillo,chuchillo"
tools.split(",")
print(tools)

game = "piedra-papel-tijera"
print(type(game_tools := game.split("-")))
print(game_tools)

"""
Particionado de cadenas de texto:
"""
text = "3 + 4"
print(text.partition("+"))

"""
Unir una lista en cadena de texto: Función join() mediante un separador.
"""
video_games = ["chess", "poker", "mahjong", "go"]
joined_games = "--".join(video_games)

print(joined_games)

"""
Ordenar una lista: sort() y sorted()
"""
# Conservando la lista original: sorted() ordena de manera descendente.
my_games = ["chess", "poker", "mahjong", "go"]

sorted(my_games)

print(my_games)

# Modificando la lista original: sort()
# Ordena de manera ascendente:
my_games.sort()

print(my_games)

# reverse(): Invertir el orden en sentido contrario.
print(sorted(my_games, reverse=True))

# Longitud de una lista: len()
print(len(my_games))

"""
Iterar sobre una lista: for
"""
for games in my_games:
    print(games)

# Iterar usando enumeración: enumerate() para conocer el índice del elemento
for i, games in enumerate(my_games):
    print(i, games)

"""
Iterar sobre múltiples listas: zip()

Python ofrece la posibilidad de iterar sobre múltiples listas en paralelo utilizando la función zip(). Se basa en ir «juntando» ambas listas elemento a elemento:
"""
shoppings = ["agua", "aceite", "arroz"]
details = ["mineral natural", "de oliva virgen", "basmati"]

for shopping, detail in zip(shoppings, details):
    print(f"{shopping} {detail}")

# Obteniendo una lista explícita:
print(list(zip(shoppings, details)))

"""
Comparar listas:
"""
print([1, 2, 3] > [4, 5, 6])

"""
Copiar una lista: copy()
"""
original_list = [1, 2, 3]
copied_list = original_list.copy()

original_list[1] = 10
print(original_list)
print(copied_list)

"""
Veracidad mútliple: Python nos ofrece dos funciones «built-in» con las que podemos evaluar si se cumplen todas las condiciones all() o si se cumple alguna condición any(). Estas funciones trabajan sobre iterables, y el caso más evidente es una lista.
"""

# all() -> Comprueba que se cumplan todas las expresiones:
word = "Python"

enough_length = len(word) > 4

right_beginning = word.startswith("Py")
min_ys = word.endswith("on")

is_cool_word = all([enough_length, right_beginning, min_ys])

if is_cool_word:
    print("¡Es un buen término!")
else:
    print("No gracias, no es un buen término")

# any() -> Comprueba que se cumpla alguna de las expresiones:
word = "Python"

enough_length = len(word) > 4
right_beginning = word.startswith("P")
min_ys = word.count("t") >= 1

is_fine_word = any([enough_length, right_beginning, min_ys])

if is_fine_word:
    print("¡FINE WORD! 👍")
else:
    print("NO THANKS 🙁")

"""
Listas por comprensión: Las listas por comprensión establecen una técnica para crear listas de forma más compacta basándose en el concepto matemático de conjuntos definidos por comprensión.
"""

# Versión clásica
values = "33,55,67,89,23,45"
int_values = []

for value in values.split(","):
    int_value = int(value)
    int_values.append(int_value)

print(int_values)

# Versión por comprensión
values = "33,55,67,89,23,45"
int_values = [int(value) for value in values.split(",")]
print(int_values)

# Condiciones en comprensiones
values = "33,55,67,89,47,45"
int_values = [int(value) for value in values.split(",") if value.startswith("4")]
print(int_values)

# Anidamients en comprensiones
values = "33,55,67,89,47,45"
s_values = values.split(",")

combinations = [f"{v1}x{v2}" for v1 in s_values for v2 in s_values]
print(combinations)

"""
Sys.argv:

Cuando queramos ejecutar un programa Python desde línea de comandos, tendremos la posibilidad de acceder a los argumentos de dicho programa. Para ello se utiliza una lista «especial» que la encontramos dentro del módulo sys y que se denomina argv:
"""

# import sys

# number = int(sys.argv[1])
# to_base = int(sys.argv[2])

# match to_base:
#     case 2:
#         result = f"{number:b}"
#     case 8:
#         result = f"{number:o}"
#     case 16:
#         result = f"{number:x}"
#     case _:
#         result = None

# if result is None:
#     print(f"Base {to_base} no soportada")
# else:
#     print(result)

"""
Funciones matemáticas: 🟨
"""

# Suma todos los valores: sum()
data = [1, 2, 3, 4, 5]
print(sum(data))

# Minímo de todos los valores: min()
second_data = [5, 3, 8, 9, 1]
print(min(second_data))

# Máximo de todos los valores: max()
third_data = [5, 3, 8, 9, 1]
print(max(third_data))

"""
Lista de listas:
"""

goal_keeper = "cata"

defenders = ["olga", "laila", "irene", "ona"]

midfielders = ["jeni", "teresa", "aitana"]

forwards = ["mariona", "salma", "alba"]

team = [goal_keeper, defenders, midfielders, forwards]
print(team)

# Accesso a elementos de una lista de listas:
print(team[3][1])

# Recorrer una lista de listas:

for play_line in team:
    if isinstance(play_line, list):
        for player in play_line:
            print(player, end=" ")
    else:
        print(play_line)

"""
TUPLAS: Una tupla no admite cambios y por lo tanto, es inmutable.
"""
print("\n")
print(f"---- TUPLAS ----")

# Creando tuplas
emtpy_tuple = ()

tenerife_geoloc = (28.2423, -16.234234)

three_wise_men = ("melchor", "gaspar", "baltasar")

one_element_tuple = "aprendiendo python"

# Modificar una tupla: ❌ No se puede modificar una tupla.

# three_wise_men[0] = "Tom and Jerry"
# print(three_wise_men)

# Coversión:
# Lista a tuppla:
shopping9 = ["agua", "aceite", "papaya"]

# Iterables: str, list, dict, set, etc. ✅
# number ❌
shopping10 = tuple(shopping9)

print(shopping10)

# El uso de la función tuple() sin argumentos devuelve una tupla vacía.
empty_tuple = ()
print(empty_tuple)

"""
Operaciones con tuplas:

reverse(), append(), extend(), remove(), clear(), sort()
"""

"""
Desempaqueado de tuplas: El desempaquetado es una característica de las tuplas que permite asignar una tupla a variables independientes.
"""

my_tuple = ("jefferson", "mario", "jorge")

king1, king2, king3 = my_tuple
print(king1, king2, king3)

# divmod() devuelve el cociente y el resto de una división para el desempaquetado.

quotient, remainder = divmod(10, 3)
print(quotient, remainder)

# Intercambio de valores mediante el desempaquetado:

value1 = 10
value2 = 40

value1, value2 = value2, value1

print(value1, value2)

"""
Desempaquetado extendido: Operador *
"""

ranking = ("G", "A", "R", "Y", "W")

head, *body, tail = ranking

print(head, body, tail)

print(len(ranking))

"""
Desempaquetado genérico: 
- Tipos de datos iterables: str, list, dict, set, etc.
"""
# Sobre cadenas de texto:
oxygen = "O2"
first, last = oxygen
print(first, last)

text = "Hola, mundo!"
head, *body, tail = text
print(head, body, tail)

# Sobre listas:
writer1, writer2, writer3 = ["John", "Mary", "Peter"]
print(writer1, writer2, writer3)

"""
Tuplas vs Listas: 

- La tuplas ocupan menos espacio en memoria.
- En las tuplas exite protecciín frente a cambios indeseados.
- Las tuplas se pueden usar como claves de diccionarios.
"""
print("\n")
print("---- DICCIONARIOS ----")

"""
Los diccionarios en Python tienen las siguientes características:

- Mantienen el orden en el que se insertan las claves.
- Son mutables, con lo que admite añadir, borrar y modificar sus elementos.
- Las claves deben ser únicas. Pueden ser cualquier tipo de datos inmutables.
- Tienen un acceso rápido a sus elementos, debido a la forma en la que están implementados internamente.
"""

# Creando diccionarios
empty_dict = {}

rae = {
    "bifronte": "de dos frentes o dos caras",
    "anarcoide": "que tiende al desorden",
    "montuvio": "campesino de la costa",
}

population_can = {
    2015: 3693000,
    2016: 3713000,
    2017: 3733000,
    2018: 3753000,
}

"""
Conversión: Para convertir otros tipos de datos en un diccionario, usamos la función dict()
"""
# A partir de una lista
print(dict(["a1", "b2"]))
# A partir de una tupla
print(dict(("a1", "b2")))
# A partir de una lista de listas <- lista de tuplas
print(dict([["a1", 1], ["b2", 2]]))

# diccionario vacío: {}, dict()

# Creación con dict: Pasar clave y valor como argumentos

person = dict(
    name="Juan",
    sur_name="Perez",
    job="Software Engineer",
)

print(person)

# Crear un diccionario especificando sus claves y un único valor de relleno
print(dict.fromkeys("aeiou", 0))

"""
Operaciones con diccionarios:
"""

# Obtener un elemento
print(rae["bifronte"])

print(rae.get("bifronte"))

print(person["name"])

# Añadir o modificar un elemento:
rae["enjuiciar"] = "someter una cuestión a examen, discusión y juicio"

rae["enjuiciar"] = "instruir, juzgar o sentenciar una causa"

print(rae)

"""
Creando desde vacío:
"""

VOWELS = "aeiou"

enum_vowels = {}

for vowel in enumerate(VOWELS, start=1):
    enum_vowels[vowel] = 1

print(enum_vowels)

"""
Pertenencia de una clave: La forma pitónica de comprobar la existencia de una clave dentro de un diccionario, es utilizar el operador in.
"""

print("a" in rae)

print("c" in person)

# Longitud de un diccionario: len()
print(len(rae))

"""
Obtener todos los elementos de un diccionario:

métodos: keys(), values(), items()
"""

print(rae.keys())

print(rae.values())

print(rae.items())

"""
Iterar sobre un diccionario: for
"""

# Iterar sobre las claves:
for word in rae.keys():
    print(word)

# Iterar sobre los valores:
for meaning in rae.values():
    print(meaning)

# Iterar sobre las claves y los valores:
for word, meaning in rae.items():
    print(f"{word}: {meaning}")

"""
Borrar elementos de un diccionario:
"""

# Por su clave: del

del rae["anarcoide"]
print(rae)

# Por su valor (con extracción): pop()

print(rae.pop("bifronte"))

# Borrado completo: clear()

rae.clear()

rae = {}

print(rae)

"""
Combinar diccionarios:
"""

rae1 = {
    "casa": "en el interior",
    "cocina": "en el exterior",
    "sala": "en una parte",
}

rae2 = {
    "comedor": "en el interior",
    "mesa": "en el exterior",
    "silla": "en una parte",
}

# SIN MODIFICAR LOS DICIONARIOS ORIGINALES:

# Con el operador **
combination1 = {**rae1, **rae2}
print(combination1)

# Con el operador |
combination2 = rae1 | rae2
print(combination2)

# MODIFICANDO LOS DICIONARIOS ORIGINALES:

# Mediante la función update()

rae1.update(rae2)
print(rae1)

"""
Copia de diccionarios: copy()
"""
original_dict = {
    "perro": "animal de compañía",
    "gato": "son más grandes que los perros",
    "cachorro": "son más grandes que los gatos",
}

copied_dict = original_dict.copy()

original_dict["cachorro"] = "bla bla bla"

print(original_dict)
print(copied_dict)

"""
Diccionarios por comprensión: Usando las llaves -> {}
"""

words = ("sun", "space", "rocket", "earth", "moon")

word_length = {word: len(word) for word in words}

print(word_length)

# Condiciones en diccionarios por comprensión

words2 = ("sun", "space", "rocket", "earth", "moon")

word_length2 = {word: len(word) for word in words2 if word[0] not in "aeiou"}

print(word_length2)

"""
CONJUNTOS: Representa una serie de valores únicos y sin orden establecido.
"""

print("\n")
print(f"---- CONJUNTOS ----")

# Creando conjuntos:
lottery = {1, 2, 45, 67, 99, 100}

print(lottery)

# Conjunto vacío: set()

empty_set = set()

print(empty_set)

# Conversiones:

print(set("aplatanada"))

print(set([1, 33, 3, 3, 4, 4, 4, 6, 6, 6]))

print(set(("ADENINA", "TIMINA", "TIMINA", "GUANINA", "ADENINA", "CITOSINA")))

print(set({"manzana": "apple", "melocotón": "watermelon", "pera": "pear"}))

"""
Operaciones con conjuntos:

- Obtener un elemento: En un conjunto, no existe un orden establecido para los elementos, por lo tanto, no permite acceder a un elemento en concreto.

- Igualmente no permite modificar un elemento existente.

- Permite añadir o borrar elementos de un conjunto.

AÑADIR UN ELEMENTO:

Para añadir un elemento a un conjunto, se utiliza la función add().
"""

# Añadir un elemento a un conjunto:

beatles = set(["lennon", "mccartney", "harrison", "starr"])

beatles.add("pete best")

print(beatles)

periodic_table = set()

metals = ("Fe", "Ni", "Co", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr")

periodic_table.add(metals)

non_metals = ("H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne")
periodic_table.add(non_metals)
print(periodic_table)

"""
Borrar elementos:

- Para borrar un elemento de un conjunto, se utiliza la función remove().
"""

beatles.remove("lennon")

print(beatles)

# Longitud de un conjunto: len()
print(len(beatles))

# Iterar sobre un conjunto: for

for element in beatles:
    print(element)

# Pertenencia a un conjunto: in

print("pete best" in beatles)

print("mccartney" not in beatles)

"""
Ordenando un conjunto:
"""

marks = {8, 9, 4, 6, 2, 5}

sorted_marks = sorted(marks)

print(sorted_marks)


"""
TEORÍA DE CONJUNTOS:

- Intersección: Elementos que están a la vez en A y en B.
- Unión: Elementos que están tanto en A como en B.
- Diferencia: Elementos que están en A pero no están en B.
- Diferencia simétrica: Elementos que están en A o en B pero no están en ambos.

- Inclusión: 
* Un conjunto B es un subconjunto de otro conjunto A si todos los elementos de B están incluidos en A.

* Un conjunto A es un superconjunto de otro conjunto B si todos los elementos de B están incluidos en A.
"""

A = {1, 2}
B = {2, 3, 4}

# Intersección
print(A & B)
print(A.intersection(B))

# Unión
print(A | B)
print(A.union(B))

# Diferencia
print(A - B)
print(A.difference(B))

# Diferencia simétrica
print(A ^ B)
print(A.symmetric_difference(B))

# Inclusión
A = {1, 2, 3, 4, 5}
B = {2, 3, 4, 6, 7}

# subconjunto
print(B < A)
print(B.issubset(A))

print(B <= A)

# superconjunto
print(A > B)
print(A.issuperset(B))

print(A >= B)

"""
Conjuntos por comprensión: 
"""
# Números impares
m3 = {number for number in range(0, 20) if number % 3 == 0}
print(m3)

"""
Conjuntos inmutables: Python ofrece la posibilidad de crear conjuntos inmutables haciendo uso de la función frozenset().
"""

my_marks = [1, 3, 2, 3, 1, 4, 2, 4, 5, 2, 5, 5, 3, 1, 4]

marks_levels = frozenset(my_marks)
print(marks_levels)

# Piezas de ajedrez:
CHESS_PIECES = frozenset(("king", "queen", "bishop", "knight", "rook", "pawn"))

print(CHESS_PIECES)
