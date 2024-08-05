# Sentencia if

temperature = 25


if temperature >= 30:
    print("El número es mayor o igual a 30")
else:
    print("El número es menor a 30")

# Sentencia if-else

temperature = 20
if temperature > 35:
    print("Aviso por alta temperatura ⚠")
else:
    print("Parametros normales ✔")

# Sentencia if-elif-else
temperature = 5

if temperature < 20:
    if temperature < 10:
        print("Nivel Azul 🔵")
    else:
        print("Nivel Verde 🟢")
elif temperature < 30:
    print("Nivel Naranja 🟧")
else:
    print("Nivel Rojo 🔴")

# Asignación condicional:
temperature = 33

fire_risk = "LOW" if temperature < 30 else "HIGH"
print(f"El riesgo de incendio es {fire_risk}")

"""
Operadores de comparación: ==, !=, >, <, >=, <= 🟨
"""
# Igualdad

print("*** Operadores de comparación ***")
print(5 == 5)
print(5 == 6)

# Diferente
print(5 != 5)
print(5 != 6)

# Mayor que
print(5 > 4)
print(5 > 5)

# Menor que
print(5 < 4)
print(5 < 5)

# Mayor o igual que
print(5 >= 4)
print(5 >= 5)

# Menor o igual que
print(5 <= 4)
print(5 <= 5)

"""
Operadores lógicos: and (&), or (|), not (!)

AND:
True and True -> True
False and True -> False
True and False -> False
False and False -> False

OR:
True or True -> True
False or True -> True
True or False -> True
False or False -> False

NOT:
not True -> False
not False -> True
"""
print("*** Operadores lógicos ***")
x = 8
print(x > 5 and x < 10)
print(x > 5 or x < 10)
print(not (x != 5))

# Cortocircuito and
power = 10
signal_4g = 60
print(power > 25 and signal_4g > 10)

# Cortocircuito or
power = 50
signal_4g = 20
print(power > 40 or signal_4g > 30)

"""
Booleanos en los condicionales:
"""
is_cold = False

if is_cold:
    print("¡Hola! ¡Estoy frío!")
else:
    print("¡Hola! ¡Estoy caliente!")

if not is_cold:
    print("Ponte una camiseta!")
else:
    print("Ponte una chaqueta!")

print("*** Valor nulo ***")

value = None

if value is None:
    print("Value is clearly None")
else:
    print("Value has some useful value")

value = 99

if value is not None:
    print(f"{value}")

"""
Veracidad: 

- Valores que evalúan como verdaderos son: bool("False"), bool(" "), bool(1e-10), bool([0]), bool("🚽")

- Valores que evalúan como falsos son: bool(0), bool(0.0), bool(0.0), bool(""), bool([]), bool({}), bool(None), bool(False), bool(True), bool(set())
"""

# Asignación lógica con el operador OR:
b = 0
c = 5
a = b or c
print(a)

# Asignación lógica con el operador AND:
b = 0
c = 5
a = b and c
print(a)

"""
Sentencia match-case: Parecido a JavaScript (switch-case)
"""

color = "amarillo"

match color:
    case "rojo":
        print("Color rojo 🔴")
    case "verde":
        print("Color verde 🟢")
    case "azul":
        print("Color azul 🔵")
    case "amarillo":
        print("Color amarillo 🟨")
    case _:
        print("Color desconocido ❌")

# Patrón avanzado:

point = (4, 5, 10)

match point:
    case (int(), int()):
        print(f"{point} is in plane")
    case (int(), int(), int()):
        print(f"{point} is in space")
    case _:
        print(f"Unknown point {point}")

age = 21

match age:
    case 0 | None:
        print("Not a person!")
    case n if n < 17:
        print("None")
    case n if n < 22:
        print("Not in the US")
    case _:
        print("Yes")

"""
Operadore morsa: := Permite unificar sentencias de asignación dentro de expresiones
"""

radius = 4.23
if (perimeter := 2 * 3.14 * radius) < 100:
    print(f"Increase radius to reach minimum perimeter of 100")
    print(f"Actual perimeter: {perimeter:.2f}")
