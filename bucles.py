"""
Sentencia While: Mientras se cumpla una condición, ejecuta una instrucción

NOTA: Incrementar el contador para evitar que este en un bucle infinito
"""

# want_greet = "S"

# while want_greet.upper() == "S":
#     print("¡Hola! que tal")
#     want_greet = input("¿Quieres saludar otra vez? [S/N]: ")

# print("¡Adiós! que tengas un buen día 👋")

# print("*** Romper un bucle while: Break ***")

# MAX_GREETS = 4
# num_greets = 0
# want_greet = "S"

# while want_greet.upper() == "S":
#     print("¡Hola! Te hablo desde la computadora")
#     num_greets += 1
#     if num_greets == MAX_GREETS:
#         print(f"Has alcanzado el máximo número de saludos: {MAX_GREETS}")
#         break
#     want_greet = input("¿Quieres saludar otra vez? [S/N]: ")
# else:
#     print("Usted no quiere más saludos 🤪")

# print("¡BYE! 👋")


# print("*** Continuar un bucle while: Continue ***")

# Saltar delante hacia la siguiente repetición del bucle
# want_greet = "S"
# valid_option = 0

# while want_greet == "S":
#     print("¡HOLA! CÓMO ESTÁS ?")
#     want_greet = input("¿Quieres un saludo de nuevo? [S/N]: ")
#     if want_greet not in "SN":
#         print("No te entiendo, pero te saludo de nuevo...")
#         want_greet = "S"
#         continue
#     valid_option += 1

# print(f"{valid_option} respuestas válidas")
# print("¡ADIÓS! que tengas un buen día 👋")

"""
Bucle for: Permite iterar strings, lists, tuples, dictionaries, ficheros, etc.
"""

word = "python"

for letter in word:
    print(letter)

# Romper un bucle for con break
print("ROMPIENDO UN BUCLE FOR:")

word = "Python"

for letter in word:
    if letter == "t":
        break
    print(letter)

print("SECUENCY OF NUMBERS ⬇")

# for i in range(10):
#     print(i)

# for i in range(1, 10):
#     print(i)

for i in range(1, 7, 3):
    print(i)

# Usando el guión bajo: _ -> Repetir una acción un número de veces.
for _ in range(15):
    print("Repeat me 15 times")

"""
Bucles anidados:
"""

print("BUCLES ANIDADOS:")

for num_table in range(1, 10):
    for mul_factor in range(1, 10):
        result = num_table * mul_factor
        print(f"{num_table} x {mul_factor} = {result}")
