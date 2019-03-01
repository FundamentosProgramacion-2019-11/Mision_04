#FRANCISCO JAVIER GONZALEZ MOLINA A01748636
#CALCULAR Y COMPARAR RECTANGULOS

#Las siguientes dos funciones, calculan el area  del rectangulo A
#y del rectangulo B
def calcularAreaA(rectanguloAB, rectanguloAH):
    area= rectanguloAB*rectanguloAH
    return area
def calcularAreaB(rectanguloBB, rectanguloBH):
    area= rectanguloBB*rectanguloBH
    return area

#Las siguientes dos funciones, calcular el perimetro del rectangulo A
#y del rectangulo B
def calcularPerimetroB(rectanguloBB, rectanguloBH):
    perimetro=(2*rectanguloBB)+(2*rectanguloBH)
    return perimetro
def calcularPerimetroA(rectanguloAB, rectanguloAH):
    perimetro=(2*rectanguloAB)+(2*rectanguloAH)
    return perimetro

#Esta funcion compara las areas, para determinar la area mayor y regresarla; a la
#vez, dibuja el triangulo de mayor area de color rojo y el menor en color azul.
def calcularAreaMayor (rectanguloAB,rectanguloAH,rectanguloBB, rectanguloBH):
    import turtle
    areaA=rectanguloAB*rectanguloAH
    areaB=rectanguloBB*rectanguloBH
    if areaA > areaB:
        print("El primer rectangulo es mas grande que el segundo")

        turtle.color('white')
        turtle.fd(rectanguloAB)
        turtle.left(90)
        turtle.color('red')
        turtle.fd(rectanguloAH)
        turtle.left(90)
        turtle.fd(rectanguloAB)
        turtle.left(90)
        turtle.fd(rectanguloAH)
        turtle.left(90)
        turtle.fd(rectanguloAB)
        turtle.color('white')
        turtle.fd(30)
        turtle.color('blue')
        turtle.fd(rectanguloBB)
        turtle.left(90)
        turtle.fd (rectanguloBH)
        turtle.left(90)
        turtle.fd (rectanguloBB)
        turtle.left(90)
        turtle.fd (rectanguloBH)
        turtle.left(90)

        turtle.exitonclick()


    elif areaA < areaB:
        print("El segundo rectangulo es mas grande que el primero")

        turtle.color('white')
        turtle.fd(rectanguloBB)
        turtle.left(90)
        turtle.color('red')
        turtle.fd(rectanguloBH)
        turtle.left(90)
        turtle.fd(rectanguloBB)
        turtle.left(90)
        turtle.fd(rectanguloBH)
        turtle.left(90)
        turtle.fd(rectanguloBB)
        turtle.color('white')
        turtle.fd(30)
        turtle.color('blue')
        turtle.fd(rectanguloAB)
        turtle.left(90)
        turtle.fd(rectanguloAH)
        turtle.left(90)
        turtle.fd(rectanguloAB)
        turtle.left(90)
        turtle.fd(rectanguloAH)
        turtle.left(90)

        turtle.exitonclick()

    else:
        print("Ambos rectangulos son de igual tamaño")

        turtle.color('white')
        turtle.fd(rectanguloAB)
        turtle.left(90)
        turtle.color('blue')
        turtle.fd(rectanguloAH)
        turtle.left(90)
        turtle.fd(rectanguloAB)
        turtle.left(90)
        turtle.fd(rectanguloAH)
        turtle.left(90)
        turtle.fd(rectanguloAB)
        turtle.color('white')
        turtle.fd(30)
        turtle.color('blue')
        turtle.fd(rectanguloBB)
        turtle.left(90)
        turtle.fd(rectanguloBH)
        turtle.left(90)
        turtle.fd(rectanguloBB)
        turtle.left(90)
        turtle.fd(rectanguloBH)
        turtle.left(90)

        turtle.exitonclick()

#Esta funcion lee datos y llama a las funciones.
def main ():
    rectanguloAB=int (input("Dame valor de Base del primer Rectangulo: "))
    rectanguloAH=int (input("Dame valor de Altura del primer Rectanuglo: "))
    areaA = calcularAreaA(rectanguloAB, rectanguloAH)
    perimetroA=calcularPerimetroA(rectanguloAB,rectanguloAH)
    print("""
El area es: %d
El perimetro es: %d
"""%(areaA,perimetroA))


    rectanguloBB=int (input("Dame valor de Base del segundo Rectangulo: "))
    rectanguloBH=int (input("Dame valor de Altura del segundo Rectangulo: "))
    areaB=calcularAreaB(rectanguloBB,rectanguloBH)
    perimetroB=calcularPerimetroB(rectanguloBH,rectanguloBH)
    print("""El area es: %d
El perimetro es: %d
"""%(areaB,perimetroB))

    areaMayor=calcularAreaMayor(rectanguloAB,rectanguloAH,rectanguloBB,rectanguloBH)
    print(areaMayor)

main()