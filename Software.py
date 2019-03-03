# Autor: Guillermo De Anda Casas , A01375892
# Código que calcula el total a pagar de los paquetes que se venden.


#Función que calcula el descuento con base al número de paquetes comprados.
def calcularDescuento(paquetes, costoSinDescuento):
    if paquetes >= 10 and paquetes <= 19:
        descuento = (costoSinDescuento * 0.15)
        return descuento
    elif paquetes >= 20 and paquetes <= 29:
        descuento = (costoSinDescuento * 0.22)
        return descuento
    elif paquetes >= 30 and paquetes <= 99:
        descuento = (costoSinDescuento * 0.35)
        return descuento
    elif paquetes >= 100:
        descuento = (costoSinDescuento * 0.44)
        return descuento
    else:
        return 0


# Función main que lee la cantidad de paquetes e imprime el resultado
def main():
    paquetes = int(input("Inserte el total de paquetes: "))
    if paquetes <= 0:
        print("ERROR")
    else:
        costoSinDescuento = 2300 * paquetes
        descuento = calcularDescuento(paquetes , costoSinDescuento)
        totalAPagar = (costoSinDescuento - descuento)
        print("El descuento es de: $%.2f"% descuento, "pesos")
        print("El total a pagar es de: $%.2f "% totalAPagar, "pesos")


main()