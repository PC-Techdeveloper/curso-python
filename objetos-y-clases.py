"""
PROGRAMACIÓN ORIENTADA A OBJETOS: Permite llevar el código a mecanismos usados con entidades de la vida real.

ENCAPSULTAMIENTO:
Permite empaquetar el código dentro de unidad (objeto) donde se puede determinar el ámbito de actuación.

ABSTRACCIÓN:
Permite generalizar los tipos de objetos a través de las clases y simplificar el código.

HERENCIA:
Permite reutilizar el código al poder heredar sus atributos y comportamientos de una clase a otra.

POLIMORFISMO:
Permite crear múltiples objetos a partir de una misma pieza flexible de código.
"""

"""
¿QUÉ ES UN OBJETO?
Es una estructura de datos personalizada que contiene datos y código. Un objeto representa una instancia única de alguna entidad a través de los valores de sus atributos e interactúa con otros objetos a través de sus métodos.

¿QUÉ ES UNA CLASE?
La clase es un molde o plantilla con el que se pueden crear objetos de ese tipo. Un objeto es una instancia de una clase. Los nombres de las clases se escriben en nomenclatura CamelCase.
"""


# Creando clase:
class StarWarsDroid:
    pass


c1 = StarWarsDroid()
c2 = StarWarsDroid()
c3 = StarWarsDroid()

"""
Añadiendo métodos a clases: Un método es una función que forma parte de una clase o de un objeto. Incorporando un primer parámetro 'self' que hace referencia al objeto al que pertenece el método.
"""


class Droid:
    # Método: Acciones que puede tener un objeto
    def switchOn(self):
        print("El droide está encendido")

    def switchOff(self):
        print("El droide está apagado")


# Creando una instancia a partir de una clases: Objeto
droide1 = Droid()

droide1.switchOn()

"""
Añadiendo atributos a clases: Un atributo es una variable que forma parte de una clase o de un objeto.
"""


class Droid2:
    def switchOn(self):
        # Atributo
        self.power = True
        print("Droide encendido")

    def switchOff(self):
        self.power = False
        print("Droide apagado")


droide2 = Droid2()

droide2.switchOn()
print(droide2.power)

droide2.switchOff()
print(droide2.power)

"""
INICIALIZACIÓN: El método __init__ es un método especial que se llama automáticamente cuando se crea un objeto de una clase. Se conoce como el constructor de clase.

Es importante tener en cuenta que si no se utiliza 'self' estaremos creando una variable local en vez de un atributo del objeto.
"""


class Droid3:
    def __init__(self, name: str):
        self.name = name


droide3 = Droid3("B5-34")
print(droide3.name)

"""
ATRIBUTOS: 

- Acesso directo: Permite modificar desde fuera con un acceso directo.
"""


class Droid4:
    def __init__(self, name: str):
        self.name = name


droid4 = Droid4("R1-43")

print(droid4.name)

# Modificar el atributo ✅
droid4.name = "R1-43 mod"
print(droid4.name)

# Añadir atributos después de su creación ✅
droid4.manufacturer = "Star Wars"

droid4.height = 1.77

print(droid4.manufacturer)
print(droid4.height)

"""
PROPIEDADES: Para la privacidad de los atributos es el uso de las propiedades. La forma más común de aplicar propiedades es mediante el uso de decoradores.

- @property: Para leer el valor de un atributo (getter).
- @name.setter: Para escribir el valor de un atributo (setter).
"""


class Androide:
    def __init__(self, name: str):
        self.hidden_name = name

    @property
    def name(self) -> str:
        print("Dentro del getter")
        return self.hidden_name

    @name.setter
    def name(self, name: str) -> None:
        print("Dentro del setter")
        self.hidden_name = name


droid = Androide("N1-3GL")

droid.name = "Nigel"

droid.name

print(droid.hidden_name)

droid.hidden_name = "waka-waka"

print(droid.hidden_name)

"""
Ocultando atributos: Python tiene una convención sobre aquellos atributos que queremos hacer privados, comenzando con un doble guiones bajos (_).
"""


class Androide2:
    def __init__(self, name: str):
        self.__name = name

    # Método público
    def getAttribute(self):
        return self.__name


droid2 = Androide2("BC-44")

# ❌ Al acceder directamente genera un error.
# print(droid2.__name)

# ✅ Acceder a los atributos privados desde un método público.
print(droid2.getAttribute())

"""
Atributos de clase:
- Si se modifica un atributo de clase desde un objeto, sólo se modifica el valor en el objeto y no en la clase.

- Si se modifica un atributo de clase desde una clase, se modifica el valor en todos los objetos pasados y futuros.
"""


class Androide3:
    obeys_owner = True


droid3 = Androide3()
droide4 = Androide3()

# Desde un objeto:
print(droid3.obeys_owner)

# Cambiando pasado y futuro ✅
# Desde una clase:
Androide3.obeys_owner = False
print(droid3.obeys_owner)
print(droide4.obeys_owner)

# Modificando los droides futuros pero no los pasados


class Androide4:
    obeys_owner = True

    def __init__(self):
        self.obeys_owner = Androide4.obeys_owner


androide1 = Androide4()
androide2 = Androide4()
print(androide1.obeys_owner)
print(androide2.obeys_owner)

Androide4.obeys_owner = False

print(androide1.obeys_owner)
print(androide2.obeys_owner)

androide3 = Androide4()

print(androide3.obeys_owner)

"""
Métodos:

- Método de instancia: 
Es un método que modifica o accede al estado del objeto al que hace referencia. Recibe como primer parámetro 'self'.
"""


class Androide5:
    # Método de instancia constructor:
    def __init__(self, name: str):
        self.name = name
        self.covered_distance = 0

    # Método de instancia
    def move_up(self, steps: int) -> None:
        self.covered_distance += steps
        print(f"Moviendome {steps} pasos")


droid5 = Androide5("C1-10P")

droid5.move_up(10)

"""
Métodos de clasE:
Es un método que modifica o accede al estado de la clase a la que hace referencia. Recibe como primer parámetro 'cls'. La identificación de estos métodos se completan aplicando el decorator @classmethod a la función.
"""


# Método de clase que muestra el número de droides creados.
class Androide6:
    count = 0

    def __init__(self):
        Androide6.count += 1

    # cls: Permite acceder y modificar los atributos
    # Y métodos de la clase.
    @classmethod
    def total_droides(cls) -> None:
        print(f"Hay {cls.count} droides")


droid6 = Androide6()
droid7 = Androide6()
droid8 = Androide6()

Androide6.total_droides()

"""
Métodos estáticos: Es un método que no deberia modificar el estado del objeto ni de la clase. No recibe ningún parámetro especial. La identificación de estos métodos se completan aplicando el decorator @staticmethod a la función.
"""


class Androide7:
    def __init__(self):
        pass

    # Método estático que devuelve una tupla de strings
    # Y las categorias de los droides.
    @staticmethod
    def getDroidCategory() -> tuple[str]:
        return ("Messenger", "Astromech", "Power", "Protocol")


droid7 = Androide7()
print(droid7.getDroidCategory())

"""
Métodos decorados: 
"""


class Androide8:
    @staticmethod
    def audit(method):
        def wrapper(self, *args, **kwargs):
            print(f"Androide {self.name} corriendo {method.__name__}")
            return method(self, *args, **kwargs)

        return wrapper

    def __init__(self, name: str):
        self.name = name
        self.pos = [0, 0]

    @audit
    def move(self, x: int, y: int):
        self.pos[0] += x
        self.pos[1] += y

    @audit
    def reset(self):
        self.pos = [0, 0]


androide8 = Androide8("B1")

androide8.move(1, 1)

androide8.reset()

"""
Métodos mágicos: 
Los métodos mágicos empiezan y terminan con __ y son llamados automáticamente cuando se invocan. Uno de los más famosos es el constructor __init__().
"""

# __eq__: Permite comparar objetos.
# Para poder utilizar la anotación de tipo Droid se importa desde __future__
# from __future__ import annotations


class Droid:
    def __init__(self, name: str, serial_number: int):
        self.name = name
        self.serial_number = serial_number

    def __eq__(self, droid: Droid) -> bool:
        return self.name == droid.name


droid9 = Droid("C-3PO", 123450)
droid10 = Droid("R2-D2", 678910)

print(droid9.__eq__(droid10))

"""
Métodos mágicos para comparaciones y operaciones matemáticas:
== -> __eq__
!= -> __ne__
< -> __lt__
<= -> __le__
> -> __gt__
>= -> __ge__

+ -> __add__
* - __sub__
* -> __mul__
/ -> __truediv__
// -> __floordiv__
% -> __mod__
** -> __pow__
"""

# Sumando dos robots
# from __future__ import annotations


class Robot:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    # other hace referencia al otro objeto
    def __add__(self, other: Droid) -> Droid:
        new_name = self.name + other.name
        new_power = self.power + other.power
        # Devolver un objeto de tipo Robot
        return Robot(new_name, new_power)


robot1 = Robot("C3PO", 100)
robot2 = Robot("R2D2", 200)

sumRobot = robot1 + robot2

print(f"Fusión robots:\n {sumRobot.name} con poder {sumRobot.power}")

"""
Herencia: 
La herencia consiste en construir una nueva clase partiendo de una clase existente, pero añade o modifica ciertos aspectos. La herencia se considera una buena práctica de programación tanto para reutilizar código como para realizar generalizaciones.
"""


"""
Heredar desde una clase base: Indicar entre paréntesis la clase a la que se quiere heredar.
"""


class Robot2:
    # Clase padre
    def switchOn(self):
        print("El robot está encendido")

    def switchOff(self):
        print("Bye, iré a dormir!")


# Heredando desde Robot2
class ProtocolRobot(Robot2):
    # Clase hija
    pass


# Comprobando que ProtocolRobot hereda de Robot2
# print(issubclass(ProtocolRobot, Robot2))

r1 = Robot2()
r2 = ProtocolRobot()

r1.switchOn()

# Método heredado de Robot2
r2.switchOn()

"""
Sobreescribir un método: 

Modificar el comportamiento de una herencia existente. Para sobreescribir un método, se utiliza el decorador @override.
"""


class Robot3:
    # Clase padre
    def switchOn(self):
        print("El robot está encendido")

    def switchOff(self):
        print("Bye, iré a dormir!")


# Heredando desde Robot3
class SecondProtocolRobot(Robot3):
    # Sobreescribiendo el método switchOn
    def switchOn(self):
        print("Hola!, SOY UN ROBOT PROTOCOLO. EN QUE TE PUEDO AYUDAR?")


r3 = Robot3()
r4 = SecondProtocolRobot()

# Método heredado pero ha sido sobreescrito
r4.switchOn()

"""
Añadir un método: Añadir métodos que no estaban presentes en su clase base.
"""


class Robot4:
    def switchOn(self):
        print("Robot prendido")

    def switchOff(self):
        print("Bye, Apagado!")


class OtherRobot(Robot4):
    def switchOff(self):
        print("Hola, soy otro robot... En que te puedo ayudar?")

    def translate(self, msg: str, from_lang: str) -> str:
        return f"{msg} means 'ZASCA' in {from_lang}"


r5 = Robot4()
r6 = OtherRobot()
result = r6.translate("Klitos", from_lang="Huttese")
print(result)

"""
Accediendo a la clase base: Python ofrece el parámetro 'super' para acceder a los métodos (o atributos) de la clase base.
"""


class Robot5:
    def __init__(self, name: str):
        self.name = name


class MoreRobots(Robot5):
    def __init__(self, name: str, languages: list[str]):
        # Llama al constructor de la clase base
        super().__init__(name)
        self.languages = languages


r7 = MoreRobots("R2D2", ["Huttese", "Klingon", "English"])

print(r7.name)
print(r7.languages)

"""
Herencia múltiple: Permite heredar de más de una clase.	
"""


class Robot6:
    def greet(self):
        return "Hola, soy un robot"


class OtroRobot(Robot6):
    def greet(self):
        return "Here a protocol robot"


class TercerRobot(Robot6):
    def greet(self):
        return "Hola, soy el tercer robot"


# Heredando de múltiples clases
class SuperRobot(OtroRobot, TercerRobot):
    pass


# El orden en el que se específican las clases es importante.
class MegaRobot(OtroRobot, TercerRobot):
    pass


# Comprobar las herencias múltiples:

print(issubclass(SuperRobot, (TercerRobot, OtroRobot, Robot6)))

print(issubclass(MegaRobot, (TercerRobot, OtroRobot, Robot6)))

super_droid = OtroRobot()
mega_droid = TercerRobot()

print(super_droid.greet())
print(mega_droid.greet())

"""
Estructuras de una clase:

- Descripción de la clase.
- Constructor.
- Decoradores.
- Metodos de instancia.
- Propiedades.
- Metodos mágicos.
- Métodos de clase.
- Métodos estáticos.
"""
