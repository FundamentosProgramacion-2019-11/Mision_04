#Roberto Castro Barrios A01748559
#Descripción: Programa que aplica un descuento de acuerdo al numero de paquetes que compres.


def calcularDescuento (n):
    if n<10 :
        total = n*2300
        return total
    elif n>=10 and n<=19:
        total = (n*2300)*0.85
        return total
    elif n>=20 and n<=49:
        total = (n*2300)*0.78
        return total
    elif n >= 50 and n<=99:
        total = (n * 2300) * 0.65
        return total
    else:
        total = (n * 2300) * 0.58
        return total

def main ():
    n = int(input("Cuantos paquetes compraste: "))
    descuento = calcularDescuento(n)
    if descuento<=0:
        print("Error, valor incorrecto")
    else:
        print("El total a pagar es: %.2f"%(descuento))

main()