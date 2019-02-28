# Autor: Paulina Guerrero Ruiz
# Descripcion: Leer la base y la altura de dos rectangulos y calcular su area y su perimetro


import turtle
def dibujarRectanguloGrande(base,altura):                # Dibujar Rectangulo grande
    turtle.color("red")
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)


def dibujarRectanguloChico(base,altura):                  # Dibujar rectangulo chico
    turtle.color("green")
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)


def calcularArea (base1,altura1):                                # Funcion para calcular area
    A1 = (altura1*base1)
    return A1


def calcularPerimetro (base1,altura1):                           # Funcion para calcular perimetro
    P1 = 2 * (altura1+base1)
    return P1


def main():                                                     # Funcion que pide datos e imprime resultado
    base1 = int(input("Teclea la base del rectangulo 1: "))
    altura1 = int(input("Teclea la altura del rectangulo 1: "))
    base2 = int(input("Teclea la base del rectangulo 2: "))
    altura2 = int(input("Teclea la altura del rectangulo 2: "))
    Area1 = calcularArea(base1,altura1)
    Perimetro1 = calcularPerimetro(base1,altura1)
    Area2 = calcularArea(base2,altura2)
    Perimetro2 = calcularPerimetro(base2,altura2)
    print("El area del rectangulo 1 es: ", Area1, "cm",
          "El area del rectangulo 2 es:", Area2, "cm",
          "El perimetro del rectangulo 1 es: ", Perimetro1, "cm",
          "El perimetro del rectangulo 2 es: ", Perimetro2, "cm")
    if Area1>Area2:
        print("El rectangulo con mayor area es Area 1")
        dibujarRectanguloGrande(base1,altura1)
        dibujarRectanguloChico(base2,altura2)
    elif Area1<Area2:
        print("El rectangulo con mayor area es Area 2")
        dibujarRectanguloGrande(base2,altura2)
        dibujarRectanguloChico(base1,altura1)
    else:
        print("Las areas son iguales")

    turtle.exitonclick()


main()
