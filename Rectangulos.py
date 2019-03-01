# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Programa que calcula e imprime el perímetro y el área de dos rectángulos.

import turtle


# Función que calcula el área del rectángulo.
def calcularArea(b, a):
    areaRectangulo = b * a
    return areaRectangulo


# Función que calcula el perímetro del rectángulo.
def calcularPerimetro(b, a):
    perimetroRectangulo = 2 * b + 2 * a
    return perimetroRectangulo


# Función que dibuja los rectángulos.
def dibujarRectangulo(b, a, b2, a2):
    turtle.color("red")
    turtle.forward(b)
    turtle.left(90)  # GRADOS
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.color("green")
    turtle.forward(b2)
    turtle.left(90)  # GRADOS
    turtle.forward(a2)
    turtle.left(90)
    turtle.forward(b2)
    turtle.left(90)
    turtle.forward(a2)
    turtle.left(90)


# Función principal.
def main():
    base1 = int(input("Teclea la base del primer rectángulo: "))
    altura1 = int(input("Teclea la altura del primer rectángulo: "))
    base2 = int(input("Teclea la base del segundo rectángulo: "))
    altura2 = int(input("Teclea la altura del segundo rectángulo: "))
    area1 = calcularArea(base1, altura1)
    area2 = calcularArea(base2, altura2)
    perimetro1 = calcularPerimetro(base1, altura1)
    perimetro2 = calcularPerimetro(base2, altura2)
    print("El área del primer rectángulo es: ", area1)
    print("El área del segundo rectángulo es: ", area2)
    print("El perímetro del primer rectángulo es: ", perimetro1)
    print("El perímetro del segundo rectángulo es: ", perimetro2)

    if area1 > area2:
        print("El área del primer rectángulo es mayor a la del segundo rectángulo.")
    elif area1 == area2:
        print("Las áreas de los dos rectángulos son iguales")
    else:
        print("El área del segundo rectángulo es mayor a la del primer rectángulo.")

    # La siguiente condición decide cuál rectángulo va a ser rojo y cuál va a ser verde.
    if area1 > area2:
        dibujarRectangulo(base1, altura1, base2, altura2)
        turtle.exitonclick()
    else:
        dibujarRectangulo(base2, altura2, base1, altura1)
        turtle.exitonclick()


# Llamada a la función principal.
main()



