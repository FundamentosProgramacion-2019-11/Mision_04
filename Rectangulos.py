#Autor: Karla Ximena Rueda Ruiz
#Aplicar la técnica Top-Down para calcular área y perímetro de un rectángulo estableciendo condiciones.
def main():
    base1 = int(input("Inserte valor de la base1 : "))
    altura1 = int(input("Inserte valor de la altura1 : "))
    base2 = int(input("Inserte valor de la base2 : "))
    altura2 = int(input("Inserte valor de la altura2 : "))

    area1=calcularArea(base1,altura1)
    print("El área de primer rectángulo es =",area1)

    perimetro1=calcularPerimetro(base1,altura1)
    print("El perímetro del primer rectángulo es =",perimetro1)

    area2 = calcularArea(base2, altura2)
    print("El área del segundo rectángulo es=", area2)

    perimetro2 = calcularPerimetro(base2, altura2)
    print("El perímetro del segundo rectángulo es =", perimetro2)

    compararRectangulos(area1, area2)

def calcularArea(base,altura):
    area=base*altura
    return area

def calcularPerimetro(base,altura):
    perimetro=base+base+altura+altura
    return perimetro

def compararRectangulos(area1,area2):
    if area1>area2:
        print("El primer rectángulo es más grande")

    elif area2>area1:
        print("El segundo rectángulo es más grande")

    else:
        print("Las áreas son iguales")

main()
