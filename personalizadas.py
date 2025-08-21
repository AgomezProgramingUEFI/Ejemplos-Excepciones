class EdadInvalidaError(Exception):
    def __init__(self, edad, mensaje="La edad no es válida. Debe ser mayor o igual a 18."):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def verificar_edad(edad):
    if edad < 18:
        raise EdadInvalidaError(edad)
    else:
        print("Acceso permitido")

try:
    edad_usuario = int(input("Ingrese su edad: "))
    verificar_edad(edad_usuario)
except EdadInvalidaError as e:
    print(f"Error: {e}")
