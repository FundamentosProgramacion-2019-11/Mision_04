# Autor: Rosalía Serrano Herrera
# Define qué tipo de triángulo corresponde a las medidas que teclea el usuario


def definirTriangulo(lado1, lado2, lado3):  #determina que tipo de triangulo es dependiendo sus lados
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    elif lado1**2 == lado2**2 + lado3**2 or lado2**2 == lado1**2 + lado3**2 or lado3**2 == lado1**2 + lado2**2:
        return "Rectángulo"
    else:
        return "Otro"


def main():
    lado1 = int(input("Teclea un lado del triángulo: "))
    lado2 = int(input("Teclea otro lado del triángulo: "))
    lado3 = int(input("Teclea el último lado del triángulo: "))
    if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado2 + lado1:
        print("Estos lados no corresponden a un triángulo.")
    else:
        triangulo = definirTriangulo(lado1, lado2, lado3)
        print("El tipo de triángulo es:", triangulo)


main()