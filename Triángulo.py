# Autor: Roberto Emmanuel González Muñoz
# Escribe un programa que lea el valor de cada uno de
# los lados de un triángulo (puede ser en cualquier orden).


def esTrianguloRectagulo(a, b, c):
    if a*a == b*b + c*c:
        return True
    if b*b == a*a + c*c:
        return True
    if c*c == b*b + a*a:
        return True
    else:
        return False


def esTrianguloIsoceles(a, b, c):
    if a == b and c != a:
        return True
    if a == c and b != a:
        return True
    if b == c and b != a:
        return True
    else:
        return False


def esTrianguloEquilatero(a, b, c):
    if a == b and b == c:
        return True
    else:
        return False


def main():
    # Pregunta la medida de los lados de un triángulo.
    ladoA = int(input("Teclea el primer lado del triángulo: "))
    ladoB = int(input("Teclea el segundo lado del triángulo: "))
    ladoC = int(input("Teclea el tercer lado del triángulo: "))

    # Determina el tipo de triángulo.
    if ladoA > 0 and ladoB > 0 and ladoC > 0:
        trianguloRectangulo = esTrianguloRectagulo(ladoA, ladoB, ladoC)
        trianguloIsoceles = esTrianguloIsoceles(ladoA, ladoB, ladoC)
        trianguloEquilatero = esTrianguloEquilatero(ladoA, ladoB, ladoC)
    else:
        return print("Estos lados no corresponden a un triángulo.")

    # Evalúa cual de los 4 tipos de triiángulo se obtiene con los lados dados triángulo.
    if trianguloRectangulo == True:
        print("El triángulo es Rectángulo.")
    elif trianguloEquilatero == True:
        print("El tríangulo es Equilátero.")
    elif trianguloIsoceles == True:
        print("El triángulo es Isóceles.")
    else:
        print("El triángulo es de otro tipo")


main()