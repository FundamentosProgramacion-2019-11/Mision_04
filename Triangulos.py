#Bruno Omar Jiménez Mancilla
#Un programa que reciba los lados de un triangulo y defina su tipo


def main():
    lado1 = int(input("Dame el primer lado de tu triangulo: "))
    lado2 = int(input("Dame el segundo  lado de tu triangulo: "))
    lado3 = int(input("Dame el tercer lado de tu triangulo: "))

    x=tipoDeTriangulo(lado1,lado2,lado3)
    print(x)

def tipoDeTriangulo(lado1,lado2,lado3):
    if lado1<=0 or lado2<=0 or lado3<=0:
        return "El triangulo no existe"
    elif lado1==lado2 and lado1==lado3 and lado2==lado3:
        return "Triángulo equilatero"
    elif lado2==lado1 or lado3==lado1 or lado2==lado3:
        return "Triangulo isoceles"
    elif lado2!=lado1 and lado1!=lado3 and lado2!=lado3:
        return "Triángulo escaleno"

main()

