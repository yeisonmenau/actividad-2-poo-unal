from cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float, sobregiro: float = 0.0):
        super().__init__(saldo, tasa_anual)
        self._sobregiro = sobregiro
        
    def retirar(self, cantidad):
        resultado = self._saldo - cantidad
        if resultado < 0:
            self._sobregiro -= resultado
            self._saldo = 0
        else:
            super().retirar(cantidad)
        
    def consignar(self, cantidad: float) -> None:
        residuo = self._sobregiro - cantidad
        if self._sobregiro > 0:
            if residuo > 0:
                self._sobregiro = 0
                self._saldo = residuo
            else:
                self._saldo = 0
                self._saldo = -residuo  
        else:
            super().consignar(cantidad)
            
    def extracto_mensual(self) -> None:
        super().extracto_mensual()
        
    def imprimir(self) -> None:
        print(f"Saldo = ${self._saldo}")
        print(f"Cargo mensual = ${self._comision_mensual}")
        print(f"Número de transacciones = {self._numero_consignaciones + self._numero_retiros}")
        print(f"Valor de sobregiro = ${self._sobregiro}\n")
        

