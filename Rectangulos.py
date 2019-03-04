#Alan Giovanni Rodriguez Camacho A01748185
#Lee las dimensiones y calcula alcula el area y el perimetro de 2 rectangulos.


def calcularAreaRectanguloA(baseA,alturaA): #Calcula el area del rectangulo
    areaA = baseA*alturaA
    return areaA


def calcularPerimetroRectanguloA(baseA, alturaA): #Calcula el perimetro del rectangulo
    perimetroA = (baseA*2)+(alturaA*2)
    return perimetroA


def calcularAreaRectanguloB(baseB, alturaB): #Calcula el area del rectangulo 2
    areaB = baseB * alturaB
    return areaB


def calcularPerimetroRectanguloB(baseB, alturaB): #Calcula el perimetro del rectangulo 2
    perimetroB = (baseB * 2) + (alturaB * 2)
    return perimetroB


def main():
    baseA=int(input("Indica el valor de la base de tu rectangulo A: "))
    alturaA=int(input("Indica el valor de la altura de tu rectangulo A: "))
    baseB=int(input("Indica el valor de la base de tu rectangulo B: "))
    alturaB=int(input("Indica el valor de la altura de tu rectangulo B: "))
    areaA=calcularAreaRectanguloA(baseA,alturaA)
    areaB=calcularAreaRectanguloB(baseB,alturaB)
    perimetroA=calcularPerimetroRectanguloA(baseA,alturaA)
    perimetroB=calcularPerimetroRectanguloB(baseB,alturaB)
    print("El area y el perimetro de tu rectangulo A es:\nArea = {0}cm2\nPerimetro = {1}cm".format(areaA,perimetroA))
    print("El area y el perimetro de tu rectangulo B es:\nArea = {0}cm2\nPerimetro = {1}cm".format(areaB, perimetroB))
    if areaA>areaB:
        print("El rectangulo A tiene mayor area que el B.")
    elif areaA==areaB:
        print("El area de tus rectangulos es igual.")
    else:
        print("El rectangulo B tiene mayor area que el A.")


main()