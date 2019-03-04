# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Programa que calcula cuanto descuento se te ha aplicado en la compra de paquetes y el pago total


#Esta función calcula el descuento que se aplica dependiendo de los paquetes comprados
def calcularDescuento(paquetes):
    if paquetes>=1 and paquetes<=9:
        descuento= 0
    elif paquetes>=10 and paquetes<=19:
        descuento=.15
    elif paquetes>=20 and paquetes<=49:
        descuento= .22
    elif paquetes>=50 and paquetes<=99:
        descuento= .35
    elif paquetes>=100:
        descuento= .42
    else:
        descuento = "error"

    return descuento


#la función imprime el total de la compra incluyendo el descuento y te dice cuanto se te desconto
def main():
    paquetes= int(input("Ingresa cuantos paquetes deseas comprar (si compras 10 o mas se aplica un descuento): "))

    descuento= calcularDescuento(paquetes)

    if descuento == "error":
        print("Error")
    else:
        total= paquetes*(2300-(2300*(descuento)))
        cantidadDescontada = 2300*descuento*paquetes

        print("Se te desconto $",cantidadDescontada,"y tendras que pagar en total $",total)


main()