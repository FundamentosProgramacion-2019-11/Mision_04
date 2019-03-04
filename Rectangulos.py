# Autor: Sofía Daniela Méndez Sandoval, A01242259
# Descripción: Este programa calcula área y perímetro de dos rectángulos y compara los tamaños

#Llama a las funciones utilizadas
def main():

    #Pide la información al usuario
    base1 = int(input("Inserte el área del primer rectángulo: "))
    altura1 = int(input("Inserte la altura del primer rectángulo: "))

    base2 = int(input("Inserte el área del segundo rectángulo: "))
    altura2 = int(input("Inserte la altura del segundo rectángulo: "))

    #Imprime los resultados obtenidos
    area1 = calcularArea1(base1, altura1)
    print("El área del rectángulo 1 es: ", area1, "cm cuadrados")

    perimetro1 = calcularPerimetro1(base1, altura1)
    print("El perímetro del rectángulo 1 es: ", perimetro1, "cm")

    area2 = calcularArea2(base2, altura2)
    print("El área del rectángulo 2 es: ", area2, "cm cuadrados")

    perimetro2 = calcularPerimetro2(base2, altura2)
    print("El perímetro del rectángulo 2 es: ", perimetro2, "cm")

    comparacion = compararTamanios(area1, area2)
    print(comparacion)

#Calcula el área con la fórmula
def calcularArea1(base1, altura1):

    areau = base1*altura1

    return areau


def calcularPerimetro1(base1, altura1):

    perimetrou = (base1*2) + (altura1*2)

    return perimetrou


def calcularArea2(base2, altura2):

    aread = base2 * altura2

    return aread

#Calcula el perímetro con las fórmulas
def calcularPerimetro2(base2, altura2):

    perimetrod = (base2 * 2) + (altura2 * 2)

    return perimetrod

#Compara los tamaños comparando con if
def compararTamanios(area1, area2):

    if area1>area2:
        return "El rectángulo 1 es de mayor tamaño que el rectángulo 2"

    elif area2>area1:
        return "El rectángulo 2 es de mayot tamaño que el rectángulo 1"

    else:
        return "Son del mismo tamaño"

#Llama a la función principal
main()
