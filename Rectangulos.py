# Autor: Ronaldo Estefano Lira Buendia
# Calcular el area y el perimetro de dos rectangulos con la base y la alturo de los valores dados por el usuario, indicar cual rectangulo es mayor o si son iguales y dibujarlos.

import turtle


def calcularAreaPrimerRectangulo(b1, h1):
    area = b1 * h1
    return area


def calcularAreaSegundoRectangulo(b2, h2):
    area = b2 * h2
    return area


def calcularPerimetroPrimerRectangulo(b1, h1):
    perimetro = (b1*2) + (h1*2)
    return perimetro


def calcularPerimetroSegundoRectangulo(b2, h2):
    perimetro = (b2*2) + (h2*2)
    return perimetro


def main():
    b1 = int(input("Ingrese la base del primer rectangulo: "))
    h1 = int(input("Ingrese la altura del primer rectangulo: "))
    b2 = int(input("Ingrese la base del segundo rectangulo: "))
    h2 = int(input("Ingrese la altura del segundo rectangulo: "))
    area1 = calcularAreaPrimerRectangulo(b1, h1)
    area2 = calcularAreaSegundoRectangulo(b2, h2)
    perimetro1 = calcularPerimetroPrimerRectangulo(b1, h1)
    perimetro2 = calcularPerimetroSegundoRectangulo(b2, h2)
    print("El area del primer rectangulo es: ",area1)
    print("El area del segundo rectangulo es: ",area2)
    print("El perimetro del primer rectangulo es: ",perimetro1)
    print("El perimetro del segundo rectangulo es: ",perimetro2)
    if area1==area2:
        print("El area de los rectangulos son iguales.")
        turtle.fd(b1)
        turtle.left(90)
        turtle.fd(h1)
        turtle.left(90)
        turtle.fd(b1)
        turtle.left(90)
        turtle.fd(h1)
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.fd(b1 + 10)
        turtle.pendown()
        turtle.fd(b2)
        turtle.left(90)
        turtle.fd(h2)
        turtle.left(90)
        turtle.fd(b2)
        turtle.left(90)
        turtle.fd(h2)
        turtle.left(90)

        turtle.done()

    elif area1>area2:
        print("El area del primer rectangulo es mayor que la area del segundo rectangulo.")
        turtle.fillcolor("Red")
        turtle.begin_fill()
        turtle.fd(b1)
        turtle.left(90)
        turtle.fd(h1)
        turtle.left(90)
        turtle.fd(b1)
        turtle.left(90)
        turtle.fd(h1)
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.fd(b1 + 10)
        turtle.pendown()
        turtle.fillcolor("Green")
        turtle.begin_fill()
        turtle.fd(b2)
        turtle.left(90)
        turtle.fd(h2)
        turtle.left(90)
        turtle.fd(b2)
        turtle.left(90)
        turtle.fd(h2)
        turtle.left(90)
        turtle.end_fill()


        turtle.done()
    else:
        print("El area del segundo rectangulo es mayor que la area del primer rectangulo.")
        turtle.fillcolor("Green")
        turtle.begin_fill()
        turtle.fd(b1)
        turtle.left(90)
        turtle.fd(h1)
        turtle.left(90)
        turtle.fd(b1)
        turtle.left(90)
        turtle.fd(h1)
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.fd(b1 + 10)
        turtle.pendown()
        turtle.fillcolor("Red")
        turtle.begin_fill()
        turtle.fd(b2)
        turtle.left(90)
        turtle.fd(h2)
        turtle.left(90)
        turtle.fd(b2)
        turtle.left(90)
        turtle.fd(h2)
        turtle.left(90)
        turtle.end_fill()

        turtle.done()


main()