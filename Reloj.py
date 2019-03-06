#Autor: Luis Renteria
#Convertit formato de hora

def convertirHora(hora,minuto,segundo):
    if hora>12 and hora<23:
        Hora=hora-12
        return Hora


def main():
    hora=int(input("introduce la hora"))
    minuto=int(input("introduce los minutos"))
    segundos=int(input("introduce los segundos"))
    if hora<0 or hora>24:
        print "hora no valida"
    elif minuto<0 or minuto>60:
        print "minuto no valido"
    elif segundos<0 or segundos>60:
        print "segundo no valido"
    elif hora>12:
        print "PM"
    else:
        print "AM"
    HoraConvertida=convertirHora(hora,minuto,segundos)
    print("son las",HoraConvertida,minuto,segundos)

main()