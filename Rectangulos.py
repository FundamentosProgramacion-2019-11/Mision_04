#Autor Dabid Yair Fernández Salas  #Matícula A01747088
# Este programa te dice el area y perimetro de dos rectangulos oara ver cual es mas grande.

"""En este paso la funcion main(), usa los parametros del area del primer rectangulo y  el area del segundo, y determina  " \
cual es la mayor"""
def CalcularAreabien(areabien, areabien2):
    if areabien > areabien2:
       return"El primer rectangulo es mas grande"
    elif areabien2 > areabien:
        return "El segundo rectangulo es más grande"
    else:
        return "Los dos son iguales"


"""En este caso la función main(), usa las variables que el usuario le ha dado y resuelve las operaciones necesarias
para obtener el perimetro de la figura"""
def CalcularPerimetro(base,h):
    perimetro=(base+base) +(h+h)
    return perimetro


"""En este caso la función main(), usa las variables que el usuario le ha dado y resuelve las operaciones necesarias
para obtener el area de la figura"""
def CalcularArea(base,h):
    area=(base*h)
    return area


"""Para este paso la función main(), tomo los parametros dados por el usuario y y resuleve las operaciones necesarias
para obtener el perímetro de la segunda figura"""
def CalcularPerimetro2(base2,h2):
    perimetrosegundo=(base2+base2)+(h2+h2)
    return perimetrosegundo


"""Para este paso la función main(), uso los parametros dados por el usario y resuleve las operaciones necesarias 
para obtener el area de la segunda figura"""
def CalcularArea2(base2,h2):
    areasegunda= base2*h2
    return areasegunda


"""La funcion main(), envia a cada función los parametros de la base y altura de cada triángulo, para obtener
el perimetro y el área de cada rectangulo e imprime el area y perimetro de cada rectángulo y imprime cual es mayor"""
def main():
    base=float(input("Dame tu base del primer rectángulo: " ))
    h=float(input("Dame tu altura del primer rectángulo: " ))
    base2=float(input("Dame tu base del segundo rectángulo: " ))
    h2=float(input("Dame tu altura del segundo rectángulo: " ))
    perimetrobien =CalcularPerimetro(base,h)
    areabien =CalcularArea(base,h)
    perimetrobien2 =CalcularPerimetro2(base2,h2)
    areabien2 =CalcularArea2(base2,h2)
    print("Tu perímetro es para el primer rectángulo", perimetrobien)
    print("Tu área es para el primer rectángulo", areabien)
    print("Tu perímetro para el segundo rectángulo es", perimetrobien2)
    print("Tu área para el segundo rectángulo es", areabien2)
    comparacion = CalcularAreabien(areabien, areabien2)
    print(comparacion)


main()