#Autor: Michel Antoine Dionne Gutierrez Grupo:03 A01748632
#Este programa determina que tipo de triangulo es

#Esta funcion determina que triangulo es
def esTrianguloRectangulo(lado1, lado2, lado3):
    if lado1*lado1 == lado2*lado2 + lado3*lado3 or lado2*lado2 == lado1*lado1 + lado3*lado3 or lado3*lado3 == lado1*lado1 + lado2*lado2:
        return "Es triangulo rectangulo"
    else:
        if lado1 == lado2 == lado3:
            return "Es un triangulo equilatero"
        else:
            if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                return "Es un triangulo isoceles"
            else:
                return "Es otro "


def main():
    lado1 = int(input("Dame el primer lado"))
    lado2 = int(input("Dame el segundo lado"))
    lado3 = int(input("Dame el tercer lado"))
    if lado1>lado2+lado3 or lado2>lado1+lado3 or lado3>lado1 + lado2:
        print("Estos lados no corresponden a un triangulo")
    else:
        r = esTrianguloRectangulo(lado1, lado2, lado3)
        print(r)


main()