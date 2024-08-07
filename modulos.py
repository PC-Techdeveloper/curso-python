"""
Los módulos son simplemente ficheros de texto que contienen código Python y representan unidades con las que evitar la repetición y favorecer la reutilización de código.

Los módulos pueden agruparse en carpetas denominadas 'packages' mientras que estas carpetas, a su vez, pueden dar lugar a librerías que contienen módulos.
"""

"""
Importar un módulo:

La forma más sencilla de importar un módulo es import <module>, donde <module> es el nombre de otro fichero Python sin la extensión .py
"""

# Importando el módulo completo -> fichero: stats.py
import extramath.stats as stats

print(stats.mean(4, 7, 2.11, 9))
print(stats.std(6, 3, 9, 5))

# Un módulo de librería estándar: import os
import os

print(os.getcwd())

"""
Ruta de búsqueda de módulos:

Cuando importamos un módulo en Python el intérprete trata de encontrarlo (por orden) en las rutas definidas en la variable sys.path.
"""
# import sys

# print(sys.path)

"""
Importar partes de un módulo:

Solo importar una parte de un módulo es posible utilizando la sintaxis 'from <module> import <name>'. Esto es útil cuando queremos utilizar solo una parte de un módulo.
"""

from extramath.stats import mean

print(mean(4, 7, 31, 9))

"""
Para importar varios objetos (funciones, clases, constantes, etc.) de un módulo, se especifican los nombres separados por comas.

from stats import * -> Importa todos los componentes del módulo.
"""

from extramath.stats import mean, std

print(mean(1, 2, 3))
print(std(4, 5, 6))

"""
Importar usando un alias:
Python ofrece la posibilidad a través de la sentencia 'as' de importar un módulo con un alias diferente al que se le asigna al nombre del módulo.
"""

from extramath.stats import mean as avg

print(avg(6, 5, 4))

"""
Paquetes: Un paquete es una carpeta que contiene ficheros .py. Además permite tener una jerarquía con más de un nivel de sub-carpetas anidadas.
"""

# Importamdo desde un paquete
from extramath import frac, stats

print(frac.gcd(12, 18))

print(stats.mean(4, 7, 2.11, 9))

"""
Programa principal: El fichero __main__.py es el que se ejecuta cuando se ejecuta el programa en la línea de comandos.

if__name__=="__main__":

La variable __name__ toma los siguientes valores:

* El nombre del módulo o paquete al importar el fichero.
* El valor __main__ cuando se ejecuta el fichero como un módulo.
"""

if __name__ == "__main__":
    # Punto de entrada del programa
    print("Hola Python!")
