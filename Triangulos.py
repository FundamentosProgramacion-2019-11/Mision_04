#Alan Giovanni Rodriguez Camacho A01748185
#Lee la longitud de los lados de un triangulo e imprime el tipo de triangulo que es.


def calcularTipoTriangulo(ladoA,ladoB,ladoC): #Determina que tipo de triangulo es el dado en la funcion main.
    comprobacionA = (ladoA**2)+(ladoB**2)
    comprobacionB = ladoC**2
    if ladoA == ladoB != ladoC or ladoA == ladoC != ladoB or ladoB == ladoC != ladoA:
        triangulo = 1
        return triangulo
    elif ladoA == ladoB == ladoC:
        triangulo = 2
        return triangulo
    elif comprobacionA == comprobacionB:
        triangulo = 3
        return triangulo
    else:
        triangulo = 4
        return triangulo


def main():
    ladoA = int(input("Indica la medida del cateto a de tu triangulo: "))
    ladoB = int(input("Indica la medida del cateto b de tu triangulo: "))
    ladoC = int(input("Indica la medida de la hipotenusa de tu triangulo: "))
    if ladoA > 0 or ladoB > 0 or ladoC >0:
        print("ERROR: SU TRIANGULO NO EXISTE.")
    else:
        triangulo = calcularTipoTriangulo(ladoA,ladoB,ladoC)
        if triangulo == 1:
            print("Tu triangulo es un triangulo isosceles")
        elif triangulo == 2:
            print("Tu triangulo es un triangulo equilatero.")
        elif triangulo == 3:
            print("Tu triangulo es un triangulo rectangulo.")
        elif triangulo == 4:
            print("Tu triangulo no se encuentra en nuestras opciones.")


main()