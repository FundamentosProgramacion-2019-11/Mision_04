#Autor: Cesar Guzman Guadarrama
#Este programa te dice el tipo de triangulo que podria coincidir con los lados dadodos

import turtle
import math


def saberQueTipoDeTrianguloEs(lado1,lado2,lado3):
    if lado1 == lado2 and lado1 == lado3:
        trianguloEquilatero = ("Es un triangulo equilatero")
        turtle.fd(lado1)
        turtle.left(120)
        turtle.fd(lado1)
        turtle.left(120)
        turtle.fd(lado1)
        turtle.exitonclick()
        return trianguloEquilatero
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        isoceles = "Es un triangulo Isoceles"
        if lado1 == lado2:
            turtle.fd(lado3)
            b = lado3 / 2
            rad = (math.acos(b/lado1))
            angulo = math.degrees(rad)
            turtle.left(90)
            turtle.left(90-angulo)          #Arreglar los angulos de giro
            turtle.fd(lado2)
            turtle.left( 90 )
            angulof= 180 - (angulo * 2)
            turtle.left(angulof)
            turtle.fd(lado1)
            turtle.exitonclick()
        elif lado2 == lado3:
            turtle.fd( lado1 )
            b = lado1 / 2
            rad = (math.acos( b / lado2 ))
            angulo = math.degrees( rad )
            turtle.left( 90 )
            turtle.left( 90 - angulo )  # Arreglar los angulos de giro
            turtle.fd( lado2 )
            turtle.goto(0,0)

            turtle.exitonclick()
        else:
            turtle.fd( lado2 )
            b = lado2 / 2
            rad = (math.acos( b / lado1 ))
            angulo = math.degrees( rad )
            turtle.left( 90 )
            turtle.left(90- angulo )
            turtle.fd( lado1 )
            turtle.goto(0,0)
            turtle.exitonclick()

        return isoceles



    elif lado1 ** 2 == ((lado2) ** 2) + ((lado3) ** 2) or lado2 ** 2 == ((lado1) ** 2) + ((lado3) ** 2) or lado3 ** 2 == ((lado2) ** 2) + ((lado1) ** 2):
        trianguloRectangulo = ( "Es un triangulo rectangulo" )
        if lado1**2 == (lado2**2) + (lado3**2):
            turtle.fd(lado3)
            turtle.left(90)
            turtle.fd(lado2)
            b = math.asin((lado3) / (lado1))
            angulo = math.degrees(b)
            turtle.left(90)
            turtle.left(90-angulo)
            turtle.fd(lado1)
            turtle.exitonclick()
        elif lado2**2 == (lado1**2) + (lado3**2):
            turtle.fd( lado3 )
            turtle.left( 90 )
            turtle.fd( lado1 )
            b = math.asin( (lado3) / (lado1) )
            angulo = math.degrees(b)
            turtle.left( 90 )
            turtle.left(90-angulo)
            turtle.fd( lado2 )
            turtle.exitonclick()
        else:
            turtle.fd( lado2 )
            turtle.left( 90 )
            turtle.fd( lado1 )
            b = math.asin( (lado2) / (lado1) )
            angulo = math.degrees(b)
            turtle.left( 90 )
            turtle.left(90-angulo)
            turtle.fd( lado3 )
            turtle.exitonclick()
        return trianguloRectangulo

    elif (lado1 + lado2) > lado3 or (lado2 + lado3) > lado1 or (lado1 + lado3) > lado2:
        NO = ("No existe")
        return NO


    elif lado1 != lado2 and lado1 != lado3 and lado3 != lado2:
        Escaleno = ("Es un triangulo escaleno")
        return Escaleno


    else:
        otro = ("Otro")
        return otro

def main():
    lado1 = float(input("Dame el primer lado"))
    lado2 = float(input("Dame el segundo lado"))
    lado3 = float(input("Dame el tercer lado"))
    triangulo = saberQueTipoDeTrianguloEs(lado1,lado2,lado3)
    print("El tipo de triangulo es: ",triangulo)
main()
