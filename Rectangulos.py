#Autor: Yasmín Landaverde Nava
#Descripción: Compara de dos rectángulos

import turtle

def calcularPerimetro(base, altura):
    perimetro = (base*2)+(altura*2)
    return perimetro

def calcularArea(base, altura):
    area = base*altura
    return area

def esMayor(area1, area2):
    if area1>area2:
        return ("El primero")
    if area1==area2:
        return ("Son iguales")
    else:
        return ("El segundo")

def dibujarRectangulo1(a1, b1, a2, b2):
    turtle.color("turquoise")
    turtle.left(90)
    turtle.forward(a1)
    turtle.left(90)
    turtle.forward(b1)
    turtle.left(90)
    turtle.forward(a1)
    turtle.left(90)
    turtle.forward(b1)
    turtle.color("black")
    turtle.goto(300,0)
    turtle.color("green")
    turtle.left(90)
    turtle.forward(a2)
    turtle.left(90)
    turtle.forward(b2)
    turtle.left(90)
    turtle.forward(a2)
    turtle.left(90)
    turtle.forward(b2)


def main():
    a1 = int(input("Teclea la primera altura: "))
    b1 = int(input("Teclea la primera  base:"))
    a2 = int(input("Teclea la segunda altura: "))
    b2 = int(input("Teclea la segunda base:"))
    per = calcularPerimetro(a1,b1)
    area1 = calcularArea(a1,b1)
    print ("El primer triángulo tiene un perímetro de: ", per, "y un área de: ", area1 )
    calcularPerimetro(a2, b2)
    calcularArea(a2, b2)
    per2 = calcularPerimetro(a2, b2)
    area2 = calcularArea(a2, b2)
    print ("El primer triángulo tiene un perímetro de: ", per2, "y un área de: ", area2)
    esMayor(area1, area2)
    print ("El tríangulo de mayor area es:", esMayor(area1,area2))
    dibujarRectangulo1(a1, b1, a2, b2)


    turtle.exitonclick()

main()