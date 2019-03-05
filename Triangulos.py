#Autor: Santiago España Vázquez A01748311
#Descripción: Reconocer que tipo de triangulo se trata segun lados o si no es triangulo

def recognizeTri(a, b, c):
    if not ((a+b)>c) and ((a+c)>b) and ((c+b)>a):
        return "No es un triangulo"

    elif a==b and b==c:
        return "El triangulo es equilatero"

    elif a==b or b==c:
        return "El triangulo es isoceles"

    else:
        return "El triangulo es triangulo rectangulo"

def main():
    a=float(input("Por favor introduzca el primer lado del triangulo"))
    b=float(input("Por favor introduzca el segundo lado del triangulo"))
    c=float(input("Por favor introduzca el tercer lado del triangulo"))

    ans= recognizeTri(a, b, c)
    print(ans)

main()