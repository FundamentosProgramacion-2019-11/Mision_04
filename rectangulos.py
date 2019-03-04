#Rafael Romero Bello  A01747730
#imprime las dimensiones de dos triangulos y luego los comprara

def calcularP1(b,h):
    p1=(2*b)+(2*h)
    return p1

def calcularP2(b2,h2):
    p2=(2*b2)+(2*h2)
    return p2

def calculararea1(b,h):
    a1=b*h
    return a1

def calcularArea2(b2,h2):
    a2=b2*h2
    return a2

def compararArea(a1,a2):
    if a1 < a2:
        r="el area mas grande  es la figura 2"
    elif a1>a2:
        r="el area mas grande es la figura 1"
    elif a1==a2:
        r="sus areas son iguales"
    else:
        r="algo esta mal"
    return r

def main():
    Base1=int(input("Inserte la base1"))
    Base2=int(input("inserte la base2"))
    Altura1=int(input("inserte la altura1"))
    Altura2=int(input("inserte la altura2"))
    pe1=calcularP1(Base1,Altura1)
    pe2=calcularP2(Base2,Altura2)
    A1=calculararea1(Base1,Altura1)
    A2=calcularArea2(Base2,Altura2)
    Rf=compararArea(A1,A2)
    print("perimetro 1",pe1)
    print("perimetro 2",pe2)
    print("area1",A1)
    print("area2",A2)
    print(Rf)

main()