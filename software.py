#Bruno Omar Jiménez Mancilla
#Programa que lea las unidades vendidas de un paquete de software e imprime el descuento y la cantidad descontada
def main():
    numPaquetes = int(input("Ingresa el numero de paquetes que deseas: "))
    if numPaquetes <= 0:
        print("Error")
    else:
        totalSinDescuento = numPaquetes * 2300
        descuento = Descuento(numPaquetes)
        totalAPagar = totalSinDescuento-descuento
        print("El total sin descuento es: ",totalSinDescuento)
        print("La cantidad descontada es: ", descuento)
        print("El total a pagar es: ",totalAPagar)



def Descuento(numPaquetes):
    if numPaquetes < 10:
        return 0
    elif numPaquetes >= 10 and numPaquetes <= 19:
        descuento = (numPaquetes*2300) *.15
        return descuento
    elif numPaquetes >= 20 and numPaquetes <= 49:
        descuento = (numPaquetes*2300)*.22
        return descuento
    elif numPaquetes >= 50 and numPaquetes <= 99:
        descuento = (numPaquetes * 2300) * .35
        return descuento
    elif numPaquetes >= 100:
        descuento = (numPaquetes*2300)*.42
        return descuento


main()