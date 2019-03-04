# Autor: Victor Manuel Ceron Navarrete
# Descripcion: El código calcula el costo total por mayoreo de un software


#Calcula el descuento de acuerdo a las unidades compradas
def sacarDescuento(unidades, costoSinDescuento):
    if unidades >= 10 and unidades <= 19:
        descuento = (costoSinDescuento * 0.15)
        return descuento
    elif unidades >= 20 and unidades <= 29:
        descuento = (costoSinDescuento * 0.22)
        return descuento
    elif unidades >= 30 and unidades <= 99:
        descuento = (costoSinDescuento * 0.35)
        return descuento
    elif unidades >= 100:
        descuento = (costoSinDescuento * 0.44)
        return descuento
    else:
        return 0


# Función main que lee la cantidad de paquetes e imprime el resultado con descuento y el descuento
def main():
    unidades = int(input("Teclee el total de paquetes de software adquiridos: "))
    if unidades <= 0:
        print("ERROR: No ha comprado softwares")
    else:
        costoSinDescuento = 2300 * unidades
        descuento = sacarDescuento(unidades , costoSinDescuento)
        totalAPagar = (costoSinDescuento - descuento)
        print("El descuento de su compra es : $%.2f"% descuento, "MXN")
        print("Su total a pagar es : $%.2f "% totalAPagar, "MXN")


main()