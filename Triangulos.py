# Autor: José Luis Macías Vázquez, A01655713, Grupo 03
# El programa recibe los lados de un triangulo y te dice de que tipo de triangulo se trata

def nombrarTriangulo(lU,lD,lT):

    if lU <= 0 or lD <= 0 or lT <= 0:
        return "El triángulo no existe"
    if lU == lD and lD == lT:
        return "Es un triangulo equilatero"
    if lU == lD and lU != lT:
        return "Es un triángulo isoceles"
    if lU == lT and lU != lD:
        return "Es un triángulo isoceles"
    if lD == lT and lD != lU:
        return "Es un triángulo isoceles"
    if lU != lD and lD != lT:
        return "Es un triángulo rectángulo"



def main():

    lU = int(input("Escribe el largo del primer lado: "))
    lD  = int(input("Escribe el ancho del segundo lado: "))
    lT = int(input("Escribe el largo del tercer lado: "))
    print(nombrarTriangulo(lU,lD,lT))

main()