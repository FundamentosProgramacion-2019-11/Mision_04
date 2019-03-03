#Autor:Bernardo Mondragón Ramirez A01022325
#lee el valor de cada uno de los lados de un triángulo


def TipoDeTriangulo(lado1, lado2, lado3):

        if lado1==lado2 and lado2==lado3:
            return"triangulo equilatero"
        elif lado1==lado2 or lado1==lado3 or lado3==lado2:
            return "Triangulo Isoseles"
        elif (lado1*lado1 + lado2*lado2)== lado3*lado3 or (lado3*lado3-lado2*lado2)== lado1*lado1 :
            return"Triangulo Rectangulo"
        elif (lado3*lado3 - lado1*lado1)== lado2*lado2:
            return"Triangulo Rectangulo"
        else:
            return"Estos lados no corresponden a un triángulo"


def main():
   lado1=int(input("Teclea el primer lado: "))
   lado2 = int(input("Teclea el segundo lado: "))
   lado3 = int(input("Teclea el tercer lado: "))

   print(TipoDeTriangulo(lado1, lado2, lado3))


main()