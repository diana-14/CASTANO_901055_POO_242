class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0  
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 <= cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad inválida para retirar.")

    def mostrar_saldo(self):
        return f"Saldo actual: {self.__saldo} unidades."

cuenta = CuentaBancaria("Juan Pérez")


cuenta.depositar(200000)
cuenta.retirar(80000)

print(cuenta.mostrar_saldo())
