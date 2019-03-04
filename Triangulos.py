# Autor: Ronaldo Estefano Lira Buendia
# Definir el nombre del triangulo con los lados dados por el usuario.

import math

def definirTriangulo(l1, l2, l3):
    if l1==l2==l3:
        triangulo = ("Triangulo equilatero")
    elif l3==math.sqrt((l1**2)+(l2**2)) or l2==math.sqrt((l1**2)+(l3**2)) or l1==math.sqrt((l3**2)+(l2**2)):
        triangulo = ("Triangulo rectangulo")
    elif l1!=l2!=l3:
        triangulo = ("Triangulo escaleno")
    elif (l1==l3 and l1!=l2 and l3!=l2) or (l2==l3 and l1!=l2 and l3!=l1) or (l1==l2 and l1!=l3 and l3!=l2):
        triangulo = ("Triangulo isosceles")
    else:
        triangulo = ("Estos lados no corresponden a un triangulo")
    return triangulo


def main():
    l1 = int(input("Ingrese el valor del primer lado: "))
    l2 = int(input("Ingrese el valor del segundo lado: "))
    l3 = int(input("Ingrese el valor del tercer lado: "))
    triangulo = definirTriangulo(l1, l2, l3)
    print(triangulo)


main()