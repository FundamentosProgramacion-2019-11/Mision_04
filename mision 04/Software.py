# Luis Fernando Durán Castillo
# Calcular el descuento de una compra y el pago total.


def calcularDescuento(precio):
    if precio >= 1 and precio <= 9:
        descuento = 0
    elif precio>= 10 and precio <= 19:
        descuento = .15
    elif precio >= 20 and precio <= 49:
        descuento = .22
    elif precio >= 50 and precio <= 99:
        descuento = .35
    elif precio >= 100:
        descuento = .42
    else:
        descuento = "Error"
    return descuento


def main():
    print("Bienvenido, usted hace una compra de 10 o mas paquetes recibira un descuento.")
    precio = int(input("Escribe la cantidad de paquetes va a comprar: "))
    descuento = calcularDescuento(precio)

    if descuento == "Error":
        print("Error en el descuento, por favor intente de nuevo con numeros mayores a 0")
    else:
        pago = precio * 2300
        descuentototal = 2300 * descuento * precio
        total = precio * (2300 - (2300 * descuento))
        print("El pago sin descuento es de: $", pago)
        print("Lo que se descontara de su compra es: $", descuentototal)
        print("El total a pagar por los paquetes es de: $", total)


main()