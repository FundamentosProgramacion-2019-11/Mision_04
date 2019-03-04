#Roberto Castro Barrios A01748559
# Programa que calcula el area y perimetro de dos rectangulos y determina cual tiene mayor area.


def esMayor (area1, area2):
    if area1>area2:
        return "Tu primer rectangulo tiene mayor area"
    elif area1==area2:
        return "Las areas son iguales"
    else:
        return "Tu segundo rectangulo tiene mayor area"


def calcularPerimetro (a, b):
    perimetroRectangulo = (2*a) + (2*b)
    return perimetroRectangulo


def calcularArea(a, b):
    areaRectangulo = a * b
    return areaRectangulo


def main():
    largo1 = int(input("Ingresa el largo de tu primer rectangulo: "))
    ancho1 = int(input("Ingresa el ancho de tu primer rectangulo: "))
    largo2 = int(input("Ingresa el largo de tu segundo rectangulo: "))
    ancho2 = int(input("Ingresa el ancho de tu segundo rectangulo: "))
    area1 = calcularArea(largo1, ancho1)
    area2 = calcularArea(largo2, ancho2)
    perimetro1 = calcularPerimetro(largo1, ancho1)
    perimetro2 = calcularPerimetro(largo2, ancho2)
    mayor = esMayor(area1, area2)
    print("El area de tu primer rectangulo es: %.2f" %(area1))
    print("El area de tu segundo rectangulo es: %.2f" %(area2))
    print("El perimetro de tu primer rectangulo es: %.2f" %(perimetro1))
    print("El perimetro de tu segundo rectangulo es: %.2f" %(perimetro2))
    print(mayor)


main()
