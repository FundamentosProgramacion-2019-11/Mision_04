#Autor: Aline Paulette Villegas Berdejo
#Calcula de acuerdo a las medidas dadas del triángulo, si es isósceles, equilátero, rectángulo u otro.


def calcularTipoTriangulo(a,b,c,):  #Calcula el tipo de triángulo de acuerdo a las medidas de sus lados
    if a==0 or b==0 or c==0:
        triangulo= "Estos lados no corresponden a los de un un triángulo"
    else:
        if a==b and a==c and b==c:
            triangulo="La figura es un triángulo equilátero"
        elif a==b or b==c or c==a:
            triangulo="La figura es un triángulo isósceles"
        elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
            triangulo="La figura es un triángulo rectángulo"
        else:
            triangulo="La figura es otro tipo de triángulo"

    return triangulo


def main():      #Indica las funciones que se van a correr al llamar a la funición "main()"
    a=int(input("Escribe valor del lado 1: "))
    b=int(input("Escribe el valor del lado 2: "))
    c=int(input("Escribe el valor del lado 3: "))
    tipoTriangulo= calcularTipoTriangulo(a,b,c)
    print (tipoTriangulo)


main()