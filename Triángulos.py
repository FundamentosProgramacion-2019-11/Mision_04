# Autor: Victor Manuel Ceron Navarrete
# Confirma si existe un triángulo, y su tipo. Se dibuja el triángulo tambien

# Esto invoca a la tortuga jaja
import turtle
import math


# esta funcion comprueva que se pueda hacer un triangulo con las medidas
def compruebaTriangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


# se calcula que triangulo es
def calcularTriangulo(a, b, c):
    if compruebaTriangulo(a, b, c) == True:
       if a == b == c:
           return "Las medidas corresponden a un triángulo equilátero"
       elif  (c**2) + (a**2) - (b**2) == 0 or (b**2) + (c**2) - (a**2) == 0 or (a**2) + (b**2) - (c**2) == 0:
           return "Las medidas corresponden a un triángulo rectángulo"
       elif a == c != b or a == b != c or a == c != b:
           return "Las medidas corresponden a un triángulo isóceles"
       elif (a**2) + (b**2) - (c**2) < 0 or (c**2) + (a**2) - (b**2) < 0 or (b**2) + (c**2) - (a**2) < 0:
           return "Las medidas corresponden a un triángulo escaleno obtusángulo"
       elif (a**2) + (b**2) - (c**2) > 0 or (c**2) + (a**2) - (b**2) > 0 or  (b**2) + (c**2) - (a**2) > 0:
           return "Las medidas corresponden a un triángulo escaleno acutángulo"
    else:
        return "tus medidas no son de un triangulo."


# la tortuga invocada dibuja el triangulo con las medidas que el usuario teclee, si es que existe. Si no existe, devuelve error
def dibujarTriangulo(a, b, c):
    if compruebaTriangulo(a, b, c) == True:
        uno = (math.acos(((a ** 2) - (b ** 2) - (c ** 2)) / - (2 * b * c)) * 180/math.pi)
        dos = (math.acos(((b ** 2) - (a ** 2) - (c ** 2)) / - (2 * a * c)) * 180/math.pi)
        tres = (math.acos(((c ** 2) - (b ** 2) - (a ** 2)) / - (2 * a * b)) * 180/math.pi)
        turtle.forward(a)
        turtle.left(180 - dos)
        turtle.forward(c)
        turtle.left(180 - uno)
        turtle.forward(b)
        turtle.left(180 - tres)
        return uno, dos, tres
    else:
        return "Error: No puedo dibujar un triángulo con esas medidas"


# aqui se llaman a las funciones después de que el usuario teclee las medidas
def main():
    a = float(input("Escribe la primer medida de tu triángulo: "))
    b = float(input("Escribe la segunda medida de tu triángulo: "))
    c = float(input("Escribe la tercer medida de tu triángulo: "))
    compruebaTriangulo(a, b, c)
    print(calcularTriangulo(a, b, c))
    print(dibujarTriangulo(a, b, c))
    turtle.exitonclick()


main()