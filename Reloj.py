#Bernardo Mondragon Ramírez
#Convertir hoaras de reloj 24 horas a 12 horas


def RestaHoras(h):
    if h>=1 and h<=12:
        hora = h
        return hora

    elif h>=13 and h<=23:
        hora= h - 12
        return hora

    elif h==0:
        hora = 12

        return hora
    else:
        return "Error en"


def Minutos(m):
    if m>=0 and m<=59:

        return(m)
    else:
        return "Error en "

def Segundos(s):
    if s>=0 and s<=59:

        return(s)
    else:
        return "Error en "


def main():
    h = int(input("Horas en formato 24: "))
    print(RestaHoras(h),"Horas")

    m = int(input("Minutos: "))
    print(Minutos(m), "Minutos")

    s = int(input("Segundos: "))
    print(Segundos(s), "Segundos")



main()