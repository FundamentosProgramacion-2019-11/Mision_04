#Autor: Cesar Guzman Guadarrama
#Este programa lee el numero de paquetes vendidos e imprime el total a pagar ya con descuento.


def calcularCosto(paquetes):       #Esta funcion calcula el costo
    if paquetes >= 1 and paquetes <= 9:
        precio = (paquetes * 2300)
        return precio
    elif paquetes >= 10 and paquetes <= 19:
        precio = (paquetes * 2300) * .85
        return precio
    elif paquetes >= 20 and paquetes <= 49:
        precio = (paquetes * 2300) * .78
        return precio
    elif paquetes >= 50 and paquetes <= 99:
        precio = (paquetes * 2300) * .65
        return precio
    elif paquetes <= 0:
        print( "ERROR" )
    else:
        precio = (paquetes * 2300) * .58
        return precio



def main():    #Resuelve el problema
    paquetes = int(input("¿Cuantos paquetes de software compraron?"))
    precio = calcularCosto(paquetes)
    print("El precio final es de $",precio)

main()