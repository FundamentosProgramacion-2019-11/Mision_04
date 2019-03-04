#Escribe un programa que lea el valor de cada uno de los lados de un triángulo (puede ser en cualquier orden)


def definirTriangulo(a, b, c):
    if a==b and b==c:
        x = "El triángulo es equilátero."
    elif a==b and c!=b:
        x = "El triángulo es isóceles."
    elif b==c and c!=a:
        x = "El triángulo es isóceles."
    elif a==c and a!=b:
        x = "El triángulo es isóceles."
    elif (((a+b)**2)**.5)==c or (((b+c)**2)**.5)==a or (((a+c)**2)**.5)==b:
        x = "El triángulo es rectángulo."
    else:
        x = "Estos lados no corresponden a ninguno de los triángulos del sistema."
    return x

def main():
    a = float(input("Teclea el primer lado del triángulo: "))
    b = float(input("Teclea el segundo lado: "))
    c = float(input("Teclea el tercer lado: "))
    tipo = definirTriangulo(a, b, c)
    print(tipo)

main()