# Autor: Ronaldo Estefano Lira Buendia
# Convertir la hora en formato 24hrs. a formato 12hrs. 


def calcularHora12hrs(h):
    if h>=1 and h<=12:
        hora = h
    elif h>=13 and h<=23:
        hora = h - 12
    elif h == 0 or h == 00:
        hora = 12
    else:
        hora = "ERROR"
    return hora


def calcularMinutos(m):
    if m>=00 and m<=59:
        minuto = m
    else:
        minuto = "ERROR"
    return minuto


def calcularSegundos(s):
    if s>=00 and s<=59:
        segundo = s
    else:
        segundo = "ERROR"
    return segundo


def definirMeridiem(h):
    if h>=00 and h<12:
        r = "AM"
    else:
        r = "PM"
    return r


def main():
    h = int(input("Introduzca la hora en formato 24hrs.: "))
    m = int(input("Introduzca los minutos: "))
    s = int(input("Introduzca los segundos: "))
    hora = calcularHora12hrs(h)
    minuto = calcularMinutos(m)
    segundo = calcularSegundos(s)
    formato = definirMeridiem(h)
    print('%02d' % int(hora),":",'%02d' % int(minuto),":",'%02d' % int(segundo), formato)


main ()