#Autor: Eric Andrés Jardón Chao
#Programa que calcula el costo total a pagar según la cantidad de unidades de software vendidas y el descuento correspondiente.

def main(): #La función principal recibe el número de unidades. Si el número es menor a cero, no corre el cálculo de costo e imprime error. Si es positivo, corre la función para encontrar el costo y lo imprime.
    unidades=int(input("Teclea el número de unidades de software vendidas: "))
    if unidades<0:
        print("Error: no es posible realizar el cálculo con números negativos.")
    else:
        costo=calcularCosto(unidades)
        print("El costo de",unidades,"unidades de software es de: $%.2f"%(costo))


def calcularCosto(unidades): #Dependiendo del número de unidades se determina el descuento que se aplica al costo de las unidades en total. Se multiplica por (1-d) donde d es el descuento porcentual.
    if unidades<10:
        costo=unidades*2300
        return costo
    if unidades>=10 and unidades<=19:
        costo=unidades*2300*0.85 #Descuento de 15 porciento
        return costo
    if unidades>=20 and unidades<=49:
        costo=unidades*2300*0.78 #Descuento de 22 porciento
        return costo
    if unidades>=50 and unidades<=99:
        costo=unidades*2300*0.65 #Descuento de 35 porciento
        return costo
    if unidades>=100:
        costo=unidades*2300*0.58 #Descuento de 42 porciento
        return costo

main()
#Fin del programa