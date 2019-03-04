#Autor: Marianela Contreras D.
#Programa para calcular el descuento y el total a pagar de una compañiía de software.


# función para calcular el descuento de los paquetes vendidos
def calcularDescuento(paquetes):
    if paquetes> 0 and paquetes<10:
        descuento= 0
    elif paquetes<=19 and paquetes>=10:
        descuento= (2300*.15)*paquetes
    elif paquetes<=49 and paquetes >=20:
        descuento= (2300*.22)*paquetes
    elif paquetes<=99 and paquetes>=50:
        descuento = (2300*.35)*paquetes
    elif paquetes>=100:
        descuento= (2300*.42)*paquetes
    else:
        descuento = "Error"

    return descuento


#función que recibe los paquetes como parámetro, calcula y regresa el total a pagar, aplicando el descuento correspondiente
def calcularTotalApagar(paquetes):
    descuento= calcularDescuento(paquetes)

    if descuento == "Error":
        totalAPagar = "Error"
    else:
        totalAPagar = (paquetes*2300)-descuento
    return totalAPagar


# función principal del programa y la que se correrá. Las lecturas e impresiones se hacen en esta función.
def main():
 paquetes= int(input("Introduzca el número de paquetes vendidos:"))
 descuento= calcularDescuento(paquetes)
 totalAPagar= calcularTotalApagar(paquetes)

 if descuento=="Error":
     print ("Error")
 else:
     print ("El descuento es de: $%.2f"%descuento)
     print("El total a pagar es: $%.2f"%totalAPagar)

main()

