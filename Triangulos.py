#Autor: Elizabeth Citlalli Zapata Cortes
# De acuerdo a la longitud de sus lados, el programa indica que tipo de triángulo es (rectángulo, isóseles, equilatero,
# o que sus medidas no corresponden a un triangulo).

import turtle


def indicarTipoTriangulo(a,b,c):
    if (a*a)+(b*b)==(c*c):
        return "Triángulo Rectángulo"
    elif (c*c)-(b*b)==(a*a):
        return "Triángulo Rectángulo"
    elif (c*c)-(a*a)== (b*b):
        return "Triángulo Rectángulo"
    elif a==b:
        return "Triángulo Isóseles"
    elif b==c :
        return "Triángulo Isóseles"
    elif c==a:
        return "Triángulo Isóseles"
    elif a==b and b==c:
        return "Triángulo Equilátero"
    return "Estos lados no corresponden a un triángulo"


#EXTRA
def dibujarTriangulo(a,b,c):
    if (a*a)+(b*b)==(c*c):
        turtle.forward(a)
        turtle.left(135)
        turtle.forward(c)
        turtle.left (135)
        turtle.forward(b)
        turtle.left(90)
    elif (c*c)-(b*b)==(a*a):
        turtle.forward(a)
        turtle.left(135)
        turtle.forward(c)
        turtle.left(135)
        turtle.forward(b)
        turtle.left(90)
    elif (c*c)-(a*a)== (b*b):
        turtle.forward(a)
        turtle.left(135)
        turtle.forward(c)
        turtle.left(135)
        turtle.forward(b)
        turtle.left(90)
    elif  a==b:
        turtle.forward(c)
        turtle.left(100)
        turtle.forward(b)
        turtle.left(160)
        turtle.forward(a)
        turtle.left(10)
    elif b==c :
        turtle.forward(a)
        turtle.left(100)
        turtle.forward(b)
        turtle.left(160)
        turtle.forward(c)
        turtle.left(10)
    elif c==a:
        turtle.forward(b)
        turtle.left(100)
        turtle.forward(a)
        turtle.left(160)
        turtle.forward(c)
        turtle.left(10)
    elif  a==b and b==c:
        turtle.forward(a)
        turtle.left(120)
        turtle.forward(b)
        turtle.left(120)
        turtle.forward(c)
        turtle.left(120)


def main():
    a = int(input("Teclea lado A: "))
    b = int(input("Teclea lado B: "))
    c = int(input("Teclea lado C: "))

    print(indicarTipoTriangulo(a,b,c))

    #EXTRA
    dibujarTriangulo(a,b,c)
    turtle.exitonclick()


main()