 #Autor: Luis Alberto Zepeda Hernandez
#Descripcion: Escribe un programa que lee el número de paquetes vendidos
# y despliega la cantidad descontada y el total a pagar

#Esta función se encarga de calcular el descuento.
def calcularDescuento(numeroPaquetes):
    costoSin = numeroPaquetes * 2300
    if  numeroPaquetes < 10:
        descuento = (costoSin*0)/100
        return descuento

    elif numeroPaquetes>= 10 and numeroPaquetes<=19:
        descuento = (costoSin * 15) / 100
        return descuento

    elif numeroPaquetes>=20 and numeroPaquetes<=49:
        descuento = (costoSin * 22) / 100
        return descuento

    elif numeroPaquetes>=50 and numeroPaquetes<=99:
        descuento = (costoSin * 35) / 100
        return descuento

    elif numeroPaquetes>=100:
        descuento = (costoSin * 42) / 100
        return descuento


#Esta función se encarga de calcular el total con descuento.
def calcularTotal(numeroPaquetes, descuento):
     total = (numeroPaquetes *2300) - descuento
     return total
# Esta función pide al usuario los datos, y llama a las otras funciones.
def main():
    numeroPaquetes = float(input("Ingresa el número de paquetes vendidos: "))
    descuento = calcularDescuento(numeroPaquetes)
    total = calcularTotal(numeroPaquetes, descuento)
    print("Descuento: $", descuento)
    print("Costo Total: $",total )




main()