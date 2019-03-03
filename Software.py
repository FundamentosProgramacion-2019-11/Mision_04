#Autor: Daniela Estrella Tovar
# Calcular el costo total con el descuento correspondiente según la cantidad de paquetes comorados.

#Esta función calcula el costo total a pagar.

def calcularCosto(cantPaq):
    costo= cantPaq * 2300
    if cantPaq>=1 and cantPaq<=10:
        total= costo
    elif cantPaq>=10 and cantPaq<=19:
        total = costo * .85
    elif cantPaq>=20 and cantPaq<=49:
        total =costo * .78
    elif cantPaq>=50 and cantPaq<=99:
        total =costo * .65
    elif cantPaq>100:
        total = costo * .58
    else:
        total = "Error"
    return total


#Esta función calcula cuanto descuento se aplicó.

def calcularDescuento(cantPaq):
    costo = cantPaq * 2300
    if cantPaq >= 1 and cantPaq <= 10:
        descuento = "No hay descuento"
    elif cantPaq >= 10 and cantPaq <= 19:
        descuento = costo * .15
    elif cantPaq >= 20 and cantPaq <= 49:
        descuento = costo * .22
    elif cantPaq >= 50 and cantPaq <= 99:
        descuento = costo * .35
    elif cantPaq > 100:
        descuento = costo * .42
    else:
        descuento = "Error"
    return descuento

#La función main lee e imprime valores.

def main():
    cantPaq= int(input("Teclea la cantidad de Paquetes de Software Comprados: "))
    total= calcularCosto(cantPaq)
    print("El costo total a pagar es de $ ", total)
    rebaja= calcularDescuento(cantPaq)
    print("El descuento fue de $", rebaja)

main()