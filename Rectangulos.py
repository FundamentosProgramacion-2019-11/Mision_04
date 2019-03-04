#Autor: Katia Hernández Barrera
#Programa que calcula área y perímetro de dos rectángulos
import turtle


def calcularArea1 (baseA,alturaA): #función que calcula el área del primer rectángulo
    a1 = baseA * alturaA
    return a1


def calcularPerimetro1(baseA,alturaA):  #función que cxalcula el perímetro del primer rectángulo
    p1 = (2*baseA) * (2*alturaA)
    return p1


def calcularArea2 (baseB,alturaB):  #función que calcula el área del segundo rectángulo
    a2 = baseB * alturaB
    return a2


def calcularPerimetro2 (baseB, alturaB): #función que calcula el perímetro del segundo rectángulo
    p2 = (2*baseB) * (2*alturaB)
    return p2


def identificarMayor (baseA,alturaA,baseB,alturaB):  #función que identifica cuál de los os rectángulos es mayor
    if calcularArea1(baseA,alturaA)> calcularArea2(baseB,alturaB):
        return "Es mayor el primer rectángulo"
    elif calcularArea1(baseA,alturaA) == calcularArea2(baseB,alturaB):
        return "Son iguales"
    else:
        return "Es mayor el segundo rectángulo"


#Extra
def dibujarRectangulos(baseA,alturaA, baseB, alturaB):
    if (baseA*alturaA > baseB*alturaB):
        turtle.color("green")
        turtle.forward(baseA)
        turtle.left(90)
        turtle.forward(alturaA)
        turtle.left(90)
        turtle.left(baseA)
        turtle.left(90)
        turtle.forward(alturaA)
        turtle.left(90)

        turtle.color("red")
        turtle.forward(baseB)
        turtle.left(90)
        turtle.forward(alturaB)
        turtle.left(90)
        turtle.left(baseB)
        turtle.left(90)
        turtle.forward(alturaB)
        turtle.left(90)

    else:
        turtle.color("red")
        turtle.forward(baseA)
        turtle.left(90)
        turtle.forward(alturaA)
        turtle.left(90)
        turtle.left(baseA)
        turtle.left(90)
        turtle.forward(alturaA)
        turtle.left(90)

        turtle.color("green")
        turtle.forward(baseB)
        turtle.left(90)
        turtle.forward(alturaB)
        turtle.left(90)
        turtle.left(baseB)
        turtle.left(90)
        turtle.forward(alturaB)
        turtle.left(90)

        turtle.exitonclick()




def main():
    baseA = int(input("Teclea la base del primer rectángulo:"))
    alturaA = int(input("Teclea la altura del primer triangulo"))
    print("                                          ")
    baseB = int(input("Teclea la base del segundo rectangulo"))
    alturaB = int(input("Teclea la altura del segundo triangulo"))
    print("-------------------------------------------------")
    area1 = calcularArea1(baseA,alturaA)
    print("El área del primer rectángulo es:", area1)
    peri1 = calcularPerimetro1(baseA,alturaA)
    print("El perímetro del primer rectángulo es:",peri1)
    area2 = calcularArea2(baseB,alturaB)
    print("El área del segundo rectángulo es:", area2)
    peri2 = calcularPerimetro2(baseB,alturaB)
    print("El perímetro del segundo rectángulo es:", peri2)
    m = identificarMayor(baseA,alturaA,baseB,alturaB)
    print("                                           ")
    print(m)
    dibujarRectangulos(baseA, alturaA, baseB, alturaB)



main()