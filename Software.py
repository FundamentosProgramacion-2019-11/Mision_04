#Autor: María Fernanda García Gastélum A01376181
#Calcular el total a pagar de un software con descuento


#Calcular el descuento dependiendo de los paquetes comprados
def calcularDescuento(paquetesComprados, costoSinDescuento):
    if paquetesComprados >= 10 and paquetesComprados <= 19:
        descuento=(costoSinDescuento*0.15)
        return descuento
    elif paquetesComprados >= 20 and paquetesComprados <= 29:
        descuento= (costoSinDescuento*0.22)
        return descuento
    elif paquetesComprados >= 30 and paquetesComprados <= 99:
        descuento= (costoSinDescuento*0.35)
        return descuento
    elif paquetesComprados >= 100:
        descuento = (costoSinDescuento*0.44)
        return descuento
    else:
        return 0


def main():
    paquetesComprados= int(input("Escribe el número de paquetes a comprar: "))
    if paquetesComprados <= 0:
        return print("Error.")
    else:
        costoSinDescuento = 2300 * paquetesComprados
        descuento = calcularDescuento(paquetesComprados, costoSinDescuento)
        totalAPagar= (costoSinDescuento - descuento)
        print("Costo sin descuento= $", costoSinDescuento)
        print("Descuento= -$ %.2f" %(descuento))
        print("Total a pagar= $", totalAPagar)


main()