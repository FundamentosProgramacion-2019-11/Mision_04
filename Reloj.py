#Luis Adrian Carmona Villalobos
#Progama que convierte reloj de 24 a 12 horas

def calcularHora(h,m,s):
    if h == 12:
        print("Hora: %d:%02d:%02d PM" % (h, m, s))
    elif h >12:
        h12 = h - 12
        print("Hora: %d:%02d:%02d PM" %(h12,m,s))
    elif h == 0:
        print("Hora: %d:%02d:%02d AM" % (h, m, s))
    elif  h < 12:
        print("Hora: %d:%02d:%02d:AM") %(h,m,s)


def main():
    h = int(input("Cual es la hora: "))
    m = int(input("Cuales son los minutos: "))
    s = int(input("Cuales son los segundos"))
    if h < 0 or h >= 24:
        print("ERROR")
    elif m < 0 and m >= 60:
        print("ERROR")
    elif s < 0 and s >= 60:
        print("ERROR")

    calcularHora(h,m,s)

main()
