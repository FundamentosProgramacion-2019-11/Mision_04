#Autor: Karla Ximena Rueda Ruiz
#Este programa calcula el total a pagar de paquetes de software, con su respectivo descuento.

def main():

    paquetes = int(input("Inserte la cantidad de paquetes: "))
    total=calcularPrecio(paquetes)
    print("El total a pagar es =", total)


def calcularPrecio(paquetes):
    tnormal= paquetes*2300

    if paquetes<10 and paquetes>=1:
        tdescuento = tnormal

    elif paquetes>=10 and paquetes<=19:
        tdescuento = tnormal-tnormal*0.15

    elif paquetes>=20 and paquetes<=49:
        tdescuento = tnormal-tnormal*0.22

    elif paquetes>=50 and paquetes<=99:
       tdescuento = tnormal-tnormal*0.35

    elif paquetes>=100:
        tdescuento = tnormal-tnormal*0.42

    else:
        tdescuento = "Error"

    return tdescuento


main()







