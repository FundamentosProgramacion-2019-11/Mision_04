# Autor: Guillermo De Anda Casas, A01375892
# Código que lee las dimensiones de 2 rectángulos y calcula e imprime el perímetro y área.


import turtle


# Función que calcula el ÁREA de la figura.
def calcularArea(b, h):
    area = b * h
    return area


# Función que calcula el PERÍMETRO de la figura.
def calcularPerimetro(b, h):
    perimetro = (b*2) + (h*2)
    return perimetro


# Función que definde qué color usar para la primer figura
def definirColor1(areaFiguraUno, areaFiguraDos):
    if areaFiguraUno > areaFiguraDos:
        return turtle.color("red")
    else:
        return turtle.color("green")


# Función que definde qué color usar para la segunda figura
def definirColor2(areaFiguraUno, areaFiguraDos):
    if areaFiguraDos > areaFiguraUno:
        return turtle.color("red")
    else:
        return turtle.color("green")


# Función que dibuja las figuras con la tortuga
def dibujarTortuga(b, h):
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)


# Función main que lee los datos, calcula los valores y los compara
def main():
    baseUno = float(input("Teclea la base de la primer figura: "))
    alturaUno = float(input("Teclea la altura de la primera figura: "))
    baseDos = float(input("Teclea la base de la segunda figura: "))
    alturaDos = float(input("Teclea la altura de la segunda figura: "))
    areaFiguraUno = calcularArea(baseUno, alturaUno)
    perimetroFiguraUno = calcularPerimetro(baseUno, alturaUno)
    areaFiguraDos = calcularArea(baseDos, alturaDos)
    perimetroFiguraDos = calcularPerimetro(baseDos, alturaDos)
    print("El área de la primer figura es",areaFiguraUno, " y el perímetro de la primer figura es",perimetroFiguraUno)
    print("El área de la segunda figura es",areaFiguraDos, " y el perímetro de la segunda figura es",perimetroFiguraDos)
    if areaFiguraUno > areaFiguraDos:
        print("La primer figura tiene mayor área")
    elif areaFiguraUno < areaFiguraDos:
        print("La segunda figura tiene mayor área")
    else:
        print("Las áreas de ambas figuras son iguales")
    definirColor1(areaFiguraUno, areaFiguraDos)
    dibujarTortuga(baseUno, alturaUno)
    turtle.penup()
    turtle.forward(baseUno + 20)
    turtle.pendown()
    definirColor2(areaFiguraUno, areaFiguraDos)
    dibujarTortuga(baseDos, alturaDos)
    turtle.exitonclick()


main()