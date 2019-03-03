#Autor: Cecilia Daniela Olivares Hernández, a01745727
#Este programa calcula el area y perimetro de dos rectangulos y compara si sus areas son iguales


#Esta función calcula el area del primer rectangulo
def calcularArea1(b1, a1, b2, a2):
    area1 = b1 * a1
    return area1


#Esta función calcula el area del segundo rectangulo
def calcularArea2(b1, a1, b2, a2):
    area2 = b2 * a2
    return area2


#Esta función calcula el perimetro del primer rectangulo
def calcularPerimetro1(b1, a1, b2, a2):
    perimetro1 = b1*2 + a1*2
    return perimetro1


#Esta función calcula el area del segundo rectangulo
def calcularPerimetro2(b1, a1, b2, a2):
    perimetro2 = b2*2 + a2*2
    return perimetro2


#Esta función indica cual de las areas es mayor o si son iguales
def areaMayorOIgual(b1, a1, b2, a2):
    area1 = calcularArea1(b1, a1, b2, a2)
    area2 = calcularArea2(b1, a1, b2, a2)
    if area1 > area2:
        return "El primer rectangulo tiene Mayor Area"
    if area1 < area2:
        return "El segundo rectangulo tiene Mayor Area"
    if area1 == area2:
        return "El area de los rectangulos es IGUAL"


#Funcion principal que resuelve el problema
def main():
    b1 = int(input("Ingresa la base del primer rectangulo: "))
    a1 = int(input("Ingresa la altura del primer rectangulo: "))
    b2 = int(input("Ingresa la base del segundo rectangulo: "))
    a2 = int(input("Ingresa la altura del segundo rectangulo: "))
    area1 = calcularArea1(b1, a1, b2, a2)
    area2 = calcularArea2(b1, a1, b2, a2)
    perimetro1 = calcularPerimetro1(b1, a1, b2, a2)
    perimetro2 = calcularPerimetro2(b1, a1, b2, a2)
    print("""Los valores del primer rectangulo son: 
Area: """,(area1),"""cm
Perimetro: """,(perimetro1),"""cm""")
    print("""Los valores del segundo rectangulo son: 
Area: """,(area2),"""cm
Perimetro: """,(perimetro2),"""cm""")
    areaMayorOIgual(b1, a1, b2, a2)
    print(areaMayorOIgual(b1, a1, b2, a2))


main()
