"""
Manejo de errores:
Para capturar las excepciones podemos utilizr el método 'try' y 'except'.
"""


def intDiv(a: int, b: int) -> int:
    # Ejecutá siempre y cuando no haya excepción
    try:
        return a // b
    except:
        print("Please do not divide by zero...")


result = intDiv(4, 0)

"""
Especificando excepciones:

TypeError: Por si los operandos no permiten la división.
ZeroDivisionError: Por si el denominador es 0.
Exception: Para cualquier otro error que se pueda producir.
"""


def int_div(a, b):
    try:
        result = a // b
    except TypeError:
        print("Check your operands...Some of them seems strange...")
    except ZeroDivisionError:
        print("Please do not divide by zero...")
    except Exception:
        print("Ups! Something went wrong...")


int_div(3, "0")

"""
EXCEPCIONES PREDEFINIDAS:

- AttributeError: Referencia de atributo inexistente.
- IndexError: Subíndice de secuencia fuera de rango.
- KeyError: Clave de diccionario no encontrada.
- NotImplementedError: La operación debe ser implementada.
- OSError: Error al usar una función del sistema operativo (E/S).
- RecursionError: Alcanzado el máximo nivel de recursión.
- StopIteration: Fin del protocolo de iteración.
- TypeError: Operación sobre un objeto de tipo inapropiado.
- ValueError: Operación sobre un objeto de tipo correcto pero valor inapropiado.
- ZeroDivisionError: Segundo argumento de división o módulo es cero.
"""

"""
Agrupando excepciones:
Si tratamos distintas excepciones con el mismo comportamiento, es posible agruparlas en una única excepción.
"""


def intDiv2(a, b):
    try:
        result = a // b
    except (TypeError, ZeroDivisionError):
        print("Check operands: Some of them caused errors")
    except Exception:
        print("Ups! Something went wrong...")


intDiv2(2, 0)

"""
Variantes en el tratamiento: 
Python ofrece la cláusula 'else' para saber que todo ha ido bien y que no se ha lanzado ninguna excepción. Esto es relevante a la hora de manejar los errores.

De igual modo, tenemos a nuestra disposición la cláusula 'finally' que se ejecuta siempre, independientemente de si ha habido o no ha habido error.
"""

values = [4, 2, 7]

try:
    result = values[2]
except IndexError:
    print("Error: Index not in list")
else:
    print(f"Your wishes are my command: {result}")
finally:
    print("Have a good day!")

"""
Mostrando los errores: 

Además de capturar las excepciones podemos mostrar los mensajes de errores asociados. Para ello, se utiliza la palabra reservada 'as' junto a un nombre de variable que contendrá el objeto de la excepción.
"""

try:
    print(values[5])
except IndexError as error:
    print(f"Something went wrong: {error}")

"""
Elevando excepciones:

Utilizar la sentencia 'raise' para lanzar una excepción. Esto es útil cuando queremos lanzar una excepción de manera programática.
"""


# def _sum(a: int, b: int) -> int:
#     if isinstance(a, int) and isinstance(b, int):
#         return a + b
#     raise TypeError("Operands must be integers")


# _sum(4, 3)

# _sum("4", "3")

"""
Jerarquía de excepciones:

Todas las excepciones predefinidas en Python heredan de la clase Exception y de la clase BaseException (más alla de heredar de object).
"""

# print(TypeError.mro())

# print(ZeroDivisionError.mro())

# print(IndexError.mro())

# print(FileExistsError.mro())

"""
Excepciones propias:
"""

# Para crear una excepción propia basta con crear una clase
# vacía. No es necesario incluir código más alla de un pass.


# class NotIntError(Exception):
#     pass


# values = (4, 7, 2.11, 9)

# for value in values:
#     if not isinstance(value, int):
#         raise NotIntError(value)

"""
Mensaje personalizado:
Añadiendo un mensaje como valor por defecto.
"""


class NotIntError(Exception):
    def __init__(self, message="This module only works with integers. Sorry!"):
        super().__init__(message)


raise NotIntError()
