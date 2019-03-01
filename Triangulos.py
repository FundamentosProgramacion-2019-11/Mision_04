# Autor: Itzel Yanabany Castro Becerril
# Saber que tipo de triangulo es el que se tiene
import turtle
import math



# La funcion calculara que tipo de rectangulo es
def calcularTipoDeTriangulo(a, b, c):
    if c * c == a * a + b * b or a * a == c * c +b * b or b * b == c * c + a * a:
        rectangulo = "Es un Triangulo RECTANGULO"
        return rectangulo
    else:
        if a == b and a != c or a == c and a != b or b == c and a != b:
            isoceles = "Es  un triangulo ISOCELES"
            return isoceles
        else:
            if a == b == c:
                equilatero = "Es un triangulo EQUILATERO"
                return equilatero
            else:
                if a != b and b != c and c != a:
                    escaleno = "Es un  triangulo ESCALENO"
                    return escaleno
                else:
                    print("Estos lados no corresponden a un triangulo")


# La funcion imprimira que tipo de rectangulo es
def imprimirTriangulo(a, b, c):
    triangulo = calcularTipoDeTriangulo(a, b, c)
    print(triangulo)


# La funcion dibujara el rectangulo con las medidas introducidas
def dibujarTriangulo(a, b, c):
    angulo = math.atan(a / b)
    angulo1 = math.degrees(angulo)
    if c * c == a * a + b * b:
        turtle.forward(b)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.left(angulo1)
        turtle.forward(c)
    else:
        if a * a == c * c + b * b and a > b > c:
            angulo = math.atan(c /b )
            angulo1 = math.degrees(angulo)

            turtle.forward(b)
            turtle.left(90)
            turtle.forward(c)
            turtle.left(90)
            turtle.left(angulo1)
            turtle.forward(a)

        else:
            if a == b and a > c:
                an1 = math.acos((c / 2) / b)
                angulo1 = math.degrees(an1)
                angulo3 = (180 - 90 - angulo1) * 2
                turtle.forward(c / 2)
                turtle.left(180 - angulo1)
                turtle.forward(b)
                turtle.left(180 - angulo3)
                turtle.forward(a)
                turtle.left(180 - angulo1)
                turtle.forward(c / 2)
            else:
                if b == c and c > a:
                    an1 = math.acos((a / 2) / b)
                    angulo1 = math.degrees(an1)
                    angulo3 = (180 - 90 - angulo1) * 2
                    turtle.forward(a / 2)
                    turtle.left(180 - angulo1)
                    turtle.forward(b)
                    turtle.left(180 - angulo3)
                    turtle.forward(c)
                    turtle.left(180 - angulo1)
                    turtle.forward(a / 2)
                else:
                    if a == c and a > b:
                        an1 = math.acos((b / 2) / c)
                        angulo1 = math.degrees(an1)
                        angulo3 = (180 - 90 - angulo1) * 2
                        turtle.forward(b / 2)
                        turtle.left(180 - angulo1)
                        turtle.forward(c)
                        turtle.left(180 - angulo3)
                        turtle.forward(a)
                        turtle.left(180 - angulo1)
                        turtle.forward(b / 2)
                    else:
                        if a == b == c:
                            turtle.forward(a)
                            turtle.left(120)
                            turtle.forward(b)
                            turtle.left(120)
                            turtle.forward(c)



def main():
    a = int(input("Teclea el numero del primer lado: "))
    b = int(input("Teclea el numero del segungo lado: "))
    c = int(input("Teclea el numero del tercer lado: "))
    imprimirTriangulo(a, b, c)
    dibujarTriangulo(a, b, c)
    turtle.exitonclick()

main()

