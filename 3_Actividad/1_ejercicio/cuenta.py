class Cuenta:
    def __init__(self, saldo: float, tasa_anual: float, numero_consignaciones: int = 0, numero_retiros: int = 0, comision_mensual: float = 0.0):
        self._saldo = saldo
        self._tasa_anual = tasa_anual
        self._numero_consignaciones = numero_consignaciones
        self._numero_retiros = numero_retiros
        self._comision_mensual = comision_mensual
        
    def consignar(self, cantidad: float) -> None:
        self._saldo += cantidad
        self._numero_consignaciones += 1
        print(f"Se ha consignado {cantidad}. Nuevo saldo: {self._saldo}")      
    
    def retirar(self, cantidad: float) -> None:
        if cantidad > self._saldo:
            print("No hay suficiente saldo para realizar el retiro.")
        else:
            self._saldo -= cantidad
            self._numero_retiros += 1
            print(f"Se ha retirado {cantidad}. Nuevo saldo: {self._saldo}")        
    
    def calcular_interes(self) -> None:
        tasa_mensual = self._tasa_anual / 12
        interes_mensual = self._saldo * tasa_mensual
        self._saldo += interes_mensual
        print(f"Se ha calculado el interés mensual: {interes_mensual}. Nuevo saldo: {self._saldo}")
        
    def extracto_mensual(self) -> None:
        self._saldo -= self._comision_mensual
        self.calcular_interes()