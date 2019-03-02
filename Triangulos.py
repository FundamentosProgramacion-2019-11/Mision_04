#Autor: Mariana Teyssier Cervantes
#Escribir si el triangulo existe y de que tipo es.


#Conocer por sus lados que tipo de triangulo es o si existe.
def conocerTriangulo(lado1, lado2, lado3):
    if lado1==lado2 and lado1>lado3:
        t = "Triangulo isoceles"

    elif lado1==lado3 and lado1>lado2:
        t = "Triangulo isoceles"

    elif lado3==lado2 and lado3>lado1:
        t = "Triangulo isoceles"

    elif lado1==lado2 and lado1==lado3:
        t = "Triangulo equilatero"

    elif lado3**2==(lado1**2 + lado2**2):
        t = "Triangulo rectangulo"

    elif lado2**2==(lado1**2 + lado3**2):
        t = "Triangulo rectangulo"

    elif lado1**2==(lado3**2 + lado2**2):
        t = "Triangulo rectangulo"

    else:
         t = "Estos lados no corresponden a un triangulo"

    return t


#Definir tres lados e imprimir que tipo de triangulo es o si no existe.
def main():
    lado1 = int(input("Teclea el primer lado: "))
    lado2 = int(input("Teclea el segundo lado: "))
    lado3 = int(input("Teclea el tercer lado: "))
    triangulo = conocerTriangulo(lado1, lado2, lado3)
    print(triangulo)


#Llamar a la funcion -main-
main()
