#Autor: María Fernanda García Gastélum A01376181
#Determinar si 3 lados dados forman un triángulo, si si, clasificar el tipo de triángulo


#importar Tortuga y Math
import turtle
import math


#definir si los lados forman un triángulo
def esTriangulo(lado1, lado2, lado3):
    if not lado1+lado2 >= lado3 and lado2+lado3 >= lado1 and lado3 + lado1 >= lado2:
        return False
    else:
        return True


#EXTRA: para poder dibujar cualquier triángulo, hay que calcular los ángulos
def calcularAngulos(lado1, lado2, lado3):
    anguloLado2Rad= math.acos(((lado1**2)+(lado2**2)-(lado3**2))/(2*(lado1)*(lado2)))
    anguloLado3Rad= math.pi-math.asin((lado2/lado3)* math.sin(anguloLado2Rad))
    anguloLado2=(180/math.pi)*anguloLado2Rad
    anguloLado3= (180 / math.pi) * anguloLado3Rad
    return anguloLado2, anguloLado3


#EXTRA: dibujar cualquier triángulo
def dibujarTriangulo(lado1, lado2, lado3, anguloLado2, anguloLado3):
    turtle.forward(lado1)
    turtle.left(anguloLado3)
    turtle.forward(lado3)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.right(anguloLado3)
    turtle.left(anguloLado2)
    turtle.pendown()
    turtle.forward(lado2)
    turtle.hideturtle()


#determinar el tipo de triángulo que forman los lados
def determinarTipoDeTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2==lado3:
        return "Es un triángulo equilátero"
    elif (lado1 == lado2 and lado3 != lado2) or (lado2==lado3 and lado1 !=lado3) or (lado1==lado3 and lado2 != lado3):
        return "Es un triángulo isóceles"
    elif (lado1**2)+(lado2**2)== (lado3**2) or (lado1**2)+(lado3**2)== (lado2**2) or (lado2**2)+(lado3**2)== (lado1**2):
        return "Es un triángulo rectángulo"
    else:
        return "Otro"


def main():
    lado1 = int(input("Escribe el lado 1: "))
    lado2 = int(input("Escribe el lado 2: "))
    lado3 = int(input("Escribe el lado 3: "))
    if not esTriangulo(lado1, lado2, lado3):
        print("Estos lados no corresponden a un triángulo")
    else:
        print(determinarTipoDeTriangulo(lado1, lado2, lado3))
        anguloLado1,anguloLado2 =calcularAngulos(lado1, lado2, lado3)
        dibujarTriangulo(lado1, lado2, lado3, anguloLado1,anguloLado2)
        turtle.exitonclick()


main()