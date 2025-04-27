from cuenta_bancaria import CuentaBancaria, TipoCuenta

if __name__ == "__main__":

    cuenta = CuentaBancaria("Pedro1", "Pérez", 123456789, TipoCuenta.AHORRO)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)