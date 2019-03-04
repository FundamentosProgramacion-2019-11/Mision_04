#Autor: Aline Villegas Berdejo
#Calcula la cantidad a pagar por un software junto con los descuentos aplicables


def calcularPagoTotal(paquetes):         #Calcula el total a pagar de acuerdo a los descuentos correspondientes
    if paquetes>=1 and paquetes<=9:
        costo=(paquetes*2300)
    elif paquetes>=10 and paquetes<=19:
        costo=(paquetes*2300)-(paquetes*2300)*.15
    elif paquetes>=20 and paquetes<=49:
        costo=(paquetes*2300)-(paquetes*2300)*.22
    elif paquetes>=50 and paquetes<=99:
        costo=(paquetes*2300)-(paquetes*2300)*.35
    elif paquetes>=100:
        costo=(paquetes*2300)-(paquetes*2300)*.42
    else:
        costo= 0

    return costo


def main():                 #Indica las funciones que se van a correr al llamar a la funición "main()"
    paquetes=int(input("Introduzca la cantidad de paquetes comprados: "))
    cp= calcularPagoTotal(paquetes)
    if cp==0:
        print("Error, no se aceptan valores negativos ni cero.")
    else:
        print("El total a pagar por los paquetes es= $%.2f " % cp)


main()