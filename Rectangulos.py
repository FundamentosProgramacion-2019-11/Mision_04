# Autor: Victor Manuel Ceron Navarrete
# Descripcion: Calcula el perímetro y área de dos rectángulos y da el area mayor


#Calcula el área de un rectángulo con su base y altura

def calcuA(b, h):
    return b*h


#Calcula el perímetro de un rectángulo con su base y altura

def calcuP(b,h):
    return (2*b)+(2*h)


#Calcula el área de los dos rectángulo y devuelve el mayot

def esMayorAUno(A1, A2):
    if A1 == A2:
        return "Las áreas son iguales"
    if A2 > A1:
        return "El area del segundo rectángulo es mayor"
    return "El area del primer rectangulo es mayor"


#Preguntar datos al usuario, devuelve los resultados
def main():
    baseUno = int(input("Teclea la base del primer rectángulo: "))
    alturaUno = int(input("Teclea la altura del primer rectángulo: "))
    baseDos = int(input("Teclea la base del segundo rectángulo: "))
    alturaDos = int(input("Teclea la altura del primer rectángulo: "))

    areaUno = calcuA(baseUno, alturaUno)
    areaDos = calcuA(baseDos, alturaDos)
    print()
    print("Area del primer rectángulo: %d" % areaUno)
    print("Perímetro del primer rectángulo: %d" % calcuP(baseUno, alturaUno))
    print("Area del segundo rectángulo: %d" % areaDos)
    print("Perímetro del segundo rectángulo: %d" % calcuP(baseDos, alturaDos))
    print("%s" % (esMayorAUno(areaUno, areaDos)))


# Funciona main()
main()
