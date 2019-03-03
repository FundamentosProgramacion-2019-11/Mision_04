#Autor: Cecilia Daniela Olivares Hernández, a01745727
#Este programa calcula el descuento y total a pagar dependiendo del número de paquetes comprados


#Esta función calcula la cantidad que se descontara
def calcularDescuento(p):
    precio = 2300*p
    if  p <= 0:
        d = "ERROR"
    elif p <= 9:
        d = "No hay descuento"
    elif p>=10 and p<=19:
        d = precio*.15
    elif p>=20 and p<=49:
        d = precio*.22
    elif p>=50 and p<=99:
        d = precio*.35
    elif p>=100:
        d = precio*.42
    return d


#Esta función calcula el precio total a pagar
def calcularTotal(p):
    precio = 2300*p
    if p <=0:
        t = "ERROR"
    elif p<=9:
        t = "2300"
    elif p>=10 and p<=19:
        t = precio*.85
    elif p>=20 and p<=49:
        t = precio*.78
    elif p>=50 and p<=99:
        t = precio*.65
    elif p>=100:
        t = precio*.58
    return t


#Funcion principal que resuelve el problema
def main():
    p = int(input("Inserta la cantidad de paquetes comprados: "))
    d = calcularDescuento(p)
    t = calcularTotal(p)
    print("""La cantidad descontada es: $""", (d), """
La cantidad total a pagar es: $""",(t))


main()
