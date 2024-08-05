print("CALCULADORA BÁSICA")

number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

sum = number1 + number2
dif = number1 - number2
mult = number1 * number2
div = number1 / number2

mensaje = f"""
Para los números {number1} y {number2}

El resultado de la suma es: {sum}
El resultado de la resta es: {dif}
El resultado de la multiplicación es: {mult}
El resultado de la división es: {div:.2f}
"""

print(mensaje)
