class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto, mensaje="Saldo insuficiente para realizar la operación."):
        self.saldo = saldo
        self.monto = monto
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class MontoInvalidoError(Exception):
    def __init__(self, mensaje="El monto ingresado no es válido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def retirar(saldo, monto):
    if monto <= 0:
        raise MontoInvalidoError()
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    saldo -= monto
    print(f"Retiro exitoso. Saldo restante: {saldo}")
    return saldo

try:
    saldo_actual = float(input("Ingrese su saldo actual: "))
    monto_retiro = float(input("Ingrese el monto a retirar: "))
    saldo_actual = retirar(saldo_actual, monto_retiro)
except MontoInvalidoError as e:
    print(f"Error: {e}")
except SaldoInsuficienteError as e:
    print(f"Error: {e} (saldo: {e.saldo}, intento de retiro: {e.monto})")
except ValueError:
    print("Error: El monto debe ser un número entero")