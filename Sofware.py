#Autor:Bernardo Mondragón Ramirez A01022325
#Calcular el precio con descuento



def CantidadDeCanciones(c):
    if c>=1 and c<=9:
        return "2,300$ no hay descuento"
    elif c>=10 and c<=19:

        d = (c * 2300) * .15
        t = (2300*c) - d
        return t
    elif c>=20 and c<=49:
        d = (c * 2300) * .22
        t = (2300*c) - d
        return t
    elif c>=49 and c<=99:
        d = (c * 2300) * .35
        t = (2300*c) - d
        return t
    elif c>100:
        d = (c * 2300) * .45
        t = (2300*c) - d
        return t
    else:
        return "Error"


def main():
    c = int(input("Cantiad de canciones: "))
    t = CantidadDeCanciones(c)
    print(t)


main()