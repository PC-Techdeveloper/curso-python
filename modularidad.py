"""
Funciones: Una función viene definida por su nombre, sus parámetros y su valor de retorno.

Objetivos:
- No repetir fragmentos de código en un programa.
- Reutilizar el código en distintos escenarios.
"""


# Definición de una función: Definir antes de ser llamada.
def say_hello():
    print("Hello World!")


# Invocar una función:
say_hello()

"""
Retornar un valor: Las funciones pueden retornar o devolver un valor.
"""


def one():
    return 1


print(one())

# value = one()
# print(value)

# En condiciones:
if one() == 1:
    print("Excelente trabajo ✅!")
else:
    print("Incorrecto, algo está roto ❌.")

# Si una función no incluye un 'return' devolverá 'None' de forma implícita.


def empty():
    x = 0


print(empty())

# Usar la sentencia 'return' a secas hace que se se salga inmediatamente de la función.
# También devulve 'None'.


def quick_return():
    return


print(quick_return())

"""
Retornando múltiples valores: Una función puede retornar más de un valor, el secreto es hacerlo mediante una tupla.
"""


def multiple():
    return 0, 1  # Es una tupla!✔


result = multiple()

print(result)
print(type(result))

# Por lo tanto, permite el desempaquetado de la tupla.
x, y = multiple()

print(x)
print(y)

"""
Parámetros y argumentos: Los parámetros permiten variar los datos que consume una función para obtener distintos resultados.
"""


# Parámetros -> (value)
def sqrt(value):
    return f"Raíz cuadrada de {value}: {value ** (1 / 2):.2f}"


# Argumentos -> (4)
print(sqrt(15))

# La sentencia 'pass' permite no hacer nada en una función.


def _min(a, b):
    if a < b:
        return a
    return b


print(_min(7, 9))

"""
Argumentos posicionales: Los argumentos posicionales son aquellos argumentos que se copian en sus correspondientes parámetros por orden de escritura.
"""


# Mapeo en el mismo orden de escritura:
def buil_cpu(vendor, num_cores, freq):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


# Llamada con argumentos posicionales:
# Un error en el orden de escritura puede producir resultados inesperados.
print(buil_cpu("AMD", 8, 4.2))

"""
Argumentos nominales: Los argumentos nominales no son copiados en un orden específico, sino que se asignan por nombre a cada parámetro.
"""


# Retorna un diccionario con los argumentos nominales.
def second_build_cpu(vendor, num_cores, freq):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


# El orden de los argumentos no importa.
print(second_build_cpu(num_cores=8, freq=4.2, vendor="AMD"))

"""
Argumentos posicionales y nominales: Python permite mezclar argumentos posicionales y nominales en la llamada de una función.

- NOTA: Los argumentos posicionales siempre deben ir antes de los argumentos nominales.
"""

result_cpu = second_build_cpu("AMD RYSEN 5", num_cores=12, freq=5.8)
print(result_cpu)

"""
Argumentos mutables e inmutables: 

Mutables: listas, diccionarios, conjuntos, ...
Inmutables: tuplas, enteros, flotantes, cadenas de texto,...
"""


# Función que recibe una lista y devuelve sus valores elevados al cuadrado:
def square_list(list):
    return [number**2 for number in list]


print(square_list([1, 2, 3, 4, 5]))

"""
Parámetros por defecto: Especifíca valores por defecto para los parámetros de una función.
"""


def my_cpu(vendor, num_cores, freq=3.2):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


# Sin especificar valores por defecto:
print(my_cpu("AMD", 12))

# Especificando valores por defecto:
print(my_cpu("AMD", 12, freq=7.2))

"""
Modificando parámetros mutables: Utilizando un parámetro con valor por defecto con un tipo de dato inmutable y tener en cuenta cuál es la primer llamada:
"""


def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nonbuggy("a", ["b", "c", "d"])

"""
Empaquetar/Desempaquetar argumentos posicionales:
Al utilizar el operador * delante del nombre de un parámetro posicional, indica que los argumentos pasados a la función se empaquetarán en una tupla.
"""


# Empaquetando argumentos posicionales:
def _sum(*values):
    print(f"{values=}")
    result = 0

    for value in values:
        result += value
    return result


_sum(4, 3, 2, 1)

# Desempaquetando argumentos posicionales:
values = (6, 5, 4, 3, 2, 1)
_sum(*values)

"""
Empaquetar/Desempaquetar argumentos nominales:
Al utilizar el operador ** delante del nombre de un parámetro nominal, indica que los argumentos pasados a la función se empaquetarán en un diccionario.
"""


# Empaquetando argumentos nominales:
def best_student(**marks):
    print(f"{marks=}")
    max_mark = -1
    for student, mark in marks.items():
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return f"{best_student} es el mejor estudiante con {max_mark} puntos."


best_student(ana=8, bob=9, carol=10, dave=7)

# Desempaquetando argumentos nominales:
marks = dict(sara=8, julian=9, roger=10, jose=7)
best_student(**marks)

"""
Convensiones: En muchas ocasiones se utiliza 'args' como nombre de parámetro para los argumentos posicionales y kwargs como nombre de parámetro para los argumentos nominales.
"""


def func(*args, **kwargs):
    # TODO
    pass


"""
Forzando modo de paso de argumentos: 

- Argumentos sólo nominales: Delimitador *
"""

print("Solo nominales:")


def sumPower(a, b, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


print(sumPower(3, 4))
print(sumPower(a=3, b=4))
print(sumPower(3, 4, power=True))

"""
Argumentos sólo posicionales: Delimitador /
"""

print("Solo posicionales:")


def secondSumPower(a, b, /, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


print(secondSumPower(3, 4))
print(secondSumPower(3, 4, True))
print(secondSumPower(3, 4, power=True))

"""
Fijando argumentos posicionales y nominales: Combinación de los delimitadores * y /
"""
print("Combinación de los delimitadores * y /:")


def thirdSumPower(a, b, /, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


print(thirdSumPower(3, 6, power=True))

"""
Funciones como parámetros:

Son objetos que pueden ser asignados a variables, usados en expresiones, devueltos como valores de retorno o pasados como argumentos a otras funciones.
"""


def success():
    print("¡¡¡ÉXITO!! 🎉")


def doit(f):
    f()


# Pasando una función como argumento:
doit(success)

# Pasando los valores con los que debe operar la función:


def repeatPlease(text, times=1):
    return text * times


def secondDoit(f, arg1, arg2):
    return f(arg1, arg2)


print(secondDoit(repeatPlease, "Funciones como parámetros\n", 5))

"""
Documentación: Documentar funciones para que otros puedan entenderlas.
"""
print("Documentación:")


def sqrt(value):
    "Return the square root of the value."
    return value ** (1 / 2)


result = sqrt(16)
print(result)

# Para ver el docstring de una función: help(function_name)
help(sqrt)

"""
Anotación  de tipos: Las anotaciones de tipos o type-hints permiten indicar tipos para los parámetros de una función y/o para su valor de retorno.
"""
print("Anotación de tipos:")


def ssplit(text: str, split_pos: int) -> tuple:
    return text[:split_pos], text[split_pos:]


print(ssplit("Hello Python", 2))
print(ssplit([1, 2, 4, 5, 6, 7, 8, 9, 10], 5))

"""
Valores por defecto en la anotación de tipos:
"""


def secondSsplit(text: str, split_pos: int = -1) -> tuple:
    if split_pos == -1:
        split_pos = len(text) // 2
    return text[:split_pos], text[split_pos:]


print(secondSsplit("Always remember us this way"))

"""
Tipos compuestos:

Anotación:

list[str] -> ["a", "b", "c"]
set[int] -> {1, 2, 3}
dict[str, float] -> {"a": 1.0, "b": 2.0, "c": 3.0}
tuple[str, int] -> ("a", 1)
tuple[float, ...] -> (1.0, 2.0, 3.0)

Múltiples tipos:

tuple|dict -> Tupla o diccionario.
list[str|int] -> Lista de cadenas o enteros.
set[int|float] -> Conjunto de enteros o flotantes.
"""


def _max(*args: int | float):
    pass


_max(1, 2, 3, 4, 5)

"""
TIPOS DE FUNCIONES:

Funciones anónimas <lambda>:  

def num_words(text: str) -> int:
    return len(text.split())

Funciones lambda:

num_wrods = lambda text: len(text.split())
"""

num_words = lambda text: len(text.split())

print(type(num_words))
print(num_words("Hello Python"))

logic_and = lambda a, b: a & b

for i in range(2):
    for j in range(2):
        print(f"{i} & {j} = {logic_and(i, j)}")

"""
Lambdas como argumentos: Son bastante útiles como argumentos a otras funciones. 🟨
"""
geoloc = (
    (40.416775, -3.703790),
    (40.420083, -3.690376),
    (40.417597, -3.687181),
    (40.414662, -3.684031),
)

# Ordenación por longitud (primer elemento de la tupla)
print(sorted(geoloc, key=lambda x: x[0]))

# Ordenación por latitud (segundo elemento de la tupla)
print(sorted(geoloc, key=lambda x: x[1]))

# Ordenación por latitud y longitud
print(sorted(geoloc, key=lambda x: (x[1], x[0])))

"""
Programación Funcional: map(), filter(), reduce()
"""


# map() aplica otra función sobre cada elemento de un iterable.
# Devuelve un generador.
def f(x):
    return x**2 / 2


data = range(1, 11)

map_gen = map(f, data)

print(list(map_gen))

print(type(map_gen))

# filter() Selecciona aquellos elementos de un iterable que cumplen una condición.


def odd_number(x):
    return x % 2 == 1


data2 = range(1, 11)

filter_gen = filter(odd_number, data2)

print(type(filter_gen))

print(list(filter(lambda x: x % 2 == 1, data2)))

# Simular un filter a través de una lista por comprensión:
print([x for x in data2 if x % 2 == 1])

# reduce() Usar el módulo 'functools' para aplicar una función a un iterable.
# Permite reducir un iterable a un solo valor.

from functools import reduce


def mult_values(a, b):
    return a * b


data3 = range(1, 6)

print(reduce(mult_values, data3))
# Aplicando una función lambda:
print(reduce(lambda a, b: a * b, data3))

"""
GENERADORES:

Funciones generadoras: Se escriben como funciones ordinarias con el matiz de incorporar la sentencia 'yield', de alguna manera a 'return'. Esta sentencia devuelve el valor indicado, y a la vez, congela el estado de la función hasta la siguiente invocación.
"""


def evens(lim: int):
    for i in range(0, lim + 1, 2):
        yield i


evens_gen = evens(20)  # retorna un generador

print(type(evens_gen))

print(next(evens_gen))

# Una vez creado el generador, se puede iterar sobre el valor devuelto.

for even in evens(20):
    print(even, end=" ")

"""
Expresiones de generadores: Una expresión generadora es sintácticamente muy similar a una lista por comprensión, sólo que se utilizan los paréntesis en vez de corchetes.
"""

evens_gen2 = (i for i in range(0, 20, 2))

for i in evens_gen2:
    print("\n", i, end=" ")

# Una expresión generadora admite condiciones y anidamiento de bucles.

print(list(i for i in range(0, 20, 2)))

print(sum(i for i in range(0, 20, 2)))

print(min(i for i in range(0, 20, 2)))

print(max(i for i in range(0, 20, 2)))

"""
Funciones interiores: Definir una función dentro de otra función.	
"""


def getWordsWithAllVowels(text: str) -> list[str]:
    VOWELS = "aeiou"

    def getUniqueVowels(word: str) -> set[str]:
        return set(c for c in word if c in VOWELS)

    result = []
    for word in text.split():
        if len(getUniqueVowels(word)) == len(VOWELS):
            result.append(word)
    return result


print(getWordsWithAllVowels("La euforia de ver el riachuelo fue inmensa"))

"""
Clausuras (closure): Una clausura estable el uso de una función interior que se genera dinámicamente y recuerda los valor de los argumentos con los que fue creada.
"""


def makeMultiplierOf(n: int):
    def multiplier(x: int) -> int:
        return x * n

    return multiplier


m3 = makeMultiplierOf(3)
print(m3(5))

m5 = makeMultiplierOf(5)
print(m5(8))

# Invocación directa:
print(makeMultiplierOf(7)(9))

"""
Decoradores: Un decorador es una función que recibe como parámetro una función y devuelve otra función. 
"""


def my_decorator(func):
    def wrapper(*args, **kwargs):
        # some code before calling func
        return func(*args, **kwargs)
        # some code after calling func

    return wrapper


print(my_decorator.__name__)

# Decordador que convierte el resultado númerico de una función  a su representación binaria:


def binary(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return bin(result)

    return wrapper


print(binary(lambda number: number + 1)(5))

# Definiendo una función ordinaria:


def power(x: int, n: int) -> int:
    return x**n


result1 = power(2, 3)
result2 = power(4, 5)

print(result1)
print(result2)

# Ahora aplicando un decorador
decorated_power = binary(power)

print(decorated_power(2, 3))

"""
Usando @ para aplicar decoradores a funciones.
"""


@binary
def power(x: int, n: int) -> int:
    return x**n


print(power(6, 6))

"""
Funciones recursivas: La recursividad es el mecanismo por el cual una función se llama a sí misma.
"""


def pow(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    return base * pow(base, exponent - 1)


result = pow(2, 3)
print(result)

"""
Espacios de nombres:

Acceso a variables globales: Cuando una variable se define en el espacio de nombres global podemos hacer uso de ella con total transparencia dentro del ámbito de las funciones del programa.
"""

# Definición de una variable global
language = "Spanish"


def getLanguage():
    return f"The language is {language}"


print(getLanguage())

"""
Creando variables locales: En el caso de que se le asigne un valor a una variable dentro de una función, esta variable se crea en el ámbito de esa función.
"""

language2 = "English"


# Definición de una variable local
def changeLanguage():
    language = "catalan"
    print(f"The language is {language}")


changeLanguage()

"""
FORZAR UNA MODIFICACIÓN DE VARIABLES GLOBALES:

Usar el modificador 'global' para forzar la modificación de una variable global. 
"""

idioma = "Portuguese"


def secondChangeLanguage():
    global idioma
    idioma = "Basque"
    return f"{idioma=}"


print(secondChangeLanguage())
