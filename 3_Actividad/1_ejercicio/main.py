from cuenta_ahorros import CuentaAhorros

def main():
    print("Cuenta de ahorros")
    saldo_inicial = float(input("Ingrese saldo inicial: $"))
    tasa_interes = float(input("Ingrese tasa de interés (ej. 0.05 para 5%): "))

    cuenta1 = CuentaAhorros(saldo_inicial, tasa_interes)

    cantidad_depositar = float(input("Ingresar cantidad a consignar: $"))
    cuenta1.consignar(cantidad_depositar)

    cantidad_retirar = float(input("Ingresar cantidad a retirar: $"))
    cuenta1.retirar(cantidad_retirar)

    cuenta1.extracto_mensual()
    cuenta1.imprimir()

if __name__ == "__main__":
    main()
