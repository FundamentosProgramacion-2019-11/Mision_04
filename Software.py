#Autor: Ivana Olvera Mérida
#Una compañía de software vende un paquete por $2,300.00 cuando compras menos de 10 unidades.
#Si se compran 10 o más, se aplica un descuento.


def calcularPagoTotal(numPaquetes):
    if numPaquetes >= 1 and numPaquetes <=9:
        pagoTotal = numPaquetes*2300
        return pagoTotal
    elif numPaquetes >= 10 and numPaquetes <=19 :
        pagoTotal = (numPaquetes*2300)-((numPaquetes*2300)*0.15)
        return pagoTotal
    elif numPaquetes >= 20 and numPaquetes <=49:
        pagoTotal = (numPaquetes*2300)-((numPaquetes*2300)*0.22)
        return pagoTotal
    elif numPaquetes >= 50 and numPaquetes <= 99:
        pagoTotal = (numPaquetes*2300)-((numPaquetes*2300)*0.35)
        return pagoTotal
    elif numPaquetes >= 100:
        pagoTotal = (numPaquetes*2300)-((numPaquetes*2300)*0.42)
        return pagoTotal
    elif numPaquetes <= 0:
        return "Error, introduce un número positivo mayor a 0"

def calcularDescuento(numPaquetes):
    if numPaquetes >= 10 and numPaquetes <=19:
        descuento = (numPaquetes * 2300) * 0.15
        return descuento
    elif numPaquetes >= 20 and numPaquetes <=49:
        descuento = (numPaquetes * 2300) * 0.22
        return descuento
    elif numPaquetes >= 50 and numPaquetes <= 99:
        descuento = (numPaquetes * 2300) * 0.35
        return descuento
    elif numPaquetes >= 100:
        descuento = (numPaquetes * 2300) * 0.42
        return descuento


def main():
   numPaquetes = int(input("Número de paquetes vendidos: "))
   pago = calcularPagoTotal(numPaquetes)
   descuento = calcularDescuento (numPaquetes)
   print ("Descuento: $", descuento)
   print ("El pago total es: $",pago)


main()