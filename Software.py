# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Programa que calcula el descuento y el total a pagar de un paquete de software.

# Función que decide el porcentaje de descuento que se aplicará al total.
def calcularDescuento(p):
    if p >= 10 and p <= 19:
        descuento = 15
    elif p >= 20 and p <= 49:
        descuento = 22
    elif p >= 50 and p <= 99:
        descuento = 35
    elif p >= 100:
        descuento = 42
    else:
        descuento = 0
    return descuento


# Función que calcula el total a pagar aplicando el descuento correspondiente.
def calcularTotal(d, p):
    subTotal = p * 2300
    descuento = (d / 100) *subTotal
    total = subTotal - descuento
    return total


# Función principal.
def main():
    paquetes = int(input("Teclea el número de paquetes que compraste: "))
    if paquetes <= 0:
        print("Error, cantidad no válida.")
    else:
        descuento = calcularDescuento(paquetes)
        totalAPagar = calcularTotal(descuento, paquetes)
        print("El descuento es de: %2d" % descuento, "%")
        print("El total a pagar es de: $%.2f" % totalAPagar)


# Llamada a la función principal.
main()
