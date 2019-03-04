#Luis Adrian Carmona Villalobos
#Progama que calcula area y perimetro de 2 rectangulos


def calcularArea1(base1,h1):
    area1 = base1*h1
    return area1


def calcularArea2(base2,h2):
    area2 = base2 * h2
    return area2


def calcularPerimetro1(base1,h1):
    perimetro1 = base1*2+h1*2
    return perimetro1


def calcularPerimetro2(base2,h2):
    perimetro2 = base2*2+h2*2
    return perimetro2


def main():
    base1 = int(input("Cual es base del rectangulo 1: "))
    base2 = int(input("Cual es base del rectangulo 2: "))
    h1 = int(input("Cual es la altura del rectangulo 1: "))
    h2 = int(input("Cual es la altura del rectangulo 2: "))


    if calcularArea1(base1,h1) == calcularArea2(base2,h2):
        print("Sus areas son iguales")
    elif calcularArea1(base1,h1) > calcularArea2(base2,h2):
        print("El primer rectangulo tiene un area mayor")
    elif calcularArea1(base1,h1) < calcularArea2(base2,h2):
        print("El segundo rectangulo tiene un area mayor")

main()