#Autor: Diego Raul Elizalde Uriarte
#Calcular la cantidad descontada y el total a pagar



def calcularTotal(paquetes):
    Total = ((paquetes*2300)*calcularDescuento(paquetes))+(paquetes*2300)
    return Total
def calcularCantidad(paquetes):
    Cant = calcularDescuento(paquetes)*2300
    return Cant

def calcularDescuento(paquetes):
    if paquetes < 10:
         descuento = 0
    elif paquetes >= 10 and paquetes < 20:
        descuento = .15
    elif paquetes >= 20 and paquetes <50:
        descuento = .22
    elif paquetes >= 50 and paquetes <100:
        descuento = .35
    else:
        descuento = .42

    return descuento





def main():
    paquetes = int(input("Dame el número de paquetes vendidos: "))
    if paquetes <1:
     print("Error")
    else:
        calcularDescuento(paquetes)
        print("La cantidad descontada es de: ", calcularCantidad(paquetes))
        print("El total a pagar es: ", calcularTotal(paquetes))



main()