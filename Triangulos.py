#Autor: Mario Hernández Cárdenas
#Define si un triangulo es triángulo, isósceles, equilátero u otro o si no es triángulo

import turtle
import math

#Utiliza las medidas para saber que ley cumple y regresar el tipo de triángulo
def definirTriangulo(a, b, c):
    if a == b and b == c:
        return "equilátero"
    elif (a == b or b == c or a == c) and( a != b or b != c or a != c):
        return "isósceles"
    elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        return "rectángulo"
    else:
        return "otro diferente a equilátero, isósceles o rectángulo"

#EXTRA
#Obtiene el cateto opuesto para el triángulo rectángulo, o el lado diferente en un isósceles
def obtenerOpuesto(triangulo, a, b, c):
    if triangulo == "isósceles":
        if a != b and a != c:
            return a
        elif b != a and b != c:
            return b
        else:
            return c
    if triangulo == "rectángulo":
        if a < b and a < c:
            return a
        elif b < a and b < c:
            return b
        else:
            return c
    else:
        return a    #Regresa a porque al dibujar necesita un lado para calcular aunque no se utilice la función


#Obtiene el cateto opuesto para el triángulo rectángulo, o el lado diferente en un isósceles
def obtenerAdyacente(triangulo, a, b, c, opuesto, hipotenusa):
    if triangulo == "rectángulo":
        if a > opuesto and a < hipotenusa:
            return a
        elif b > opuesto and b < hipotenusa:
            return b
        else:
            return c
    else:
        if a != b and a != c:
            return a
        if b != a and b != c:
            return b
        else:
            return c


#Obtiene la hipotenusa para un triángulo rectángulo, o regresa un lado para un triángulo equilatero
def obtenerHipotenusa(triangulo, a, b, c):
    if triangulo == "rectángulo":
        if a > b and a > c:
            return a
        if b > a and b > c:
            return b
        else:
            return c
    else:
        return a    #Regresa a porque al dibujar necesita un lado para calcular aunque no se utilice la función, o para poder dibujar un triangulo equilátero.


#Obtiene los lados iguales en un rectángulo isósceles
def obtenerLadoIgual(triangulo, a, b, c):
    if triangulo == "isósceles":
        if a == b:
            return a
        if b == c:
            return b
        else:
            return c


#Obtiene el ángulo para dibujar un triángulo rectángulo o isósceles
def calcularAnguloExtra(triangulo, opuesto, hipotenusa, ladoIgual):
    if triangulo == "isósceles":
        anguloTrianguloRectangulo = math.asin((opuesto/2) / ladoIgual) * (180 / math.pi)
        return anguloTrianguloRectangulo
    else:
        anguloTrianguloRectangulo = math.asin((opuesto) / hipotenusa) * (180 / math.pi)
        return anguloTrianguloRectangulo


#Dibuja el triángulo dependiendo su tipo
def dibujarTriangulo(triangulo, opuesto, hipotenusa, anguloExtra, adyacente, ladoIgual):
    if triangulo == "isósceles":
        anguloSuperior = anguloExtra * 2
        anguloIgual = ((90 - anguloExtra))
        turtle.forward(opuesto)
        turtle.left(180-anguloIgual)
        turtle.forward(ladoIgual)
        turtle.left(180-anguloSuperior)
        turtle.forward(ladoIgual)
        turtle.exitonclick()
    if triangulo == "equilátero":
        turtle.forward(hipotenusa)
        turtle.left(120)
        turtle.forward(hipotenusa)
        turtle.left(120)
        turtle.forward(hipotenusa)
        turtle.exitonclick()
    if triangulo == "rectángulo":
        anguloIgual = ((90 - anguloExtra))
        turtle.forward(opuesto)
        turtle.left(180 - anguloIgual)
        turtle.forward(hipotenusa)
        turtle.left(180 - anguloExtra)
        turtle.forward(adyacente)
        turtle.exitonclick()
    else:
        return "Este triángulo no se puede dibujar por falta de información"


def main():
    lado1 = int(input("Introduce el primer lado del triángulo: "))
    lado2 = int(input("Introduce el segundo lado del triángulo: "))
    lado3 = int(input("Introduce el tercer lado del triángulo: "))
    if lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado1 + lado3 <= lado2:
        print("\nLos lados no corresponden a un triángulo")
    else:
        triangulo = definirTriangulo(lado1, lado2, lado3)
        print("\nEl triángulo es",triangulo)
        catetoOpuesto = obtenerOpuesto(triangulo, lado1, lado2, lado3)
        ladosIguales = obtenerLadoIgual(triangulo, lado1, lado2, lado3)
        hipotenusa = obtenerHipotenusa(triangulo, lado1, lado2, lado3)
        catetoAdyacente = obtenerAdyacente(triangulo, lado1, lado2, lado3, catetoOpuesto, hipotenusa)
        anguloExtra = calcularAnguloExtra(triangulo, catetoOpuesto, hipotenusa, ladosIguales)
        dibujarTriangulo(triangulo, catetoOpuesto, hipotenusa, anguloExtra, catetoAdyacente, ladosIguales)


main()