# Autor: Rosalía Serrano Herrera
# Calcula el área y perímetro de dos rectángulos


def calcularArea(base, altura): #calcula el area del rectángulo
    area = base * altura
    return area


def calcularPerimetro(base, altura):    #calcula el perímetro del rectángulo
    perimetro = (base * 2) + (altura * 2)
    return perimetro


def main():
    base = int(input("Teclea la base del primer rectángulo: "))
    altura = int(input("Teclea la altura del primer rectángulo: "))
    area1 = calcularArea(base, altura)
    perimetro1 = calcularPerimetro(base, altura)
    base = int(input("Teclea la base del segundo rectángulo: "))
    altura = int(input("Teclea la altura del segundo rectángulo: "))
    area2 = calcularArea(base, altura)
    perimetro2 = calcularPerimetro(base, altura)
    print("El área del primer rectángulo es:", area1, "y su perímetro es:", perimetro1)
    print("El área del segundo rectángulo es:", area2, "y su perímetro es:", perimetro2)
    if area1 == area2:
        print("Ambos rectángulos tienen la misma área.")
    elif area1 > area2:
        print("El primer rectángulo tiene mayor área.")
    else:
        print("El segundo rectángulo tiene mayor área.")


main()