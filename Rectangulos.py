#Escribe un programa que lea las dimensiones (base y altura) de dos rectángulos y que calcule e imprima el perímetro y área
#de cada uno.

def calcularArea1(base1, altura1):
    area = base1*altura1
    return area

def calcularArea2(base2, altura2):
    area = base2*altura2
    return area

def calcularPerimetro1(base1, altura1):
    p = (base1*2)+(altura1*2)
    return p

def calcularPerimetro2(base2, altura2):
    p = (base2*2)+(altura2*2)
    return p

def compararAreas(area1, area2):
    if area1>area2:
        x = "El área del primer rectángulo es mayor que el segundo."
    elif area2>area1:
        x = "El área del segundo rectángulo es mayor que el primero."
    elif area1==area2:
        x = "El área de los rectángulos es la misma."
    return x

def main():
    base1 = int(input("Teclea el largo del rectángulo1: "))
    altura1 = int(input("Teclea la altura del rectángulo1: "))
    base2 = int(input("Teclea el largo del rectángulo2: "))
    altura2 = int(input("Teclea la altura del rectángulo2: "))
    area1 = calcularArea1(base1, altura1)
    area2 = calcularArea2(base2, altura2)
    perimetro1 = calcularPerimetro1(base1, altura1)
    perimetro2 = calcularPerimetro2(base2, altura2)
    comparacion = compararAreas(area1, area2)
    print(comparacion)

main()