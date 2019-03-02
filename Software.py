# Autor: Roberto Emmanuel González Muñoz
# Una compañía de software vende un paquete por $2,300.00 cuando compras menos de 10 unidades.
# Si se compran 10 o más, se aplica un descuento de acuerdo a la siguiente tabla.


def calcularTotal(p):
    # Calcula los costos y decuentos.
    costoPaquete = 2300
    costoDescuento15 = costoPaquete * (1 - .15)
    costoDescuento22 = costoPaquete * (1 - .22)
    costoDescuento35 = costoPaquete * (1 - .35)
    costoDescuento42 = costoPaquete * (1 - .42)

    # Calcula el costo total con el descuento indicado.
    if 1 <= p <= 9:
        costo = p * costoPaquete
        return costo

    elif 10 <= p <= 19:
        costo = p * costoDescuento15
        return costo

    elif 20 <= p <= 49:
        costo = p * costoDescuento22
        return costo

    elif 50 <= p <= 99:
        costo = p * costoDescuento35
        return costo

    elif p >= 100:
        costo = p * costoDescuento42
        return costo

def main():
    # Recibe el número de paquetes vendidos.
    paquetesVendidos = int(input("Teclea el número de paquetes vendidos: "))
    print("---------------------------------------------------")

    # Si el número de paquetes es igual o menor a 0 genera error.
    if paquetesVendidos > 0:
        # Calcula el total a pagar con descuentos.
        totalAPagar = calcularTotal(paquetesVendidos)
        print("El total a pagar de %.d paquetes es %.2f" % (paquetesVendidos, totalAPagar))

    else:
        print("Error, el número de paquetes no es válido.")

main()