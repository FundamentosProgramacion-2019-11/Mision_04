# Autor: Rosalía Serrano Herrera
# Calcula la cantidad a pagar dependiendo cuantos paquetes de software se vendan


def calcularCosto(numeroPaquetes):  #calcula el costo de los paquetes
    costo = numeroPaquetes * 2300
    return costo


def calcularDescuento(numeroPaquetes, costo):   #calcula el descuento que se le va a aplicar a los paquetes
    if numeroPaquetes>=10 and numeroPaquetes<=19:
        descuento = costo *.15
    elif numeroPaquetes >=20 and numeroPaquetes <=49:
        descuento = costo * .22
    elif numeroPaquetes>=50 and numeroPaquetes<=99:
        descuento = costo * .35
    elif numeroPaquetes>=100:
        descuento = costo * .42
    else:
        descuento = "0.0"
    return descuento


def calcularPrecio(numeroPaquetes, costo, descuento):   #calcula el precio aplicando el descuento
    if numeroPaquetes>=10 and numeroPaquetes<=19:
        precio = costo - descuento
    elif numeroPaquetes >=20 and numeroPaquetes <=49:
        precio = costo - descuento
    elif numeroPaquetes>=50 and numeroPaquetes<=99:
        precio = costo - descuento
    elif numeroPaquetes>=100:
        precio = costo - descuento
    else:
        precio = costo
    return precio


def main():
    numeroPaquetes = int(input("Teclea el número de paquetes vendidos: "))
    if numeroPaquetes <= 0:
        print("ERROR")
    else:
        costo = calcularCosto(numeroPaquetes)
        descuento = calcularDescuento(numeroPaquetes, costo)
        precio = calcularPrecio(numeroPaquetes, costo, descuento)
        print("La cantidad descontada es: $", descuento)
        print("El total a pagar es: $", precio)


main()