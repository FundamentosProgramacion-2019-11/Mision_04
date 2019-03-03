#Bernardo Mondragon Ramirez A01022325
# Calcular Area, Perimetro de 2 rectangulos e idincar cual es mayor



def ARectangulo1(base, altura):
    a1= base * altura
    return a1

def PRectangulo1(base, altura):
    p1= base *2 + altura*2
    print()
    print("Perimetro Rectangulo 1:", p1)




def ARectangulo2(base2, altura2):
    a2= base2 * altura2
    return a2

def PRectangulo2(base2, altura2):
    p2= base2 *2 + altura2*2
    print("Perimetro Rectangulo 1", p2)



def RectanguloMayor(a1,a2):

    if a1>a2:
        return "El area del Rectangulo 1 es mayor"
    elif a1<a2:
        return "El area del Rectangulo 2 es mayor"
    else:
        return "Las areas iguales las area"


def main():
    altura = int(input("Teclea altura 1: "))
    base = int(input("Teclea base 1: "))
    altura2 = int(input("Teclea altura 2: "))
    base2 = int(input("Teclea base 2: "))

    a1= ARectangulo1(base, altura)
    a2= ARectangulo2(base2, altura2)




    ARectangulo1(base, altura)
    ARectangulo2(base2, altura2)
    RectanguloMayor(a1, a2)
    PRectangulo1(base, altura)
    PRectangulo2(base2, altura2)

    print()
    print("Area Rectangulo 1: ",ARectangulo1(base, altura))
    print("Area Rectangulo 2: ",ARectangulo2(base2, altura2))

    print(RectanguloMayor(a1, a2))




main ()