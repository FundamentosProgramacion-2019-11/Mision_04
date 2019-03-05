#Autor: Santiago España Vázquez A01748311 Grupo 03
#Descripción: Calcular perimetro y area de un rectangulo a partir de sus lados

def calculateArea(h,b):
    area= h*b
    return area

def calculatePerimeter(h,b):
    perimeter= (2*h)+(2*b)
    return perimeter

def main():
    h1=float(input("Por favor introduzca la altura del rectangulo 1: "))
    b1=float(input("Por favor introduzca la base del rectangulo 1: "))
    h2 = float(input("Por favor introduzca la altura del rectangulo 2: "))
    b2 = float(input("Por favor introduzca la base del rectangulo 2: "))
    print("El area del rectangulo 1 es:", calculateArea(h1,b1), "y el perimetro es:", calculatePerimeter(h1,b1))
    print("El area del rectangulo 2 es:", calculateArea(h2,b2), "y el perimetro es:", calculatePerimeter(h2,b2))

main()