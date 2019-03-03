#Autor: Cecilia Daniela Olivares Hernández, a01745727
#Este programa identifica que tipo de triangulo se forma dependiendo los valores ingresados


#Esta función compara los valores e identifica que triangulo es
def identificarTriangulo(lado1, lado2, lado3):
    if lado1<=0 or lado2<=0 or lado3<=0:
        tipo = "Estos lados NO corresponden a un triángulo"
    elif lado1==lado2!=lado3 or lado1==lado3!=lado2 or lado2==lado3!=lado1:
        tipo = "El triangulo es ISÓSCELES"
    elif lado1==lado2==lado3==lado1:
        tipo =  "El triangulo es EQUILÁTERO"
    elif lado1**2==lado2**2+lado3**2 or lado2**2==lado1**2+lado3**2 or lado3**2==lado1**2+lado2**2:
        tipo = "El triangulo es RECTANGULO"
    elif lado1!=lado2!=lado3!=lado1:
        tipo = "El triangulo es ESCALENO"
    return tipo


#Funcion principal que resuelve el problema
def main():
    lado1 = int(input("Inserta el valor del lado 1 del triangulo: "))
    lado2 = int(input("Inserta el valor del lado 2 del triangulo: "))
    lado3 = int(input("Inserta el valor del lado 3 del triangulo: "))
    tipo = identificarTriangulo(lado1, lado2, lado3)
    print(tipo)


main()
