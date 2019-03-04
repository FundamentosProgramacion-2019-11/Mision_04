# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Calcular el area y perimetro de un rectangulo, y decir que area es mayor


#la función calcula el area de cada rectangulo
def calcularArea(base1, altura1, base2, altura2):
    areaRectangulo1= base1*altura1
    areaRectangulo2= base2*altura2

    return areaRectangulo1, areaRectangulo2


#la función calcula el perimetro de cada rectangulo
def calcularPerimetro(base1, altura1, base2, altura2):
    perimetroRectangulo1= (base1*2)+(altura1*2)
    perimetroRectangulo2= (base2*2)+(altura2*2)

    return perimetroRectangulo1, perimetroRectangulo2


#la función imprime el area y perimetro de cada rectangulo y te dice cual de estos tiene un area mayor
def main():
    print ("Se te dara el area y el perimetro de dos rectangulos, y cual tiene una mayor area, por favor escribre lo siguiente")

    base1= int(input("Ingresa la base del primer rectangulo: "))
    altura1= int(input("Ingresa la altura del primer rectangulo: "))

    base2 = int(input("Ingresa la base del segundo rectangulo: "))
    altura2 = int(input("Ingresa la altura del segundo rectangulo: "))

    areaRectangulo1, areaRectangulo2= calcularArea(base1, altura1, base2, altura2)
    perimetroRectangulo1, perimetroRectangulo2= calcularPerimetro(base1, altura1, base2, altura2)

    print("El area del primer rectangulo es", areaRectangulo1, "y su perimetro es", perimetroRectangulo1)
    print("El area del segundo rectangulo es", areaRectangulo2, "y su perimetro es", perimetroRectangulo2)

    if areaRectangulo1>areaRectangulo2:
        print ("El primer rectangulo tiene mayor area que el segundo")

    elif areaRectangulo2>areaRectangulo1:
        print ("El segundo rectangulo tiene mayor area que el primero")

    else:
        print ("Ambos rectangulos tienen la misma area")


main()