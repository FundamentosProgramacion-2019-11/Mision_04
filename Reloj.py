#Autor: Yasmín Landaverde Nava
#Descripción: Convierte el reloj de 24 horas a 12 horas

def esHora(hora):
    if hora>=00 and hora<=23:
        return True
    else:
        return False


def convertirHora(hora, minutos, segundos):
    if esHora(hora):
        if hora == 0:
            return "%d : %02d : %02d" % (12 ,minutos, segundos)
        if hora == 23:
            return "%d : %02d : %02d" % (11, minutos, segundos)
        if hora == 22:
            return "%d : %02d : %02d" % (10, minutos, segundos)
        if hora == 21:
            return "%02d : %02d : %02d" % (9, minutos, segundos)
        if hora == 20:
            return "%02d : %02d : %02d" % (8, minutos, segundos)
        if hora == 19:
            return "%02d : %02d : %02d" % (7, minutos, segundos)
        if hora == 18:
            return "%02d : %02d : %02d" % (6, minutos, segundos)
        if hora == 17:
            return "%02d : %02d : %02d" % (5, minutos, segundos)
        if hora == 16:
            return "%02d : %02d : %02d" % (4, minutos, segundos)
        if hora == 15:
            return "%02d : %02d : %02d" % (3, minutos, segundos)
        if hora == 14:
            return "%02d : %02d : %02d" % (2, minutos, segundos)
        if hora == 13:
            return "%02d : %02d : %02d" % (1, minutos, segundos)
    else:
        print ("error")


def main():
    hora = int(input("Teclea la hora "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))
    convertirHora(hora, minutos, segundos)
    print (convertirHora(hora, minutos, segundos,), "PM")

main()