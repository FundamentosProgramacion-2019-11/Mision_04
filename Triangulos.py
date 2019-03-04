#Autor: Marianela Contreras D.
#Programa para definir un tipo de triángulo conforme los valores leídos.


#función para calcular el tipo de triángulo que puede ser
def calcularTriángulo(a,b,c):
    if a == b and a == c:
        triangulo= "Equilátero"
    elif a ==b or a == c or b==c:
        triangulo= "Iscóceles"
    else:
        triangulo= "Escaleno"
    return triangulo


#función para saber si el triángulo es rectángulo o no
def calcularTriánguloRectángulo(a,b,c):
    if a*a + b*b== c*c:
        rectangulo= "Rectángulo"
    elif b*b + c*c== a*a:
        rectangulo = "Rectángulo"
    elif c*c + a*a == b*b:
        rectangulo= "Rectángulo"
    else:
        rectangulo = "este triángulo no es rectángulo"
    return rectangulo


#función para conocer si es posible hacer un triángulo con los valores tecleados por el usuario
def conocerTriánguloPosible(a,b,c):
    if (a>0 and b>0 and c>0) and ((a+b)>c and (b+c)>a and (c+a)>b):
        posible= calcularTriángulo(a,b,c)
    else:
        posible= "Estos lados no corresponden a un triángulo"
    return posible


# función principal del programa y la que se correrá. Las lecturas e impresiones se hacen en esta función.
def main():
    a= float(input("Introduzca el primer lado del triángulo:"))
    b= float(input("Introduzca el segundo lado del triángulo:"))
    c= float(input("Introduzca el tercer lado del triángulo:"))
    triangulo= calcularTriángulo(a,b,c)
    rectangulo= calcularTriánguloRectángulo(a,b,c)
    posible=conocerTriánguloPosible(a,b,c)

    if posible == "Estos lados no corresponden a un triángulo":
        print ("Estos lados no corresponden a un triángulo")
    else:
        print("\nEl triángulo es:", triangulo,"y",rectangulo)


main()

#que la suma de dos lados sea mayor que la del tercer lado