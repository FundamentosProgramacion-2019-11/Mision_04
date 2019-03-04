#Autor: Diego Raul Elizalde Uriarte
#escribir el tipo de triángulo de acuerdo a la longitud de sus lados


import math as m






def identificarTriangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado1 ==lado3:
        return "Equilatero"
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return "Isoceles"
    elif (lado1 > lado2 and lado1 > lado3) or (lado2 > lado1 and lado2 > lado3) or (lado3 > lado2 and lado3 > lado1) :
        if (lado1) == m.sqrt((lado2 ** 2) + (lado3 ** 2)) or (lado2) == m.sqrt((lado1 ** 2) + (lado3 ** 2)) or(lado3) == m.sqrt((lado2 ** 2) + (lado1 ** 2)):
            return "Rectangulo"
    else:
        return "Otro"






def main():
    lado1 = int(input("Dame el valor del primer lado"))
    lado2 = int(input("Dame el valor del segundo lado"))
    lado3 = int(input("Dame el valor del tercer lado"))
    if (lado1+lado2)>lado3 or (lado1+lado3)>lado2 or (lado3+lado2)>lado1:
        identificarTriangulo(lado1,lado2,lado3)
        print("El triangulo es: ", identificarTriangulo(lado1,lado2,lado3))
    else:
        print("Estos lados no corresponden a un triángulo.")





main()