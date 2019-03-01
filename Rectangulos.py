#Autor: Mario Hernández Cárdenas
#Calcula el área y perímetro de dos rectángulos e indica el de mayor area

import turtle

#Calcula el área de un rectángulo
def calcularArea(base, altura):
    area = base * altura
    return area


#Calcula el perímetro de un rectángulo
def calcularPerimetro(base, altura):
    perimetro = base*2 + altura*2
    return perimetro


#Calcula cuál es el área mayor entre 2 rectángulos
def calcularAreaMayor(area1, area2):
    if area1 == area2:
        return "Ambos rectángulos tienen la misma área"
    else:
        if area1>area2:
            return "El área del primer rectángulo es mayor"
        else:
            return "El área del segundo rectángulo es mayor"


#EXTRA
#Dibuja el rectángulo según su base y altura
def dibujarRectangulo(base, altura):
    turtle.backward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.right(90)
    turtle.forward(base)
    turtle.right(90)
    turtle.forward(altura)


#Indica a la tortuga el color que debe ser el rectángulo
def definirColorRectangulo(area1, area2):
    if area1 > area2:
        color = turtle.color("red")
    else:
        color = turtle.color("green")
    return color


#Dibuja ambos rectángulos con el color correspondiente al mayor
def dibujarRectangulos(base1, altura1, base2, altura2, area1, area2):
    definirColorRectangulo(area1, area2)
    dibujarRectangulo(base1, altura1)
    turtle.penup()
    turtle.left(90)
    turtle.forward(base2 + 25)
    turtle.pendown()
    definirColorRectangulo(area2, area1)
    dibujarRectangulo(base2, altura2)
    turtle.exitonclick()


def main():
    baseRectangulo1 = int(input("Teclea la base del primer rectángulo: "))
    alturaRectangulo1 = int(input("Teclea la altura del primer rectángulo: "))
    baseRectangulo2 = int(input("Teclea la base del segundo rectángulo: "))
    alturaRectangulo2 = int(input("Teclea la altura del segundo rectángulo: "))
    area1 = calcularArea(baseRectangulo1,alturaRectangulo1)
    area2 = calcularArea(baseRectangulo2,alturaRectangulo2)
    perimetro1 = calcularPerimetro(baseRectangulo1, alturaRectangulo1)
    perimetro2 = calcularPerimetro(baseRectangulo2, alturaRectangulo2)
    mayor = calcularAreaMayor(area1, area2)
    print("\nEl área del primer rectángulo es: %d centimetros cuadrados" %area1)
    print("El área del segundo rectángulo es: %d centimetros cuadrados"%area2)
    print("El perímetro del primer rectángulo es: %d centimetros"%perimetro1)
    print("El perímetro del segundo rectángulo es: %d centimetros"%perimetro2)
    print(mayor)
    dibujarRectangulos(baseRectangulo1, alturaRectangulo1, baseRectangulo2, alturaRectangulo2, area1, area2)


main()