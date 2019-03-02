#Autor: Yasmín Landaverde Nava
#Descripción: Calcula el total a pagar de un software


def calcularDescuento(n):
    if n>=1 and n<=9:
        descuento = 0
    elif n>=10 and n<=19:
        descuento = (2300*n)*.15
    elif n>=20 and n<=49:
        descuento = (2300*n)*.22
    elif n>=50 and n<=99:
        descuento = (2300*n)*.35
    elif n>=100:
        descuento = (2300*n)*.42
    else:
        descuento = "error"

    return descuento

def calcularTotal(n):
    if n <= 0:
        return "error"
    else:
        des = calcularDescuento(n)
        total =  (2300*n)-(des)
        return total

def main():
    n = int(input("Teclea el número de unidades: "))
    des =calcularDescuento(n)
    print ("Descuento de: $", des)
    total = calcularTotal(n)
    print ("El total es: $", total)

main()