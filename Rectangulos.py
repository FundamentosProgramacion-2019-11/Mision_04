# Autor: Elizabeth Citlalli Zapata Cortes
# Lee las dimensiones de dos rectangulos e imprime el perimetro y el áre de cada uno.

import turtle

def calcularPerimetroA(baseA, alturaA):
    perimetroA = (2 * baseA) + (2 * alturaA)
    return perimetroA

def calcularPerimetroB(baseB, aluraB):
    perimetroB = (2 * baseB) + (2 * aluraB)
    return perimetroB

def calcularAreaA(baseA, alturaA):
    areaA = baseA * alturaA
    return areaA

def calcularAreaB (baseB, alturaB):
    areaB = baseB * alturaB
    return areaB

def indicarRectanguloAreaMayor(areaA, areaB):
    if areaA > areaB:
        return "El área del rectángulo A es mayor que el área del rectángulo B"
    else:
        if areaB > areaA:
            return "El área del rectángulo B es mayor que el área del rectángulo A"
        else:
            return "El área del rectángulo A es igual a el área del rectángulo B"

#EXTRA
def dibujarRectanguloAreaMayor(baseA, alturaA, baseB, alturaB):
    areaA = baseA * alturaA
    areaB = baseB * alturaB
    if areaA > areaB:
        turtle.color("red")
        turtle.forward(baseA)
        turtle.left(90)
        turtle.forward(alturaA)
        turtle.left(90)
        turtle.forward(baseA)
        turtle.left(90)
        turtle.forward(alturaA)
        turtle.left(90)
    else:
        if areaB > areaA:
            turtle.color("red")
            turtle.forward(baseB)
            turtle.left(90)
            turtle.forward(alturaB)
            turtle.left(90)
            turtle.forward(baseB)
            turtle.left(90)
            turtle.forward(alturaB)
            turtle.left(90)

def dibujarRectanguloAreaMenor(baseA, alturaA, baseB, alturaB):
    areaA = baseA * alturaA
    areaB = baseB * alturaB
    if areaA < areaB:
        turtle.color("green")
        turtle.forward(baseA)
        turtle.left(90)
        turtle.forward(alturaA)
        turtle.left(90)
        turtle.forward(baseA)
        turtle.left(90)
        turtle.forward(alturaA)
        turtle.left(90)
    else:
        if areaB < areaA:
            turtle.color("green")
            turtle.forward(baseB)
            turtle.left(90)
            turtle.forward(alturaB)
            turtle.left(90)
            turtle.forward(baseB)
            turtle.left(90)
            turtle.forward(alturaB)
            turtle.left(90)


def main():
    baseA = int(input("Teclea la base del rectángulo A: "))
    alturaA = int(input("Teclea la altura del rectángulo A:"))
    print()
    baseB = int(input("Teclea la base del rectángulo B: "))
    alturaB = int(input("Teclea la altura del rectángulo B:"))

    perimetroA = calcularPerimetroA(baseA,alturaA)
    perimetroB = calcularPerimetroB(baseB, alturaB)
    areaA = calcularAreaA(baseA,alturaA)
    areaB = calcularAreaB(baseB, alturaB)

    indicarRectanguloAreaMayor(areaA, areaB)

    print()
    print("Rectángulo A")
    print("Perímetro: ", perimetroA)
    print("Área: ", areaA)
    print()
    print("Rectángulo B")
    print("Perímetro: ", perimetroB)
    print("Área: ", areaB)
    print()
    print(indicarRectanguloAreaMayor(areaA,areaB))

    #EXTRA
    turtle.shape("turtle")
    dibujarRectanguloAreaMayor(baseA, alturaA, baseB, alturaB)
    dibujarRectanguloAreaMenor(baseA, alturaA, baseB, alturaB)
    turtle.exitonclick()

main()