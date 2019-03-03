#Autor: Luis Alberto Zepeda Hernandez
#Descripción:Escribe un programa que lea las dimensiones (base y altura) de dos rectángulos
# y que calcule e imprima el perímetro y área de cada uno.

#Esta función determina el  área 1
def calcularArea1(altura1,base1):
    area = altura1 * base1
    return area


#Esta función determina el área 2
def calcularArea2(altura2,base2):
    area = altura2 * base2
    return area


#Esta función determina el perímetro 1
def calcularPerimetro1(altura1,base1):
    perimetro = (altura1*2) + (base1*2)
    return perimetro


#Esta función determina el perímetro 2
def calcularPerimetro2(altura2,base2):
    perimetro = (altura2*2) + (base2*2)
    return perimetro
#Esta función determina cual de las dos areas ya calculadas es mayor.
def esMayor(area1,area2):
    if area1 > area2:
        return "Rectángulo 1 tiene mayor área."
    if area1 < area2:
        return "Rectángulo 2 tiene menor área."
    if area1 == area2:
        return "Rectángulo 1 y 2 tienen la misma área."

#Esta función pide los datos, y llama a las funciones para poder realizar las operaciones.
def main():
    altura1 = int(input("Ingresa la altura del primer rectángulo: "))
    altura2 = int(input("Ingresa la altura del segundo rectángulo: "))
    base1 = int(input("Ingresa la base del primer rectángulo: "))
    base2 = int(input("Ingresa la base del segundo rectángulo: "))
    area1 = calcularArea1(altura1,base1)
    area2 = calcularArea2(altura2,base2)
    perimetro1 = calcularPerimetro1(altura1,base1)
    perimetro2 = calcularPerimetro2(altura2,base2)
    areaMayor = esMayor(area1,area2)

    print("Rectángulo 1:")
    print("Área:",area1)
    print("Perímetro: ",perimetro1)
    print()
    print("Rectángulo 2:")
    print("Área: ",area2)
    print("Perímetro: ",perimetro2)
    print()
    print(areaMayor)





main()