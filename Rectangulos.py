#Mariana Coria Rodríguez, A01374765
# Calcular área y perimetro de dos rectangulos

#Pedir al usuario la base y la altura de los rectangulos

#Calcular el área con la base y la altura
def area (b,h):
    areA = b*h
    return areA

#Calcular el perimetro con la base y la altura
def perimetro(b,h):
    perimetrO = (b*2)+(h*2)
    return perimetrO

#Comparar las medidas e indicar si son mayores, menores o iguales
def ambosArea(A,A2):
    if A == A2:
        return "Las áreas son iguales"
    if A2 > A:
        return "El area de tu segundo rectángulo es mayor"
    return "El area de tu primer triangulo es mayor"


#Preguntar por las medidas, llamar a las funciones
def main():
    base = int(input("¿Cuanto mide la base de tu primer rectangulo? "))
    altura = int(input("¿Cuanto mide la altura de tu primer rectangulo? "))
    base2 = int(input("¿Cuanto mide la base de tu segundo rectangulo? "))
    altura2 = int(input("¿Cuanto mide la altura de tu segundo rectangulo? "))

    area1= area(base,altura)
    area2 = area(base2, altura2)
    print("Area de tu primer rectangulo: %d" % area1)
    print("Perimetro de tu primer rectángulo: %d" % perimetro(base,altura))
    print("Area de tu segundo rectángulo: %d " % area2)
    print("Perimetro de tu segundo rectángulo %d" % perimetro(base2,altura2))
    print(ambosArea(area1,area2))

#marcar que se cumpla main
main()


