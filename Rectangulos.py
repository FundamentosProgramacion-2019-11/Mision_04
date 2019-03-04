#Autor: Marianela Contreras Dominguez
#Programa para calcular el área y perímetro de dos rectángulos, e indicar al mayor de ambos, o si son iguales.

import turtle
#función para calcular el área de ambos rectángulos
def calcularArea(base, altura):
    area = base * altura
    return area


#función para calcular el perímetro de ambos rectángulos
def calcularPerimetro(base, altura):
    perimetro = (2 * base) + (2 * altura)
    return perimetro


#función para calcular el área mayor
def calcularMayor(area1, area2):
    if area1 > area2:
        mayor= "El primer rectángulo"
    elif area1 == area2:
        mayor = "Las áreas son iguales"
    else:
        mayor= "El segundo rectángulo"
    return mayor


#función para dibujar los rectángulos y pintarlos
def pintarRectangulos(base1,base2,altura1,altura2):
    if (base1 * altura1) > (base2 * altura2):
        turtle.color("red")
        turtle.forward(base1)
        turtle.left(90)
        turtle.forward(altura1)
        turtle.left(90)
        turtle.forward(base1)
        turtle.left(90)
        turtle.forward(altura1)
        turtle.left(90)
        turtle.penup()
        turtle.forward(base1 + 100)
        turtle.pendown()
        turtle.color("green")
        turtle.forward(base2)
        turtle.left(90)
        turtle.forward(altura2)
        turtle.left(90)
        turtle.forward(base2)
        turtle.left(90)
        turtle.forward(altura2)
        turtle.penup()
        turtle.forward(2 * altura2)
    elif (base2 * altura2) > (base1 * altura1):
        turtle.color("red")
        turtle.forward(base2)
        turtle.left(90)
        turtle.forward(altura2)
        turtle.left(90)
        turtle.forward(base2)
        turtle.left(90)
        turtle.forward(altura2)
        turtle.left(90)
        turtle.penup()
        turtle.forward(base2 + 100)
        turtle.pendown()
        turtle.color("green")
        turtle.forward(base1)
        turtle.left(90)
        turtle.forward(altura1)
        turtle.left(90)
        turtle.forward(base1)
        turtle.left(90)
        turtle.forward(altura1)
        turtle.penup()
        turtle.forward(2 * altura1)
    else:
        turtle.color("red")
        turtle.forward(base1)
        turtle.left(90)
        turtle.forward(altura1)
        turtle.left(90)
        turtle.forward(base1)
        turtle.left(90)
        turtle.forward(altura1)
        turtle.left(90)
        turtle.penup()
        turtle.forward(base1 + 100)
        turtle.pendown()
        turtle.color("green")
        turtle.forward(base2)
        turtle.left(90)
        turtle.forward(altura2)
        turtle.left(90)
        turtle.forward(base2)
        turtle.left(90)
        turtle.forward(altura2)
        turtle.penup()
        turtle.forward(2 * altura2)
    return pintarRectangulos



# función principal del programa y la que se correrá. Las lecturas e impresiones se hacen en esta función.
def main():
    base = float(input("Escriba la base del primer rectángulo: "))
    altura = float(input("Escriba la altura del primer rectángulo:"))
    area1 = calcularArea(base, altura)
    perimetro1 = calcularPerimetro(base, altura)
    base1=base
    altura1=altura
    base = float(input("Escriba la base del segundo rectángulo:"))
    altura = float(input("Escriba la altura del segundo rectángulo:"))
    area2 = calcularArea(base, altura)
    perimetro2 = calcularPerimetro(base, altura)
    base2=base
    altura2=altura
    mayor = calcularMayor(area1, area2)
    print("\nEl área del primer rectángulo es: %.2f"% area1, "y el perímetro es: %.2f"%perimetro1)
    print("\nEl área del segundo rectángulo es: %.2f "% area2, " y el perímetro es: %.2f"%perimetro2)
    print ("\nEl área mayor es:", mayor)
    pintarRectangulos(base1, altura1, base2, altura2)

    turtle.exitonclick()

main()

