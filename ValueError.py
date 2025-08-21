def calcular_cuadrado():
    try:
        numero = float(input("Ingrese un número para calcular su cuadrado: "))
        print(f"El cuadrado de {numero} es {numero ** 2}")
    except ValueError:
        print("Error: este val")

calcular_cuadrado()
