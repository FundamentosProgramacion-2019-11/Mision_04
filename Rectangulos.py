# Autor: Jose Luis Mata Lomeli
# Objetivo: Crear un programa que lea las dimensiones (base, altura) de 2 rectangulos y que calcule e imprima perimetro y area de cada uno

#Funciones

def calcularArea(base, altura):
    area = base * altura
    return area

def compararAreas(area1, area2):
    #Cual es el mayor de los dos
    if area1 > area2:
        return ('La primer area es mayor a la segunda')
    elif area2 > area1:
        return ('La segunda area es mayor que la primera')
    elif area1 == area2:
        return ('Ambas areas son iguales')


##Funcion Principal
def main():

    #Entrada
    base1 = int(input('Base del 1er rectangulo: '))
    altura1 = int(input('Altura del 1er rectangulo: '))
    base2 = int(input('Base del 2do rectangulo: '))
    altura2 = int(input('Altura del 2do rectangulo: '))

    #Calcular area
    area1 = calcularArea(base1, altura1)
    area2 = calcularArea(base2, altura2)
    print('El area del 1er rectangulo es de', area1, 'm^2 mientras que la del 2do es ', area2,'m^2')

    #Comparar cual area es mayor de ambas
    comparar = compararAreas(area1, area2)
    print('la Mayor Area =', comparar)


main()
