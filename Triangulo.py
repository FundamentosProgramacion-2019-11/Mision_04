# Paulina Guerrero Ruiz
# Definir triangulo

import turtle
def dibujarTrianguloEquilatero(lado1,lado2,lado3):          # Funcion para dibujar triangulo equilatero
    turtle.forward(lado1)
    turtle.left(120)
    turtle.forward(lado2)
    turtle.left(120)
    turtle.forward(lado3)
    turtle.left(120)


def dibujarTrianguloRectangulo(lado1,lado2,lado3):          #Funcion para dibujar triangulo rectangulo
    turtle.forward(lado1)
    turtle.left(90)
    turtle.forward(lado2)
    turtle.left(135)
    turtle.forward(lado3)
    turtle.left(135)


def dibujarTrianguloIsosceles(lado1,lado2,lado3):           #Funcion para dibujar triangulo Iscoceles
    turtle.forward(lado1)
    turtle.left(125)
    turtle.forward(lado2)
    turtle.left(125)
    turtle.forward(lado3)
    turtle.left(130)


def definirTriangulo (lado1,lado2,lado3):                       # Funcion que definirá que tipo de triangulo es
    if lado1==lado2==lado3:
        triangulo = "Triangulo equilatero"
        equilatero = dibujarTrianguloEquilatero(lado1,lado2,lado3)
    elif lado1==lado2 and lado1!=lado3:
        triangulo = "Triangulo isosceles"
        isosceles = dibujarTrianguloIsosceles(lado1, lado2, lado3)
    elif lado1==lado3 and lado1!=lado2:
        triangulo ="Triangulo isosceles"
        isosceles = dibujarTrianguloIsosceles(lado1, lado2, lado3)
    elif lado3==lado2 and lado3!=lado1:
        triangulo ="Triangulo isosceles"
        isosceles = dibujarTrianguloIsosceles(lado1, lado2, lado3)
    elif lado1!=lado2 !=lado3:
        triangulo= "Triangulo rectangulo"
        rectangulo = dibujarTrianguloRectangulo(lado1, lado2, lado3)

    return triangulo


def main():
    lado1 = int(input("Teclea el lado 1: "))
    lado2 = int(input("Teclea el lado 2: "))
    lado3 = int(input("Teclea el lado 3: "))
    triangulos= definirTriangulo(lado1,lado2,lado3)
    print("Tu triangulo es un: ", triangulos)

    turtle.exitonclick()


main()