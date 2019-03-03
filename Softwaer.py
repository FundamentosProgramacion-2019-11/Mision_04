#Autor Sofía Trujillo Vargas
#De acuerdo al número de productos que se compre aplicar un descuento.

def main():
    npaquetes = int(input("¿Cuantos paquetes quieres?: "))
    if npaquetes <= 0:
        print("Valor inválido")
    else:
        total = npaquetes * 2300
        descuento = Descuentopaquetes(npaquetes)
        totalFinal = total-descuento
        print("El total sin descuento es: ",total)
        print("La cantidad descontada es: ", descuento)
        print("El total a pagar es: ",totalFinal)

def Descuentopaquetes(npaquetes):
    if npaquetes < 10:
        return 0
    elif npaquetes >= 10 and npaquetes <= 19:
        des = (npaquetes*2300)*.15
        return des
    elif npaquetes >= 20 and npaquetes <= 49:
        des = (npaquetes*2300)*.22
        return des
    elif npaquetes >= 50 and npaquetes <= 99:
        des = (npaquetes * 2300)*.35
        return des
    elif npaquetes >= 100:
        des = (npaquetes*2300)*.42
        return des


main()