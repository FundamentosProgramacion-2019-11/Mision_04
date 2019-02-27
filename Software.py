#María Angélica Hernández Parada
#Compras de un software y dependiendo la cantidad es el descuento

def cantidadDePaquetes(paquetes,precio):
    if paquetes<=0:
        return "error"
    if paquetes<10:
        precio1 = paquetes*precio
        return ("$",precio1)
    if paquetes>=10 and paquetes<=19:
        precioSinD=paquetes*precio
        precio2 = (paquetes*precio)*.85
        return ("Sin descuento",precioSinD,"Con descuento",precio2)
    if paquetes>=20 and paquetes<=49:
        precioSinD1 = paquetes * precio
        precio3= (paquetes*precio)*.78
        return ("Sin descuento",precioSinD1,"Con descuento",precio3)
    if paquetes>=50 and paquetes<=99:
        precioSinD2 = paquetes * precio
        precio4 = (paquetes * precio) *.65
        return ("Sin descuento", precioSinD2, "Con descuento", precio4)
    if paquetes>=100:
        precioSinD3 = paquetes * precio
        precio5 = (paquetes * precio) * .58
        return ("Sin descuento", precioSinD3, "Con descuento", precio5)


def main():
    paquetes = int(input("Cuantos paquetes quieres comprar?"))
    precio=2300
    print(cantidadDePaquetes(paquetes,precio))


main()
