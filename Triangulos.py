#Autor Dabid Yair Fernández Salas  #Matícula A01747088
# Este programa te dice el area y perimetro de dos rectangulos oara ver cual es mas grande.


"""En este problema se esta usando la funcion main, con los parametros que el usario intrduce, lado1,lado2,lado3
y esta funcion realiza las compraciones necesarias para devolver el un resultado  """
def CalcularTriangulo(l1,l2,l3):
    if l1 ==l2 and l1==13:
        return "Equilatero"
    elif l1==l2 or l1==l3:
        return "Isolceles"
    elif l2==l3:
        return "Isóceles"
    elif l1==((l2 ** 2) + (l3 ** 2))**0.5:
        return "Rectángulo"
    elif 12==((l1**2)+(l3**2))**0.5:
        return "Rectángulo"
    if l3==(l1**2)+(l2)**0.5:
        return "Rectangulo"
    else:
        return "Estos lados no corrsponden a un triángulo"


"""En esta parte la funcion main, se usa para preguntar al usuario los lados de la figura, en envia los datos a la funcion de arriba
e impime un resultado predeterminado"""
def main():
    l1=float(input("Dime un lado del triangulo: "))
    l2=float(input("Dime otro lado del triangulo: "))
    l3=float(input("Dume otor lado del trinagulo: "))
    print("Tu figura es ",CalcularTriangulo(l1,l2,l3))

main()
