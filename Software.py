#Karimn Daniel Hernández Castorena
#Programa que calcula el descuento de una compra y el pago total de la misma.

#Funciión que calcula el descuento a realizar.
def calcularDescuento(p):
    if p>=1 and p<=9:
        d=0
    elif p>=10 and p<=19:
        d=.15
    elif p>=20 and p<=49:
        d=.22
    elif p>=50 and p<=99:
        d=.35
    elif p>=100:
        d=.42
    else:
        d= "Error"
    return d


#Función que pregunta la cantidad de paquetes e imprime el pago sin descuento, el descuento y el pago con descuento incluido.
def main():
    print()
    print("Bienvenido a PAQUETELANDIA. Si adquieres 10 o más paquetes eres candidato a recibir un descuento.")
    p=int(input("Escribe la cantidad de paquetes que estás comprando: "))
    d= calcularDescuento(p)

    if d== "Error":
        print()
        print("Error en el descuento")
    else:
        pago = p * 2300
        da = 2300*d*p
        tot = p * (2300 - (2300 * d))
        print()
        print("El pago sin descuento es de: $", pago)
        print("El descuento que recibirás es de: $", da)
        print("El total a pagar es de: $", tot)
main()