#Autor: Eric Andrés Jardón Chao
#Lee las dimensiones altura y base de dos rectángulos, calcula perímetro y área e indica cuál es mayor. EXTRA: traza los rectángulos con la tortuga, el mayor es rojo y el menor es verde.
#EXTRA: dibuja los rectángulos con la tortuga, de color rojo el más grande y verde el más pequeño.
import turtle

def main(): #La función principal recibe los datos de entrada, corre las funciones pertinentes, imprime los perímetros y áreas y corre las funciones de dibujo.
    base1=float(input("Teclea la magnitud de la base del Rectángulo 1: "))
    alto1= float(input("Teclea la magnitud de la altura del Rectángulo 1: "))
    base2 = float(input("Teclea la magnitud de la base del Rectángulo 2: "))
    alto2 = float(input("Teclea la magnitud de la altura del Rectángulo 2: "))
    perim1=calcularPerimetro(base1,alto1)
    perim2=calcularPerimetro(base2,alto2)
    area1=calcularArea(base1,alto1)
    area2=calcularArea(base2,alto2)
    print("El perímetro del Rectángulo 1 es %.2f" % (perim1))
    print("El perímetro del Rectángulo 2 es %.2f" % (perim2))
    print("El área del Rectángulo 1 es %.2f" %(area1))
    print("El área del Rectángulo 2 es %.2f" % (area2))

    aMayor=encontrarMayor(area1,area2)
    imprimirMayor(aMayor)
    dibujarRectangulos(alto1,base1,alto2,base2)


def calcularPerimetro(b,a): #función simple que calcula el perímetro con los parámetros base y altura de un rectángulo dado
    p=2*b+2*a
    return p

def calcularArea(b,a): #función simple que calcula el área con los parámetros base y altura de un rectángulo dado
    a=b*a
    return a

def encontrarMayor(a1,a2): #Decide a qué rectángulo pertenece el área de mayor dimensión, o si las áreas están empatadas.
    if a1>a2:
        return 1 #rectángulo 1 es mayor
    else:
        if a1 == a2:
            return 0 #Ningún rectángulo es mayor
        else:
            return 2 #Rectángulo 2 es mayor

def imprimirMayor(aMayor): #Estas función se apoya en estructuras de selección para decidir qué imprimir según el rectángulo de mayor área.
    if aMayor ==0:
        print("Las dos areas son equivalentes.")
    if aMayor ==1:
        print("El área de mayor magnitud es la del Rectángulo 1.")
    if aMayor ==2:
        print("El área de mayor magnitud es la del Rectángulo 2.")

def dibujarRectangulos(a1,b1,a2,b2): #esta función escoge los rectángulos y su color según el tamaño de su área y luego corre funciones para dibujarlos.
    wn = turtle.Screen()
    mayor=encontrarMayor(a1*b1, a2*b2)  #compara las dos áreas nuevamente
    if mayor==0: #si las áreas son iguales, los dos son trazados de color rojo
        turtle.color("red")
        trazarRect(b1,a1)
        turtle.penup()
        turtle.forward(100)
        turtle.right(90) #La tortuga se desplaza para tener espacio para trazar el siguiente rectángulo
        turtle.pendown()
        trazarRect(b2,a2)
    else:
        if mayor ==1: #las dimensiones del primer rectángulo son asignadas al rojo y las del segundo al verde
            rojox=b1
            rojoy=a1
            verdex=b2
            verdey=a2
        if mayor ==2: #Las dimensiones del segundo rectángulo son asignadas al rojo y las del primero al verde
            rojox=b2
            rojoy=a2
            verdex=b1
            verdey=a1
        turtle.color("red")
        trazarRect(rojox,rojoy) #Se traza el rectángulo de mayor área de color rojo
        turtle.penup()
        turtle.forward(50)
        turtle.right(90)
        turtle.pendown() #Se desplaza la tortuga un poco para tener espacio
        turtle.color("green")
        trazarRect(verdex,verdey) #Se traza el rectángulo de menor área de color verde

def trazarRect(b,a): #Esta función traza un rectángulo dadas la base y altura.
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)


main()
turtle.exitonclick()
#Fin del programa