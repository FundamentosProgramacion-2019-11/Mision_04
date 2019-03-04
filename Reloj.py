#Alan Giovanni Rodriguez Camacho A01748185
#Lee la hora en formato de 24 hrs y lo convierte a formato de 12 hrs.


def determinarHoraFormatoDoce(horas,minutos,segundos): #Determina la hora en formato de 12 hrs.
    if horas >= 1 and horas <= 12:
        horas=horas
        return horas
    elif horas == 13:
        horas= 1
        return horas
    elif horas == 14:
        horas= 2
        return horas
    elif horas == 15:
        horas= 3
        return horas
    elif horas == 16:
        horas= 4
        return horas
    elif horas == 17:
        horas= 5
        return horas
    elif horas == 18:
        horas= 6
        return horas
    elif horas == 19:
        horas= 7
        return horas
    elif horas == 20:
        horas= 8
        return horas
    elif horas == 21:
        horas= 9
        return horas
    elif horas == 22:
        horas= 10
        return horas
    elif horas == 23:
        horas= 11
        return horas
    elif horas == 00:
        horas= 12
        return horas


def main():
    horas=int(input("Teclea la hora: "))
    minutos=int(input("Teclea los minutos: "))
    segundos=int(input("Teclea los segundos: "))
    if horas >= 24 or horas < 0:
        print("ERROR: NO EXISTE LA HORA TECLEADA:")
    elif minutos >= 60 or minutos < 0:
        print("ERROR: LOS MINUTOS TECLEADOS SON INCORRECTOS.")
    elif segundos >= 60 or segundos < 0:
        print("ERROR: LOS SEGUNDOS TECLADOS SON INCORRECTOS.")
    else:
        if horas < 12:
            finalam = determinarHoraFormatoDoce(horas, minutos,segundos)
            print("En formato de hora de 12hrs son las {0}:{1}:{2} am.".format(finalam,minutos,segundos))
        else:
            finalpm = determinarHoraFormatoDoce(horas,minutos,segundos)
            print("En formato de hora de 12hrs son las {0}:{1}:{2} pm..".format(finalpm,minutos,segundos))


main()

