# Autor: Ronaldo Estefano Lira Buendia
# Calcular el descuento y el total segun los paquetes que estes comprando.

def mostrarDescuento(paquetes):
    if paquetes==1 and paquetes<=9:
        descuento = 0
    elif paquetes<20:
        des = .15
        descuento = (paquetes * 2300) * des
    elif paquetes<50:
        des = .22
        descuento = (paquetes * 2300) * des
    elif paquetes<100:
        des = .35
        descuento = (paquetes * 2300) * des
    elif paquetes>100:
        des = .42
        descuento = (paquetes * 2300) * des
    else:
        descuento = ("ERROR")
    return descuento


def calcularTotal(paquetes, descuento):
    if paquetes>1:
        total = (paquetes * 2300) - (descuento)
    else:
        total = ("ERROR")

    return total


def main():
    paquetes = int(input("Cuantos paquetes va a querer?: "))
    descuento = mostrarDescuento(paquetes)
    total = calcularTotal(paquetes, descuento)
    print("Deescuento que se te aplica: $",descuento)
    print("Total a pagar: $",total)


main()