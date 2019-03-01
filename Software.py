# Autor: Itzel Yanabany Castro Becerril
# Calcular el pago total de la compra con el descuento adquirido


# La funcion calculara el cual sera el descuento que tendra el cliente
def calcularCantidadDescontada(paquete):
    if paquete > 0 and paquete < 10:
        descuento = 0
        return descuento
    else:
        if paquete >= 10 and paquete <= 19:
            descuento = paquete * 2300 * 0.15
            return descuento
        else:
            if paquete >= 22 and paquete <= 49:
                descuento = paquete * 2300 * 0.22
                return descuento
            else:
                if paquete >= 50 and paquete <= 99:
                    descuento = paquete * 2300 * 0.35
                    return descuento
                else:
                    if paquete >= 100:
                        descuento = paquete * 2300 * 0.12
                        return descuento
                    else:
                        print("error")


# La funcion imprimira el descuento de la compra
def imprimirCantidadDescontada(paquete):
    descuento = calcularCantidadDescontada(paquete)
    print("El descuento de la compra es de:$ ", descuento)


# La funcion calculara el pago total de la compra
def calcularPagoTotal(paquete):
    if paquete > 0 and paquete < 10:
        pago = paquete * 2300
        return pago
    else:
        if paquete >= 10 and paquete <= 19:
            costo = (paquete * 2300)
            descuento=costo*0.15
            pago=costo-descuento
            return pago
        else:
            if paquete >= 22 and paquete <= 49:
                costo = (paquete * 2300)
                descuento=costo*0.22
                pago=costo-descuento
                return pago
            else:
                if paquete >= 50 and paquete <= 99:
                    costo = (paquete * 2300)
                    descuento=costo*0.35
                    pago=costo-descuento
                    return pago
                else:
                    if paquete >= 100:
                        costo = (paquete * 2300)
                        descuento=costo*0.42
                        pago=costo-descuento
                        return pago
                    else:
                            print("error")


# la funcion imprimira el pago total
def imprimirPagoTotal(paquete):
    costo = calcularPagoTotal(paquete)
    print("El costo total de su compra es de:$ ", costo)


def main():
    paquete = int(input("Teclea el numero de un unidades que compraste: "))
    imprimirCantidadDescontada(paquete)
    imprimirPagoTotal(paquete)


main()

