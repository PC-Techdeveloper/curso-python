# Sys.arv

import sys

number = int(sys.argv[1])
to_base = int(sys.argv[2])

match to_base:
    case 2:
        result = f"{number:b}"
    case 8:
        result = f"{number:o}"
    case 16:
        result = f"{number:x}"
    case _:
        result = None

if result is None:
    print(f"Base {to_base} no soportada")
else:
    print(result)
