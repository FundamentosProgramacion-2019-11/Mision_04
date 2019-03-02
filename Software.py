#Autor: Michel Antoine Dionne Gutierrez Grupo:03 A01748632
#Determina el costo y posible descuento de uos paquetes

#Esta funcion determina los costos totales y descuentos dependiendo del numero de paquetes
def calcularCosto(paquetes):
    if paquetes<=0:
        return "Error"
    else:
        if paquetes<10:
            costo = paquetes*2300
            descuento = 0
            return 'El costo total es de ', costo,' y el descuento es de ',descuento
        else:
            if paquetes>=10 and paquetes<=19:
                costo = (paquetes*2300)-((paquetes*2300)*.15)
                descuento = (paquetes*2300)*.15
                return 'El costo total es de ', costo,' y el descuento es de ',descuento
            else:
                if paquetes>=20 and paquetes<=49:
                    costo = (paquetes * 2300) - ((paquetes * 2300) * .22)
                    descuento = (paquetes * 2300) * .22
                    return 'El costo total es de ', costo, ' y el descuento es de ', descuento
                else:
                    if paquetes>=50 and paquetes<=99:
                        costo = (paquetes * 2300) - ((paquetes * 2300) * .35)
                        descuento = (paquetes * 2300) * .35
                        return 'El costo total es de ', costo, ' y el descuento es de ', descuento
                    else:
                        if paquetes>=100:
                            costo = (paquetes * 2300) - ((paquetes * 2300) * .42)
                            descuento = (paquetes * 2300) * .42
                            return 'El costo total es de ', costo, ' y el descuento es de ', descuento


def main():
    paquetes=int(input("Dame el numero de paquetes vendidos"))
    respuesta = calcularCosto(paquetes)
    print(respuesta)

main()
