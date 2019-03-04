#Karimn Daniel Hernández Castorena
#Programa que calcula el área y el perímetro de dos rectángulos.


#Función que calcula el área.
def calcularArea(b1, a1, b2, a2):
    ar1=b1*a1
    ar2=b2*a2

    return ar1, ar2

#Función que calcula el perímetro.
def calcularPerimetro(b1, a1, b2, a2):
    pr1= (b1*2)+(a1*2)
    pr2=(b2*2)+(a2*2)

    return pr1, pr2

#Función que recibe los datos e imprime el área y el perímetro.
def main():
    print()
    b1= int(input("Escribe la base del primer rectángulo: "))
    a1= int(input("Escribe la altura del primer rectángulo: "))
    print()
    b2= int(input("Escribe la base del segundo rectángulo: "))
    a2= int(input("Escribe la altura del segundo rectángulo: "))

    ar1, ar2 = calcularArea(b1, a1, b2, a2)
    pr1, pr2 = calcularPerimetro(b1, a1, b2, a2)
    print ()
    print("El area del primer rectángulo es:", ar1,)
    print("Mientras que el perímetro es:", pr1)
    print()
    print("El area del segundo rectángulo es:", ar2,)
    print("Mientras que el perímetro es:", pr2)
    print()

    if ar1 > ar2:
        print("El área del primer rectángulo es mayor.")
    elif ar2 > ar1:
        print("El área del segundo rectángulo es mayor.")
    else:
        print("Ambos rectángulos tienen la misma área.")

main()

