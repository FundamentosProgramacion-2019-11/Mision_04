#Mariana Coria Rodríguez, A01374765
#Programa que cuente los paquetes comprados, cantidad descontada y total de pago


#Calcular el descuento
def descontado (paquetes, costoSolo):
    if paquetes >= 10 and paquetes <= 19:
        descuento = (0.15 *costoSolo)
        return descuento
    elif paquetes >= 20 and paquetes <= 29:
        descuento = (0.22 * costoSolo)
        return descuento
    elif paquetes >= 30 and paquetes <= 99:
        descuento = (0.35 * costoSolo)
        return descuento
    elif paquetes >= 100:
        descuento = (0.44 * costoSolo)
        return descuento
    else:
        return 0


#Definir main y preguntar por datos
def main():
    paquetes = int(input("¿Cuantos paquetes compraste? "))
    if paquetes <= 0:
        print("Los números negativos no son validos.")
    else:
        costoSolo = paquetes*2300
        descuento = descontado(paquetes, costoSolo)
        costoTotal = (costoSolo - descuento)
        print("Costo con descuento: $ %.2f " % descuento)
        print("Pago total: $ %.2f " % costoTotal)

main()



