# Luis Fernndo Duran Castillo
# Calcular el área y el perímetro de dos rectángulos y ver cual es mayor o si son iguales.


def calcularArea(base1, altura1, base2, altura2):
    area1 = base1 * altura1
    area2 = base2 * altura2
    return area1, area2


def calcularPerimetro(base1, altura1, base2, altura2):
    perimetro1 = (base1 * 2) + (altura1 * 2)
    perimetro2 = (base2 * 2) + (altura2 * 2)
    return perimetro1, perimetro2


def main():
    base1 = int(input("Escribe la base del rectángulo 1: "))
    altura1 = int(input("Escribe la altura del rectángulo 1: "))
    print()
    base2 = int(input("Escribe la base del rectángulo 2: "))
    altura2 = int(input("Escribe la altura del rectángulo 2: "))

    area1, area2 = calcularArea(base1, altura1, base2, altura2)
    perimetro1, perimetro2 = calcularPerimetro(base1, altura1, base2, altura2)
    print()
    print("El area del rectángulo 1 es de:", area1, )
    print("Mientras que su perímetro es de:", perimetro1)
    print()
    print("El area del rectángulo 2 es de:", area2, )
    print("Mientras que su perímetro es de:", perimetro2)
    print()

    if area1 > area2:
        print("El área del rectángulo 1 es mayor.")
    elif area2 > area1:
        print("El área del rectángulo 2 es mayor.")
    else:
        print("Los 2 rectangulos son iguales en área")



main()


