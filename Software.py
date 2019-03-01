#Autor: Mario Hernández Cárdenas
#Calcula el pago de la compra de un software con su respectivo descuento

#Calcula el pago por las unidades de software
def calcularPago(n):
    if n<10:
        costo = n*2300
    elif n>=10 and n<=19:
        costo =n*2300*.85
    elif n>=20 and n<=49:
        costo = n*2300*.78
    elif n>=50 and n<=99:
        costo = n*2300*.65
    else:
        costo = n*2300*.58
    return costo


def calcularDescuento(paquetes, pago):
    descuento = paquetes * 2300 - pago
    return descuento


def main():
    paquetes = int(input("Escribe la cantidad de software que compras: "))
    if paquetes<=0:
        print("No se puede comprar nada o en negativo")
    else:
        pago = calcularPago(paquetes)
        descuento = calcularDescuento(paquetes, pago)
    print("El descuento aplicado es: $ %.2f"%descuento)
    print("El total a pagar es: $ %.2f"%pago)


main()