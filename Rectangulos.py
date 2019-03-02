#Autor: Ivana Olvera Mérida
#Escribe un programa que lea las dimensiones (base y altura) de dos rectángulos y que calcule e imprima
#el perímetro y área de cada uno.

def calcularPerimetro (bR2, aR2):
    perimetroCalculado2 = 2*bR2 + 2*aR2
    return perimetroCalculado2

def calcularPerimetro (bR1, aR1):
    perimetroCalculado1 = 2*bR1 + 2*aR1
    return perimetroCalculado1

def calcularArea2 (bR2, aR2):
    areaCalculada2 = bR2*aR2
    return areaCalculada2

def calcularArea1 (bR1, aR1):
    areaCalculada1 = bR1*aR1
    return areaCalculada1


def determinarMayorMenorArea(area1, area2):
    if area1>area2:
        return ("El rectángulo 1 es mayor")
    elif area1<area2:
        return ("El rectángulo 2 es mayor")
    else:
        return ("Ambos rectángulos son iguales")


def main():
    #Variables funciones
    baseR1 = int(input ("Base de rectángulo 1: "))
    baseR2 = int(input ("Base de rectángulo 2: "))
    alturaR1 = int(input ("Altura de rectángulo 1: "))
    alturaR2 = int(input ("Altura de rectángulo 2: "))
    #Resultados funciones
    area1 = calcularArea1 (baseR1, alturaR1)
    area2 = calcularArea2 (baseR2, alturaR2)
    perimetro1 = calcularPerimetro (baseR1, alturaR1)
    perimetro2 = calcularPerimetro (baseR2, alturaR2)
    rectangulos = determinarMayorMenorArea (area1, area2)
    print(perimetro1)
    print(perimetro2)
    print(area1)
    print(area2)
    print(rectangulos)

main()