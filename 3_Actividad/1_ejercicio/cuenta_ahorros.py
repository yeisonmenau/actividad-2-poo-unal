from cuenta import Cuenta
class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        if saldo < 10000:
            self._activa = False
        else:
            self._activa = True
        
    def retirar (self,cantidad: float) -> None:
        if self._activa:
            super().retirar(cantidad)
        else:
            print("La cuenta no está activa. No se puede retirar dinero.")
    
    def consignar (self,cantidad: float) -> None:
        if self._activa:
            super().consignar(cantidad)
        else:
            print("La cuenta no está activa. No se puede consignar dinero.")

    def extracto_mensual(self) -> None:
        if self._numero_retiros > 4:
            self._comision_mensual += (self._numero_retiros - 4) * 1000
        super().extracto_mensual()
        if self._saldo < 10000:
            self._activa = False
            
    def imprimir(self) -> None:
        print(f"Saldo: ${self._saldo}")
        print(f"Comisión Mensual: ${self._comision_mensual}")
        print(f"Número de Transacciones: {self._numero_consignaciones + self._numero_retiros}")
        print(f"Número de Consignaciones: {self._numero_consignaciones}\n")