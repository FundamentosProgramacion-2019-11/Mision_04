import turtle
#Bruno Omar Jiménez Mancilla
#Programa que reciba la base y la altura de dos triangulos y calcule sus areas y sus perimetros además de dibujarlos usando la herramienta turtle

def main():
    b1 = float(input("Ingresa la base de el primer rectangulo: "))
    a1 = float(input("Ingresa la altura de el primer rectangulo: "))
    b2 = float(input("Ingresa la base de el segundo rectangulo: "))
    a2 = float(input("Ingresa la altura de el segundo rectangulo: "))
    area1 = CalculaArea1(b1,a1)
    perimetro1 = CalculaPerimetro1(b1,a1)
    area2 = CalculaArea2(b2,a2)
    perimetro2 = CalculaPerimetro2(b2,a2)
    mayor =CompararAreas(area1,area2,b1,a1,b2,a2)
    print("El perimetro del primer rectagnulo es:  ",perimetro1)
    print("El area del primer rectagnulo es:       ",area1)
    print("El perimetro del segundo rectagnulo es: ", perimetro2)
    print("El area del segundo rectagnulo es:      ", area2)
    print(mayor)

    turtle.exitonclick()

def DibujarRectangulos1M(b1,a1,b2,a2):
    turtle.color("red")
    turtle.forward(b1)
    turtle.left(90)
    turtle.forward(a1)
    turtle.left(90)
    turtle.forward(b1)
    turtle.left(90)
    turtle.forward(a1)
    turtle.color("green")
    turtle.forward(b2)
    turtle.left(90)
    turtle.forward(a2)
    turtle.left(90)
    turtle.forward(b2)
    turtle.left(90)
    turtle.forward(a2)

def DibujarRectangulos2M(b1,a1,b2,a2):
    turtle.color("green")
    turtle.forward(b1)
    turtle.left(90)
    turtle.forward(a1)
    turtle.left(90)
    turtle.forward(b1)
    turtle.left(90)
    turtle.forward(a1)
    turtle.color("red")
    turtle.forward(b2)
    turtle.left(90)
    turtle.forward(a2)
    turtle.left(90)
    turtle.forward(b2)
    turtle.left(90)
    turtle.forward(a2)

def DibujarRectangulosIguales(b1,a1):
    turtle.color("green")
    turtle.forward(b1)
    turtle.left(90)
    turtle.forward(a1)
    turtle.left(90)
    turtle.forward(b1)
    turtle.left(90)
    turtle.forward(a1)


def CompararAreas(area1,area2,b1,a1,b2,a2):
    if area1 > area2:
        DibujarRectangulos1M(b1,a1,b2,a2)
        return "El area del primer rectangulo es mayor"
    elif area1 == area2:
        DibujarRectangulosIguales(b1,a1)
        return "Las areas son iguales"
    else:
        DibujarRectangulos2M(b1,a1,b2,a2)
        return "El area del segundo rectangulo es mayor"
def CalculaPerimetro1(base,altura):
    perimetro = (2*base)+(2*altura)
    return perimetro

def CalculaArea1 (base,altura):
    area = base*altura
    return area

def CalculaPerimetro2(base,altura):
    perimetro = (2*base)+(2*altura)
    return perimetro

def CalculaArea2(base,altura):
    area = base*altura
    return area


main()