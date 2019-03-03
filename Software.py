#Autor: Elizabeth Citlalli Zapata Cortes
# De acuerdo con el número de paquetes vendidos se muestra la cantidad descontada y el total a pagar.

def calcularTotalConDescuento(numPaquetes):
    if numPaquetes >= 10 and numPaquetes <= 19:
        total = (numPaquetes*2300) *.85
        return total
    elif numPaquetes >= 20 and numPaquetes <=49:
        total = (numPaquetes * 2300) * .78
        return total
    elif numPaquetes >= 50 and numPaquetes <=99:
        total = (numPaquetes * 2300) * .65
        return total
    elif numPaquetes >= 100:
        total = (numPaquetes * 2300) * .58
        return total
    else:
        return "Error"


def indicarDescuento(numPaquetes):
    if numPaquetes >= 10 and numPaquetes <= 19:
        descuento = (numPaquetes * 2300) * .15
        return  descuento
    elif numPaquetes >= 20 and numPaquetes <= 49:
        descuento = (numPaquetes * 2300) * .22
        return descuento
    elif numPaquetes >= 50 and numPaquetes <= 99:
        descuento = (numPaquetes * 2300) * .35
        return descuento
    elif numPaquetes >= 100:
        descuento = (numPaquetes * 2300) * .42
        return descuento
    else:
        return "Error"

def main():
    numPaquetes = int(input("Número de paquetes: "))

    print("Cantidad descontada: $", indicarDescuento(numPaquetes))

    print("Total a pagar: $", calcularTotalConDescuento(numPaquetes))


main()