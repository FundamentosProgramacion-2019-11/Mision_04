#Autor: María Fernanda García Gastélum A01376181
#Calcular perímetro y área de 2 rectángulos y después comparar


#importar tortuga
import turtle

#función para calcular perímetro
def calcularPerimetro(base, altura):
    perimetro= (base*2) + (altura*2)
    return perimetro


#función para calcular área
def calcularArea(base, altura):
    area= base*altura
    return area


#calcular cuál es el rectángulo mayor
def calcularRectanguloMayor(area1, area2):
    if area1 > area2:
        return "El primer rectángulo es mayor"
    if area2 > area1:
        return "El segundo rectángulo es mayor"
    else:
        return "Los rectángulos son iguales"


#definir el color de los rectángulo mayor y menor
def definirColor(area1, area2):
    if area1 > area2:
        return turtle.color("red")
    else:
        turtle.color("green")


#EXTRA: dibujar rectángulo
def dibujarRectangulo(base, altura):
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)


def main():
    base1= int(input("Escribe la base del primer rectángulo: "))
    altura1= int(input("Escribe la altura del primer rectángulo: "))
    base2= int(input("Escribe la base del segundo rectángulo: "))
    altura2= int(input("Escribe la altura del segundo rectángulo: "))
    perimetro1= calcularPerimetro(base1, altura1)
    area1= calcularArea(base1, altura1)
    perimetro2 = calcularPerimetro(base2, altura2)
    area2 = calcularArea(base2, altura2)
    rectanguloMayor= calcularRectanguloMayor(area1, area2)
    print("Perímetro del 1er rectángulo: ", perimetro1)
    print("Área del 1er rectángulo: ", area1)
    print("Perímetro del 2ndo rectángulo: ", perimetro2)
    print("Área del 2ndo rectángulo: ", area2)
    print(rectanguloMayor)
    definirColor(area1, area2)
    dibujarRectangulo(base1, altura1)
    turtle.penup()
    turtle.forward(base1 + 15)
    turtle.pendown()
    definirColor(area2, area1)
    dibujarRectangulo(base2, altura2)
    turtle.exitonclick()


main()