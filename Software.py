# Autor: Paulina Guerrero Ruiz
# Dar el total a pagar con descuento


def calcularDescuento(paquetesVendidos):                      # Funcion para calcular el descuento
    if paquetesVendidos>=10 and paquetesVendidos<20:
        descuento = paquetesVendidos*2300 * .15
    elif paquetesVendidos>=20 and paquetesVendidos<50:
        descuento = paquetesVendidos*2300 * .22
    elif paquetesVendidos >= 50 and paquetesVendidos <100:
        descuento = paquetesVendidos*2300 * .35
    elif paquetesVendidos>=100:
        descuento =  paquetesVendidos*2300 * .42
    elif paquetesVendidos<10:
        descuento = 0

    return descuento

def calcularCosto(paquetesVendidos):                # Funcion para calcular el costo toatl de los paquetes vendidos
    if paquetesVendidos>=10 and paquetesVendidos<20:
        precio = paquetesVendidos*2300 * .85
    elif paquetesVendidos>=20 and paquetesVendidos<50:
        precio = paquetesVendidos*2300  * .78
    elif paquetesVendidos >= 50 and paquetesVendidos <100:
        precio = paquetesVendidos*2300  * .65
    elif paquetesVendidos>=100:
        precio = paquetesVendidos*2300  * .58
    elif paquetesVendidos<10:
        precio = paquetesVendidos *2300


    return precio


def main():                                         # Funcion que pide datos e imprime resultado
    paquetesVendidos = int(input("Teclea el numero de paquetes vendidos: "))
    if paquetesVendidos<=0:
        print("error")
    else:
        precio = calcularCosto(paquetesVendidos)
        descuento = calcularDescuento(paquetesVendidos)
        print("El precio es: $", precio)
        print ("El descuento aplicado es de: %.2f" % descuento)


main()
