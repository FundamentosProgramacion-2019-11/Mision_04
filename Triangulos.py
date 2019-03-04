#Roberto Castro Barrios A01748559
#Descripción: Programa que determina el tipo de triangulo de acuerdo a las medidas que des.


def calcularTriangulo (l1, l2, l3):
    if l1==l2 and l1==l3 and l2==l3:
        if (l1+l2)>l3 and (l1+l3)>l2 and (l2+l3)>l1:
            return "Es un triangulo Equilatero"
        else:
            return "Este triangulo no existe"
    elif (l1==l2 or l1==l3 or l2==l3) and (l2!=l3 or l1!=l3 or l2!=l1):
        if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
            return "Es un triangulo Isosceles"
        else:
            return "Este triangulo no existe"
    elif l1!=l2 and l1!=l3 and l2!=l3:
        if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
            return "Es un triangulo Escaleno"
        else:
            return "Este triangulo no existe"
    else:
        return "Es otro triangulo"


def main ():
    l1 = int(input("¿Cuanto mide el lado 1 de tu triangulo? "))
    l2 = int(input("¿Cuanto mide el lado 2 de tu triangulo? "))
    l3 = int(input("¿Cuanto mide el lado 3 de tu triangulo? "))
    tipo = calcularTriangulo(l1, l2, l3)
    print(tipo)

main ()