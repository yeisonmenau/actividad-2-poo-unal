from enum import Enum

class TipoCuenta(Enum):
    AHORRO = 1
    CORRIENTE = 2

class CuentaBancaria:
    def __init__ (self, titular:str, apellido:str, numero_cuenta:int, tipo:TipoCuenta, saldo:float = 0.0):
        self.titular = titular
        self.apellido = apellido
        self.numero_cuenta = numero_cuenta
        self.tipo = tipo
        self.saldo = saldo
        
    def imprimir(self) -> None:
        print(f"Titular: {self.titular}")
        print(f"Apellido: {self.apellido}")
        print(f"Numero de cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo.name}")
        print(f"Saldo: {self.saldo}")
        
    def consultar_saldo(self)-> None:
        print(f"El saldo de la cuenta es: {self.saldo}")
        
    def consignar(self, cantidad:float) -> bool:
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se ha ingresado ${cantidad} a la cuenta. Nuevo saldo: ${self.saldo}")
            return True
        else:
            print("La cantidad a ingresar debe ser mayor que 0.")
            return False

    def retirar(self, cantidad:float) -> bool:
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se ha retirado ${cantidad} de la cuenta. Nuevo saldo: ${self.saldo}")
            return True
        else:
            print("La cantidad a retirar debe ser mayor que 0 y menor o igual al saldo disponible.")
            return False