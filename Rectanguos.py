# Autor: Roberto Emmanuel González Muñoz
# Programa que le las dimensiones (base y altura) de dos rectángulos
# y calcula e imprime el perímetro y área de cada uno.


def calcularArea(b, a):
    area = b * a
    return area


def calcularPerimetro(b, a):
    perimetro = 2*b + 2*a
    return perimetro


def main():
    # Leer Dimensiones del rectángulo 1.
    base1 = int(input("Teclea la medida de la base 1: "))
    altura1 = int(input("Teclea la medida de la altura 1: "))

    # Leer dimensiones del rectángulo 2.
    base2 = int(input("Teclea la medida de la base 2: "))
    altura2 = int(input("Teclea la medida de la altura 2: "))

    # Calcula el área 1.
    area1 = calcularArea(base1, altura1)
    # Calcula el perímeto 1.
    perimetro1 = calcularPerimetro(base1, altura1)
    # Calcula el área 2.
    area2 = calcularArea(base2, altura2)
    # Calcula el área 2.
    perimetro2 = calcularPerimetro(base2, altura2)

    print("---------------------------------------------------")
    print("El área del rectángulo 1 es: %.d" % area1)
    print("El perímetro del rectángulo 1 es: %.d" % perimetro1)
    print("---------------------------------------------------")
    print("El área del rectángulo 2 es: %.d" % area2)
    print("El perímetro del rectángulo 2 es: %.d" % perimetro2)
    print("---------------------------------------------------")

    if area1 > area2:
        print("EL área del rectángulo 1 es mayor.")

    elif area1 == area2:
        print("El área del rectángulo 1 y 2 son iguales.")

    else:
        print("El área del rectángulo 2 es mayor.")


main()