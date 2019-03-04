#Alan Giovanni Rodriguez Camacho A01748185
#Lee el numero de paquetes que deseas comporar y dependiendo de la cantidad se te aplica un descuento.


def calcularDescuentoTotal(paquetes): #Calcula el descuento dependiendo del numero de paquetes comprados.
    if paquetes < 10:
        descuento=0
    elif paquetes >= 10 and paquetes <=19:
        descuento=15
    elif paquetes >= 20 and paquetes <=49:
        descuento=22
    elif paquetes >= 50 and paquetes <=99:
        descuento=35
    else:
        descuento=42
    return descuento


def calcularTotalPago(paquetes): #Calcula el total a pagar dependiendo del descuento y los paquetes comprados.
    descuento=calcularDescuentoTotal(paquetes)
    totalPago=(paquetes*2300)-((paquetes*2300)*(descuento/100))
    return totalPago


def main():
    paquetes=int(input("Teclea el numero de paquetes que deseas adquirir: "))
    if paquetes<= 0:
        print("ERROR: EL NUMERO QUE USTED AH TECLEADO NO ES VALIDO.")
    else:
        totalPago=calcularTotalPago(paquetes)
        descuento=calcularDescuentoTotal(paquetes)
        print("El total a pagar por {0} paquetes con un descuento de {1}% es: {2}$".format(paquetes,descuento,totalPago))


main()
