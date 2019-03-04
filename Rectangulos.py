# Autor: José Luis Macías Vázquez, A01655713, Grupo 03
#Es un programa que recibe la base y altura de dos rectangulos y regresa el area de cada uno. 


def calcularPerimetroU(bU,aU):
    perimetroU = (bU * 2 )+ (aU * 2)
    return perimetroU


def calcularPerimetroD(bD,aD):
    perimetroD = (bD * 2 )+ (aD * 2)
    return perimetroD


def calcularAreaU(bU,aU):
    areaU = bU * aU
    return areaU


def calcularAreaD(bD,aD):
    areaD = bD * aD
    return areaD




def compararCuadrados(bU,aU,bD,aD):
    areaD = bD * aD
    areaU = bU * aU
    if areaD > areaU:
        return "El segundo rectángulo es el más grande"
    else:
        if areaD < areaU:
            return "El primer rectángulo es el más grande"
        else:
            if areaD == areaD:
                return "Ambos rectángulos son iguales"





def main():

    bU = int(input("Escribe la base del primer rectángulo: "))
    aU = int(input("Escribe la altura del primer rectángulo: "))
    bD = int(input("Escribe la altura del segundo rectángulo: "))
    aD = int(input("Escribe la altura del segundo rectángulo: "))
    print("El perimetro del primer rectángulo es: ",calcularPerimetroU(bU,aU)," El perimetro del segundo rectangulo es: ", calcularPerimetroD(bD,aD), " El área del primer rectangulo es: ", calcularAreaU(bU,aD), " El área del segundo rectángulo es: ", calcularAreaD(bD,aD))
    print(compararCuadrados(bU,aU,bD,aD))


main()