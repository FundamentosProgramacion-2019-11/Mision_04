#Autor: Katia Hernández Barrera
#Programa que clasifica el tipo de triangulo de acuerdo a sus lados

def main():
    a = int(input("Teclea el primer lado del triángulo: "))
    b = int(input("Teclea el segundo lado del triángulo"))
    c = int(input("Teclea el tercer lado del triángulo"))
    triangulo = clasificarTriangulo(a,b,c)
    t = validarTriangulo(a,b,c)
    print("El tipo de triángulo es: ", triangulo,  t)


def clasificarTriangulo(a,b,c):
    if (a == b and a != c and b != c) or (c == a and c != b and a != b ) or (c == b and c != a and b != a):
        t = "Isosceles."
    elif (a == b and b == c) or (a == c and c == b):
        t = "Equilátero."
    elif (c**2 == a**2 + b**2) or (a**2 == b**2 + c**2) or(b**2 == a**2 + c**2 ):
        t = "Rectángulo."
    elif (a != b and b != c) or (a != c and c != b):
        t = "Otro."
    else:
        t = "Error."
    return t


def validarTriangulo(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return "estos lados corresponden a un triángulo"
    else:
        return" estos lados no corresponden a ningún triángulo"



main()