#Autor: Jose Luis Mata Lomeli
#Diferenciar cual es un triangulo Rectangulo, Isosceles o Equilaterolas medidas dadas

import math

def determinarTriangulo(lado1, lado2, lado3):

    hipo = math.sqrt(lado1 ** 2 + lado2 ** 2)

    if hipo == lado3:
        return ("Es un triangulo rectangulo")

    elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
        return("Es un triangulo Isoceles")

    elif lado1 == lado2 and lado2 == lado3:
        return("Es un triangulo Equilatero")

    return ('No existe este triangulo')


def main():

    lado1 = int(input("Escribe la magnitud del lado 1 del triangulo: "))
    lado2 = int(input("Escribe la magnitud del lado 2 del triangulo: "))
    lado3 = int(input("Escribe la magnitud del lado 3 del triangulo: "))

    determinar = determinarTriangulo(lado1, lado2, lado3)

    print(determinar)

main()