# Autor: Itzel Yanabany Castro Becerril
# Calcular el valor del Area y el Perimetro de os dos rectangulos
import turtle


def calcularAreas(baseUno, alturaUno, baseDos, alturaDos):
    area1 = baseUno * alturaUno
    area2 = baseDos * alturaDos
    area = "El area uno es de: " + str(area1) + " m2" + " y el area dos es de: " + str(area2) + " m2"

    return area


def imprimirAreas(baseUno, alturaUno, baseDos, alturaDos):
    area = calcularAreas(baseUno, alturaUno, baseDos, alturaDos)
    print(area)


def calcularPerimetros(baseUno, alturaUno, baseDos, alturaDos):
    perimetroUno = 2 * baseUno + 2 * alturaUno
    perimetroDos = 2 * baseDos + 2 * alturaDos
    perimetro = "El perimetro del primero es de : " + str(
        perimetroUno) + " m" " y el perimetro del segundo es de: " + str(perimetroDos) + " m"
    return perimetro


def imprimirPerimetros(baseUno, alturaUno, baseDos, alturaDos):
    perimetro = calcularPerimetros(baseUno, alturaUno, baseDos, alturaDos)
    print(perimetro)


def esMayor(baseUno, alturaUno, baseDos, alturaDos):
    a1 = baseUno * alturaUno
    a2 = baseDos * alturaDos
    if a1 > a2:
        print("El area mayor es del  primer Rectangulo")
    else:
        if a1 < a2:
            print("El area mayor es del  segundo Rectangulo")
        else:
            if a1 == a2:
                print("El area de los dos rectangulos son iguales")


def dibujarRectanguloUno(baseUno, alturaUno, baseDos, alturaDos):
    a1 = baseUno * alturaUno
    a2 = baseDos * alturaDos
    if a1 > a2:
        turtle.color("red")
        turtle.forward(baseUno)
        turtle.left(90)
        turtle.forward(alturaUno)
        turtle.left(90)
        turtle.forward(baseUno)
        turtle.left(90)
        turtle.forward(alturaUno)

    else:
        turtle.color("green")
        turtle.forward(baseUno)
        turtle.left(90)
        turtle.forward(alturaUno)
        turtle.left(90)
        turtle.forward(baseUno)
        turtle.left(90)
        turtle.forward(alturaUno)


def dibujarRectanguloDos(baseUno, alturaUno, baseDos, alturaDos):
    a1 = baseUno * alturaUno
    a2 = baseDos * alturaDos
    if a2 > a1:
        turtle.color("red")
        turtle.forward(baseDos)
        turtle.left(90)
        turtle.forward(alturaDos)
        turtle.left(90)
        turtle.forward(baseDos)
        turtle.left(90)
        turtle.forward(alturaDos)

    else:
        turtle.color("green")
        turtle.forward(baseDos)
        turtle.left(90)
        turtle.forward(alturaDos)
        turtle.left(90)
        turtle.forward(baseDos)
        turtle.left(90)
        turtle.forward(alturaDos)


def main():
    baseUno = int(input("Teclear la base del primer rectangulo: "))
    alturaUno = int(input("Teclea la altura de primer rectangulo: "))
    baseDos = int(input("Tecla la base del segundo rectangulo: "))
    alturaDos = int(input("Teclea la altura del segundo rectangulo: "))
    imprimirAreas(baseUno, alturaUno, baseDos, alturaDos)
    imprimirPerimetros(baseUno, alturaUno, baseDos, alturaDos)
    esMayor(baseUno, alturaUno, baseDos, alturaDos)
    dibujarRectanguloUno(baseUno, alturaUno, baseDos, alturaDos)
    dibujarRectanguloDos(baseUno, alturaUno, baseDos, alturaDos)
    turtle.exitonclick()


main()


