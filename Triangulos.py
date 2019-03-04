#Karimn Daniel Hernández Castorena
#Programa que escriba el tipo de triángulo que esta siendo ingresado.


#Función que analiza que tipo de triángulo se está ingresando.
def analizarTriangulo(l1,l2,l3):

    if l1!= l2 != l3:
        t = "Escaleno"
    elif (l1**2==l2**2+l3**2) or (l2**2==l1**2+l3**2) or (l3**2==l2**2+l2**2):
        t = "Rectángulo"
    elif l1==l2==l3:
        t = "Equilatero"
    elif l1==l2 or l2==l3 or l1==l3:
        t = "Isósceles"
    else:
        t = "Error"

    return t


#Función que lee los 3 lados e imprime que tipo de triángulo es.
def main():
    print()
    l1 = int(input("Escribe el primer lado de tu triángulo: "))
    l2 = int(input("Escribe el segundo lado de tu triángulo: "))
    l3 = int(input("Escribe el tercer lado de tu triángulo: "))
    t = analizarTriangulo(l1, l2, l3)

    if t == "Error":
        print()
        print("Los lados no corresponden a un triángulo conocido.")
    else:
        print()
        print("Tu triangulo es:", t)


main()