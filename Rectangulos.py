#Autor: Cesar Guzman Guadarrama
#Este programa lee las dimensiones de 2 rectangulos y te imprime su perimetro y area

import turtle


def calcularPerimetro1(base1,altura1):       #Esta funcion da el perimetro del primer rectangulo
    perimetro1 = (base1 * 2) + (altura1 * 2)
    return perimetro1


def calcularPerimetro2(base2,altura2):      #Esta funcion da el perimetro del primer rectangulo
    perimetro2 = (base2 * 2) + (altura2 * 2)
    return perimetro2


def calcularAreaRectangulo1(base1,altura1):    #Esta funcion calcula el area del primer rectangulo
    area1 = base1 * altura1
    return area1


def calcularAreaRectangulo2(base2,altura2):    #Esta funcion calcula el area del segundo rectangulo
    area2 = base2 * altura2
    return area2


def dibujarRectangulos(base1,altura1,base2,altura2):    #Dibujar rectangulos
    if calcularAreaRectangulo1(base1,altura1) > calcularAreaRectangulo2(base2,altura2):
        turtle.color( "red" )
        turtle.fd( base1 )
        turtle.left( 90 )
        turtle.fd( altura1 )
        turtle.left( 90 )
        turtle.fd( base1 )
        turtle.left( 90 )
        turtle.fd( altura1 )

        turtle.right( 90 )
        turtle.pu()
        turtle.fd( 50 )
        turtle.pd()

        turtle.color( "green" )
        turtle.fd( base2 )
        turtle.left( 90 )
        turtle.fd( altura2 )
        turtle.left( 90 )
        turtle.fd( base2 )
        turtle.left( 90 )
        turtle.fd( altura2 )

        turtle.exitonclick()
    else:
        turtle.color( "green" )
        turtle.fd( base1 )
        turtle.left( 90 )
        turtle.fd( altura1 )
        turtle.left( 90 )
        turtle.fd( base1 )
        turtle.left( 90 )
        turtle.fd( altura1 )

        turtle.right( 90 )
        turtle.pu()
        turtle.fd( 50 )
        turtle.pd()

        turtle.color( "red" )
        turtle.fd( base2 )
        turtle.left( 90 )
        turtle.fd( altura2 )
        turtle.left( 90 )
        turtle.fd( base2 )
        turtle.left( 90 )
        turtle.fd( altura2 )

        turtle.exitonclick()


def saberRectanguloConMayorArea(area1,area2):
    if area1 > area2:
        areaMayor = ("El rectangulo con mayor area es el primero con ",area1,"m2")
        return areaMayor
    elif area1 == area2:
        areaMayor = ("Las areas son iguales")
        areaMayor
    else:
        areaMayor = ("El rectangulo con mayor area es el segundo con ",area2,"m2")
        return areaMayor


def main ():
    base1 = float(input("Dame la base del primer rectangulo"))
    altura1 = float(input("Dame la altura del primer rectangulo"))
    base2 = float(input("Dame la base del segundo rectangulo"))
    altura2 = float(input("Dame la altura"))
    area1 = calcularAreaRectangulo1(base1,altura1)
    area2 = calcularAreaRectangulo2(base2,altura2)
    perimetro1 = calcularPerimetro1(base1,altura1)
    perimetro2 = calcularPerimetro2(base2,altura2)
    print("El area del primer rectangulo es de ",area1,"m2")
    print("El perimetro del primer rectangulo es de ",perimetro1,"m")
    print("El area del segundo rectangulo es de ",area2,"m2")
    print("El perimetro del segundo rectangulo es de ",perimetro2,"m")
    areaM = saberRectanguloConMayorArea(area1,area2)
    print(areaM)


    dibujarRectangulos(base1,altura1,base2,altura2)



main()