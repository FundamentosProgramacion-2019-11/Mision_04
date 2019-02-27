#María Angélica Hernández Parada
#Decir los lados de un triangulo y decir a que triangulo corresponde

def queTrianguloEs(lado1,lado2,lado3):
    if lado1<=0:
        return "Estos lados no corresponden a un triangulo"
    if lado2<=0:
        return "error"
    if lado3<=0:
        return "error"
    if lado1==lado2 and lado2==lado3:
        return "Es un triangulo equilatero"
    if lado1==lado2 and lado2!=lado3:
        return "Es un triangulo isósceles"
    if lado1!=lado2 and lado2==lado3:
        return "Es un triangulo isósceles"
    if lado1==lado3 and lado2!=lado1:
        return "Es un triangulo isósceles"
    if lado1 != lado2 and lado2 != lado3 and lado3!=lado1:
        return "Es un triangulo escaleno"

def main():
    lado1=int(input("Dime el primer lado del triangulo"))
    lado2=int(input("Dime el segundo lado del triangulo"))
    lado3=int(input("Dime el tercer lado del triangulo"))
    print(queTrianguloEs(lado1,lado2,lado3))

main()