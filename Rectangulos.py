#Autor: Mariana Teyssier Cervantes
#Leer las dimensiones de dos rectangulos, calcular e imprimir su perimetro.


#Calcular el perimetro del rectangulo 1
def calcularPerimetro1(base1, altura1):
    p1 = (2*base1) + (2*altura1)
    return p1


#Calcular el area del rectangulo 1
def calcularArea1(base1, altura1):
    a1 = base1 * altura1
    return a1


#Calcular el perimetro del rectangulo 2
def calcularPerimetro2(base2, altura2):
    p2 = (2*base2) + (2*altura2)
    return p2


#Calcular el area del rectangulo 2
def calcularArea2(base2, altura2):
    a2 = base2 * altura2
    return a2


#Conocer cual de las dos areas es la mayor o si son iguales
def definirMayor(a1, a2):
    if a1>a2:
        return "Rectangulo1 es mayor"
    if a1<a2:
        return "Rectangulo2 es mayor"
    if a1==a2:
        return "Areas iguales"


#Definir los datos de los rectangulos (base y altura), llamar a las funciones de area, perimetro y el mayor de las areas
def main():
    base1 = int(input("Teclea la base del rectangulo 1: "))
    altura1 = int(input("Teclea la altura del rectangulo 1: "))
    base2 = int(input("Teclea la base del rectangulo 2: "))
    altura2 = int(input("Teclea la altura del rectangulo 2: "))
    perimetro1 = calcularPerimetro1(base1, altura1)
    print("Perimetro1:", perimetro1)
    perimetro2 = calcularPerimetro2(base2, altura2)
    print("Perimetro2:", perimetro2)
    a1 = calcularArea1(base1, altura1)
    print("Area1:", a1)
    a2 = calcularArea2(base2, altura2)
    print("Area2:", a2)
    mayor = definirMayor(a1, a2)
    print(mayor)


#Llamar a la funcion -main-
main()