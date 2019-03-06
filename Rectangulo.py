#Autor: Luis Renteria
#Calcular areas de rectangulos


def calcularAreaR1(base1, altura1):
    Area=base1*altura1
    return Area

def calcularAreaR2(base2, altura2):
    Area2=base2*altura2
    return Area2

def calcularPerimetroR1(base1, altura1):
    Perimetro=(base1*2)+(altura1*2)
    return Perimetro

def calcularPerimetroR2(base2, altura2):
    Perimetro2=(base2*2)+(altura2*2)
    return Perimetro2

def main():
    base1=int(input("introduce la base del primer rectangulo"))
    altura1=int(input("introduce la altura del primer rectangulo"))
    base2=int(input("introduce la base del segundo rectangulo"))
    altura2=int(input("introduce la altura del segundo rectangulo"))
    calcularAreaR1(base1, altura1)
    calcularAreaR2(base2, altura2)
    calcularPerimetroR1(base1, altura1)
    calcularPerimetroR2(base2, altura2)
    print "El area del primer rectangulo es:",calcularAreaR1(base1, altura1)
    print "El perimetro del primer rectangulo es:",calcularPerimetroR1(base1, altura1)
    print "El area del segundo rectangulo es:",calcularAreaR2(base2, altura2)
    print "El perimetri del segundo rectangulo es:",calcularPerimetroR2(base2, altura2)
    if base1*altura1>base2*altura2:
        print ("el rectangulo 1 tine mayor area")
    elif base1*altura1<base2*altura2:
        print ("el segundo rectangulo tiene mayor area")
    else:
        print ("las areas son iguales")


main()
