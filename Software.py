#Autor: Katia Hernández Bsrrera
#Programa que calcula el descuento en la compra de software así como el precio total.

def main():
    n = int(input("Cantidad de paquetes vendidos: "))
    descuento = calcularDescuento(n)
    print("Cantidad descontada: ", descuento)
    total = calcularTotal(n)
    print("Total a pagar: ", total)


def calcularDescuento(n):   #función que calcula la cantidad descontada del precio total
    if n < 10:
        d = 0
    elif n >= 10 and n <= 19:
        d = 2300 * 0.15
    elif n >= 20 and n <=49:
        d = 2300 * 0.22
    elif n >= 50 and n <= 99:
        d = 2300 * 0.35
    elif n >= 100:
        d = 2300 *0.42
    return d

def calcularTotal(n):   # función que calcula el precio total de los softwares
    if n <= 0:
        t = "ERROR, no ha comprado ningún software"
    elif n <= 10:
        t = 2300
    elif n >= 10 and n <= 19:
        t = 2300-(2300*0.15)
    elif n >= 20 and n <=49:
        t = 2300-(2300*0.22)
    elif n >=50 and n <=99:
        t = 2300-(2300*0.35)
    elif n >=100:
        t = 2300-(2300*0.42)
    return t


main()