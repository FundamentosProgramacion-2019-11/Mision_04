#Autor: Michel Antoine Dionne Gutierrez Grupo:03 A01748632
#Imprime el area y perimetro de los rectangulos
import turtle
#Esta funcion calcula el perimetro de un rectangulo
def calcularPerimetro(b,a):
    perimetro = 2*b + 2*a
    return perimetro

#Esta funcion calcula el area de un rectangulo
def calcularArea(b,a):
    area = b*a
    return area

#Esta funcion determina cual es mayor o si son iguales
def esAreaMayor(areaRectangulo1,areaRectangulo2):
    if areaRectangulo1==areaRectangulo2:
        return "Los rectangulos son iguales"
    else:
        if areaRectangulo1>areaRectangulo2:
            return "El area del rectangulo 1 es mayor"
        else:
            return "El area del rectangulo 2 es mayor"

#Esta funcion se encarga de dibujar los rectangulos
def dibujarRectangulo(base1, altura1, base2, altura2,respuesta):
    if respuesta=="El area del rectangulo 1 es mayor":
        turtle.color("red")
        turtle.forward(base1)
        turtle.left(90)
        turtle.forward(altura1)
        turtle.left(90)
        turtle.forward(base1)
        turtle.left(90)
        turtle.forward(altura1)
        turtle.left(90)
        turtle.color("green")
        turtle.forward(base2)
        turtle.left(90)
        turtle.forward(altura2)
        turtle.left(90)
        turtle.forward(base2)
        turtle.left(90)
        turtle.forward(altura2)
        turtle.left(90)
    else:
        turtle.color("red")
        turtle.forward(base2)
        turtle.left(90)
        turtle.forward(altura2)
        turtle.left(90)
        turtle.forward(base2)
        turtle.left(90)
        turtle.forward(altura2)
        turtle.left(90)
        turtle.color("green")
        turtle.forward(base1)
        turtle.left(90)
        turtle.forward(altura1)
        turtle.left(90)
        turtle.forward(base1)
        turtle.left(90)
        turtle.forward(altura1)
        turtle.left(90)

def main():
    turtle.exitonclick
    base1 = int(input("Dame la base del primer rectangulo"))
    altura1 = int(input("Dame la altura del primer rectangulo"))
    base2 = int(input("Dame la base del segundo rectangulo"))
    altura2 = int(input("Dame la altura del segundo rectangulo"))
    perimetroRectangulo1 = calcularPerimetro(base1,altura1)
    perimetroRectangulo2 = calcularPerimetro(base2,altura2)
    print("El perimetro del primer rectangulo es de", perimetroRectangulo1)
    print("El perimetro del segundo rectangulo es de", perimetroRectangulo2)
    areaRectangulo1 = calcularArea(base1,altura1)
    areaRectangulo2 = calcularArea(base2,altura2)
    print("El area del primer rectangulo es de", areaRectangulo1)
    print("El area del segundo rectangulo es de", areaRectangulo2)
    respuesta=esAreaMayor(areaRectangulo1,areaRectangulo2)
    print(respuesta)
    dibujarRectangulo(base1,altura1,base2,altura2,respuesta)

    turtle.exitonclick()


main()