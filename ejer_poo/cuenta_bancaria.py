class cuenta_banco:
    def __init__(self, numero_cuenta: int, propietario: str, balance: int):
        self.numero_cuenta: str = numero_cuenta
        self.propietario: int = propietario
        self.balance: int = balance

    def depositar (self, cantidad: int):
        self.balance += cantidad

    def retirar (self, cantidad: int):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("no hay suficiente saldo en su cuenta")

    def aplicar_cuata_manejo (self):
        self.balance *= 0.98

    def mostrar_detalles (self):
        print(f"su número de cuenta es: {self.numero_cuenta}")
        print(f"el propietoario es: {self.propietario}")
        print(f"el balance es: {self.balance}")

cuenta1= cuenta_banco ('234189', ['luz maría'], 100)
cuenta1.depositar(276)
cuenta1.retirar(98)
cuenta1.aplicar_cuata_manejo()
cuenta1.mostrar_detalles()
