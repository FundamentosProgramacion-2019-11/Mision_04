#Luis Fernando Duran Castillo
#Hacer un programa que sepa que triangulos estas ingresando.


def analizarTriangulo(lado1, lado2, lado3):
    if lado1==lado2==lado3:
        triangulo = "Equilatero"
    elif (lado1**2==lado2**2+lado3**2) or (lado2**2==lado1**2+lado3**2) or (lado3**2==lado1**2+lado2**2):
        triangulo = "Rectángulo"
    elif lado1!= lado2 != lado3:
        triangulo = "Escaleno"
    elif lado1==lado2 or lado2==lado3 or lado1==lado3:
        triangulo = "Isósceles"
    else:
        triangulo = "Error"
    return triangulo


def ReconocerTriangulo(triangulo):
    if triangulo == "Error":
        print("Los datos no reconocen ningun triangulo.")
    else:
        print("El triangulo es un:", triangulo)


def main():
    lado1 = int(input("Escribe el primer lado del triángulo: "))
    lado2 = int(input("Escribe el segundo lado del triángulo: "))
    lado3 = int(input("Escribe el tercer lado del triángulo: "))
    triangulo = analizarTriangulo(lado1, lado2, lado3)
    ReconocerTriangulo(triangulo)


main()