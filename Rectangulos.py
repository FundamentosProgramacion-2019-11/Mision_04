# Autor: Daniela Estrella Tovar
# Dadas la base y altura de dos rectangulos, calcular su peímetro y su área
# Indicar cuál de los dos réctangulos tiene un área mayor.


import turtle

# Esta función calcula el área de los rectángulos.

def calcularPArea(basePrimerR, alturaPrimerR):
    areaUno = basePrimerR * alturaPrimerR
    return areaUno


#Esta función calcula el área del segundo Rectángulo

def calcularSArea(baseSegundoR, alturaSegundoR):
    areaDos = baseSegundoR * alturaSegundoR
    return areaDos


# Esta función calcula el Perímetro del Primer rectángulo.

def calcularPPerimetro(basePrimerR, alturaPrimerR):
    periUno = basePrimerR * 2 + alturaPrimerR * 2
    return periUno


#Esta función calcula el Perímetro del Segundo Rectángulo

def calcularSPerimetro(baseSegundoR, alturaSegundoR):
    periDos = baseSegundoR * 2 + alturaSegundoR * 2
    return periDos


# Esta funcion compara las áres de los dos rectangulos y dice cual es el más grande

def compararArea(basePrimerR, alturaPrimerR,baseSegundoR, alturaSegundoR ):
    areaPrimer= calcularPArea(basePrimerR, alturaPrimerR)
    areaSegund= calcularSArea(baseSegundoR, alturaSegundoR)
    if areaPrimer > areaSegund:
        mayor = "El Primer Rectángulo es mayor"
    elif areaPrimer < areaSegund:
        mayor = "El Segundo Rectángulo es mayor"
    else:
        mayor = "Los dos Rectángulos tienen la misma área."
    return mayor


#Esta función lee e imprime variables.
def main():
    basePrimerR = int(input("Teclea la base del Primer Rectángulo en cm: "))
    alturaPrimerR = int(input("Teclea la altura del Primer Rectángulo en cm: "))
    baseSegundoR = int(input("Teclea la base del Segundo Rectángulo en cm: "))
    alturaSegundoR = int(input("Teclea la altura del Segundo Rectángulo en cm: "))
    areaUno = calcularPArea(basePrimerR, alturaPrimerR)
    print("""
El Área del  Primer Rectángulo es de: """, areaUno, "cm")
    periUno = calcularSPerimetro(basePrimerR, alturaPrimerR)
    print("El Perímetro del Primer Rectángulo es de:", periUno, "cm")
    areaDos = calcularSArea(baseSegundoR, alturaSegundoR)
    print("""El Área del  Segundo Rectángulo es de: """,
areaDos, "cm")
    periDos = calcularPPerimetro(baseSegundoR, alturaSegundoR)
    print("El Perímetro del Segundo Rectángulo es de:", periDos, "cm")
    comparación = compararArea(basePrimerR, alturaPrimerR,baseSegundoR, alturaSegundoR)
    print("""
""", comparación)

main()
