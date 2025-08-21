import math

try:
    resultado = math.exp(1000)
    print(resultado)
except OverflowError:
    print("Se produce un valor demasiado grande")