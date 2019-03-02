#Autor: Ivana Olvera Mérida
#Escribe un programa que lea el valor de cada uno de los lados de un triángulo


def calcularTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        return ("Triángulo equilátero")
    elif (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2) or (lado2 == lado3 and lado2 != lado1):
        return ("Triángulo isósceles")
    elif lado1 != lado2 and lado2 != lado3:
        return ("Triángulo rectángulo")
    else:
        return "Error"


def main():
    lado1 = int(input("Valor primer lado:"))
    lado2 = int(input("Valor segundo lado:"))
    lado3 = int(input("Valor tercer lado:"))
    triangulo = calcularTriangulo (lado1, lado2, lado3)
    print(triangulo)

main()