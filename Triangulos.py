# Autor: Sofía Daniela Méndez Sandoval, A01242259
# Descripción: Define si los lados son un triángulo y cuál es.

#Llama a las funciones utilizadas
def main():

    #Pide al usuario los datos y se aceptan decimales.
    lado1 = float(input("Inserta el primer lado del triangulo: "))
    lado2 = float(input("Inserta el segundo lado del triángulo: "))
    lado3 = float(input("Inserta el tercer lado del triángulo: "))

    verificaTriangulo(lado1, lado2, lado3)

    #Imprime el resultado
    definir = defineTriangulo(lado1, lado2, lado3)
    print("La figura: ", definir)

#Verifica si es o no un triángulo por medio de la formula. Si este es el caso, se determina como verdadero
def verificaTriangulo(lado1, lado2, lado3):

    if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
        return True

    else:
        return False

#Se utilizan formulas para regresar qué tipo de triángulo es
def defineTriangulo(lado1, lado2, lado3):

    #Esto se realiza unicamente si el resultado de la primera función es True
    if verificaTriangulo(lado1, lado2, lado3) == True:

        if lado1 == lado2 == lado3:
            return "Es un triángulo equilatero"

        elif  (lado3**2) + (lado1**2) - (lado3**2) == 0 or (lado1**2) + (lado2**2) - (lado3**2) == 0 or (lado2**2) + (lado3**2) - (lado1**2) == 0:
           return "Es un triángulo rectángulo"

        elif lado1 == lado3 != lado2 or lado1 == lado2 != lado3 or lado1 == lado3 != lado2:
           return "Es un triángulo isóceles"

        elif (lado1**2) + (lado2**2) - (lado3**2) > 0 or (lado3**2) + (lado1**2) - (lado2**2) > 0 or (lado2**2) + (lado3**2) - (lado1**2) > 0:
           return "Es un triángulo escaleno acutángulo"

        else:
            return "Es otro tipo de triángulo"

    #Se regresa que no es un triángulo si el resultado de arriba es False
    else:
        return "No es un triángulo"

#Se llama a función principal
main()
