#Autor: Mariana Teyssier Cervantes
#Conocer la cantidad de paquetes vendidos, el descuento e imprimir el total a pagar.


#Calcula el total a pagar, dependiendo del numero de paquetes
def contarPaquetes(paq):
    if paq>=1 and paq<=9:
        total = paq * 2300
    elif paq>=10 and paq<=19:
        total = paq *(2300*.85)
    elif paq>=20 and paq<=49:
        total = paq * (2300*.78)
    elif paq>=50 and paq<=99:
        total = paq * (2300*.65)
    elif paq>100:
        total = paq * (2300*.58)
    else:
        total = "Error"

    return total



#Llamamos a la funcion para contar los paquetes
def main():
    paq = int(input("Numero de paquetes: "))
    totalPago = contarPaquetes(paq)
    print"El total a pagar es", totalPago


#Llamamos a la funcion -main-
main()
