#Autor: Yasmín Landaverde Nava
#Descripción: identifica el tipo de triángulo

def definirTriangulo(a,b,c):
    if a*a == (c*c)-(b*b):
        return ("Es triángulo rectángulo")
    if b*b == (c*c)-(a*a):
        return ("Es triángulo rectángulo")
    if c*c == (a*a)-(b*b):
        return ("Es triángulo rectángulo")
    if a == b and a == c and b == c:
        return ("Es triángulo isosceles")
    if  a == b or a == c or b == c:
        return ("Es triángulo equilátero")
    else:
        return ("otro")

def main():
    a = int(input("Teclea la medida: "))
    b = int(input("Teclea la medida: "))
    c = int(input("Teclea la medida: "))
    definirTriangulo(a,b,c)
    print (definirTriangulo(a,b,c))

main()