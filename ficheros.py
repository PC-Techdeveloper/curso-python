"""
Un fichero es un conjunto de bytes almacenados en algún dispositivo. Cada fichero se identifica unívocamente a través de una ruta que nos permite acceder a él.
"""

"""
LECTURA DE UN FICHERO: open()

- Lectura del contenido de un fichero existente.
- Escritura en un fichero nuevo.
- Añadido al contenido de un fichero existente.

LECTURA COMPLETA DE UN FICHERO: read(), readlines()
- read() devuelve el contenido completo del fichero como una cadena de caracteres.
- readlines() Devuelve todo el contenido del fichero como una lista donde cada línea es un elemento de la lista.
"""

# Lectura de un fichero.
# archive = open("./files/temps.txt", "r")

# Lectura completa de un fichero: read()
archive = open("./files/temps.txt", "r")
# print(archive.read())

# Devolviendo como una lista de líneas: readlines()
archive = open("./files/temps.txt", "r")
# print(archive.readlines())

"""
LECTURA LÍNEA A LÍNEA: Optimzar rendimiento de lectura de ficheros grandes.
"""

files = open("./files/temps.txt", "r")

# for line in files:
#     print(line)

# Lectura de una línea:

# for line in files:
#     print(line)
#     break

# Lectura de las 3 primeras líneas:

# for _ in range(3):
#     print(files.readline().strip())

# Lectura de las restantes líneas:

# for line in files:
#     print(line.strip())

# Volver a leer desde el principio del fichero: seek()

# for line in files:
#     print(line.strip(), end="")


# print(files.seek(0))

# Enumerando líneas: enumerate()
for i, line in enumerate(files, start=1):
    print(f"L1{i}: {line.strip()}")

"""
ESCRITURA DE UN FICHERO: open(), write(), close()
"""

canary_iata = ("tfn", "tfs", "lpa", "gmz", "vde", "spc", "ace", "fue")

files = open("./files/canary.txt", "w")

files.write("\n".join(canary_iata))

files.close()

"""
AÑADIDO A UN FICHERO: Se utiliza "a" por "append"
"""

# files = open(".files/more-data.txt", "a")

"""
USANDO CONTEXTOS: la sentencia with y el contexto creado se ocupará de cerrar adecuadamente el fichero.
"""
with open("./files/temps.txt") as file:
    for line in file:
        min_temp, max_temp = line.strip().split()
        print(f"La temperatura mínima es {min_temp} y la máxima es {max_temp}")
