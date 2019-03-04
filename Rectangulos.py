#Autor: Aline Villegas Berdejo
#Calcula e imprime el perímetro y área de dos rectángulos


def calcularPerimetro(base, altura): #Calcula el perímetro de un rectángulo
    p1=base+base+altura+altura
    return p1


def calcularArea(base, altura):       #Calcula el área de un rectángulo
    a1= base*altura
    return a1


def main():         #Indica las funciones que se van a correr al llamar a la funición "main()"
    base=int(input("Teclea la altura del primer rectángulo: "))
    altura= int(input("Teclea la base del primer rectángulo: "))
    base2=int(input("Teclea la altura del segundo rectángulo: "))
    altura2=int(input("Teclea la base del segundo rectángulo: "))
    perimetro1=calcularPerimetro(base,altura)
    perimetro2=calcularPerimetro(base2,altura2)
    area1=calcularArea(base, altura)
    area2=calcularArea(base2, altura2)
    print("\nEl perímetro del primer rectángulo es: ", perimetro1, "cm")
    print("El área del primer rectángulo es: ", area1, "cm2")
    print("\nEl perímetro del segundo rectángulo es: ", perimetro2, "cm")
    print("El área del segundo rectángulo es: ", area2, "cm2")
    if area1>area2:
        print("\nEl área del primer rectángulo es mayor.")
    elif area1<area2:
        print("\nEl área del segundo rectángulo es mayor.")
    else:
        print("\nLos rectángulos tienen la misma área.")


main()