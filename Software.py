#Autor: Luis Renteria
#Calcular los precios del software

def calcularPrecio(PaquetesVendidos):
    Precio=PaquetesVendidos*2300
    if Precio >=10 and Precio<20:
        PrecioTotal=Precio*.85
    elif Precio >=20 and Precio<50:
        PrecioTotal=Precio*.78
    elif Precio >=50 and Precio<100:
        PrecioTotal=Precio*.65
    elif Precio >=100:
        PrecioTotal=Precio*.58
    else:
        PrecioTotal=Precio
    return PrecioTotal


def main():
    PaquetesVendidos=int(input("Introduce el numero de paquetes vendidos"))
    Total=calcularPrecio(PaquetesVendidos)
    print ("El precio con descuento es:",Total)


main()
