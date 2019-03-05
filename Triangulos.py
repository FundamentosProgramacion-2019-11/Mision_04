#Autor: Karla Ximena Rueda Ruiz
#Este programa lee el valor de cada uno de los lados de un triángulo y te indica qué tipo de triángulo es.

def main():
    lado1=float(input("Valor lado 1:"))
    lado2 = float(input("Valor lado 2:"))
    lado3 = float(input("Valor lado 3:"))

    valorTriangulo(lado1,lado2,lado3)


    valor=calcularTriangulo(lado1,lado2,lado3)
    print("Esto", valor)

def valorTriangulo(lado1,lado2,lado3):
    if lado1+lado2>lado3 and lado2+lado3>lado1 and lado1+lado3>lado2:
        return True
    else:
        return False

def calcularTriangulo(lado1,lado2,lado3):
    if valorTriangulo(lado1,lado2,lado3)==True:
        if lado1==lado2==lado3:
            return"corresponde a un triángulo equilátero"
        elif(lado3**2)+(lado1**2)-(lado3**2)==0 or (lado1**2)+(lado2**2)-(lado3**2)==0 or(lado2**2)+(lado3**2)-(lado1**2):
            return"corresponde a un triángulo rectángulo"
        elif lado1==lado3 !=lado2 or lado1==lado2!=lado3 or lado1== lado3 != lado2:
            return "corresponde a un triángulo isóceles"
        elif(lado1**2)+(lado2**2)-(lado3**2)>0 or (lado3**2)+(lado1**2)-(lado2**2)>0 or(lado2**2)+(lado3**2)-(lado1**2):
            return"corresponde a un triángulo escaleno"
        else:
            return "corresponde a otro triángulo"
    else:
        return "No es un triángulo"

main()