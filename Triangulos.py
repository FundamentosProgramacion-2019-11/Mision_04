#Autor Sofía Trujillo Vargas
#De acuerdo al largo de los lados de un triángulo decir que tipo de triangulo es.


def main():
    l1 = int(input("Dame el primer lado de tu triangulo: "))
    l2 = int(input("Dame el segundo  lado de tu triangulo: "))
    l3 = int(input("Dame el tercer lado de tu triangulo: "))

    t=tipoTriangulo(l1,l2,l3)
    print(t)

def tipoTriangulo(l1,l2,l3):
    if l1<=0 or l2<=0 or l3<=0:
        return "El triangulo no existe"
    elif l1==l2 and l1==l3 and l2==l3:
        return "Triángulo equilatero"
    elif l2==l1 or l3==l1 or l2==l3:
        return "Triangulo isoceles"
    elif l2!=l1 and l1!=l3 and l2!=l3:
        return "Triángulo escaleno"

main()

