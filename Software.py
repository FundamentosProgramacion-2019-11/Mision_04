# Autor: José Luis Macías Vázquez, A01655713, Grupo 03
# El programa dice cuanto es el descuento por una comra y de cuaánto es el total a pagar


def aplicarDescuento(p):

    if p < 10 and p >= 1:
        return p * 2300
    elif p >= 10 and p <= 19:
        return ((p * 2300)/100) * 85
    elif p >= 20 and p <= 49:
        return ((p * 2300)/100) * 78
    elif p >= 50 and p <= 99:
        return ((p * 2300) / 100) * 65
    elif p >= 10:
        return ((p * 2300) / 100) * 58
    else:
        return "Error"






def main():

    p = int(input("Escribe la cantidad de paquetes: "))
    print("El total a pagar es: ", aplicarDescuento(p))

main()