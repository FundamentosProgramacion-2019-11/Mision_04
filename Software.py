#Luis Adrian Carmona Villalobos
#progama que lee cantidad de paqueets vendidos y la cantidad a pagar dependiendo del descuento por cantidad

def calcularTotalPago(p):
    if p > 0 and p <10:
        t = p*2300
        print("Su total es de: ", t)
    elif p >=10 and p <= 19 :
        sin_descuento = p*2300
        t = sin_descuento*.85
        print("Su total es de: ",t)
    elif p >=20 and p <= 49:
        sin_descuento = p*2300
        t = sin_descuento*.78
        print("Su total es de: ",t)
    elif p >= 50 and p<= 99:
        sin_descuento = p*2300
        t = sin_descuento*.65
        print("Au total es de: ",t)
    elif p >= 100:
        sin_descuento = p*2300
        t = sin_descuento*.58
        print("Su total a pagar es de: ", t)
    else:
        print("error")



def main():
    p = int(input("Teclea la cantidad de paquetes vendidos: "))
    calcularTotalPago(p)


main()