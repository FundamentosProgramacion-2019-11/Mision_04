#Autor: Santiago España Vázquez A01748311
#Descripción: Entrega precio de paquetes vendidos aplicando descuentos


def calculatePrice(n):
    if n<1:
        return "Error"
    elif n<10:
        m=n*2300
        return m
    elif n<20:
        m=(n*2300)*.85
        d=(n*2300)*.15
        r=("El descuento es de: %i y el Total a pagar es de: %i" %(d,m))
        return r
    elif n<50:
        m=(n*2300)*.78
        d=(n*2300)*.22
        r = ("El descuento es de: %i y el Total a pagar es de: %i" % (d, m))
        return r
    elif n<100:
        m=(n*2300)*.65
        d=(n*2300)*.35
        r = ("El descuento es de: %i y el Total a pagar es de: %i" % (d, m))
        return r
    else:
        m = (n * 2300) * .58
        d = (n * 2300) * .42
        r = ("El descuento es de: %i y el Total a pagar es de: %i" % (d, m))
        return r


def main():
    n=int(input("Por favor introduzca la cantidad de paquetes que comprara: "))
    price= calculatePrice(n)
    print(price)

main()