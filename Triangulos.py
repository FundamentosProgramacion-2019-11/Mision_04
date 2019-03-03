# Autor: Guillermo De Anda Casas , A01375892
# Código que comprueba que tres medidas correspondan a los lados de un tríangulo, informa qué triéngulo es.

import turtle
import math


# Función que define si es las medidas pueden generar un triángulo.
def esTriangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


# Función que define qué tipo de triángulo es el que se forma.
def definirTriangulo(a, b, c):
    if esTriangulo(a, b, c) == True:
       if a == b == c:
           return "Triángulo equilátero"
       elif (a**2) + (b**2) - (c**2) == 0 or (b**2) + (c**2) - (a**2) == 0 or (c**2) + (a**2) - (b**2) == 0:
           return "Triángulo rectángulo"
       elif a == c != b or a == b != c or a == c != b:
           return "Triángulo isóceles"
       elif (a**2) + (b**2) - (c**2) < 0 or (b**2) + (c**2) - (a**2) < 0 or (c**2) + (a**2) - (b**2) < 0:
           return "Otro: Triángulo escaleno obtusángulo"
       elif (a**2) + (b**2) - (c**2) > 0 or (b**2) + (c**2) - (a**2) > 0 or (c**2) + (a**2) - (b**2) > 0:
           return "Otro: Triángulo escaleno acutángulo"
    else:
        return "Estos lados no corresponden a un triángulo."


# Función que traza el triángulo.
def trazarTriangulo(a, b, c):
    if esTriangulo(a, b, c) == True:
        alpha = (math.acos(((a ** 2) - (b ** 2) - (c ** 2)) / - (2 * b * c)) * 180/math.pi)
        beta = (math.acos(((b ** 2) - (a ** 2) - (c ** 2)) / - (2 * a * c)) * 180/math.pi)
        gamma = (math.acos(((c ** 2) - (b ** 2) - (a ** 2)) / - (2 * a * b)) * 180/math.pi)
        turtle.forward(a)
        turtle.left(180 - beta)
        turtle.forward(c)
        turtle.left(180 - alpha)
        turtle.forward(b)
        turtle.left(180 - gamma)
        turtle.hideturtle()
        return alpha, beta, gamma
    else:
        return "ERROR"


# Función main que lee las medidas y llama a las demás funciones.
def main():
    a = float(input("Teclea la primer medida: "))
    b = float(input("Teclea la segunda medida: "))
    c = float(input("Teclea la tercer medida: "))
    esTriangulo(a, b, c)
    print(definirTriangulo(a, b, c))
    print(trazarTriangulo(a, b, c))
    turtle.exitonclick()


main()