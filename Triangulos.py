# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Programa que te dice si tu triangulo es


#Función que clasifica los triangulos de acuerdo a sus lados
def clasificarTriangulo(lado1, lado2, lado3):
    if (lado1**2==lado2**2+lado3**2) or (lado2**2==lado1**2+lado3**2) or (lado3**2==lado1**2+lado3**2):
        triangulo = "rectangulo"
    elif lado1==lado2==lado3:
        triangulo = "equilatero"
    elif lado1==lado2 or lado2==lado3 or lado1==lado3:
        triangulo = "isosceles"
    elif lado1!=lado2!=lado3:
        triangulo = "otro (escaleno)"
    else:
        triangulo = "error"

    return triangulo


#funcion que pide los lados y que te dice si tu triangulo es o no real y los clasifica
def main():
    print("Se te dira que tipo de triangulo tienes")
    lado1= int(input("Introduce cuanto mide cualquier lado de tu triangulo: "))
    lado2 = int(input("Introduce otro lado de tu triangulo: "))
    lado3 = int(input("Introduce el ultimo lado de tu triangulo: "))

    triangulo= clasificarTriangulo(lado1,lado2,lado3)

    if triangulo=="error":
        print("Estos lados no corresponden a un triángulo.")
    else:
        print("Tu triangulo es",triangulo)


main()
