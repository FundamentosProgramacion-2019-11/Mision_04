#Bruno Omar Jiménez Mancilla
#Escribe un programa que convierta la hora en formato de 24 horas al formato de 12 hrs.

def main():
    hora       =   int(input("Ingresa la hora: "))
    minuto   = int(input("Ingresa los minutos: "))
    segundo = int(input("Ingresa los segundos: "))
    if hora<0 or hora >24:
        print("La hora es incorrecta")
    elif minuto<0 or minuto >60:
        print("Los minutos son inválidos")
    elif segundo<0 or segundo>60:
        print("Los segundos son inválidos")
    else:
        horaFinal = Convertir24a12(hora)
        print("La hora es: ", horaFinal, ",", minuto, ",", segundo)
def Convertir24a12(hora):
    if hora <= 12:
        return hora
    elif hora > 12 and hora <= 24:
        hora12 = (hora-12)
        return hora12

main()
